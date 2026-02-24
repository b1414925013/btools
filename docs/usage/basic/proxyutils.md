# ProxyUtil 使用指南

`ProxyUtil` 是一个切面代理工具类，提供了动态代理创建、切面增强、方法拦截等功能，类似于 Java 中的 AOP（面向切面编程）。

## 功能特性

- 创建动态代理（支持类和实例）
- 切面增强（支持 before、after、around、on_exception 回调）
- 内置计时切面
- 内置日志切面
- 内置事务切面
- 代理对象管理

## 基本用法

### 创建动态代理

```python
from btools import ProxyUtil

# 定义一个目标类
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

# 创建代理对象
def before_callback(target, method_name, args, kwargs):
    print(f"执行前: {method_name}({args}, {kwargs})")

def after_callback(target, method_name, args, kwargs, result):
    print(f"执行后: {method_name} 返回 {result}")

calculator = Calculator()
proxy = ProxyUtil.createProxy(calculator, before=before_callback, after=after_callback)

# 使用代理对象
result = proxy.add(1, 2)  # 会触发回调函数
print(f"结果: {result}")
```

### 创建切面

```python
from btools import ProxyUtil

# 定义一个目标类
class Calculator:
    def add(self, a, b):
        return a + b

# 创建切面
def around_callback(target, method_name, args, kwargs, proceed):
    print(f"环绕前: {method_name}")
    result = proceed()  # 执行原始方法
    print(f"环绕后: {method_name}")
    return result

def on_exception_callback(target, method_name, args, kwargs, e):
    print(f"异常: {method_name} - {e}")

calculator = Calculator()
aspect = ProxyUtil.createAspect(
    calculator,
    around=around_callback,
    on_exception=on_exception_callback
)

# 使用带切面的对象
result = aspect.add(1, 2)
print(f"结果: {result}")
```

## 内置切面

### 计时切面

```python
from btools import ProxyUtil

# 定义一个目标类
class Calculator:
    def add(self, a, b):
        import time
        time.sleep(0.1)  # 模拟耗时操作
        return a + b

# 创建计时切面
calculator = Calculator()
timer_proxy = ProxyUtil.createTimerAspect(calculator)

# 使用计时代理
result = timer_proxy.add(1, 2)  # 会打印执行时间
print(f"结果: {result}")
```

### 日志切面

```python
from btools import ProxyUtil

# 定义一个目标类
class Calculator:
    def add(self, a, b):
        return a + b

# 创建日志切面
calculator = Calculator()
log_proxy = ProxyUtil.createLoggingAspect(calculator)

# 使用日志代理
result = log_proxy.add(1, 2)  # 会打印详细的日志信息
print(f"结果: {result}")
```

### 事务切面

```python
from btools import ProxyUtil

# 定义一个目标类
class UserService:
    def create_user(self, name, email):
        print(f"创建用户: {name}, {email}")
        # 模拟事务操作
        return {"id": 1, "name": name, "email": email}

# 模拟事务操作
def begin_transaction():
    print("开始事务")
    return "tx123"

def commit_transaction(tx):
    print(f"提交事务: {tx}")

def rollback_transaction(tx):
    print(f"回滚事务: {tx}")

# 创建事务切面
user_service = UserService()
tx_proxy = ProxyUtil.createTransactionAspect(
    user_service,
    begin_transaction=begin_transaction,
    commit_transaction=commit_transaction,
    rollback_transaction=rollback_transaction
)

# 使用事务代理
try:
    user = tx_proxy.create_user("John", "john@example.com")
    print(f"创建成功: {user}")
except Exception as e:
    print(f"创建失败: {e}")
```

## 代理对象管理

```python
from btools import ProxyUtil

# 定义一个目标类
class Calculator:
    def add(self, a, b):
        return a + b

# 创建代理对象
calculator = Calculator()
proxy = ProxyUtil.createProxy(calculator)

# 检查是否为代理对象
is_proxy = ProxyUtil.isProxy(proxy)
print(f"是否为代理对象: {is_proxy}")

# 获取目标对象
target = ProxyUtil.getTarget(proxy)
print(f"目标对象: {target}")

# 获取代理配置
config = ProxyUtil.getProxyConfig(proxy)
print(f"代理配置: {config}")

# 添加额外的切面
proxy_with_timer = ProxyUtil.addAspect(proxy, before=lambda *args: print("额外的前置回调"))

# 移除切面，获取原始对象
original = ProxyUtil.removeAspect(proxy)
print(f"原始对象: {original}")
```

## 高级用法

### 为类创建代理

```python
from btools import ProxyUtil

# 定义一个目标类
class Calculator:
    def __init__(self, name):
        self.name = name
    
    def add(self, a, b):
        return a + b

# 为类创建代理
ProxyCalculator = ProxyUtil.createProxy(Calculator, before=lambda target, method, args, kwargs: print(f"执行 {method}"))

# 使用代理类创建实例
calculator = ProxyCalculator("My Calculator")
result = calculator.add(1, 2)
print(f"结果: {result}")
```

### 链式调用多个切面

```python
from btools import ProxyUtil

# 定义一个目标类
class Calculator:
    def add(self, a, b):
        import time
        time.sleep(0.1)
        return a + b

# 创建原始对象
calculator = Calculator()

# 添加计时切面
timer_proxy = ProxyUtil.createTimerAspect(calculator)

# 在计时切面上添加日志切面
log_timer_proxy = ProxyUtil.createLoggingAspect(timer_proxy)

# 使用链式切面
result = log_timer_proxy.add(1, 2)
print(f"结果: {result}")
```

## 注意事项

1. 代理对象会拦截所有非私有方法（不以下划线开头的方法）
2. 对于内置方法（如 `__init__`, `__str__` 等），代理不会拦截
3. 创建代理时，会为目标对象添加一些内部属性（如 `_proxy_target`, `_proxy_config`），请避免使用这些名称的属性
4. 对于复杂的对象，代理可能会影响性能，建议仅在必要时使用

## 完整示例

```python
from btools import ProxyUtil

# 定义一个业务类
class OrderService:
    def create_order(self, user_id, products):
        print(f"创建订单: 用户 {user_id}, 产品 {products}")
        total = sum(p["price"] * p["quantity"] for p in products)
        return {"order_id": 123, "total": total}
    
    def cancel_order(self, order_id):
        print(f"取消订单: {order_id}")
        return {"success": True}

# 创建业务对象
order_service = OrderService()

# 创建带多个切面的代理
def custom_before(target, method_name, args, kwargs):
    print(f"[业务日志] 开始 {method_name} 操作")

def custom_after(target, method_name, args, kwargs, result):
    print(f"[业务日志] {method_name} 操作完成，结果: {result}")

# 组合使用内置切面和自定义切面
proxy = ProxyUtil.createTimerAspect(order_service)
proxy = ProxyUtil.addAspect(proxy, before=custom_before, after=custom_after)

# 使用代理对象
order = proxy.create_order(1001, [
    {"id": 1, "name": "商品1", "price": 100, "quantity": 2},
    {"id": 2, "name": "商品2", "price": 50, "quantity": 1}
])
print(f"创建的订单: {order}")

cancel_result = proxy.cancel_order(order["order_id"])
print(f"取消订单结果: {cancel_result}")
```