# BeanUtils 使用指南

`BeanUtils` 类提供了对象属性的操作功能，包括属性复制、深拷贝、浅拷贝、对象与字典转换、对象比较等功能。

## 基本使用

### 导入方式

```python
from btools import BeanUtils
```

## 对象属性操作

### 复制对象属性

```python
from btools import BeanUtils

class User:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.email = ""

class UserDTO:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.email = ""
        self.password = ""

# 创建源对象
source = User()
source.name = "张三"
source.age = 25
source.email = "zhangsan@example.com"

# 创建目标对象
target = UserDTO()

# 复制属性
BeanUtils.copy_properties(source, target)

print(f"姓名: {target.name}")
print(f"年龄: {target.age}")
print(f"邮箱: {target.email}")

# 忽略特定属性
BeanUtils.copy_properties(source, target, ignore_properties=['email'])
```

### 深拷贝与浅拷贝

```python
from btools import BeanUtils

class Address:
    def __init__(self):
        self.city = ""
        self.street = ""

class Person:
    def __init__(self):
        self.name = ""
        self.address = Address()

# 创建对象
person1 = Person()
person1.name = "李四"
person1.address.city = "北京"
person1.address.street = "中山路"

# 深拷贝
person2 = BeanUtils.deep_copy(person1)
person2.name = "王五"
person2.address.city = "上海"

print(f"person1姓名: {person1.name}, 城市: {person1.address.city}")
print(f"person2姓名: {person2.name}, 城市: {person2.address.city}")
# 输出:
# person1姓名: 李四, 城市: 北京
# person2姓名: 王五, 城市: 上海

# 浅拷贝
person3 = BeanUtils.shallow_copy(person1)
person3.name = "赵六"
person3.address.city = "广州"

print(f"person1姓名: {person1.name}, 城市: {person1.address.city}")
print(f"person3姓名: {person3.name}, 城市: {person3.address.city}")
# 输出:
# person1姓名: 李四, 城市: 广州
# person3姓名: 赵六, 城市: 广州
```

## 对象与字典转换

### 对象转字典

```python
from btools import BeanUtils

class Product:
    def __init__(self):
        self.name = "手机"
        self.price = 2999.0
        self.stock = 100
        self.sku = "PHONE001"

product = Product()

# 转换为字典
product_dict = BeanUtils.to_dict(product)
print(f"产品字典: {product_dict}")

# 忽略特定属性
product_dict_simple = BeanUtils.to_dict(product, ignore_properties=['sku'])
print(f"简化产品字典: {product_dict_simple}")
```

### 从字典创建对象

```python
from btools import BeanUtils

class Order:
    def __init__(self):
        self.order_id = ""
        self.user_id = ""
        self.total_amount = 0.0
        self.status = ""

# 准备字典数据
order_data = {
    "order_id": "ORD001",
    "user_id": "USER001",
    "total_amount": 999.0,
    "status": "待付款"
}

# 从字典创建对象
order = BeanUtils.from_dict(Order, order_data)

print(f"订单ID: {order.order_id}")
print(f"用户ID: {order.user_id}")
print(f"总金额: {order.total_amount}")
print(f"状态: {order.status}")
```

## 对象比较

### 比较两个对象是否相等

```python
from btools import BeanUtils

class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.age = 0
        self.create_time = ""

# 创建对象
student1 = Student()
student1.id = "S001"
student1.name = "小明"
student1.age = 18
student1.create_time = "2023-01-01"

student2 = Student()
student2.id = "S001"
student2.name = "小明"
student2.age = 18
student2.create_time = "2023-01-02"

# 完全比较
is_equal = BeanUtils.equals(student1, student2)
print(f"对象相等: {is_equal}")  # False

# 忽略特定属性
is_equal_ignore_time = BeanUtils.equals(student1, student2, ignore_properties=['create_time'])
print(f"忽略时间后相等: {is_equal_ignore_time}")  # True
```

## 单个属性操作

### 获取属性值

