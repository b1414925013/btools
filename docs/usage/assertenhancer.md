# AssertEnhancer 使用指南

`AssertEnhancer` 类提供了增强的断言方法，适用于API测试和UI测试中的各种断言场景。

## 基本使用

### 字符串断言

```python
from btools import AssertEnhancer

# 断言字符串包含
AssertEnhancer.assert_contains("Hello World", "World")
print("字符串包含断言通过")

# 断言字符串不包含
AssertEnhancer.assert_not_contains("Hello World", "Test")
print("字符串不包含断言通过")

# 断言字符串相等
AssertEnhancer.assert_equals("Hello", "Hello")
print("字符串相等断言通过")

# 断言字符串不相等
AssertEnhancer.assert_not_equals("Hello", "World")
print("字符串不相等断言通过")
```

### 数值断言

```python
# 断言数值相等
AssertEnhancer.assert_equals(10, 10)
print("数值相等断言通过")

# 断言数值不相等
AssertEnhancer.assert_not_equals(10, 20)
print("数值不相等断言通过")

# 断言数值大于
AssertEnhancer.assert_greater_than(20, 10)
print("数值大于断言通过")

# 断言数值大于等于
AssertEnhancer.assert_greater_than_or_equal(10, 10)
print("数值大于等于断言通过")

# 断言数值小于
AssertEnhancer.assert_less_than(10, 20)
print("数值小于断言通过")

# 断言数值小于等于
AssertEnhancer.assert_less_than_or_equal(10, 10)
print("数值小于等于断言通过")

# 断言数值在范围内
AssertEnhancer.assert_between(15, 10, 20)
print("数值在范围内断言通过")
```

### 集合断言

```python
# 断言列表包含元素
AssertEnhancer.assert_list_contains([1, 2, 3], 2)
print("列表包含元素断言通过")

# 断言列表不包含元素
AssertEnhancer.assert_list_not_contains([1, 2, 3], 4)
print("列表不包含元素断言通过")

# 断言列表相等
AssertEnhancer.assert_equals([1, 2, 3], [1, 2, 3])
print("列表相等断言通过")

# 断言字典包含键
AssertEnhancer.assert_dict_contains_key({"name": "John", "age": 30}, "name")
print("字典包含键断言通过")

# 断言字典包含值
AssertEnhancer.assert_dict_contains_value({"name": "John", "age": 30}, "John")
print("字典包含值断言通过")

# 断言字典包含键值对
AssertEnhancer.assert_dict_contains({"name": "John", "age": 30}, {"name": "John"})
print("字典包含键值对断言通过")
```

### 布尔断言

```python
# 断言为真
AssertEnhancer.assert_true(True)
print("断言为真通过")

# 断言为假
AssertEnhancer.assert_false(False)
print("断言为假通过")

# 断言不为空
AssertEnhancer.assert_not_none("Hello")
print("断言不为空通过")

# 断言为空
AssertEnhancer.assert_none(None)
print("断言为空通过")
```

## JSON断言

```python
# 断言JSON相等
expected_json = {"name": "John", "age": 30}
actual_json = {"name": "John", "age": 30}
AssertEnhancer.assert_json_equals(actual_json, expected_json)
print("JSON相等断言通过")

# 断言JSON包含
partial_json = {"name": "John"}
full_json = {"name": "John", "age": 30, "city": "New York"}
AssertEnhancer.assert_json_contains(full_json, partial_json)
print("JSON包含断言通过")

# 断言JSON路径存在
json_data = {"user": {"profile": {"name": "John"}}}
AssertEnhancer.assert_json_path_exists(json_data, "user.profile.name")
print("JSON路径存在断言通过")

# 断言JSON路径值
AssertEnhancer.assert_json_path_value(json_data, "user.profile.name", "John")
print("JSON路径值断言通过")
```

## HTTP响应断言

### 响应状态码断言

```python
import requests
from btools import AssertEnhancer

response = requests.get("https://api.example.com/users")
AssertEnhancer.assert_response_status(response, 200)
print("响应状态码断言通过")

# 断言响应状态码在成功范围内 (200-299)
AssertEnhancer.assert_response_success(response)
print("响应成功断言通过")

# 断言响应状态码在客户端错误范围内 (400-499)
# response = requests.get("https://api.example.com/nonexistent")
# AssertEnhancer.assert_response_client_error(response)
# print("客户端错误断言通过")

# 断言响应状态码在服务器错误范围内 (500-599)
# response = requests.get("https://api.example.com/server-error")
# AssertEnhancer.assert_response_server_error(response)
# print("服务器错误断言通过")
```

### 响应头断言

```python
# 断言响应头存在
AssertEnhancer.assert_response_header_exists(response, "Content-Type")
print("响应头存在断言通过")

# 断言响应头值
AssertEnhancer.assert_response_header_value(response, "Content-Type", "application/json")
print("响应头值断言通过")
```

