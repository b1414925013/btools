# ExceptionUtils 使用指南

`ExceptionUtils` 是一个异常工具类，提供了丰富的异常处理方法，包括获取堆栈跟踪、获取异常消息、获取异常类型、安全调用等功能。

## 功能特性

- 获取堆栈跟踪
- 获取异常消息
- 获取异常类型
- 安全调用函数
- 带默认值的安全调用

## 基本用法

### 导入

```python
from btools import ExceptionUtils
```

### 示例

#### 获取堆栈跟踪

```python
try:
    raise ValueError("Test error")
except Exception as e:
    stack_trace = ExceptionUtils.get_stack_trace(e)
    print(stack_trace)
    # 输出: 包含异常堆栈信息的字符串
```

#### 获取异常消息

```python
try:
    raise ValueError("Test error")
except Exception as e:
    message = ExceptionUtils.get_exception_message(e)
    print(message)  # 输出: Test error
```

#### 获取异常类型

```python
try:
    raise ValueError("Test error")
except Exception as e:
    exception_type = ExceptionUtils.get_exception_type(e)
    print(exception_type)  # 输出: ValueError
```

#### 安全调用函数

```python
# 定义正常函数
def test_func():
    return "Success"

# 定义会抛出异常的函数
def error_func():
    raise ValueError("Test error")

# 安全调用正常函数
result = ExceptionUtils.safe_call(test_func)
print(result)  # 输出: Success

# 安全调用会抛出异常的函数
result = ExceptionUtils.safe_call(error_func)
print(result)  # 输出: None
```

#### 带默认值的安全调用

```python
# 定义会抛出异常的函数
def error_func():
    raise ValueError("Test error")

# 带默认值的安全调用
result = ExceptionUtils.safe_call_with_default(error_func, "Default")
print(result)  # 输出: Default
```

## 高级用法

### 安全调用带参数的函数

```python
# 定义带参数的函数
def add(a, b):
    if a < 0 or b < 0:
        raise ValueError("Negative numbers not allowed")
    return a + b

# 安全调用带参数的函数
result1 = ExceptionUtils.safe_call(add, 1, 2)
print(result1)  # 输出: 3

result2 = ExceptionUtils.safe_call(add, -1, 2)
print(result2)  # 输出: None

# 带默认值的安全调用
result3 = ExceptionUtils.safe_call_with_default(add, "Error", -1, 2)
print(result3)  # 输出: Error
```

### 安全调用带关键字参数的函数

```python
# 定义带关键字参数的函数
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

# 安全调用带关键字参数的函数
result1 = ExceptionUtils.safe_call(divide, a=10, b=2)
print(result1)  # 输出: 5.0

result2 = ExceptionUtils.safe_call(divide, a=10, b=0)
print(result2)  # 输出: None

# 带默认值的安全调用
result3 = ExceptionUtils.safe_call_with_default(divide, "Error", a=10, b=0)
print(result3)  # 输出: Error
```

## 注意事项

1. `safe_call()` 和 `safe_call_with_default()` 方法会捕获所有异常，包括 `KeyboardInterrupt` 和 `SystemExit`，因此在使用时需要注意。
2. 获取堆栈跟踪可能会返回较长的字符串，在日志记录时需要注意。

## 总结

`ExceptionUtils` 提供了全面的异常处理功能，简化了异常处理的复杂度，使代码更加简洁易读。无论是基本的异常信息获取还是高级的安全调用，`ExceptionUtils` 都能满足你的需求。