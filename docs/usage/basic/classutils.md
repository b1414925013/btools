# ClassUtils 使用指南

`ClassUtils` 是一个类工具类，提供了丰富的类相关操作功能，包括类信息获取、类加载、类型检查、成员获取等。

## 功能特性

- **类信息获取**：获取类的名称、包名、模块名、完整类名等
- **类加载**：根据类名动态加载类
- **类型检查**：检查类是否为抽象类、具体类、内部类等
- **继承关系**：获取类的父类、接口、继承层次结构等
- **成员操作**：获取类的构造器、方法、字段、所有成员等
- **实例化**：根据类和参数实例化对象
- **注解处理**：获取类、方法、字段的注解
- **访问控制**：检查成员是否为静态、私有、保护成员
- **工具方法**：获取类的加载器、路径、共同父类等

## 基本用法

### 导入

```python
from btools import ClassUtils
```

### 示例

#### 1. 获取类的基本信息

```python
class TestClass:
    pass

# 获取类的名称
print(ClassUtils.get_class_name(TestClass))  # 输出: "TestClass"

# 获取类所在的包名称
print(ClassUtils.get_package_name(TestClass))  # 输出: ""

# 获取类所在的模块名称
print(ClassUtils.get_module_name(TestClass))  # 输出: "__main__"

# 获取类的完整名称
print(ClassUtils.get_full_class_name(TestClass))  # 输出: "__main__.TestClass"
```

#### 2. 加载类

```python
# 加载内置类
cls = ClassUtils.load_class("builtins.int")
print(cls)  # 输出: <class 'int'>

# 加载自定义类
cls = ClassUtils.load_class("__main__.TestClass")
print(cls)  # 输出: <class '__main__.TestClass'>

# 加载不存在的类
cls = ClassUtils.load_class("non.existent.Class")
print(cls)  # 输出: None
```

#### 3. 类型检查

```python
import abc

class AbstractClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def method(self):
        pass

class ConcreteClass:
    pass

class OuterClass:
    class InnerClass:
        pass

# 检查是否为抽象类
print(ClassUtils.is_abstract(AbstractClass))  # 输出: True
print(ClassUtils.is_abstract(ConcreteClass))  # 输出: False

# 检查是否为具体类
print(ClassUtils.is_concrete(AbstractClass))  # 输出: False
print(ClassUtils.is_concrete(ConcreteClass))  # 输出: True

# 检查是否为内部类
print(ClassUtils.is_inner_class(OuterClass.InnerClass))  # 输出: True
print(ClassUtils.is_inner_class(ConcreteClass))  # 输出: False
```

#### 4. 继承关系

```python
class BaseClass:
    pass

class SubClass(BaseClass):
    pass

class SubSubClass(SubClass):
    pass

# 获取类的所有父类
super_classes = ClassUtils.get_super_classes(SubSubClass)
print([cls.__name__ for cls in super_classes])  # 输出: ["SubClass", "BaseClass", "object"]

# 获取类的继承层次结构
hierarchy = ClassUtils.get_class_hierarchy(SubSubClass)
print([cls.__name__ for cls in hierarchy])  # 输出: ["SubSubClass", "SubClass", "BaseClass", "object"]

# 检查类是否为子类
print(ClassUtils.is_subclass(SubClass, BaseClass))  # 输出: True
print(ClassUtils.is_subclass(BaseClass, SubClass))  # 输出: False

# 获取多个类的共同父类
common = ClassUtils.get_common_super_class([SubClass, SubSubClass])
print(common.__name__)  # 输出: "SubClass"
```

#### 5. 成员操作

```python
class TestClass:
    field1 = "value1"
    field2 = "value2"
    
    def __init__(self):
        pass
    
    def method1(self):
        pass
    
    def method2(self):
        pass

# 获取类的所有构造器
constructors = ClassUtils.get_constructors(TestClass)
print([func.__name__ for func in constructors])  # 输出: ["__init__"]

# 获取类的所有方法
methods = ClassUtils.get_methods(TestClass)
print([func.__name__ for func in methods])  # 输出: ["__init__", "method1", "method2"]

# 获取类的所有字段
fields = ClassUtils.get_fields(TestClass)
print([field[0] for field in fields])  # 输出: ["field1", "field2"]

# 获取类的所有成员
members = ClassUtils.get_all_members(TestClass)
print([name for name in members.keys()])  # 输出: 所有成员名称
```

#### 6. 实例化类

```python
class TestClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 实例化类
obj = ClassUtils.instantiate(TestClass, "Alice", 30)
print(obj.name, obj.age)  # 输出: "Alice 30"

# 实例化失败（参数错误）
obj = ClassUtils.instantiate(TestClass)
print(obj)  # 输出: None
```

#### 7. 注解处理

```python
class TestClass:
    field: int
    name: str
    
    def method(self, x: int, y: str) -> bool:
        return True

# 获取类的注解
class_annotations = ClassUtils.get_class_annotations(TestClass)
print(class_annotations)  # 输出: {"field": <class 'int'>, "name": <class 'str'>}

# 获取方法的注解
method_annotations = ClassUtils.get_method_annotations(TestClass, "method")
print(method_annotations)  # 输出: {"x": <class 'int'>, "y": <class 'str'>, "return": <class 'bool'>}

# 获取字段的注解
field_annotations = ClassUtils.get_field_annotations(TestClass, "field")
print(field_annotations)  # 输出: {"field": <class 'int'>}
```

#### 8. 访问控制