```python
from btools import BeanUtils

class Address:
    def __init__(self):
        self.city = "北京"
        self.street = "中山路"

class Customer:
    def __init__(self):
        self.name = "客户A"
        self.address = Address()

customer = Customer()

# 获取普通属性
name = BeanUtils.get_property(customer, "name")
print(f"姓名: {name}")

# 获取嵌套属性
city = BeanUtils.get_property(customer, "address.city")
print(f"城市: {city}")

# 获取不存在的属性
nonexistent = BeanUtils.get_property(customer, "nonexistent")
print(f"不存在的属性: {nonexistent}")
```

### 设置属性值

```python
from btools import BeanUtils

class Address:
    def __init__(self):
        self.city = ""
        self.street = ""

class Customer:
    def __init__(self):
        self.name = ""
        self.address = Address()

customer = Customer()

# 设置普通属性
success1 = BeanUtils.set_property(customer, "name", "客户B")
print(f"设置姓名成功: {success1}")

# 设置嵌套属性
success2 = BeanUtils.set_property(customer, "address.city", "上海")
print(f"设置城市成功: {success2}")

print(f"客户姓名: {customer.name}")
print(f"客户城市: {customer.address.city}")
```

### 检查属性是否存在

```python
from btools import BeanUtils

class Product:
    def __init__(self):
        self.name = ""
        self.price = 0.0

product = Product()

# 检查属性是否存在
has_name = BeanUtils.has_property(product, "name")
has_price = BeanUtils.has_property(product, "price")
has_stock = BeanUtils.has_property(product, "stock")

print(f"有name属性: {has_name}")
print(f"有price属性: {has_price}")
print(f"有stock属性: {has_stock}")
```

### 获取所有属性

```python
from btools import BeanUtils

class Employee:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""
        self.salary = 0.0

employee = Employee()

# 获取所有属性名
properties = BeanUtils.get_properties(employee)
print(f"所有属性: {properties}")
```

## 合并对象

### 合并两个对象的属性

```python
from btools import BeanUtils

class UserProfile:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.phone = ""

class UserSettings:
    def __init__(self):
        self.notifications = True
        self.theme = "light"
        self.language = "zh-CN"

# 创建对象
profile = UserProfile()
profile.name = "张三"
profile.email = "zhangsan@example.com"

settings = UserSettings()
settings.theme = "dark"

# 合并对象
merged_user = BeanUtils.merge(profile, settings)

print(f"合并后的用户名: {merged_user.name}")
print(f"合并后的邮箱: {merged_user.email}")
print(f"合并后的主题: {merged_user.theme}")
print(f"合并后的通知: {merged_user.notifications}")
```

## 常见使用场景

### DTO与Entity转换

```python
from btools import BeanUtils

# 数据传输对象
class UserDTO:
    def __init__(self):
        self.username = ""
        self.email = ""
        self.phone = ""

# 实体对象
class UserEntity:
    def __init__(self):
        self.id = 0
        self.username = ""
        self.email = ""
        self.phone = ""
        self.created_at = None
        self.updated_at = None

# DTO转Entity
dto = UserDTO()
dto.username = "user001"
dto.email = "user001@example.com"
dto.phone = "13800138000"

entity = BeanUtils.from_dict(UserEntity, BeanUtils.to_dict(dto))
entity.created_at = "2023-01-01"
entity.updated_at = "2023-01-01"

print(f"Entity用户名: {entity.username}")
print(f"Entity邮箱: {entity.email}")

# Entity转DTO
dto2 = BeanUtils.from_dict(UserDTO, BeanUtils.to_dict(entity))
print(f"DTO用户名: {dto2.username}")
```

### 对象克隆与修改

```python
from btools import BeanUtils

class Order:
    def __init__(self):
        self.order_id = ""
        self.status = ""
        self.total = 0.0

original = Order()
original.order_id = "ORD001"
original.status = "待付款"
original.total = 999.0

# 克隆对象并修改
cloned = BeanUtils.deep_copy(original)
cloned.status = "已付款"
cloned.total = 899.0

print(f"原订单状态: {original.status}, 金额: {original.total}")
print(f"克隆订单状态: {cloned.status}, 金额: {cloned.total}")
```
