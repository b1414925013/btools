# AnnotationUtil - 注解工具类

## 功能特性

`AnnotationUtil` 是一个注解工具类，提供了丰富的注解相关操作功能，包括：

- 获取类、方法、属性上的注解
- 检查是否存在某个注解
- 获取方法参数和返回值的注解
- 获取带有指定注解的方法和属性
- 获取带有注解的方法签名
- 合并和复制注解

## 基本用法

### 导入模块

```python
from btools.core.basic import AnnotationUtil
```

### 1. 获取类上的所有注解

```python
# 定义一个带有注解的类
class TestClass:
    name: str
    age: int

# 获取类上的所有注解
annotations = AnnotationUtil.get_class_annotations(TestClass)
print(f"类注解: {annotations}")
# 输出: 类注解: {'name': <class 'str'>, 'age': <class 'int'>}
```

### 2. 获取方法上的所有注解

```python
# 定义一个带有注解的方法
class TestClass:
    def get_name(self) -> str:
        return "test"

# 获取方法上的所有注解
get_name_method = TestClass.get_name
annotations = AnnotationUtil.get_method_annotations(get_name_method)
print(f"方法注解: {annotations}")
# 输出: 方法注解: {'return': <class 'str'>}
```

### 3. 获取方法参数的注解

```python
# 定义一个带有参数注解的方法
class TestClass:
    def set_name(self, name: str) -> None:
        pass

# 获取方法参数的注解
set_name_method = TestClass.set_name
param_annotations = AnnotationUtil.get_param_annotations(set_name_method)
print(f"参数注解: {param_annotations}")
# 输出: 参数注解: {'name': <class 'str'>}
```

### 4. 获取方法返回值的注解

```python
# 定义一个带有返回值注解的方法
class TestClass:
    def get_name(self) -> str:
        return "test"

# 获取方法返回值的注解
get_name_method = TestClass.get_name
return_annotation = AnnotationUtil.get_return_annotation(get_name_method)
print(f"返回值注解: {return_annotation}")
# 输出: 返回值注解: <class 'str'>
```

### 5. 获取类所有属性的注解

```python
# 定义一个带有属性注解的类
class TestClass:
    name: str
    age: int

# 获取类所有属性的注解
field_annotations = AnnotationUtil.get_field_annotations(TestClass)
print(f"属性注解: {field_annotations}")
# 输出: 属性注解: {'name': <class 'str'>, 'age': <class 'int'>}
```

### 6. 检查对象是否有指定名称的注解

```python
# 定义一个带有注解的方法
class TestClass:
    def get_name(self) -> str:
        return "test"

# 检查方法是否有 return 注解
get_name_method = TestClass.get_name
has_return_annotation = AnnotationUtil.has_annotation(get_name_method, "return")
print(f"是否有 return 注解: {has_return_annotation}")
# 输出: 是否有 return 注解: True

# 检查方法是否有不存在的注解
has_nonexistent_annotation = AnnotationUtil.has_annotation(get_name_method, "nonexistent")
print(f"是否有不存在的注解: {has_nonexistent_annotation}")
# 输出: 是否有不存在的注解: False
```

### 7. 获取对象上指定名称的注解

```python
# 定义一个带有注解的方法
class TestClass:
    def get_name(self) -> str:
        return "test"

# 获取方法上的 return 注解
get_name_method = TestClass.get_name
return_annotation = AnnotationUtil.get_annotation(get_name_method, "return")
print(f"return 注解: {return_annotation}")
# 输出: return 注解: <class 'str'>

# 获取方法上不存在的注解，使用默认值
nonexistent_annotation = AnnotationUtil.get_annotation(get_name_method, "nonexistent", "default")
print(f"不存在的注解: {nonexistent_annotation}")
# 输出: 不存在的注解: default
```

### 8. 获取对象上的所有注解

```python
# 定义一个带有注解的方法
class TestClass:
    def get_name(self) -> str:
        return "test"

# 获取方法上的所有注解
get_name_method = TestClass.get_name
annotations = AnnotationUtil.get_all_annotations(get_name_method)
print(f"所有注解: {annotations}")
# 输出: 所有注解: {'return': <class 'str'>}
```