```python
class TestClass:
    __private_field = "private"
    _protected_field = "protected"
    public_field = "public"
    
    def instance_method(self):
        pass

# 检查是否为静态成员
print(ClassUtils.is_static(TestClass, "public_field"))  # 输出: True
print(ClassUtils.is_static(TestClass, "instance_method"))  # 输出: False

# 检查是否为私有成员
print(ClassUtils.is_private(TestClass, "__private_field"))  # 输出: True
print(ClassUtils.is_private(TestClass, "public_field"))  # 输出: False

# 检查是否为保护成员
print(ClassUtils.is_protected(TestClass, "_protected_field"))  # 输出: True
print(ClassUtils.is_protected(TestClass, "public_field"))  # 输出: False
```

#### 9. 内部类操作

```python
class OuterClass:
    class InnerClass:
        pass

# 检查是否为内部类
print(ClassUtils.is_inner_class(OuterClass.InnerClass))  # 输出: True
print(ClassUtils.is_inner_class(OuterClass))  # 输出: False

# 获取内部类的外部类
outer_class = ClassUtils.get_outer_class(OuterClass.InnerClass)
print(outer_class)  # 输出: <class '__main__.OuterClass'>
```

#### 10. 其他工具方法

```python
class TestClass:
    pass

# 获取类的加载器
loader = ClassUtils.get_class_loader(TestClass)
print(loader)  # 输出: <_frozen_importlib_external.SourceFileLoader ...>

# 获取类的路径
path = ClassUtils.get_class_path(TestClass)
print(path)  # 输出: "/path/to/file.py"

# 检查类是否为最终类
print(ClassUtils.is_final(TestClass))  # 输出: False

# 创建最终类
class FinalClass:
    __final__ = True

print(ClassUtils.is_final(FinalClass))  # 输出: True
```

## 高级用法

### 类的继承层次结构分析

```python
def analyze_class_hierarchy(cls):
    """分析类的继承层次结构"""
    print(f"分析类: {ClassUtils.get_full_class_name(cls)}")
    
    # 获取继承层次结构
    hierarchy = ClassUtils.get_class_hierarchy(cls)
    print("继承层次结构:")
    for i, c in enumerate(hierarchy):
        indent = "  " * i
        print(f"{indent}- {ClassUtils.get_class_name(c)}")
    
    # 获取直接父类
    super_classes = ClassUtils.get_super_classes(cls)
    print("\n直接父类:")
    for c in super_classes:
        print(f"- {ClassUtils.get_class_name(c)}")

# 测试
class BaseClass:
    pass

class SubClass(BaseClass):
    pass

class SubSubClass(SubClass):
    pass

analyze_class_hierarchy(SubSubClass)
```

### 类成员的全面分析

```python
def analyze_class_members(cls):
    """分析类的所有成员"""
    print(f"分析类: {ClassUtils.get_full_class_name(cls)}")
    
    # 获取构造器
    constructors = ClassUtils.get_constructors(cls)
    print("构造器:")
    for func in constructors:
        print(f"- {func.__name__}")
    
    # 获取方法
    methods = ClassUtils.get_methods(cls)
    print("\n方法:")
    for func in methods:
        print(f"- {func.__name__}")
    
    # 获取字段
    fields = ClassUtils.get_fields(cls)
    print("\n字段:")
    for name, value in fields:
        print(f"- {name}: {value}")
    
    # 获取注解
    annotations = ClassUtils.get_class_annotations(cls)
    if annotations:
        print("\n注解:")
        for name, type_ in annotations.items():
            print(f"- {name}: {type_.__name__}")

# 测试
class TestClass:
    field: int = 42
    name: str = "test"
    
    def __init__(self):
        pass
    
    def method1(self):
        pass
    
    def method2(self):
        pass

analyze_class_members(TestClass)
```

### 安全的类实例化

```python
def safe_instantiate(class_name, *args, **kwargs):
    """安全地实例化类"""
    try:
        # 加载类
        cls = ClassUtils.load_class(class_name)
        if not cls:
            print(f"无法加载类: {class_name}")
            return None
        
        # 实例化类
        obj = ClassUtils.instantiate(cls, *args, **kwargs)
        if not obj:
            print(f"无法实例化类: {class_name}")
            return None
        
        print(f"成功实例化类: {class_name}")
        return obj
    except Exception as e:
        print(f"实例化类时发生错误: {e}")
        return None

# 测试
safe_instantiate("builtins.list")  # 成功
 safe_instantiate("__main__.TestClass", "Alice", 30)  # 成功
 safe_instantiate("non.existent.Class")  # 失败
```

## 注意事项

1. **类加载**：加载类时需要提供完整的类名（包含包名和模块名），否则可能加载失败

2. **抽象类检查**：使用 `abc.ABCMeta` 元类创建的类会被识别为抽象类

3. **内部类**：内部类的完整名称包含外部类的名称，如 `OuterClass.InnerClass`

4. **注解处理**：Python 3.6+ 支持类变量注解，较早版本可能不支持

5. **成员访问**：私有成员和保护成员的检查基于命名约定（`__private` 和 `_protected`）

6. **异常处理**：所有方法都捕获异常并返回适当的默认值，确保不会因为操作失败而导致程序崩溃

7. **平台差异**：某些方法的行为可能因平台而异，例如类路径的获取

8. **性能考虑**：反射操作可能比较慢，对于性能敏感的场景应谨慎使用

## 应用场景

`ClassUtils` 适用于以下场景：

- **框架开发**：需要动态加载类、分析类结构的框架
- **依赖注入**：需要根据类名实例化对象的依赖注入容器
- **ORM 系统**：需要分析类的字段和注解的 ORM 框架
- **序列化/反序列化**：需要分析类结构进行序列化和反序列化的系统
- **代码生成**：需要分析类结构生成代码的工具
- **测试工具**：需要动态操作类和对象的测试工具
- **插件系统**：需要动态加载和管理插件的系统

这些功能使得 `ClassUtils` 成为处理类相关操作的强大工具，可以在各种复杂的应用场景中使用。
