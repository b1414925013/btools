# TypeUtils 使用指南

`TypeUtils` 是一个类型工具类，提供了丰富的类型相关操作功能，包括类型检查、类型转换、泛型类型处理等。

## 功能特性

- **类型检查**：检查对象是否为指定类型、是否为None、是否为空等
- **类型转换**：将对象转换为指定类型，支持安全转换
- **类型信息**：获取对象的类型、类型名称、完整类型名称等
- **泛型类型处理**：处理List、Dict、Tuple、Optional、Union等泛型类型
- **可调用对象检查**：检查对象是否为可调用对象、函数、方法等
- **类相关操作**：检查类是否为子类、获取父类、获取注解等
- **模块信息**：获取对象所在的模块名称、限定名称等
- **类型分类**：检查类型是否为内置类型、自定义类型等

## 基本用法

### 导入

```python
from btools import TypeUtils
```

### 示例

#### 1. 类型检查

```python
# 检查对象是否为指定类型
print(TypeUtils.is_type(1, int))  # 输出: True
print(TypeUtils.is_type("test", str))  # 输出: True
print(TypeUtils.is_type([], list))  # 输出: True

# 检查对象是否为None
print(TypeUtils.is_none(None))  # 输出: True
print(TypeUtils.is_not_none(1))  # 输出: True

# 检查对象是否为空
print(TypeUtils.is_empty(None))  # 输出: True
print(TypeUtils.is_empty(""))  # 输出: True
print(TypeUtils.is_empty([]))  # 输出: True
print(TypeUtils.is_not_empty([1]))  # 输出: True
```

#### 2. 类型转换

```python
# 将对象转换为指定类型
print(TypeUtils.cast("1", int))  # 输出: 1
print(TypeUtils.cast(1, str))  # 输出: "1"
print(TypeUtils.cast(None, int))  # 输出: None

# 安全地将对象转换为指定类型
print(TypeUtils.safe_cast("1", int))  # 输出: 1
print(TypeUtils.safe_cast("test", int, 0))  # 输出: 0（转换失败，返回默认值）
print(TypeUtils.safe_cast(None, int, 0))  # 输出: 0（对象为None，返回默认值）
```

#### 3. 类型信息

```python
# 获取对象的类型
print(TypeUtils.get_type(1))  # 输出: <class 'int'>
print(TypeUtils.get_type("test"))  # 输出: <class 'str'>

# 获取对象的类型名称
print(TypeUtils.get_type_name(1))  # 输出: "int"
print(TypeUtils.get_type_name("test"))  # 输出: "str"
print(TypeUtils.get_type_name(None))  # 输出: "NoneType"

# 获取对象的完整类型名称
print(TypeUtils.get_full_type_name(1))  # 输出: "int"
print(TypeUtils.get_full_type_name([]))  # 输出: "list"
```

#### 4. 泛型类型处理

```python
from typing import List, Dict, Tuple, Optional, Union

# 检查类型是否为泛型类型
print(TypeUtils.is_generic_type(List[int]))  # 输出: True
print(TypeUtils.is_generic_type(Dict[str, int]))  # 输出: True

# 获取泛型类型的原始类型
print(TypeUtils.get_generic_type(List[int]))  # 输出: <class 'list'>
print(TypeUtils.get_generic_type(Dict[str, int]))  # 输出: <class 'dict'>

# 获取类型的类型参数
print(TypeUtils.get_type_args(List[int]))  # 输出: (<class 'int'>,)
print(TypeUtils.get_type_args(Dict[str, int]))  # 输出: (<class 'str'>, <class 'int'>)

# 检查类型是否为Optional类型
print(TypeUtils.is_optional_type(Optional[int]))  # 输出: True
print(TypeUtils.get_optional_type(Optional[int]))  # 输出: <class 'int'>

# 检查类型是否为Union类型
print(TypeUtils.is_union_type(Union[int, str]))  # 输出: True
print(TypeUtils.get_union_types(Union[int, str]))  # 输出: (<class 'int'>, <class 'str'>)

# 检查类型是否为List类型
print(TypeUtils.is_list_type(List[int]))  # 输出: True
print(TypeUtils.get_list_element_type(List[int]))  # 输出: <class 'int'>

# 检查类型是否为Dict类型
print(TypeUtils.is_dict_type(Dict[str, int]))  # 输出: True
print(TypeUtils.get_dict_key_type(Dict[str, int]))  # 输出: <class 'str'>
print(TypeUtils.get_dict_value_type(Dict[str, int]))  # 输出: <class 'int'>

# 检查类型是否为Tuple类型
print(TypeUtils.is_tuple_type(Tuple[int, str]))  # 输出: True
print(TypeUtils.get_tuple_element_types(Tuple[int, str]))  # 输出: (<class 'int'>, <class 'str'>)
```

#### 5. 可调用对象检查

```python
# 定义测试函数和类
def test_func():
    pass

class TestClass:
    def method(self):
        pass
    
    def __call__(self):
        pass

# 检查对象是否为可调用对象
print(TypeUtils.is_callable_type(test_func))  # 输出: True
print(TypeUtils.is_callable_type(TestClass()))  # 输出: True

# 检查对象是否为函数
print(TypeUtils.is_function(test_func))  # 输出: True
print(TypeUtils.is_function(TestClass.method))  # 输出: False

# 检查对象是否为方法
obj = TestClass()
print(TypeUtils.is_method(obj.method))  # 输出: True
print(TypeUtils.is_method(test_func))  # 输出: False

# 检查对象是否为类
print(TypeUtils.is_class(TestClass))  # 输出: True
print(TypeUtils.is_class(obj))  # 输出: False
```

