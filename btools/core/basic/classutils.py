import inspect
import importlib
import sys
from typing import Type, List, Dict, Any, Optional, Tuple, Union


class ClassUtils:
    """
    类工具类，提供类相关的操作功能
    """

    @staticmethod
    def get_class_name(cls: Type) -> str:
        """
        获取类的名称
        
        Args:
            cls: 类
            
        Returns:
            str: 类的名称
        """
        return cls.__name__

    @staticmethod
    def get_package_name(cls: Type) -> str:
        """
        获取类所在的包名称
        
        Args:
            cls: 类
            
        Returns:
            str: 包名称
        """
        module = inspect.getmodule(cls)
        if module:
            return module.__name__.rpartition('.')[0] if '.' in module.__name__ else ''
        return ''

    @staticmethod
    def get_module_name(cls: Type) -> str:
        """
        获取类所在的模块名称
        
        Args:
            cls: 类
            
        Returns:
            str: 模块名称
        """
        module = inspect.getmodule(cls)
        if module:
            return module.__name__
        return ''

    @staticmethod
    def get_full_class_name(cls: Type) -> str:
        """
        获取类的完整名称（包含包名和模块名）
        
        Args:
            cls: 类
            
        Returns:
            str: 完整类名
        """
        module = inspect.getmodule(cls)
        if module:
            return f"{module.__name__}.{cls.__name__}"
        return cls.__name__

    @staticmethod
    def load_class(class_name: str) -> Optional[Type]:
        """
        加载类
        
        Args:
            class_name: 类的完整名称（包含包名和模块名）
            
        Returns:
            Optional[Type]: 加载的类，如果加载失败则返回None
        """
        try:
            # 分割模块名和类名
            if '.' in class_name:
                module_name, class_name = class_name.rsplit('.', 1)
                module = importlib.import_module(module_name)
                return getattr(module, class_name)
            else:
                # 尝试从当前模块或内置模块加载
                return getattr(sys.modules['__main__'], class_name, None)
        except (ImportError, AttributeError):
            return None

    @staticmethod
    def is_interface(cls: Type) -> bool:
        """
        检查类是否为接口
        
        Args:
            cls: 类
            
        Returns:
            bool: 如果是接口则返回True，否则返回False
        """
        # 在Python中，接口通常使用抽象基类（ABC）实现
        return inspect.isabstract(cls) and not inspect.isclass(cls) is False

    @staticmethod
    def is_abstract(cls: Type) -> bool:
        """
        检查类是否为抽象类
        
        Args:
            cls: 类
            
        Returns:
            bool: 如果是抽象类则返回True，否则返回False
        """
        return inspect.isabstract(cls)

    @staticmethod
    def is_concrete(cls: Type) -> bool:
        """
        检查类是否为具体类（非抽象类）
        
        Args:
            cls: 类
            
        Returns:
            bool: 如果是具体类则返回True，否则返回False
        """
        return not inspect.isabstract(cls)

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
    def get_interfaces(cls: Type) -> List[Type]:
        """
        获取类实现的所有接口
        
        Args:
            cls: 类
            
        Returns:
            List[Type]: 接口列表
        """
        interfaces = []
        for base in inspect.getmro(cls):
            if inspect.isabstract(base) and base is not cls:
                interfaces.append(base)
        return interfaces

    @staticmethod
    def get_constructors(cls: Type) -> List[Any]:
        """
        获取类的所有构造器
        
        Args:
            cls: 类
            
        Returns:
            List[Any]: 构造器列表
        """
        constructors = []
        for name, member in inspect.getmembers(cls):
            if name == '__init__' and inspect.isfunction(member):
                constructors.append(member)
        return constructors

    @staticmethod
    def get_methods(cls: Type) -> List[Any]:
        """
        获取类的所有方法
        
        Args:
            cls: 类
            
        Returns:
            List[Any]: 方法列表
        """
        methods = []
        for name, member in inspect.getmembers(cls, predicate=inspect.isfunction):
            if not name.startswith('__') or name in ('__init__', '__str__', '__repr__'):
                methods.append(member)
        return methods

    @staticmethod
    def get_fields(cls: Type) -> List[Tuple[str, Any]]:
        """
        获取类的所有字段
        
        Args:
            cls: 类
            
        Returns:
            List[Tuple[str, Any]]: 字段列表，每个元素为(字段名, 字段值)
        """
        fields = []
        for name, member in inspect.getmembers(cls):
            if not name.startswith('__') and not inspect.isfunction(member) and not inspect.isclass(member):
                fields.append((name, member))
        return fields

    @staticmethod
    def get_all_members(cls: Type) -> Dict[str, Any]:
        """
        获取类的所有成员
        
        Args:
            cls: 类
            
        Returns:
            Dict[str, Any]: 成员字典，键为成员名称，值为成员对象
        """
        return dict(inspect.getmembers(cls))

    @staticmethod
    def instantiate(cls: Type, *args: Any, **kwargs: Any) -> Optional[Any]:
        """
        实例化类
        
        Args:
            cls: 类
            *args: 构造器参数
            **kwargs: 构造器关键字参数
            
        Returns:
            Optional[Any]: 实例化的对象，如果实例化失败则返回None
        """
        try:
            return cls(*args, **kwargs)
        except Exception:
            return None

    @staticmethod
    def is_subclass(sub_cls: Type, super_cls: Type) -> bool:
        """
        检查类是否为指定类的子类
        
        Args:
            sub_cls: 子类
            super_cls: 父类
            
        Returns:
            bool: 如果是子类则返回True，否则返回False
        """
        return issubclass(sub_cls, super_cls)

    @staticmethod
    def implements_interface(cls: Type, interface: Type) -> bool:
        """
        检查类是否实现了指定的接口
        
        Args:
            cls: 类
            interface: 接口
            
        Returns:
            bool: 如果实现了接口则返回True，否则返回False
        """
        try:
            return issubclass(cls, interface)
        except TypeError:
            return False

    @staticmethod
    def get_class_loader(cls: Type) -> Optional[Any]:
        """
        获取类的加载器
        
        Args:
            cls: 类
            
        Returns:
            Optional[Any]: 类加载器，如果获取失败则返回None
        """
        module = inspect.getmodule(cls)
        if module:
            return getattr(module, '__loader__', None)
        return None

    @staticmethod
    def get_class_path(cls: Type) -> Optional[str]:
        """
        获取类的路径
        
        Args:
            cls: 类
            
        Returns:
            Optional[str]: 类的路径，如果获取失败则返回None
        """
        module = inspect.getmodule(cls)
        if module and hasattr(module, '__file__'):
            return module.__file__
        return None

    @staticmethod
    def is_inner_class(cls: Type) -> bool:
        """
        检查类是否为内部类
        
        Args:
            cls: 类
            
        Returns:
            bool: 如果是内部类则返回True，否则返回False
        """
        return '.' in cls.__qualname__

    @staticmethod
    def get_outer_class(cls: Type) -> Optional[Type]:
        """
        获取内部类的外部类
        
        Args:
            cls: 内部类
            
        Returns:
            Optional[Type]: 外部类，如果不是内部类则返回None
        """
        if not ClassUtils.is_inner_class(cls):
            return None
        
        try:
            # 获取外部类的名称
            outer_class_name = cls.__qualname__.rpartition('.')[0]
            # 尝试从模块中获取外部类
            module = inspect.getmodule(cls)
            if module:
                return getattr(module, outer_class_name, None)
        except Exception:
            pass
        
        return None

    @staticmethod
    def get_class_annotations(cls: Type) -> Dict[str, Any]:
        """
        获取类的注解
        
        Args:
            cls: 类
            
        Returns:
            Dict[str, Any]: 注解字典
        """
        return getattr(cls, '__annotations__', {})

    @staticmethod
    def get_method_annotations(cls: Type, method_name: str) -> Dict[str, Any]:
        """
        获取类方法的注解
        
        Args:
            cls: 类
            method_name: 方法名称
            
        Returns:
            Dict[str, Any]: 注解字典
        """
        try:
            method = getattr(cls, method_name)
            if inspect.isfunction(method):
                return getattr(method, '__annotations__', {})
        except AttributeError:
            pass
        return {}

    @staticmethod
    def get_field_annotations(cls: Type, field_name: str) -> Dict[str, Any]:
        """
        获取类字段的注解
        
        Args:
            cls: 类
            field_name: 字段名称
            
        Returns:
            Dict[str, Any]: 注解字典
        """
        annotations = getattr(cls, '__annotations__', {})
        return {k: v for k, v in annotations.items() if k == field_name}

    @staticmethod
    def is_final(cls: Type) -> bool:
        """
        检查类是否为最终类（不可继承）
        
        Args:
            cls: 类
            
        Returns:
            bool: 如果是最终类则返回True，否则返回False
        """
        # 在Python中，没有真正的final类，但可以通过abc.ABCMeta或自定义元类实现
        # 这里简单检查是否有__final__属性
        return getattr(cls, '__final__', False)

    @staticmethod
    def is_static(cls: Type, member_name: str) -> bool:
        """
        检查类成员是否为静态成员
        
        Args:
            cls: 类
            member_name: 成员名称
            
        Returns:
            bool: 如果是静态成员则返回True，否则返回False
        """
        try:
            member = getattr(cls, member_name)
            return not inspect.ismethod(member)
        except AttributeError:
            return False

    @staticmethod
    def is_private(cls: Type, member_name: str) -> bool:
        """
        检查类成员是否为私有成员
        
        Args:
            cls: 类
            member_name: 成员名称
            
        Returns:
            bool: 如果是私有成员则返回True，否则返回False
        """
        return member_name.startswith('__') and not member_name.endswith('__')

    @staticmethod
    def is_protected(cls: Type, member_name: str) -> bool:
        """
        检查类成员是否为保护成员
        
        Args:
            cls: 类
            member_name: 成员名称
            
        Returns:
            bool: 如果是保护成员则返回True，否则返回False
        """
        return member_name.startswith('_') and not member_name.startswith('__')

    @staticmethod
    def get_class_hierarchy(cls: Type) -> List[Type]:
        """
        获取类的继承层次结构
        
        Args:
            cls: 类
            
        Returns:
            List[Type]: 继承层次结构列表，从当前类到object
        """
        return list(inspect.getmro(cls))

    @staticmethod
    def get_common_super_class(classes: List[Type]) -> Optional[Type]:
        """
        获取多个类的共同父类
        
        Args:
            classes: 类列表
            
        Returns:
            Optional[Type]: 共同父类，如果没有则返回None
        """
        if not classes:
            return None
        
        # 获取第一个类的所有父类
        common_classes = set(inspect.getmro(classes[0]))
        
        # 求所有类的父类的交集
        for cls in classes[1:]:
            common_classes.intersection_update(inspect.getmro(cls))
        
        # 按继承顺序排序，返回最具体的共同父类
        if common_classes:
            for cls in inspect.getmro(classes[0]):
                if cls in common_classes:
                    return cls
        
        return None
