# DecoratorUtil 使用指南

`DecoratorUtil` 是一个装饰器工具类，提供了创建、管理和使用装饰器的功能，包括计时、日志、缓存、重试、单例等常用装饰器的创建方法。

## 功能特性

- 创建各种常用装饰器（计时、日志、缓存、重试、单例等）
- 组合多个装饰器
- 检查对象是否为装饰器
- 获取被装饰的原始函数
- 获取装饰器链
- 创建条件装饰器

## 基本用法

### 基础装饰器创建

`createDecorator` 方法用于创建一个简单的基础装饰器，它会保留原始函数的元数据并直接调用原始函数，不添加任何额外功能。

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 定义一个普通函数
def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

# 使用 createDecorator 创建装饰器
greet_decorator = DecoratorUtil.createDecorator(greet)

# 使用装饰器
result = greet_decorator("World")
print(result)  # 输出: Hello, World!
print(f"装饰器名称: {greet_decorator.__name__}")  # 输出: greet
print(f"装饰器文档: {greet_decorator.__doc__}")  # 输出: 问候函数
```

### 作为装饰器工厂使用

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 定义一个装饰器函数
def make_bold(func):
    """将文本变为粗体的装饰器"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper

# 使用 createDecorator 创建装饰器
bold_decorator = DecoratorUtil.createDecorator(make_bold)

# 使用装饰器
@bold_decorator
def get_greeting(name):
    return f"Hello, {name}!"

result = get_greeting("Alice")
print(result)  # 输出: <b>Hello, Alice!</b>
```

### 计时装饰器

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 创建计时装饰器
timer_decorator = DecoratorUtil.createTimerDecorator()

# 使用装饰器
@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "完成"

# 执行函数
result = slow_function()
# 输出: slow_function 执行耗时: 1.0000 秒
print(result)
```

### 日志装饰器

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 创建日志装饰器
logging_decorator = DecoratorUtil.createLoggingDecorator()

# 使用装饰器
@logging_decorator
def risky_function():
    print("执行中...")
    if 1 == 1:
        raise Exception("出错了!")
    return "成功"

# 执行函数
try:
    result = risky_function()
except Exception as e:
    pass
# 输出:
# [开始] risky_function
# 执行中...
# [失败] risky_function: 出错了!
```

### 缓存装饰器

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 创建缓存装饰器
cache_decorator = DecoratorUtil.createCacheDecorator()

# 使用装饰器
@cache_decorator
def expensive_calculation(x, y):
    print(f"计算 {x} + {y}")
    import time
    time.sleep(1)  # 模拟耗时计算
    return x + y

# 第一次调用（会执行计算）
result1 = expensive_calculation(10, 20)
print(f"结果1: {result1}")

# 第二次调用（会从缓存获取，不会执行计算）
result2 = expensive_calculation(10, 20)
print(f"结果2: {result2}")
```

### 重试装饰器

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 创建重试装饰器
retry_decorator = DecoratorUtil.createRetryDecorator(max_retries=3, delay=0.5)

# 使用装饰器
@retry_decorator
def flaky_function():
    import random
    if random.random() < 0.7:
        raise Exception("随机失败")
    return "成功"

# 执行函数（最多重试3次）
result = flaky_function()
print(f"结果: {result}")
```

### 单例装饰器

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 创建单例装饰器
singleton_decorator = DecoratorUtil.createSingletonDecorator()

# 使用装饰器
@singleton_decorator
class DatabaseConnection:
    def __init__(self, connection_string):
        print(f"创建数据库连接: {connection_string}")
        self.connection_string = connection_string

# 第一次创建（会执行初始化）
db1 = DatabaseConnection("localhost:5432")

# 第二次创建（不会执行初始化，会返回同一个实例）
db2 = DatabaseConnection("different:5432")

# 验证是否为同一个实例
print(f"db1 和 db2 是同一个实例: {db1 is db2}")
print(f"db1 连接字符串: {db1.connection_string}")
print(f"db2 连接字符串: {db2.connection_string}")  # 仍然是第一次的连接字符串
```

### 过时警告装饰器

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 创建过时警告装饰器
deprecation_decorator = DecoratorUtil.createDeprecationDecorator("此方法已过时，请使用 new_function() 代替")

# 使用装饰器
@deprecation_decorator
def old_function():
    return "旧方法"

# 执行函数（会发出警告）
result = old_function()
print(result)
```

### 权限检查装饰器

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 创建权限检查装饰器
permission_decorator = DecoratorUtil.createPermissionDecorator("admin")

# 模拟用户类
class User:
    def __init__(self, permissions):
        self.permissions = permissions

# 使用装饰器
@permission_decorator
def admin_only_function(user):
    return "管理员操作成功"

# 测试有权限的用户
admin_user = User(["admin"])
try:
    result = admin_only_function(admin_user)
    print(result)
except PermissionError as e:
    print(f"错误: {e}")

# 测试无权限的用户
regular_user = User(["user"])
try:
    result = admin_only_function(regular_user)
    print(result)
except PermissionError as e:
    print(f"错误: {e}")
```

### 速率限制装饰器

```python
from btools.core.basic.decoratorutils import DecoratorUtil, RateLimitError

# 创建速率限制装饰器（1秒内最多调用2次）
rate_limit_decorator = DecoratorUtil.createRateLimitDecorator(max_calls=2, period=1)

# 使用装饰器
@rate_limit_decorator
def api_call():
    return "API 调用成功"

# 测试速率限制
try:
    print(api_call())  # 第一次调用，成功
    print(api_call())  # 第二次调用，成功
    print(api_call())  # 第三次调用，应该失败
except RateLimitError as e:
    print(f"速率限制: {e}")
