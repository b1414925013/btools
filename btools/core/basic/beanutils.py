"""Bean操作工具类"""
import copy
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

T = TypeVar('T')


class BeanUtils:
    """
    Bean操作工具类，提供对象属性的复制、比较、转换等功能
    """

    @staticmethod
    def copy_properties(source: Any, target: Any, ignore_properties: Optional[List[str]] = None) -> None:
        """
        复制对象属性
        
        Args:
            source: 源对象
            target: 目标对象
            ignore_properties: 忽略的属性列表
        """
        if source is None or target is None:
            return
        
        if ignore_properties is None:
            ignore_properties = []
        
        # 获取源对象的所有属性
        source_attrs = {attr: getattr(source, attr) for attr in dir(source) 
                      if not attr.startswith('__') and not callable(getattr(source, attr))}
        
        # 复制属性到目标对象，只复制非空值
        for attr, value in source_attrs.items():
            if attr not in ignore_properties and hasattr(target, attr) and value:
                setattr(target, attr, value)

    @staticmethod
    def deep_copy(obj: Any) -> Any:
        """
        深拷贝对象
        
        Args:
            obj: 要拷贝的对象
            
        Returns:
            拷贝后的对象
        """
        return copy.deepcopy(obj)

    @staticmethod
    def shallow_copy(obj: Any) -> Any:
        """
        浅拷贝对象
        
        Args:
            obj: 要拷贝的对象
            
        Returns:
            拷贝后的对象
        """
        return copy.copy(obj)

    @staticmethod
    def to_dict(obj: Any, ignore_properties: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        将对象转换为字典
        
        Args:
            obj: 要转换的对象
            ignore_properties: 忽略的属性列表
            
        Returns:
            转换后的字典
        """
        if obj is None:
            return {}
        
        if isinstance(obj, dict):
            return obj
        
        if ignore_properties is None:
            ignore_properties = []
        
        result = {}
        for attr in dir(obj):
            if attr.startswith('__') or callable(getattr(obj, attr)):
                continue
            if attr in ignore_properties:
                continue
            try:
                value = getattr(obj, attr)
                # 递归处理嵌套对象
                if hasattr(value, '__dict__') and not isinstance(value, (int, float, str, bool, list, dict, tuple, set)):
                    result[attr] = BeanUtils.to_dict(value, ignore_properties)
                else:
                    result[attr] = value
            except:
                pass
        return result

    @staticmethod
    def from_dict(cls: Type[T], data: Dict[str, Any]) -> T:
        """
        从字典创建对象
        
        Args:
            cls: 对象类型
            data: 字典数据
            
        Returns:
            创建的对象
        """
        obj = cls()
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return obj

    @staticmethod
    def equals(obj1: Any, obj2: Any, ignore_properties: Optional[List[str]] = None) -> bool:
        """
        比较两个对象是否相等
        
        Args:
            obj1: 第一个对象
            obj2: 第二个对象
            ignore_properties: 忽略的属性列表
            
        Returns:
            是否相等
        """
        if obj1 is obj2:
            return True
        
        if obj1 is None or obj2 is None:
            return False
        
        if type(obj1) != type(obj2):
            return False
        
        if isinstance(obj1, (int, float, str, bool, list, dict, tuple, set)):
            return obj1 == obj2
        
        if ignore_properties is None:
            ignore_properties = []
        
        # 获取两个对象的属性字典
        dict1 = BeanUtils.to_dict(obj1, ignore_properties)
        dict2 = BeanUtils.to_dict(obj2, ignore_properties)
        
        return dict1 == dict2

    @staticmethod
    def get_property(obj: Any, property_name: str) -> Any:
        """
        获取对象的属性值
        
        Args:
            obj: 对象
            property_name: 属性名，支持嵌套属性（如 "user.address.street"）
            
        Returns:
            属性值
        """
        if obj is None:
            return None
        
        # 处理嵌套属性
        properties = property_name.split('.')
        result = obj
        
        for prop in properties:
            if hasattr(result, prop):
                result = getattr(result, prop)
            else:
                return None
        
        return result

    @staticmethod
    def set_property(obj: Any, property_name: str, value: Any) -> bool:
        """
        设置对象的属性值
        
        Args:
            obj: 对象
            property_name: 属性名，支持嵌套属性（如 "user.address.street"）
            value: 属性值
            
        Returns:
            是否设置成功
        """
        if obj is None:
            return False
        
        # 处理嵌套属性
        properties = property_name.split('.')
        result = obj
        
        # 遍历到倒数第二个属性
        for prop in properties[:-1]:
            if hasattr(result, prop):
                result = getattr(result, prop)
            else:
                return False
        
        # 设置最后一个属性
        last_prop = properties[-1]
        if hasattr(result, last_prop):
            setattr(result, last_prop, value)
            return True
        
        return False

    @staticmethod
    def has_property(obj: Any, property_name: str) -> bool:
        """
        检查对象是否具有指定属性
        
        Args:
            obj: 对象
            property_name: 属性名，支持嵌套属性（如 "user.address.street"）
            
        Returns:
            是否具有该属性
        """
        if obj is None:
            return False
        
        # 处理嵌套属性
        properties = property_name.split('.')
        result = obj
        
        for prop in properties:
            if hasattr(result, prop):
                result = getattr(result, prop)
            else:
                return False
        
        return True

    @staticmethod
    def get_properties(obj: Any) -> List[str]:
        """
        获取对象的所有属性名
        
        Args:
            obj: 对象
            
        Returns:
            属性名列表
        """
        if obj is None:
            return []
        
        return [attr for attr in dir(obj) 
                if not attr.startswith('__') and not callable(getattr(obj, attr))]

    @staticmethod
    def merge(obj1: Any, obj2: Any, ignore_properties: Optional[List[str]] = None) -> Any:
        """
        合并两个对象的属性
        
        Args:
            obj1: 第一个对象
            obj2: 第二个对象
            ignore_properties: 忽略的属性列表
            
        Returns:
            合并后的对象
        """
        if obj1 is None:
            return obj2
        
        if obj2 is None:
            return obj1
        
        # 创建obj1的深拷贝
        result = BeanUtils.deep_copy(obj1)
        
        # 复制obj2的属性到result
        BeanUtils.copy_properties(obj2, result, ignore_properties)
        
        return result