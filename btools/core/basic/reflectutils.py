"""反射工具类"""
import inspect
import importlib
from typing import Any, Dict, List, Optional, Type, Union


class ReflectUtils:
    """反射工具类"""

    @staticmethod
    def get_class_name(cls: Union[Type, Any]) -> str:
        """
        获取类名
        
        Args:
            cls: 类或对象
            
        Returns:
            str: 类名
        """
        if isinstance(cls, type):
            return cls.__name__
        return cls.__class__.__name__

    @staticmethod
    def get_module_name(obj: Union[Type, Any]) -> str:
        """
        获取模块名
        
        Args:
            obj: 类、对象或模块
            
        Returns:
            str: 模块名
        """
        # 处理模块对象
        if hasattr(obj, '__name__') and hasattr(obj, '__file__'):
            return obj.__name__
        # 处理类型
        if isinstance(obj, type):
            return obj.__module__
        # 处理对象实例
        return obj.__class__.__module__

    @staticmethod
    def get_base_classes(cls: Type) -> List[Type]:
        """
        获取基类列表
        
        Args:
            cls: 类
            
        Returns:
            List[Type]: 基类列表
        """
        return list(cls.__bases__)

    @staticmethod
    def get_class_annotations(cls: Type) -> Dict[str, Any]:
        """
        获取类的注解
        
        Args:
            cls: 类
            
        Returns:
            Dict[str, Any]: 注解字典
        """
        return cls.__annotations__ if hasattr(cls, '__annotations__') else {}

    @staticmethod
    def get_class_vars(cls: Type) -> Dict[str, Any]:
        """
        获取类变量
        
        Args:
            cls: 类
            
        Returns:
            Dict[str, Any]: 类变量字典
        """
        return {k: v for k, v in cls.__dict__.items() if not k.startswith('__') and not callable(v)}

    @staticmethod
    def get_instance_vars(obj: Any) -> Dict[str, Any]:
        """
        获取实例变量
        
        Args:
            obj: 对象
            
        Returns:
            Dict[str, Any]: 实例变量字典
        """
        return {k: v for k, v in obj.__dict__.items() if not k.startswith('__')}

    @staticmethod
    def get_methods(cls: Union[Type, Any]) -> List[str]:
        """
        获取方法列表
        
        Args:
            cls: 类或对象
            
        Returns:
            List[str]: 方法名列表
        """
        if isinstance(cls, type):
            return [m[0] for m in inspect.getmembers(cls, predicate=inspect.isfunction) if not m[0].startswith('__')]
        return [m[0] for m in inspect.getmembers(cls, predicate=inspect.ismethod) if not m[0].startswith('__')]

    @staticmethod
    def get_functions(module) -> List[str]:
        """
        获取模块中的函数列表
        
        Args:
            module: 模块
            
        Returns:
            List[str]: 函数名列表
        """
        return [f[0] for f in inspect.getmembers(module, predicate=inspect.isfunction) if not f[0].startswith('__')]

    @staticmethod
    def get_classes(module) -> List[str]:
        """
        获取模块中的类列表
        
        Args:
            module: 模块
            
        Returns:
            List[str]: 类名列表
        """
        return [c[0] for c in inspect.getmembers(module, predicate=inspect.isclass) if not c[0].startswith('__')]

    @staticmethod
    def instantiate(cls: Type, *args, **kwargs) -> Any:
        """
        实例化类
        
        Args:
            cls: 类
            *args: 位置参数
            **kwargs: 关键字参数
            
        Returns:
            Any: 实例
        """
        return cls(*args, **kwargs)

    @staticmethod
    def call_method(obj: Any, method_name: str, *args, **kwargs) -> Any:
        """
        调用对象的方法
        
        Args:
            obj: 对象
            method_name: 方法名
            *args: 位置参数
            **kwargs: 关键字参数
            
        Returns:
            Any: 方法返回值
        """
        method = getattr(obj, method_name)
        return method(*args, **kwargs)

    @staticmethod
    def get_attribute(obj: Any, attr_name: str) -> Any:
        """
        获取对象的属性
        
        Args:
            obj: 对象
            attr_name: 属性名
            
        Returns:
            Any: 属性值
        """
        return getattr(obj, attr_name)

    @staticmethod
    def set_attribute(obj: Any, attr_name: str, value: Any) -> None:
        """
        设置对象的属性
        
        Args:
            obj: 对象
            attr_name: 属性名
            value: 属性值
        """
        setattr(obj, attr_name, value)

    @staticmethod
    def has_attribute(obj: Any, attr_name: str) -> bool:
        """
        检查对象是否具有指定属性
        
        Args:
            obj: 对象
            attr_name: 属性名
            
        Returns:
            bool: 如果具有指定属性则返回True，否则返回False
        """
        return hasattr(obj, attr_name)

    @staticmethod
    def is_instance(obj: Any, cls: Type) -> bool:
        """
        检查对象是否是指定类的实例
        
        Args:
            obj: 对象
            cls: 类
            
        Returns:
            bool: 如果是指定类的实例则返回True，否则返回False
        """
        return isinstance(obj, cls)

    @staticmethod
    def is_subclass(sub_cls: Type, super_cls: Type) -> bool:
        """
        检查类是否是指定类的子类
        
        Args:
            sub_cls: 子类
            super_cls: 父类
            
        Returns:
            bool: 如果是指定类的子类则返回True，否则返回False
        """
        return issubclass(sub_cls, super_cls)

    @staticmethod
    def get_type(obj: Any) -> Type:
        """
        获取对象的类型
        
        Args:
            obj: 对象
            
        Returns:
            Type: 对象的类型
        """
        return type(obj)

    @staticmethod
    def import_module(module_name: str) -> Any:
        """
        导入模块
        
        Args:
            module_name: 模块名
            
        Returns:
            Any: 模块
        """
        return importlib.import_module(module_name)

    @staticmethod
    def import_class(module_name: str, class_name: str) -> Type:
        """
        导入类
        
        Args:
            module_name: 模块名
            class_name: 类名
            
        Returns:
            Type: 类
        """
        module = importlib.import_module(module_name)
        return getattr(module, class_name)

    @staticmethod
    def get_signature(obj: Union[Type, Any]) -> inspect.Signature:
        """
        获取函数或方法的签名
        
        Args:
            obj: 函数、方法或类
            
        Returns:
            inspect.Signature: 签名
        """
        return inspect.signature(obj)

    @staticmethod
    def get_docstring(obj: Union[Type, Any]) -> Optional[str]:
        """
        获取文档字符串
        
        Args:
            obj: 类、函数、方法或模块
            
        Returns:
            Optional[str]: 文档字符串
        """
        return inspect.getdoc(obj)

    @staticmethod
    def get_source(obj: Union[Type, Any]) -> Optional[str]:
        """
        获取源代码
        
        Args:
            obj: 类、函数或方法
            
        Returns:
            Optional[str]: 源代码
        """
        try:
            return inspect.getsource(obj)
        except OSError:
            return None

    @staticmethod
    def is_function(obj: Any) -> bool:
        """
        检查对象是否是函数
        
        Args:
            obj: 对象
            
        Returns:
            bool: 如果是函数则返回True，否则返回False
        """
        return inspect.isfunction(obj)

    @staticmethod
    def is_method(obj: Any) -> bool:
        """
        检查对象是否是方法
        
        Args:
            obj: 对象
            
        Returns:
            bool: 如果是方法则返回True，否则返回False
        """
        return inspect.ismethod(obj)

    @staticmethod
    def is_class(obj: Any) -> bool:
        """
        检查对象是否是类
        
        Args:
            obj: 对象
            
        Returns:
            bool: 如果是类则返回True，否则返回False
        """
        return inspect.isclass(obj)

    @staticmethod
    def is_instance_method(obj: Any) -> bool:
        """
        检查对象是否是实例方法
        
        Args:
            obj: 对象
            
        Returns:
            bool: 如果是实例方法则返回True，否则返回False
        """
        return inspect.ismethod(obj)

    @staticmethod
    def is_static_method(obj: Any) -> bool:
        """
        检查对象是否是静态方法
        
        Args:
            obj: 对象
            
        Returns:
            bool: 如果是静态方法则返回True，否则返回False
        """
        return isinstance(obj, staticmethod)

    @staticmethod
    def is_class_method(obj: Any) -> bool:
        """
        检查对象是否是类方法
        
        Args:
            obj: 对象
            
        Returns:
            bool: 如果是类方法则返回True，否则返回False
        """
        return isinstance(obj, classmethod)

    @staticmethod
    def get_members(obj: Any, predicate: Optional[callable] = None) -> List[tuple]:
        """
        获取对象的成员
        
        Args:
            obj: 对象
            predicate: 过滤函数
            
        Returns:
            List[tuple]: 成员列表
        """
        return inspect.getmembers(obj, predicate)

    @staticmethod
    def get_arguments(func: callable) -> List[str]:
        """
        获取函数的参数列表
        
        Args:
            func: 函数
            
        Returns:
            List[str]: 参数名列表
        """
        signature = inspect.signature(func)
        return list(signature.parameters.keys())

    @staticmethod
    def get_argument_defaults(func: callable) -> Dict[str, Any]:
        """
        获取函数参数的默认值
        
        Args:
            func: 函数
            
        Returns:
            Dict[str, Any]: 参数默认值字典
        """
        signature = inspect.signature(func)
        defaults = {}
        for name, param in signature.parameters.items():
            if param.default is not inspect.Parameter.empty:
                defaults[name] = param.default
        return defaults

    @staticmethod
    def dynamic_call(func: callable, args: List[Any] = None, kwargs: Dict[str, Any] = None) -> Any:
        """
        动态调用函数
        
        Args:
            func: 函数
            args: 位置参数列表
            kwargs: 关键字参数字典
            
        Returns:
            Any: 函数返回值
        """
        if args is None:
            args = []
        if kwargs is None:
            kwargs = {}
        return func(*args, **kwargs)

    @staticmethod
    def create_class(class_name: str, bases: tuple = (object,), namespace: Dict[str, Any] = None) -> Type:
        """
        动态创建类
        
        Args:
            class_name: 类名
            bases: 基类元组
            namespace: 命名空间字典
            
        Returns:
            Type: 创建的类
        """
        if namespace is None:
            namespace = {}
        return type(class_name, bases, namespace)