```

## 高级用法

### 组合多个装饰器

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 创建多个装饰器
timer_decorator = DecoratorUtil.createTimerDecorator()
logging_decorator = DecoratorUtil.createLoggingDecorator()
cache_decorator = DecoratorUtil.createCacheDecorator()

# 组合装饰器
combined_decorator = DecoratorUtil.combineDecorators(timer_decorator, logging_decorator, cache_decorator)

# 使用组合装饰器
@combined_decorator
def complex_function(x, y):
    import time
    time.sleep(0.5)
    return x + y

# 执行函数
print(complex_function(10, 20))  # 第一次执行，会计时、记录日志
print(complex_function(10, 20))  # 第二次执行，会从缓存获取，仍然会计时和记录日志
```

### 检查装饰器

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 创建装饰器
timer_decorator = DecoratorUtil.createTimerDecorator()

# 定义函数
@timer_decorator
def decorated_function():
    return "装饰过的函数"

def regular_function():
    return "普通函数"

# 检查是否为装饰器
print(f"decorated_function 是装饰器: {DecoratorUtil.isDecorator(decorated_function)}")
print(f"regular_function 是装饰器: {DecoratorUtil.isDecorator(regular_function)}")

# 获取原始函数
original_function = DecoratorUtil.getOriginalFunction(decorated_function)
print(f"原始函数名: {original_function.__name__}")
```

### 获取装饰器链

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 创建装饰器
timer_decorator = DecoratorUtil.createTimerDecorator()
logging_decorator = DecoratorUtil.createLoggingDecorator()

# 应用多个装饰器
@timer_decorator
@logging_decorator
def multi_decorated_function():
    return "多重装饰的函数"

# 获取装饰器链
chain = DecoratorUtil.getDecoratorChain(multi_decorated_function)
print(f"装饰器链长度: {len(chain)}")
print(f"函数名列表: {[func.__name__ for func in chain]}")
```

### 条件装饰器

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 创建条件函数
def should_cache(args, kwargs):
    # 只对大于10的参数进行缓存
    return args and len(args) > 0 and args[0] > 10

# 创建缓存装饰器
cache_decorator = DecoratorUtil.createCacheDecorator()

# 创建条件装饰器
conditional_cache_decorator = DecoratorUtil.createConditionalDecorator(should_cache, cache_decorator)

# 计数调用次数
call_count = 0

# 使用条件装饰器
@conditional_cache_decorator
def conditional_function(x):
    nonlocal call_count
    call_count += 1
    print(f"执行函数，参数: {x}")
    return x * 2

# 测试不满足条件的情况（不会缓存）
print(conditional_function(5))  # 会执行
print(f"调用次数: {call_count}")
print(conditional_function(5))  # 会再次执行
print(f"调用次数: {call_count}")

# 测试满足条件的情况（会缓存）
print(conditional_function(15))  # 会执行
print(f"调用次数: {call_count}")
print(conditional_function(15))  # 不会执行，从缓存获取
print(f"调用次数: {call_count}")
```

## 自定义装饰器

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 定义装饰器函数
def custom_decorator(func):
    def wrapper(*args, **kwargs):
        print("自定义装饰器开始")
        result = func(*args, **kwargs)
        print("自定义装饰器结束")
        return result
    return wrapper

# 使用装饰器
@custom_decorator
def my_function():
    print("函数执行中")
    return "完成"

# 执行函数
result = my_function()
print(result)
```

## 注意事项

1. **装饰器顺序**：当组合多个装饰器时，装饰器的顺序很重要，它们会按照从下到上的顺序执行。

2. **缓存装饰器**：默认的缓存装饰器使用简单的字符串键，对于复杂参数可能会有问题，建议在生产环境中使用更健壮的缓存方案。

3. **速率限制装饰器**：默认的速率限制装饰器是基于内存的，在多进程环境中可能不准确。

4. **权限检查装饰器**：默认的权限检查装饰器假设第一个参数是用户对象，并且有 `permissions` 属性，实际使用时可能需要根据具体情况修改。

5. **单例装饰器**：单例装饰器会保持第一次创建时的实例，即使后续传入不同的参数。

## 完整示例

```python
from btools.core.basic.decoratorutils import DecoratorUtil

# 创建各种装饰器
timer_decorator = DecoratorUtil.createTimerDecorator()
logging_decorator = DecoratorUtil.createLoggingDecorator()
cache_decorator = DecoratorUtil.createCacheDecorator()
retry_decorator = DecoratorUtil.createRetryDecorator(max_retries=3, delay=0.1)

# 组合装饰器
@timer_decorator
@logging_decorator
@cache_decorator
@retry_decorator
def complex_operation(x, y):
    print(f"执行操作: {x} * {y}")
    # 模拟偶尔失败
    import random
    if random.random() < 0.5:
        raise Exception("随机失败")
    # 模拟耗时操作
    import time
    time.sleep(0.2)
    return x * y

# 执行操作
print("第一次执行:")
try:
    result1 = complex_operation(10, 20)
    print(f"结果: {result1}")
except Exception as e:
    print(f"最终失败: {e}")

print("\n第二次执行（应该从缓存获取）:")
try:
    result2 = complex_operation(10, 20)
    print(f"结果: {result2}")
except Exception as e:
    print(f"最终失败: {e}")

# 检查装饰器
print(f"\ncomplex_operation 是装饰器: {DecoratorUtil.isDecorator(complex_operation)}")

# 获取原始函数
original = DecoratorUtil.getOriginalFunction(complex_operation)
print(f"原始函数名: {original.__name__}")

# 获取装饰器链
chain = DecoratorUtil.getDecoratorChain(complex_operation)
print(f"装饰器链长度: {len(chain)}")
```