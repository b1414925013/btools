# MockUtils 使用指南

`MockUtils` 类提供了高级模拟工具，支持复杂对象和行为模拟。

## 基本使用

### 创建简单 Mock 对象

```python
from btools import MockUtils

# 创建简单的 Mock 对象
mock = MockUtils.create_mock()

# 设置返回值
mock.some_method.return_value = "mocked result"

# 使用 Mock
result = mock.some_method()
print(result)  # "mocked result"

# 验证调用
assert mock.some_method.called
assert mock.some_method.call_count == 1
```

### Mock 函数

```python
from btools import MockUtils

# Mock 一个函数
def original_function():
    return "original"

# 使用 Mock
with MockUtils.patch("__main__.original_function") as mock_func:
    mock_func.return_value = "mocked"
    result = original_function()
    print(result)  # "mocked"

# 离开 with 块后恢复
print(original_function())  # "original"
```

### Mock 类

```python
from btools import MockUtils

class MyClass:
    def method(self):
        return "original"

# Mock 类方法
with MockUtils.patch_object(MyClass, 'method') as mock_method:
    mock_method.return_value = "mocked"
    obj = MyClass()
    result = obj.method()
    print(result)  # "mocked"
```

## 高级功能

### 模拟异常

```python
from btools import MockUtils

# 模拟异常
mock = MockUtils.create_mock()
mock.some_method.side_effect = ValueError("Something went wrong")

try:
    mock.some_method()
except ValueError as e:
    print(e)  # "Something went wrong"
```

### 多次调用返回不同值

```python
from btools import MockUtils

# 设置多次调用的返回值
mock = MockUtils.create_mock()
mock.some_method.side_effect = [1, 2, 3, StopIteration]

print(mock.some_method())  # 1
print(mock.some_method())  # 2
print(mock.some_method())  # 3
```

### 验证调用参数

```python
from btools import MockUtils
from unittest.mock import call

# 验证调用参数
mock = MockUtils.create_mock()
mock.process(1, 2, key="value")
mock.process(3, 4)

# 验证第一次调用
mock.process.assert_called_with(1, 2, key="value")

# 验证所有调用
mock.process.assert_has_calls([
    call(1, 2, key="value"),
    call(3, 4)
])

# 验证调用顺序
mock.process.assert_any_call(3, 4)
```

### 创建复杂的 Mock 对象

```python
from btools import MockUtils

# 创建带有属性和方法的 Mock
mock = MockUtils.create_mock(spec_set=['name', 'age', 'greet'])
mock.name = "Mock User"
mock.age = 30
mock.greet.return_value = "Hello!"

print(mock.name)  # "Mock User"
print(mock.greet())  # "Hello!"
```

### Mock 属性

```python
from btools import MockUtils
from unittest.mock import PropertyMock

# Mock 属性
class MyClass:
    @property
    def value(self):
        return 42

with MockUtils.patch_object(MyClass, 'value', new_callable=PropertyMock) as mock_prop:
    mock_prop.return_value = 100
    obj = MyClass()
    print(obj.value)  # 100
```

## 异步 Mock

```python
from btools import MockUtils

# Mock 异步函数
async def async_function():
    return "original"

mock_async = MockUtils.create_async_mock()
mock_async.return_value = "mocked"

# 使用
result = await mock_async()
print(result)  # "mocked"
```

## 魔术 Mock

```python
from btools import MockUtils

# 使用 MagicMock
mock = MockUtils.create_magic_mock()

# 可以像调用函数一样调用
mock()

# 可以访问任意属性
mock.foo.bar.baz()

# 可以迭代
for item in mock:
    pass

# 可以使用 len
len(mock)
```

## Mock 上下文管理器

```python
from btools import MockUtils

# Mock 上下文管理器
mock_file = MockUtils.create_mock()
mock_file.__enter__.return_value.read.return_value = "file content"

with mock_file as f:
    content = f.read()

print(content)  # "file content"
```

## 重置 Mock

```python
from btools import MockUtils

# 创建 Mock
mock = MockUtils.create_mock()
mock.some_method()

# 重置 Mock
MockUtils.reset_mock(mock)
assert not mock.some_method.called
```

## 常见 Mock 模式

### Mock API 调用

```python
from btools import MockUtils
import requests

# Mock requests.get
with MockUtils.patch('requests.get') as mock_get:
    mock_response = MockUtils.create_mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"data": "test"}
    mock_get.return_value = mock_response
    
    response = requests.get("https://api.example.com")
    assert response.status_code == 200
    assert response.json() == {"data": "test"}
```

### Mock 数据库

```python
from btools import MockUtils

# Mock 数据库查询
db_mock = MockUtils.create_mock()
db_mock.query.return_value.filter.return_value.first.return_value = User(id=1, name="Test")

user = db_mock.query(User).filter(User.id == 1).first()
assert user.name == "Test"
```