### 响应体断言

```python
# 断言响应体JSON相等
expected_response = {"status": "success", "data": []}
AssertEnhancer.assert_response_json(response, expected_response)
print("响应体JSON相等断言通过")

# 断言响应体JSON包含
partial_response = {"status": "success"}
AssertEnhancer.assert_response_json_contains(response, partial_response)
print("响应体JSON包含断言通过")

# 断言响应体JSON路径存在
AssertEnhancer.assert_response_json_path_exists(response, "data")
print("响应体JSON路径存在断言通过")

# 断言响应体JSON路径值
AssertEnhancer.assert_response_json_path_value(response, "status", "success")
print("响应体JSON路径值断言通过")
```

## 异常断言

```python
# 断言代码抛出异常
def divide_by_zero():
    return 1 / 0

AssertEnhancer.assert_raises(divide_by_zero, ZeroDivisionError)
print("异常断言通过")

# 断言代码不抛出异常
def safe_divide():
    return 1 / 1

AssertEnhancer.assert_not_raises(safe_divide)
print("无异常断言通过")
```

## 高级功能

### 自定义错误消息

```python
# 使用自定义错误消息
AssertEnhancer.assert_equals(10, 10, message="数值应该相等")
print("带自定义错误消息的断言通过")

# 带格式化的错误消息
AssertEnhancer.assert_equals(10, 10, message="期望值: {}, 实际值: {}")
print("带格式化错误消息的断言通过")
```

### 类型断言

```python
# 断言类型
AssertEnhancer.assert_type("Hello", str)
print("类型断言通过")

# 断言不是类型
AssertEnhancer.assert_not_type("Hello", int)
print("非类型断言通过")
```

### 正则表达式断言

```python
# 断言字符串匹配正则表达式
AssertEnhancer.assert_matches_regex("test@example.com", r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
print("正则表达式断言通过")

# 断言字符串不匹配正则表达式
AssertEnhancer.assert_not_matches_regex("test", r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
print("正则表达式不匹配断言通过")
```

### 时间断言

```python
from datetime import datetime, timedelta

# 断言时间在范围内
now = datetime.now()
past = now - timedelta(hours=1)
future = now + timedelta(hours=1)

AssertEnhancer.assert_datetime_between(now, past, future)
print("时间在范围内断言通过")

# 断言时间在过去
AssertEnhancer.assert_datetime_in_past(past)
print("时间在过去断言通过")

# 断言时间在未来
AssertEnhancer.assert_datetime_in_future(future)
print("时间在未来断言通过")
```

## 与测试框架集成

### 与 pytest 集成

```python
import pytest
from btools import AssertEnhancer

class TestAPI:
    def test_get_users(self):
        import requests
        response = requests.get("https://api.example.com/users")
        
        # 断言响应状态码
        AssertEnhancer.assert_response_status(response, 200)
        
        # 断言响应体
        AssertEnhancer.assert_response_json_contains(response, {"status": "success"})
        
        # 断言用户列表非空
        json_data = response.json()
        AssertEnhancer.assert_not_empty(json_data.get("data", []))
```

### 与 unittest 集成

```python
import unittest
import requests
from btools import AssertEnhancer

class TestAPIAssertions(unittest.TestCase):
    def test_user_profile(self):
        response = requests.get("https://api.example.com/users/1")
        
        # 断言响应状态码
        AssertEnhancer.assert_response_status(response, 200)
        
        # 断言用户信息
        user_data = response.json()
        AssertEnhancer.assert_json_path_exists(user_data, "user.id")
        AssertEnhancer.assert_json_path_value(user_data, "user.id", 1)
        AssertEnhancer.assert_json_path_exists(user_data, "user.name")

if __name__ == '__main__':
    unittest.main()
```

## 常见问题

### 断言失败处理

当断言失败时，`AssertEnhancer` 会抛出 `AssertionError` 异常，包含详细的错误信息。在测试框架中，这会被捕获并标记为测试失败。

### 自定义断言方法

如果需要自定义断言方法，可以继承 `AssertEnhancer` 类并添加新的方法：

```python
class CustomAssertEnhancer(AssertEnhancer):
    @staticmethod
    def assert_user_active(user):
        """断言用户状态为活跃"""
        assert user.get("status") == "active", f"用户状态应为 'active'，实际为 '{user.get('status')}'"

# 使用自定义断言
CustomAssertEnhancer.assert_user_active({"status": "active", "name": "John"})
print("自定义断言通过")
```

### 性能考虑

对于大型数据集的断言，应注意性能影响：

- 对于大型JSON对象，`assert_json_equals` 可能会比较慢
- 对于大型列表，`assert_list_contains` 可能会比较慢
- 对于复杂的正则表达式，`assert_matches_regex` 可能会比较慢

在这种情况下，建议使用更具体的断言方法，如 `assert_json_path_value` 或 `assert_dict_contains`，以减少比较的范围。