### 9. 检查对象是否为注解

```python
# 定义一个注解类
class TestAnnotation:
    pass

# 检查是否为注解
is_annotation = AnnotationUtil.is_annotation(TestAnnotation)
print(f"TestAnnotation 是否为注解: {is_annotation}")
# 输出: TestAnnotation 是否为注解: True

# 检查普通函数是否为注解
def test_function():
    pass

is_annotation = AnnotationUtil.is_annotation(test_function)
print(f"test_function 是否为注解: {is_annotation}")
# 输出: test_function 是否为注解: True

# 检查普通对象是否为注解
test_obj = {}
is_annotation = AnnotationUtil.is_annotation(test_obj)
print(f"test_obj 是否为注解: {is_annotation}")
# 输出: test_obj 是否为注解: False
```

### 10. 获取对象上指定类型的注解

```python
# 定义一个带有注解的方法
class TestClass:
    def get_name(self) -> str:
        return "test"

# 获取方法上类型为 type 的注解
get_name_method = TestClass.get_name
type_annotations = AnnotationUtil.get_annotations_by_type(get_name_method, type)
print(f"类型注解: {type_annotations}")
# 输出: 类型注解: [<class 'str'>]
```

### 11. 获取类中带有指定注解的方法名列表

```python
# 定义一个带有多个方法的类
class TestClass:
    def get_name(self) -> str:
        return "test"
    
    def set_name(self, name: str) -> None:
        pass
    
    def get_age(self) -> int:
        return 18

# 获取带有 return 注解的方法
annotated_methods = AnnotationUtil.get_annotated_methods(TestClass, "return")
print(f"带有 return 注解的方法: {annotated_methods}")
# 输出: 带有 return 注解的方法: ['get_name', 'get_age']
```

### 12. 获取类中带有指定注解的属性名列表

```python
# 定义一个带有属性注解的类
class TestClass:
    name: str
    age: int
    score: float

# 获取带有 str 注解的属性
annotated_fields = AnnotationUtil.get_annotated_fields(TestClass, str)
print(f"带有 str 注解的属性: {annotated_fields}")
# 输出: 带有 str 注解的属性: ['name']

# 获取带有 int 注解的属性
annotated_fields = AnnotationUtil.get_annotated_fields(TestClass, int)
print(f"带有 int 注解的属性: {annotated_fields}")
# 输出: 带有 int 注解的属性: ['age']
```

### 13. 获取带有注解的方法签名

```python
# 定义一个带有注解的方法
class TestClass:
    def get_info(self, prefix: str = "Info") -> str:
        return f"{prefix}: test"

# 获取带有注解的方法签名
get_info_method = TestClass.get_info
signature = AnnotationUtil.get_method_signature_with_annotations(get_info_method)
print(f"方法签名: {signature}")
# 输出: 方法签名: get_info(prefix: <class 'str'> = Info) -> <class 'str'>
```

### 14. 合并注解

```python
# 定义两个函数

def target_function():
    pass

def source_function(name: str, age: int) -> str:
    pass

# 合并注解
AnnotationUtil.merge_annotations(target_function, source_function)

# 检查目标函数是否包含源函数的注解
target_annotations = AnnotationUtil.get_all_annotations(target_function)
print(f"合并后的注解: {target_annotations}")
# 输出: 合并后的注解: {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}
```

### 15. 复制注解

```python
# 定义两个函数

def target_function():
    pass

def source_function(name: str, age: int) -> str:
    pass

# 复制注解
AnnotationUtil.copy_annotations(source_function, target_function)

# 检查目标函数是否包含源函数的注解
target_annotations = AnnotationUtil.get_all_annotations(target_function)
source_annotations = AnnotationUtil.get_all_annotations(source_function)
print(f"复制后的注解: {target_annotations}")
print(f"源函数注解: {source_annotations}")
print(f"注解是否相同: {target_annotations == source_annotations}")
# 输出:
# 复制后的注解: {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}
# 源函数注解: {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}
# 注解是否相同: True
```

## 高级用法

### 1. 自定义注解装饰器