#### 6. 类相关操作

```python
# 定义测试类
class BaseClass:
    pass

class SubClass(BaseClass):
    pass

# 检查对象是否为指定类型的实例
obj = SubClass()
print(TypeUtils.is_instance(obj, SubClass))  # 输出: True
print(TypeUtils.is_instance(obj, BaseClass))  # 输出: True

# 检查类是否为指定类的子类
print(TypeUtils.is_subclass(SubClass, BaseClass))  # 输出: True
print(TypeUtils.is_subclass(BaseClass, SubClass))  # 输出: False

# 获取类的所有父类
super_classes = TypeUtils.get_super_classes(SubClass)
print([cls.__name__ for cls in super_classes])  # 输出: ["BaseClass", "object"]

# 获取类的注解
class TestClass:
    a: int
    b: str

annotations = TypeUtils.get_class_annotations(TestClass)
print(annotations)  # 输出: {"a": <class 'int'>, "b": <class 'str'>}

# 获取函数的注解
def test_func(a: int, b: str) -> bool:
    return True

func_annotations = TypeUtils.get_function_annotations(test_func)
print(func_annotations)  # 输出: {"a": <class 'int'>, "b": <class 'str'>, "return": <class 'bool'>}
```

#### 7. 模块信息

```python
import os

# 获取对象所在的模块名称
print(TypeUtils.get_module_name(os.path.join))  # 输出: "os.path"
print(TypeUtils.get_module_name(1))  # 输出: ""

# 获取对象的限定名称
def test_func():
    pass

class TestClass:
    def method(self):
        pass

print(TypeUtils.get_qualified_name(test_func))  # 输出: "test_func"
print(TypeUtils.get_qualified_name(TestClass.method))  # 输出: "TestClass.method"
```

#### 8. 类型分类

```python
# 检查类型是否为内置类型
print(TypeUtils.is_builtin_type(int))  # 输出: True
print(TypeUtils.is_builtin_type(str))  # 输出: True
print(TypeUtils.is_builtin_type(list))  # 输出: True

# 检查类型是否为自定义类型
class TestClass:
    pass

print(TypeUtils.is_custom_type(TestClass))  # 输出: True
print(TypeUtils.is_custom_type(int))  # 输出: False
```

## 高级用法

### 处理复杂的泛型类型

```python
from typing import List, Dict, Optional, Union

# 处理嵌套的泛型类型
type_ = List[Dict[str, Optional[Union[int, str]]]]
print(TypeUtils.is_generic_type(type_))  # 输出: True
print(TypeUtils.get_generic_type(type_))  # 输出: <class 'list'>

# 获取嵌套泛型类型的参数
args = TypeUtils.get_type_args(type_)
print(len(args))  # 输出: 1

# 处理Dict类型
dict_type = args[0]
print(TypeUtils.is_dict_type(dict_type))  # 输出: True
print(TypeUtils.get_dict_key_type(dict_type))  # 输出: <class 'str'>

# 处理Optional类型
value_type = TypeUtils.get_dict_value_type(dict_type)
print(TypeUtils.is_optional_type(value_type))  # 输出: True

# 处理Union类型
union_type = TypeUtils.get_optional_type(value_type)
print(TypeUtils.is_union_type(union_type))  # 输出: True
print(TypeUtils.get_union_types(union_type))  # 输出: (<class 'int'>, <class 'str'>)
```

### 类型判断和转换的组合使用

```python
def process_value(value, expected_type):
    """处理值，确保其为预期类型"""
    if TypeUtils.is_none(value):
        return None
    
    if TypeUtils.is_instance(value, expected_type):
        return value
    
    # 尝试转换
    return TypeUtils.safe_cast(value, expected_type, value)

# 测试
print(process_value("1", int))  # 输出: 1
print(process_value(1, str))  # 输出: "1"
print(process_value("test", int))  # 输出: "test"（转换失败，返回原值）
print(process_value(None, int))  # 输出: None
```

### 类型注解的处理

```python
class Config:
    """配置类"""
    host: str
    port: int
    debug: bool = False

# 获取类的注解
annotations = TypeUtils.get_class_annotations(Config)

# 打印注解信息
for name, type_ in annotations.items():
    print(f"{name}: {TypeUtils.get_type_name(type_)}")

# 输出:
# host: str
# port: int
# debug: bool
```

## 注意事项

1. **类型检查**：`is_type` 和 `is_instance` 方法使用 `isinstance` 函数，支持检查子类实例

2. **类型转换**：
   - `cast` 方法在转换失败时返回原对象
   - `safe_cast` 方法在转换失败或对象为None时返回默认值

3. **泛型类型处理**：
   - 仅支持Python 3.9+的泛型类型语法（如 `List[int]`）
   - 对于旧版本的 `typing.List[int]` 语法也能正常工作

4. **空值检查**：
   - `is_empty` 方法会检查：
     - None 值
     - 长度为0的字符串、列表、元组、字典、集合
     - 其他实现了 `__len__` 方法且长度为0的对象

5. **异常处理**：所有方法都设计为不会抛出异常，确保在任何情况下都能正常返回结果

## 应用场景

`TypeUtils` 适用于以下场景：

- **类型验证**：在函数或方法中验证输入参数的类型
- **类型转换**：在不同类型之间进行安全的转换
- **泛型编程**：处理泛型类型，获取类型参数
- **反射操作**：获取类的信息、注解等
- **配置处理**：处理配置值的类型转换和验证
- **API开发**：验证和转换API请求和响应的数据类型

这些功能使得 `TypeUtils` 成为处理类型相关操作的强大工具，可以大大简化类型处理的代码。
