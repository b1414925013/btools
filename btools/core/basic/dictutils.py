"""字典工具类"""
from typing import Any, Dict, List, Tuple, Union, Callable, Optional, Set, Iterable
import copy


class DictUtil:
    """字典工具类，提供字典相关的便捷操作"""

    @staticmethod
    def is_empty(dictionary: Optional[Dict]) -> bool:
        """
        判断字典是否为空
        
        Args:
            dictionary: 要判断的字典
            
        Returns:
            bool: 如果字典为None或空则返回True，否则返回False
        """
        return dictionary is None or len(dictionary) == 0

    @staticmethod
    def is_not_empty(dictionary: Optional[Dict]) -> bool:
        """
        判断字典是否不为空
        
        Args:
            dictionary: 要判断的字典
            
        Returns:
            bool: 如果字典不为None且不为空则返回True，否则返回False
        """
        return not DictUtil.is_empty(dictionary)

    @staticmethod
    def size(dictionary: Optional[Dict]) -> int:
        """
        获取字典大小
        
        Args:
            dictionary: 要获取大小的字典
            
        Returns:
            int: 字典大小，None返回0
        """
        return len(dictionary) if dictionary is not None else 0

    @staticmethod
    def get(dictionary: Optional[Dict], key: Any, default: Any = None) -> Any:
        """
        获取字典中的值
        
        Args:
            dictionary: 字典
            key: 键
            default: 默认值
            
        Returns:
            Any: 值，如果字典为None或键不存在则返回默认值
        """
        if dictionary is None:
            return default
        return dictionary.get(key, default)

    @staticmethod
    def get_int(dictionary: Optional[Dict], key: Any, default: int = 0) -> int:
        """
        获取字典中的整数值
        
        Args:
            dictionary: 字典
            key: 键
            default: 默认值
            
        Returns:
            int: 整数值，如果字典为None或键不存在则返回默认值
        """
        value = DictUtil.get(dictionary, key, default)
        try:
            return int(value)
        except (ValueError, TypeError):
            return default

    @staticmethod
    def get_float(dictionary: Optional[Dict], key: Any, default: float = 0.0) -> float:
        """
        获取字典中的浮点数值
        
        Args:
            dictionary: 字典
            key: 键
            default: 默认值
            
        Returns:
            float: 浮点数值，如果字典为None或键不存在则返回默认值
        """
        value = DictUtil.get(dictionary, key, default)
        try:
            return float(value)
        except (ValueError, TypeError):
            return default

    @staticmethod
    def get_bool(dictionary: Optional[Dict], key: Any, default: bool = False) -> bool:
        """
        获取字典中的布尔值
        
        Args:
            dictionary: 字典
            key: 键
            default: 默认值
            
        Returns:
            bool: 布尔值，如果字典为None或键不存在则返回默认值
        """
        value = DictUtil.get(dictionary, key, default)
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            lower_value = value.lower()
            if lower_value in ('true', '1', 'yes', 'on'):
                return True
            if lower_value in ('false', '0', 'no', 'off'):
                return False
        try:
            return bool(value)
        except (ValueError, TypeError):
            return default

    @staticmethod
    def get_str(dictionary: Optional[Dict], key: Any, default: str = '') -> str:
        """
        获取字典中的字符串值
        
        Args:
            dictionary: 字典
            key: 键
            default: 默认值
            
        Returns:
            str: 字符串值，如果字典为None或键不存在则返回默认值
        """
        value = DictUtil.get(dictionary, key, default)
        return str(value) if value is not None else default

    @staticmethod
    def get_list(dictionary: Optional[Dict], key: Any, default: Optional[List] = None) -> Optional[List]:
        """
        获取字典中的列表值
        
        Args:
            dictionary: 字典
            key: 键
            default: 默认值
            
        Returns:
            List: 列表值，如果字典为None或键不存在则返回默认值
        """
        value = DictUtil.get(dictionary, key, default)
        if isinstance(value, list):
            return value
        if default is None:
            return None
        return default

    @staticmethod
    def get_dict(dictionary: Optional[Dict], key: Any, default: Optional[Dict] = None) -> Optional[Dict]:
        """
        获取字典中的字典值
        
        Args:
            dictionary: 字典
            key: 键
            default: 默认值
            
        Returns:
            Dict: 字典值，如果字典为None或键不存在则返回默认值
        """
        value = DictUtil.get(dictionary, key, default)
        if isinstance(value, dict):
            return value
        if default is None:
            return None
        return default

    @staticmethod
    def put(dictionary: Optional[Dict], key: Any, value: Any) -> Optional[Dict]:
        """
        向字典中添加键值对
        
        Args:
            dictionary: 字典，如果为None则创建新字典
            key: 键
            value: 值
            
        Returns:
            Dict: 更新后的字典
        """
        if dictionary is None:
            dictionary = {}
        dictionary[key] = value
        return dictionary

    @staticmethod
    def put_all(dictionary: Optional[Dict], other: Optional[Dict]) -> Optional[Dict]:
        """
        将其他字典的所有键值对添加到当前字典中
        
        Args:
            dictionary: 当前字典，如果为None则创建新字典
            other: 其他字典
            
        Returns:
            Dict: 更新后的字典
        """
        if dictionary is None:
            dictionary = {}
        if other is not None:
            dictionary.update(other)
        return dictionary

    @staticmethod
    def put_if_absent(dictionary: Optional[Dict], key: Any, value: Any) -> Optional[Dict]:
        """
        当键不存在时向字典中添加键值对
        
        Args:
            dictionary: 字典，如果为None则创建新字典
            key: 键
            value: 值
            
        Returns:
            Dict: 更新后的字典
        """
        if dictionary is None:
            dictionary = {}
        if key not in dictionary:
            dictionary[key] = value
        return dictionary

    @staticmethod
    def remove(dictionary: Optional[Dict], key: Any) -> Optional[Dict]:
        """
        从字典中移除键值对
        
        Args:
            dictionary: 字典
            key: 键
            
        Returns:
            Dict: 更新后的字典
        """
        if dictionary is not None and key in dictionary:
            del dictionary[key]
        return dictionary

    @staticmethod
    def remove_all(dictionary: Optional[Dict], keys: Iterable[Any]) -> Optional[Dict]:
        """
        从字典中移除多个键值对
        
        Args:
            dictionary: 字典
            keys: 键的集合
            
        Returns:
            Dict: 更新后的字典
        """
        if dictionary is not None:
            for key in keys:
                if key in dictionary:
                    del dictionary[key]
        return dictionary

    @staticmethod
    def clear(dictionary: Optional[Dict]) -> Optional[Dict]:
        """
        清空字典
        
        Args:
            dictionary: 字典
            
        Returns:
            Dict: 清空后的字典
        """
        if dictionary is not None:
            dictionary.clear()
        return dictionary

    @staticmethod
    def contains_key(dictionary: Optional[Dict], key: Any) -> bool:
        """
        判断字典中是否包含指定键
        
        Args:
            dictionary: 字典
            key: 键
            
        Returns:
            bool: 如果字典包含指定键则返回True，否则返回False
        """
        return dictionary is not None and key in dictionary

    @staticmethod
    def contains_value(dictionary: Optional[Dict], value: Any) -> bool:
        """
        判断字典中是否包含指定值
        
        Args:
            dictionary: 字典
            value: 值
            
        Returns:
            bool: 如果字典包含指定值则返回True，否则返回False
        """
        return dictionary is not None and value in dictionary.values()

    @staticmethod
    def keys(dictionary: Optional[Dict]) -> List[Any]:
        """
        获取字典的所有键
        
        Args:
            dictionary: 字典
            
        Returns:
            List: 键的列表
        """
        if dictionary is None:
            return []
        return list(dictionary.keys())

    @staticmethod
    def values(dictionary: Optional[Dict]) -> List[Any]:
        """
        获取字典的所有值
        
        Args:
            dictionary: 字典
            
        Returns:
            List: 值的列表
        """
        if dictionary is None:
            return []
        return list(dictionary.values())

    @staticmethod
    def items(dictionary: Optional[Dict]) -> List[Tuple[Any, Any]]:
        """
        获取字典的所有键值对
        
        Args:
            dictionary: 字典
            
        Returns:
            List: 键值对元组的列表
        """
        if dictionary is None:
            return []
        return list(dictionary.items())

    @staticmethod
    def invert(dictionary: Optional[Dict]) -> Dict:
        """
        反转字典的键和值
        
        Args:
            dictionary: 字典
            
        Returns:
            Dict: 反转后的字典
        """
        if dictionary is None:
            return {}
        return {v: k for k, v in dictionary.items()}

    @staticmethod
    def merge(*dictionaries: Optional[Dict], overwrite: bool = True) -> Dict:
        """
        合并多个字典
        
        Args:
            *dictionaries: 要合并的字典
            overwrite: 是否覆盖重复键的值，默认为True
            
        Returns:
            Dict: 合并后的字典
        """
        result = {}
        for dictionary in dictionaries:
            if dictionary is not None:
                if overwrite:
                    result.update(dictionary)
                else:
                    for key, value in dictionary.items():
                        if key not in result:
                            result[key] = value
        return result

    @staticmethod
    def filter(dictionary: Optional[Dict], predicate: Callable[[Any, Any], bool]) -> Dict:
        """
        过滤字典
        
        Args:
            dictionary: 字典
            predicate: 过滤函数，接收键和值，返回True表示保留
            
        Returns:
            Dict: 过滤后的字典
        """
        if dictionary is None:
            return {}
        return {k: v for k, v in dictionary.items() if predicate(k, v)}

    @staticmethod
    def filter_keys(dictionary: Optional[Dict], predicate: Callable[[Any], bool]) -> Dict:
        """
        根据键过滤字典
        
        Args:
            dictionary: 字典
            predicate: 过滤函数，接收键，返回True表示保留
            
        Returns:
            Dict: 过滤后的字典
        """
        if dictionary is None:
            return {}
        return {k: v for k, v in dictionary.items() if predicate(k)}

    @staticmethod
    def filter_values(dictionary: Optional[Dict], predicate: Callable[[Any], bool]) -> Dict:
        """
        根据值过滤字典
        
        Args:
            dictionary: 字典
            predicate: 过滤函数，接收值，返回True表示保留
            
        Returns:
            Dict: 过滤后的字典
        """
        if dictionary is None:
            return {}
        return {k: v for k, v in dictionary.items() if predicate(v)}

    @staticmethod
    def map_keys(dictionary: Optional[Dict], mapper: Callable[[Any], Any]) -> Dict:
        """
        映射字典的键
        
        Args:
            dictionary: 字典
            mapper: 映射函数，接收键，返回新键
            
        Returns:
            Dict: 键映射后的字典
        """
        if dictionary is None:
            return {}
        return {mapper(k): v for k, v in dictionary.items()}

    @staticmethod
    def map_values(dictionary: Optional[Dict], mapper: Callable[[Any], Any]) -> Dict:
        """
        映射字典的值
        
        Args:
            dictionary: 字典
            mapper: 映射函数，接收值，返回新值
            
        Returns:
            Dict: 值映射后的字典
        """
        if dictionary is None:
            return {}
        return {k: mapper(v) for k, v in dictionary.items()}

    @staticmethod
    def map_items(dictionary: Optional[Dict], mapper: Callable[[Any, Any], Tuple[Any, Any]]) -> Dict:
        """
        映射字典的键值对
        
        Args:
            dictionary: 字典
            mapper: 映射函数，接收键和值，返回新键值对元组
            
        Returns:
            Dict: 键值对映射后的字典
        """
        if dictionary is None:
            return {}
        return dict(mapper(k, v) for k, v in dictionary.items())

    @staticmethod
    def sort_by_key(dictionary: Optional[Dict], reverse: bool = False) -> Dict:
        """
        按键排序字典
        
        Args:
            dictionary: 字典
            reverse: 是否倒序，默认为False
            
        Returns:
            Dict: 排序后的字典
        """
        if dictionary is None:
            return {}
        sorted_items = sorted(dictionary.items(), key=lambda x: x[0], reverse=reverse)
        return dict(sorted_items)

    @staticmethod
    def sort_by_value(dictionary: Optional[Dict], reverse: bool = False) -> Dict:
        """
        按值排序字典
        
        Args:
            dictionary: 字典
            reverse: 是否倒序，默认为False
            
        Returns:
            Dict: 排序后的字典
        """
        if dictionary is None:
            return {}
        sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse)
        return dict(sorted_items)

    @staticmethod
    def slice(dictionary: Optional[Dict], keys: Iterable[Any]) -> Dict:
        """
        提取字典的部分键值对
        
        Args:
            dictionary: 字典
            keys: 要提取的键的集合
            
        Returns:
            Dict: 提取后的字典
        """
        if dictionary is None:
            return {}
        return {k: dictionary[k] for k in keys if k in dictionary}

    @staticmethod
    def omit(dictionary: Optional[Dict], keys: Iterable[Any]) -> Dict:
        """
        忽略字典的部分键值对
        
        Args:
            dictionary: 字典
            keys: 要忽略的键的集合
            
        Returns:
            Dict: 忽略后的字典
        """
        if dictionary is None:
            return {}
        key_set = set(keys)
        return {k: v for k, v in dictionary.items() if k not in key_set}

    @staticmethod
    def to_list(dictionary: Optional[Dict]) -> List[Dict]:
        """
        将字典转换为键值对列表
        
        Args:
            dictionary: 字典
            
        Returns:
            List: 键值对列表，每个元素为{'key': key, 'value': value}
        """
        if dictionary is None:
            return []
        return [{'key': k, 'value': v} for k, v in dictionary.items()]

    @staticmethod
    def from_list(lst: Optional[List[Dict]], key_field: str = 'key', value_field: str = 'value') -> Dict:
        """
        将键值对列表转换为字典
        
        Args:
            lst: 键值对列表
            key_field: 键字段名，默认为'key'
            value_field: 值字段名，默认为'value'
            
        Returns:
            Dict: 转换后的字典
        """
        if lst is None:
            return {}
        result = {}
        for item in lst:
            if key_field in item and value_field in item:
                result[item[key_field]] = item[value_field]
        return result

    @staticmethod
    def deep_copy(dictionary: Optional[Dict]) -> Optional[Dict]:
        """
        深拷贝字典
        
        Args:
            dictionary: 字典
            
        Returns:
            Dict: 深拷贝后的字典
        """
        if dictionary is None:
            return None
        return copy.deepcopy(dictionary)

    @staticmethod
    def shallow_copy(dictionary: Optional[Dict]) -> Optional[Dict]:
        """
        浅拷贝字典
        
        Args:
            dictionary: 字典
            
        Returns:
            Dict: 浅拷贝后的字典
        """
        if dictionary is None:
            return None
        return dictionary.copy()

    @staticmethod
    def get_nested(dictionary: Optional[Dict], keys: List[Any], default: Any = None) -> Any:
        """
        获取嵌套字典中的值
        
        Args:
            dictionary: 字典
            keys: 键路径列表
            default: 默认值
            
        Returns:
            Any: 嵌套值，如果路径不存在则返回默认值
        """
        if dictionary is None:
            return default
        current = dictionary
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        return current

    @staticmethod
    def set_nested(dictionary: Optional[Dict], keys: List[Any], value: Any) -> Dict:
        """
        设置嵌套字典中的值
        
        Args:
            dictionary: 字典，如果为None则创建新字典
            keys: 键路径列表
            value: 要设置的值
            
        Returns:
            Dict: 更新后的字典
        """
        if dictionary is None:
            dictionary = {}
        current = dictionary
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        current[keys[-1]] = value
        return dictionary

    @staticmethod
    def has_nested(dictionary: Optional[Dict], keys: List[Any]) -> bool:
        """
        判断嵌套字典中是否存在指定路径
        
        Args:
            dictionary: 字典
            keys: 键路径列表
            
        Returns:
            bool: 如果路径存在则返回True，否则返回False
        """
        if dictionary is None:
            return False
        current = dictionary
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return False
        return True

    @staticmethod
    def group_by(lst: Optional[List], key_mapper: Callable[[Any], Any]) -> Dict:
        """
        将列表按指定键分组
        
        Args:
            lst: 列表
            key_mapper: 键映射函数，接收列表元素，返回分组键
            
        Returns:
            Dict: 分组后的字典
        """
        if lst is None:
            return {}
        result = {}
        for item in lst:
            key = key_mapper(item)
            if key not in result:
                result[key] = []
            result[key].append(item)
        return result

    @staticmethod
    def count_by(lst: Optional[List], key_mapper: Callable[[Any], Any]) -> Dict:
        """
        统计列表元素按指定键出现的次数
        
        Args:
            lst: 列表
            key_mapper: 键映射函数，接收列表元素，返回统计键
            
        Returns:
            Dict: 统计结果字典
        """
        if lst is None:
            return {}
        result = {}
        for item in lst:
            key = key_mapper(item)
            result[key] = result.get(key, 0) + 1
        return result
