# ReflectUtils 使用指南

`ReflectUtils` 是一个反射工具类，提供了丰富的反射操作方法，包括类、方法的动态获取和调用功能。

## 功能特性

- 获取类名
- 获取模块名
- 获取基类
- 实例化对象
- 调用方法
- 获取属性
- 设置属性
- 检查属性是否存在
- 检查对象是否为指定类型的实例
- 检查类是否为指定类的子类
- 获取对象类型
- 导入模块
- 检查是否为函数
- 检查是否为方法
- 检查是否为类

## 基本用法

### 导入

```python
from btools import ReflectUtils
```

### 示例

#### 获取类名和模块名

```python
# 定义测试类
class TestClass:
    pass

# 创建对象
obj = TestClass()

# 获取类名
print(ReflectUtils.get_class_name(obj))  # 输出: TestClass

# 获取模块名
import os
print(ReflectUtils.get_module_name(os))  # 输出: os
```

#### 获取基类

```python
# 定义基类
class BaseClass:
    pass

# 定义子类
class SubClass(BaseClass):
    pass

# 获取基类
base_classes = ReflectUtils.get_base_classes(SubClass)
print([cls.__name__ for cls in base_classes])  # 输出: ['BaseClass', 'object']
```

#### 实例化对象

```python
# 定义测试类
class TestClass:
    def __init__(self, name):
        self.name = name

# 实例化对象
obj = ReflectUtils.instantiate(TestClass, "test")
print(obj.name)  # 输出: test
```

#### 调用方法

```python
# 定义测试类
class TestClass:
    def test_method(self, a, b):
        return a + b

# 创建对象
obj = TestClass()

# 调用方法
result = ReflectUtils.call_method(obj, "test_method", 1, 2)
print(result)  # 输出: 3
```

#### 操作属性

```python
# 定义测试类
class TestClass:
    def __init__(self):
        self.name = "test"

# 创建对象
obj = TestClass()

# 获取属性
print(ReflectUtils.get_attribute(obj, "name"))  # 输出: test

# 设置属性
ReflectUtils.set_attribute(obj, "name", "new_test")
print(obj.name)  # 输出: new_test

# 检查属性是否存在
print(ReflectUtils.has_attribute(obj, "name"))  # 输出: True
print(ReflectUtils.has_attribute(obj, "age"))   # 输出: False
```

#### 类型检查

```python
# 定义测试类
class TestClass:
    pass

# 创建对象
obj = TestClass()

# 检查对象是否为指定类型的实例
print(ReflectUtils.is_instance(obj, TestClass))  # 输出: True

# 检查类是否为指定类的子类
print(ReflectUtils.is_subclass(SubClass, BaseClass))  # 输出: True

# 获取对象类型
print(ReflectUtils.get_type(obj))  # 输出: <class '__main__.TestClass'>
```

#### 模块操作

```python
# 导入模块
module = ReflectUtils.import_module("os")
print(module)  # 输出: <module 'os' from '...'>
```

#### 函数和方法检查

```python
# 定义测试函数
def test_func():
    pass

# 定义测试类
class TestClass:
    def test_method(self):
        pass

# 创建对象
obj = TestClass()

# 检查是否为函数
print(ReflectUtils.is_function(test_func))  # 输出: True

# 检查是否为方法
print(ReflectUtils.is_method(obj.test_method))  # 输出: True

# 检查是否为类
print(ReflectUtils.is_class(TestClass))  # 输出: True
```

## 高级用法

### 动态导入和使用模块

```python
# 动态导入模块
math_module = ReflectUtils.import_module("math")

# 使用模块中的函数
print(math_module.sqrt(4))  # 输出: 2.0
```

### 动态创建和使用类

```python
# 动态创建类
class_name = "DynamicClass"
class_bases = (object,)
class_attrs = {
    "name": "dynamic",
    "get_name": lambda self: self.name
}

DynamicClass = type(class_name, class_bases, class_attrs)

# 实例化对象
obj = ReflectUtils.instantiate(DynamicClass)
print(obj.get_name())  # 输出: dynamic
```

## 注意事项

1. 反射操作可能会降低代码的可读性和性能，应谨慎使用。
2. 在使用 `import_module()` 方法时，需要确保模块存在，否则会抛出异常。
3. 在使用 `call_method()` 方法时，需要确保方法存在且参数正确，否则会抛出异常。
4. 在使用 `get_attribute()` 和 `set_attribute()` 方法时，需要确保属性存在或可设置，否则会抛出异常。

## 总结

`ReflectUtils` 提供了全面的反射操作功能，简化了反射操作的复杂度，使代码更加简洁易读。无论是基本的反射操作还是高级的动态类型操作，`ReflectUtils` 都能满足你的需求。