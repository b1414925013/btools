# AssertUtil 使用指南

`AssertUtil` 是一个断言工具类，提供了丰富的断言方法，用于验证各种条件。

## 功能特性

- 布尔值断言（真/假）
- 空值断言（None/非None）
- 相等性断言
- 空集合/字符串断言
- 数字断言（零/正/负/大小比较）
- 类型断言
- 集合包含断言
- 正则匹配断言
- 异常断言
- 字符串前缀/后缀断言
- 长度断言
- 身份相等断言

## 基本用法

### 导入 AssertUtil

```python
from btools.core.basic.assertutils import AssertUtil
```

### 布尔值断言

```python
from btools.core.basic.assertutils import AssertUtil

# 断言为真
AssertUtil.is_true(True)

# 断言为假
AssertUtil.is_false(False)
```

### 空值断言

```python
from btools.core.basic.assertutils import AssertUtil

# 断言为None
AssertUtil.is_none(None)

# 断言不为None
AssertUtil.is_not_none("hello")
```

### 相等性断言

```python
from btools.core.basic.assertutils import AssertUtil

# 断言相等
AssertUtil.equals(1, 1)
AssertUtil.equals("test", "test")

# 断言不相等
AssertUtil.not_equals(1, 2)
```

### 空集合/字符串断言

```python
from btools.core.basic.assertutils import AssertUtil

# 断言为空
AssertUtil.is_empty("")
AssertUtil.is_empty([])
AssertUtil.is_empty({})
AssertUtil.is_empty(None)

# 断言不为空
AssertUtil.is_not_empty("hello")
AssertUtil.is_not_empty([1, 2, 3])
```

### 数字断言

```python
from btools.core.basic.assertutils import AssertUtil

# 断言为0
AssertUtil.is_zero(0)

# 断言不为0
AssertUtil.is_not_zero(1)

# 断言为正数
AssertUtil.is_positive(5)

# 断言为负数
AssertUtil.is_negative(-3)

# 断言大于
AssertUtil.greater(5, 3)

# 断言大于等于
AssertUtil.greater_or_equal(5, 5)

# 断言小于
AssertUtil.less(3, 5)

# 断言小于等于
AssertUtil.less_or_equal(5, 5)

# 断言在范围内
AssertUtil.between(5, 1, 10)
```

### 类型断言

```python
from btools.core.basic.assertutils import AssertUtil

# 断言为指定类型
AssertUtil.is_instance(123, int)
AssertUtil.is_instance("test", str)
AssertUtil.is_instance([1, 2], list)

# 断言不为指定类型
AssertUtil.is_not_instance(123, str)
```

### 集合包含断言

```python
from btools.core.basic.assertutils import AssertUtil

# 断言包含元素
AssertUtil.contains("hello world", "world")
AssertUtil.contains([1, 2, 3], 2)
AssertUtil.contains({"a": 1, "b": 2}, "a")

# 断言不包含元素
AssertUtil.not_contains("hello world", "test")

# 断言为子集
AssertUtil.is_subset([1, 2], [1, 2, 3])

# 断言为超集
AssertUtil.is_superset([1, 2, 3], [1, 2])
```

### 正则匹配断言

```python
from btools.core.basic.assertutils import AssertUtil

# 断言匹配正则
AssertUtil.matches(r'^\d+$', '12345')
AssertUtil.matches(r'^[a-zA-Z]+$', 'hello')

# 断言不匹配正则
AssertUtil.not_matches(r'^\d+$', 'abc123')
```

### 异常断言

```python
from btools.core.basic.assertutils import AssertUtil

# 断言抛出异常
def raise_value_error():
    raise ValueError("test error")

AssertUtil.raises(ValueError, raise_value_error)

# 断言不抛出异常
def no_error():
    return 123

AssertUtil.does_not_raise(no_error)
```

### 字符串前缀/后缀断言

```python
from btools.core.basic.assertutils import AssertUtil

# 断言以指定前缀开头
AssertUtil.starts_with("hello world", "hello")

# 断言以指定后缀结尾
AssertUtil.ends_with("hello world", "world")
```

### 长度断言

```python
from btools.core.basic.assertutils import AssertUtil

# 断言具有指定长度
AssertUtil.has_length([1, 2, 3], 3)
AssertUtil.has_length("hello", 5)
AssertUtil.has_length({"a": 1, "b": 2}, 2)
```

### 身份相等断言

```python
from btools.core.basic.assertutils import AssertUtil

# 断言是同一个对象（身份相等）
a = [1, 2, 3]
b = a
AssertUtil.is_same(a, b)

# 断言不是同一个对象（身份不相等）
c = [1, 2, 3]
AssertUtil.is_not_same(a, c)
```

## 自定义错误消息

所有断言方法都支持自定义错误消息：

```python
from btools.core.basic.assertutils import AssertUtil

try:
    AssertUtil.equals(1, 2, "数值不相等，期望1，实际2")
except AssertionError as e:
    print(e)  # 数值不相等，期望1，实际2
```

## JSON断言

```python
from btools import AssertUtil

# 断言JSON相等
expected_json = {"name": "John", "age": 30}
actual_json = {"name": "John", "age": 30}
AssertUtil.assert_json_equals(actual_json, expected_json)
print("JSON相等断言通过")

# 断言JSON包含
partial_json = {"name": "John"}
full_json = {"name": "John", "age": 30, "city": "New York"}
AssertUtil.assert_json_contains(full_json, partial_json)
print("JSON包含断言通过")

# 断言JSON路径存在
json_data = {"user": {"profile": {"name": "John"}}}
AssertUtil.assert_json_path_exists(json_data, "user.profile.name")
print("JSON路径存在断言通过")

# 断言JSON路径值
AssertUtil.assert_json_path_value(json_data, "user.profile.name", "John")
print("JSON路径值断言通过")
```

