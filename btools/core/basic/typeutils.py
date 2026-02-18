import typing
from typing import Any, Type, TypeVar, Generic, Union, Optional, List, Dict, Tuple
import inspect
import sys

T = TypeVar('T')


class TypeUtils:
    """
    类型工具类，提供类型相关的操作功能
    """

    @staticmethod
    def is_type(obj: Any, type_: Type) -> bool:
        """
        检查对象是否为指定类型
        
        Args:
            obj: 要检查的对象
            type_: 类型
            
        Returns:
            bool: 如果对象是指定类型则返回True，否则返回False
        """
        return isinstance(obj, type_)

    @staticmethod
    def is_none(obj: Any) -> bool:
        """
        检查对象是否为None
        
        Args:
            obj: 要检查的对象
            
        Returns:
            bool: 如果对象是None则返回True，否则返回False
        """
        return obj is None

    @staticmethod
    def is_not_none(obj: Any) -> bool:
        """
        检查对象是否不为None
        
        Args:
            obj: 要检查的对象
            
        Returns:
            bool: 如果对象不是None则返回True，否则返回False
        """
        return obj is not None

    @staticmethod
    def is_empty(obj: Any) -> bool:
        """
        检查对象是否为空
        
        Args:
            obj: 要检查的对象
            
        Returns:
            bool: 如果对象为空则返回True，否则返回False
        """
        if obj is None:
            return True
        if isinstance(obj, (str, list, tuple, dict, set)):
            return len(obj) == 0
        if hasattr(obj, '__len__'):
            return len(obj) == 0
        return False

    @staticmethod
    def is_not_empty(obj: Any) -> bool:
        """
        检查对象是否不为空
        
        Args:
            obj: 要检查的对象
            
        Returns:
            bool: 如果对象不为空则返回True，否则返回False
        """
        return not TypeUtils.is_empty(obj)

    @staticmethod
    def cast(obj: Any, type_: Type[T]) -> T:
        """
        将对象转换为指定类型
        
        Args:
            obj: 要转换的对象
            type_: 目标类型
            
        Returns:
            T: 转换后的对象
        """
        if obj is None:
            return None
        try:
            return type_(obj)
        except (ValueError, TypeError):
            return obj

    @staticmethod
    def safe_cast(obj: Any, type_: Type[T], default: T = None) -> T:
        """
        安全地将对象转换为指定类型
        
        Args:
            obj: 要转换的对象
            type_: 目标类型
            default: 转换失败时的默认值
            
        Returns:
            T: 转换后的对象或默认值
        """
        if obj is None:
            return default
        try:
            return type_(obj)
        except (ValueError, TypeError):
            return default

    @staticmethod
    def get_type(obj: Any) -> Type:
        """
        获取对象的类型
        
        Args:
            obj: 要获取类型的对象
            
        Returns:
            Type: 对象的类型
        """
        return type(obj)

    @staticmethod
    def get_type_name(obj: Any) -> str:
        """
        获取对象的类型名称
        
        Args:
            obj: 要获取类型名称的对象
            
        Returns:
            str: 对象的类型名称
        """
        if obj is None:
            return 'NoneType'
        return type(obj).__name__

    @staticmethod
    def get_full_type_name(obj: Any) -> str:
        """
        获取对象的完整类型名称（包含模块名）
        
        Args:
            obj: 要获取完整类型名称的对象
            
        Returns:
            str: 对象的完整类型名称
        """
        if obj is None:
            return 'NoneType'
        type_ = type(obj)
        module = type_.__module__
        if module == 'builtins':
            return type_.__name__
        return f'{module}.{type_.__name__}'

    @staticmethod
    def is_generic_type(type_: Type) -> bool:
        """
        检查类型是否为泛型类型
        
        Args:
            type_: 要检查的类型
            
        Returns:
            bool: 如果类型是泛型类型则返回True，否则返回False
        """
        return hasattr(type_, '__origin__') and type_.__origin__ is not None

    @staticmethod
    def get_generic_type(type_: Type) -> Type:
        """
        获取泛型类型的原始类型
        
        Args:
            type_: 泛型类型
            
        Returns:
            Type: 原始类型
        """
        if hasattr(type_, '__origin__'):
            return type_.__origin__
        return type_

    @staticmethod
    def get_type_args(type_: Type) -> Tuple[Type, ...]:
        """
        获取类型的类型参数
        
        Args:
            type_: 类型
            
        Returns:
            Tuple[Type, ...]: 类型参数
        """
        if hasattr(type_, '__args__'):
            return type_.__args__ or ()
        return ()

    @staticmethod
    def is_optional_type(type_: Type) -> bool:
        """
        检查类型是否为Optional类型
        
        Args:
            type_: 要检查的类型
            
        Returns:
            bool: 如果类型是Optional类型则返回True，否则返回False
        """
        origin = TypeUtils.get_generic_type(type_)
        return origin is Union and len(TypeUtils.get_type_args(type_)) == 2 and type(None) in TypeUtils.get_type_args(type_)

    @staticmethod
    def get_optional_type(type_: Type) -> Type:
        """
        获取Optional类型的实际类型
        
        Args:
            type_: Optional类型
            
        Returns:
            Type: 实际类型
        """
        if TypeUtils.is_optional_type(type_):
            args = TypeUtils.get_type_args(type_)
            for arg in args:
                if arg is not type(None):
                    return arg
        return type_

    @staticmethod
    def is_union_type(type_: Type) -> bool:
        """
        检查类型是否为Union类型
        
        Args:
            type_: 要检查的类型
            
        Returns:
            bool: 如果类型是Union类型则返回True，否则返回False
        """
        origin = TypeUtils.get_generic_type(type_)
        return origin is Union

    @staticmethod
    def get_union_types(type_: Type) -> Tuple[Type, ...]:
        """
        获取Union类型的所有类型
        
        Args:
            type_: Union类型
            
        Returns:
            Tuple[Type, ...]: 所有类型
        """
        if TypeUtils.is_union_type(type_):
            return TypeUtils.get_type_args(type_)
        return (type_,)

    @staticmethod
    def is_list_type(type_: Type) -> bool:
        """
        检查类型是否为List类型
        
        Args:
            type_: 要检查的类型
            
        Returns:
            bool: 如果类型是List类型则返回True，否则返回False
        """
        origin = TypeUtils.get_generic_type(type_)
        return origin is list

    @staticmethod
    def get_list_element_type(type_: Type) -> Type:
        """
        获取List类型的元素类型
        
        Args:
            type_: List类型
            
        Returns:
            Type: 元素类型
        """
        if TypeUtils.is_list_type(type_):
            args = TypeUtils.get_type_args(type_)
            if args:
                return args[0]
        return Any

    @staticmethod
    def is_dict_type(type_: Type) -> bool:
        """
        检查类型是否为Dict类型
        
        Args:
            type_: 要检查的类型
            
        Returns:
            bool: 如果类型是Dict类型则返回True，否则返回False
        """
        origin = TypeUtils.get_generic_type(type_)
        return origin is dict

    @staticmethod
    def get_dict_key_type(type_: Type) -> Type:
        """
        获取Dict类型的键类型
        
        Args:
            type_: Dict类型
            
        Returns:
            Type: 键类型
        """
        if TypeUtils.is_dict_type(type_):
            args = TypeUtils.get_type_args(type_)
            if len(args) > 0:
                return args[0]
        return Any

    @staticmethod
    def get_dict_value_type(type_: Type) -> Type:
        """
        获取Dict类型的值类型
        
        Args:
            type_: Dict类型
            
        Returns:
            Type: 值类型
        """
        if TypeUtils.is_dict_type(type_):
            args = TypeUtils.get_type_args(type_)
            if len(args) > 1:
                return args[1]
        return Any

    @staticmethod
    def is_tuple_type(type_: Type) -> bool:
        """
        检查类型是否为Tuple类型
        
        Args:
            type_: 要检查的类型
            
        Returns:
            bool: 如果类型是Tuple类型则返回True，否则返回False
        """
        origin = TypeUtils.get_generic_type(type_)
        return origin is tuple

    @staticmethod
    def get_tuple_element_types(type_: Type) -> Tuple[Type, ...]:
        """
        获取Tuple类型的元素类型
        
        Args:
            type_: Tuple类型
            
        Returns:
            Tuple[Type, ...]: 元素类型
        """
        if TypeUtils.is_tuple_type(type_):
            args = TypeUtils.get_type_args(type_)
            if args:
                return args
        return ()

    @staticmethod
    def is_callable_type(obj: Any) -> bool:
        """
        检查对象是否为可调用对象
        
        Args:
            obj: 要检查的对象
            
        Returns:
            bool: 如果对象是可调用对象则返回True，否则返回False
        """
        return callable(obj)

    @staticmethod
    def is_function(obj: Any) -> bool:
        """
        检查对象是否为函数
        
        Args:
            obj: 要检查的对象
            
        Returns:
            bool: 如果对象是函数则返回True，否则返回False
        """
        return inspect.isfunction(obj)

    @staticmethod
    def is_method(obj: Any) -> bool:
        """
        检查对象是否为方法
        
        Args:
            obj: 要检查的对象
            
        Returns:
            bool: 如果对象是方法则返回True，否则返回False
        """
        return inspect.ismethod(obj)

    @staticmethod
    def is_class(obj: Any) -> bool:
        """
        检查对象是否为类
        
        Args:
            obj: 要检查的对象
            
        Returns:
            bool: 如果对象是类则返回True，否则返回False
        """
        return inspect.isclass(obj)

    @staticmethod
    def is_instance(obj: Any, type_: Type) -> bool:
        """
        检查对象是否为指定类型的实例
        
        Args:
            obj: 要检查的对象
            type_: 类型
            
        Returns:
            bool: 如果对象是指定类型的实例则返回True，否则返回False
        """
        return isinstance(obj, type_)

    @staticmethod
    def is_subclass(cls: Type, base_cls: Type) -> bool:
        """
        检查类是否为指定类的子类
        
        Args:
            cls: 要检查的类
            base_cls: 基类
            
        Returns:
            bool: 如果类是指定类的子类则返回True，否则返回False
        """
        return issubclass(cls, base_cls)

    @staticmethod
    def get_super_classes(cls: Type) -> List[Type]:
        """
        获取类的所有父类
        
        Args:
            cls: 类
            
        Returns:
            List[Type]: 父类列表
        """
        return inspect.getmro(cls)[1:]

    @staticmethod
    def get_class_annotations(cls: Type) -> Dict[str, Type]:
        """
        获取类的注解
        
        Args:
            cls: 类
            
        Returns:
            Dict[str, Type]: 注解字典
        """
        return getattr(cls, '__annotations__', {})

    @staticmethod
    def get_function_annotations(func: Any) -> Dict[str, Type]:
        """
        获取函数的注解
        
        Args:
            func: 函数
            
        Returns:
            Dict[str, Type]: 注解字典
        """
        if not callable(func):
            return {}
        return getattr(func, '__annotations__', {})

    @staticmethod
    def get_module_name(obj: Any) -> str:
        """
        获取对象所在的模块名称
        
        Args:
            obj: 对象
            
        Returns:
            str: 模块名称
        """
        if obj is None:
            return ''
        module = inspect.getmodule(obj)
        if module:
            return module.__name__
        return ''

    @staticmethod
    def get_qualified_name(obj: Any) -> str:
        """
        获取对象的限定名称
        
        Args:
            obj: 对象
            
        Returns:
            str: 限定名称
        """
        if obj is None:
            return ''
        if hasattr(obj, '__qualname__'):
            return obj.__qualname__
        if hasattr(obj, '__name__'):
            return obj.__name__
        return str(obj)

    @staticmethod
    def is_builtin_type(type_: Type) -> bool:
        """
        检查类型是否为内置类型
        
        Args:
            type_: 要检查的类型
            
        Returns:
            bool: 如果类型是内置类型则返回True，否则返回False
        """
        return type_.__module__ == 'builtins'

    @staticmethod
    def is_custom_type(type_: Type) -> bool:
        """
        检查类型是否为自定义类型
        
        Args:
            type_: 要检查的类型
            
        Returns:
            bool: 如果类型是自定义类型则返回True，否则返回False
        """
        return type_.__module__ != 'builtins'
