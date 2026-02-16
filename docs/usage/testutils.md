# TestUtils 使用指南

`TestUtils` 类提供了自动化测试中常用的工具方法，包括测试数据生成、测试报告生成等功能。

## 基本使用

### 生成测试数据

```python
from btools import TestUtils

# 生成随机字符串
random_str = TestUtils.generate_random_string()
print(f"随机字符串: {random_str}")

# 生成随机邮箱
random_email = TestUtils.generate_random_email()
print(f"随机邮箱: {random_email}")

# 生成随机手机号
random_phone = TestUtils.generate_random_phone()
print(f"随机手机号: {random_phone}")

# 生成随机日期
random_date = TestUtils.generate_random_date()
print(f"随机日期: {random_date}")

# 根据模板生成测试数据
test_data_template = {
    "username": "${random_string}",
    "email": "${random_email}",
    "phone": "${random_phone}",
    "register_date": "${random_date}",
    "profile": {
        "first_name": "${random_string:5}",
        "last_name": "${random_string:5}"
    }
}

generated_data = TestUtils.generate_test_data(test_data_template)
print(f"生成的测试数据: {generated_data}")
```

### 配置文件操作

```python
# 加载测试配置
config = TestUtils.load_test_config("test_config.yaml")
print(f"加载的配置: {config}")
```

### 测试结果操作

```python
# 保存测试结果
test_results = {
    "test_name": "登录测试",
    "status": "PASS",
    "duration": 2.5,
    "timestamp": "2023-12-25 10:00:00"
}

# 保存为JSON
TestUtils.save_test_results(test_results, "test_results.json")
print("测试结果已保存为JSON")

# 保存为YAML
TestUtils.save_test_results(test_results, "test_results.yaml", format="yaml")
print("测试结果已保存为YAML")
```

## 生成测试报告

```python
# 准备测试用例数据
test_cases = [
    {
        "name": "登录成功测试",
        "description": "测试正常登录流程",
        "status": "PASS",
        "start_time": "2023-12-25 10:00:00",
        "end_time": "2023-12-25 10:00:02",
        "duration": 2.1
    },
    {
        "name": "登录失败测试",
        "description": "测试密码错误时的登录失败场景",
        "status": "PASS",
        "start_time": "2023-12-25 10:00:03",
        "end_time": "2023-12-25 10:00:05",
        "duration": 1.8
    },
    {
        "name": "注册测试",
        "description": "测试用户注册功能",
        "status": "FAIL",
        "start_time": "2023-12-25 10:00:06",
        "end_time": "2023-12-25 10:00:09",
        "duration": 3.2,
        "error": "邮箱格式不正确"
    }
]

# 生成HTML测试报告
report_path = TestUtils.generate_test_report(test_cases, "test_report.html")
print(f"测试报告已生成: {report_path}")
```

## 等待元素装饰器

```python
# 使用等待元素装饰器
@TestUtils.wait_for_element(timeout=10)
def find_element_by_id(driver, element_id):
    return driver.find_element("id", element_id)

# 调用带等待的函数
try:
    element = find_element_by_id(driver, "login-button")
    print("找到登录按钮")
except TimeoutError as e:
    print(f"找不到元素: {e}")
```

## 高级功能

### 测试数据模板语法

`TestUtils.generate_test_data()` 方法支持以下模板变量：

| 模板变量 | 描述 | 示例 |
|---------|------|------|
| `${random_string}` | 生成随机字符串 | `${random_string}` |
| `${random_string:n}` | 生成指定长度的随机字符串 | `${random_string:5}` |
| `${random_email}` | 生成随机邮箱 | `${random_email}` |
| `${random_phone}` | 生成随机手机号 | `${random_phone}` |
| `${random_date}` | 生成随机日期 | `${random_date}` |
| `${random_integer}` | 生成随机整数 | `${random_integer}` |
| `${random_integer:min:max}` | 生成指定范围的随机整数 | `${random_integer:1:100}` |
| `${random_float}` | 生成随机浮点数 | `${random_float}` |
| `${random_float:min:max}` | 生成指定范围的随机浮点数 | `${random_float:1.0:10.0}` |
| `${random_boolean}` | 生成随机布尔值 | `${random_boolean}` |

### 自定义测试报告模板

```python
# 使用自定义模板生成测试报告
report_path = TestUtils.generate_test_report(
    test_cases, 
    "custom_report.html",
    template_path="custom_report_template.html"
)
print(f"使用自定义模板生成的测试报告: {report_path}")
```

### 测试数据持久化

```python
# 生成测试数据并保存
test_data = {
    "users": [
        {"id": 1, "name": "张三", "email": "zhangsan@example.com"},
        {"id": 2, "name": "李四", "email": "lisi@example.com"}
    ]
}

# 保存为JSON
TestUtils.save_test_data(test_data, "test_data.json")

# 保存为YAML
TestUtils.save_test_data(test_data, "test_data.yaml")

# 加载测试数据
loaded_data = TestUtils.load_test_data("test_data.json")
print(f"加载的测试数据: {loaded_data}")
```

### 测试执行时间统计

```python
# 统计函数执行时间
@TestUtils.measure_execution_time
def slow_function():
    import time
    time.sleep(1)
    return "完成"

result = slow_function()
print(f"函数返回值: {result}")
# 输出示例: 函数 'slow_function' 执行时间: 1.0023秒
```

## 与其他测试框架集成

### 与 pytest 集成

```python
import pytest
from btools import TestUtils

class TestUser:
    @pytest.fixture
    def test_data(self):
        # 使用TestUtils生成测试数据
        return TestUtils.generate_test_data({
            "username": "${random_string}",
            "email": "${random_email}",
            "password": "${random_string:8}"
        })
    
    def test_register(self, test_data):
        """测试用户注册功能"""
        print(f"测试注册数据: {test_data}")
        # 执行注册测试...
        assert "username" in test_data
        assert "email" in test_data
        assert "password" in test_data
```

### 与 unittest 集成

```python
import unittest
from btools import TestUtils

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        # 生成测试数据
        self.test_data = TestUtils.generate_test_data({
            "username": "${random_string}",
            "email": "${random_email}",
            "password": "${random_string:8}"
        })
    
    def test_registration_success(self):
        """测试注册成功场景"""
        print(f"测试数据: {self.test_data}")
        # 执行注册测试...
        self.assertIn("username", self.test_data)
        self.assertIn("email", self.test_data)
        self.assertIn("password", self.test_data)

if __name__ == '__main__':
    unittest.main()
```

## 常见问题

### 模板解析错误

如果遇到模板解析错误，请检查：
1. 模板变量格式是否正确，应为 `${variable}`
2. 变量名是否拼写正确
3. 参数格式是否正确，例如 `${random_string:5}`

### 测试报告生成失败

如果测试报告生成失败，请检查：
1. 测试用例数据格式是否正确
2. 模板文件是否存在且格式正确
3. 是否有写入权限

### 等待元素超时

如果等待元素超时，请检查：
1. 元素定位器是否正确
2. 页面是否正确加载
3. 超时时间是否足够长