## HTTP响应断言

### 响应状态码断言

```python
import requests
from btools import AssertUtil

response = requests.get("https://api.example.com/users")
AssertUtil.assert_response_status(response, 200)
print("响应状态码断言通过")

# 断言响应状态码在成功范围内 (200-299)
AssertUtil.assert_response_success(response)
print("响应成功断言通过")
```

### 响应头断言

```python
# 断言响应头存在
AssertUtil.assert_response_header_exists(response, "Content-Type")
print("响应头存在断言通过")

# 断言响应头值
AssertUtil.assert_response_header_value(response, "Content-Type", "application/json")
print("响应头值断言通过")
```

### 响应体断言

```python
# 断言响应体JSON相等
expected_response = {"status": "success", "data": []}
AssertUtil.assert_response_json(response, expected_response)
print("响应体JSON相等断言通过")

# 断言响应体JSON包含
partial_response = {"status": "success"}
AssertUtil.assert_response_json_contains(response, partial_response)
print("响应体JSON包含断言通过")

# 断言响应体JSON路径存在
AssertUtil.assert_response_json_path_exists(response, "data")
print("响应体JSON路径存在断言通过")

# 断言响应体JSON路径值
AssertUtil.assert_response_json_path_value(response, "status", "success")
print("响应体JSON路径值断言通过")
```

## 异常断言

```python
from btools import AssertUtil

# 断言代码抛出异常
def divide_by_zero():
    return 1 / 0

AssertUtil.assert_raises(divide_by_zero, ZeroDivisionError)
print("异常断言通过")

# 断言代码不抛出异常
def safe_divide():
    return 1 / 1

AssertUtil.assert_not_raises(safe_divide)
print("无异常断言通过")
```

## 高级功能

### 类型断言

```python
from btools import AssertUtil

# 断言类型
AssertUtil.assert_type("Hello", str)
print("类型断言通过")

# 断言不是类型
AssertUtil.assert_not_type("Hello", int)
print("非类型断言通过")
```

### 正则表达式断言

```python
from btools import AssertUtil

# 断言字符串匹配正则表达式
AssertUtil.assert_matches_regex("test@example.com", r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
print("正则表达式断言通过")

# 断言字符串不匹配正则表达式
AssertUtil.assert_not_matches_regex("test", r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
print("正则表达式不匹配断言通过")
```

### 时间断言

```python
from datetime import datetime, timedelta
from btools import AssertUtil

# 断言时间在范围内
now = datetime.now()
past = now - timedelta(hours=1)
future = now + timedelta(hours=1)

AssertUtil.assert_datetime_between(now, past, future)
print("时间在范围内断言通过")

# 断言时间在过去
AssertUtil.assert_datetime_in_past(past)
print("时间在过去断言通过")

# 断言时间在未来
AssertUtil.assert_datetime_in_future(future)
print("时间在未来断言通过")
```

## 与测试框架集成

### 与 pytest 集成

```python
import pytest
from btools import AssertUtil

class TestAPI:
    def test_get_users(self):
        import requests
        response = requests.get("https://api.example.com/users")
        
        # 断言响应状态码
        AssertUtil.assert_response_status(response, 200)
        
        # 断言响应体
        AssertUtil.assert_response_json_contains(response, {"status": "success"})
        
        # 断言用户列表非空
        json_data = response.json()
        AssertUtil.is_not_empty(json_data.get("data", []))
```

### 与 unittest 集成

```python
import unittest
import requests
from btools import AssertUtil

class TestAPIAssertions(unittest.TestCase):
    def test_user_profile(self):
        response = requests.get("https://api.example.com/users/1")
        
        # 断言响应状态码
        AssertUtil.assert_response_status(response, 200)
        
        # 断言用户信息
        user_data = response.json()
        AssertUtil.assert_json_path_exists(user_data, "user.id")
        AssertUtil.assert_json_path_value(user_data, "user.id", 1)
        AssertUtil.assert_json_path_exists(user_data, "user.name")

if __name__ == '__main__':
    unittest.main()
```

## 常见问题

### 断言失败处理

当断言失败时，`AssertUtil` 会抛出 `AssertionError` 异常，包含详细的错误信息。在测试框架中，这会被捕获并标记为测试失败。

### 自定义断言方法

如果需要自定义断言方法，可以继承 `AssertUtil` 类并添加新的方法：

```python
class CustomAssertUtil(AssertUtil):
    @staticmethod
    def assert_user_active(user):
        """断言用户状态为活跃"""
        assert user.get("status") == "active", f"用户状态应为 'active'，实际为 '{user.get('status')}'"

# 使用自定义断言
CustomAssertUtil.assert_user_active({"status": "active", "name": "John"})
print("自定义断言通过")
```

### 性能考虑

对于大型数据集的断言，应注意性能影响：

- 对于大型JSON对象，`assert_json_equals` 可能会比较慢
- 对于大型列表，`contains` 可能会比较慢
- 对于复杂的正则表达式，`matches` 可能会比较慢

在这种情况下，建议使用更具体的断言方法，如 `assert_json_path_value` 或 `assert_dict_contains`，以减少比较的范围。