```python
# 定义一个自定义注解装饰器
def route(path):
    """路由注解"""
    def decorator(func):
        # 为函数添加注解
        if not hasattr(func, "__annotations__"):
            func.__annotations__ = {}
        func.__annotations__["route"] = path
        return func
    return decorator

# 使用注解装饰器
class TestController:
    @route("/home")
    def home(self) -> str:
        return "Home Page"
    
    @route("/about")
    def about(self) -> str:
        return "About Page"

# 获取带有 route 注解的方法
annotated_methods = AnnotationUtil.get_annotated_methods(TestController, "route")
print(f"带有 route 注解的方法: {annotated_methods}")
# 输出: 带有 route 注解的方法: ['home', 'about']

# 获取方法上的 route 注解
for method_name in annotated_methods:
    method = getattr(TestController, method_name)
    route_path = AnnotationUtil.get_annotation(method, "route")
    print(f"{method_name} 路由: {route_path}")
# 输出:
# home 路由: /home
# about 路由: /about
```

### 2. 基于注解的参数验证

```python
# 定义一个参数验证装饰器
def validate(func):
    """参数验证装饰器"""
    def wrapper(*args, **kwargs):
        # 获取函数参数注解
        param_annotations = AnnotationUtil.get_param_annotations(func)
        
        # 验证参数类型
        for i, (param_name, param_type) in enumerate(param_annotations.items()):
            if i < len(args):
                arg_value = args[i]
                if not isinstance(arg_value, param_type):
                    raise TypeError(f"参数 {param_name} 类型错误，期望 {param_type}，实际 {type(arg_value)}")
        
        return func(*args, **kwargs)
    
    # 复制原函数的注解
    AnnotationUtil.copy_annotations(func, wrapper)
    return wrapper

# 使用参数验证装饰器
class Calculator:
    @validate
    def add(self, a: int, b: int) -> int:
        return a + b
    
    @validate
    def multiply(self, a: int, b: int) -> int:
        return a * b

# 测试参数验证
calc = Calculator()

# 正确的参数
result = calc.add(1, 2)
print(f"1 + 2 = {result}")
# 输出: 1 + 2 = 3

# 错误的参数
# result = calc.add(1, "2")  # 会抛出类型错误
```

### 3. 基于注解的依赖注入

```python
# 定义一个依赖注入容器
class Container:
    def __init__(self):
        self.dependencies = {}
    
    def register(self, name, dependency):
        """注册依赖"""
        self.dependencies[name] = dependency
    
    def inject(self, cls):
        """注入依赖"""
        # 获取类属性注解
        field_annotations = AnnotationUtil.get_field_annotations(cls)
        
        # 为类添加依赖注入逻辑
        original_init = cls.__init__
        
        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            # 注入依赖
            for field_name, field_type in field_annotations.items():
                if field_type in self.dependencies:
                    setattr(self, field_name, self.dependencies[field_type])
        
        cls.__init__ = new_init
        return cls

# 定义一个服务类
class UserService:
    def get_user(self, user_id):
        return f"User {user_id}"

# 定义一个控制器类
@Container().inject
class UserController:
    user_service: UserService
    
    def get_user(self, user_id):
        return self.user_service.get_user(user_id)

# 测试依赖注入
container = Container()
container.register(UserService, UserService())

controller = UserController()
user = controller.get_user(1)
print(f"获取用户: {user}")
# 输出: 获取用户: User 1
```

## 注意事项

1. **注解类型**：在 Python 中，注解可以是任何类型，不仅仅是类型对象。它们可以是字符串、数字、函数、类等。

2. **Python 版本**：注解在 Python 3.0+ 中可用，但在 Python 3.6+ 中才支持变量注解。

3. **运行时访问**：注解会被存储在对象的 `__annotations__` 属性中，可以在运行时访问。

4. **装饰器影响**：使用装饰器时，需要确保装饰器正确处理了原函数的注解，否则可能会丢失注解信息。

5. **性能考虑**：对于大型类或方法，频繁获取注解可能会影响性能，建议缓存注解信息。

6. **继承关系**：注解不会自动继承，子类需要重新定义注解。

## 总结

`AnnotationUtil` 提供了全面的注解操作功能，简化了注解的使用和管理。通过这些工具方法，您可以更方便地处理注解相关的任务，如获取注解信息、基于注解进行验证、依赖注入等。