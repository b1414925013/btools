from typing import Any, Union, List, Dict
from datetime import datetime

class Converter:
    """
    数据类型转换类，提供常用的数据类型转换方法
    """
    
    @staticmethod
    def to_int(value: Any, default: int = 0) -> int:
        """
        转换为整数
        
        Args:
            value: 要转换的值
            default (int): 转换失败时的默认值
            
        Returns:
            int: 转换后的整数或默认值
        """
        try:
            return int(value)
        except (ValueError, TypeError):
            return default
    
    @staticmethod
    def to_float(value: Any, default: float = 0.0) -> float:
        """
        转换为浮点数
        
        Args:
            value: 要转换的值
            default (float): 转换失败时的默认值
            
        Returns:
            float: 转换后的浮点数或默认值
        """
        try:
            return float(value)
        except (ValueError, TypeError):
            return default
    
    @staticmethod
    def to_bool(value: Any, default: bool = False) -> bool:
        """
        转换为布尔值
        
        Args:
            value: 要转换的值
            default (bool): 转换失败时的默认值
            
        Returns:
            bool: 转换后的布尔值或默认值
        """
        if value is None:
            return default
        
        if isinstance(value, bool):
            return value
        
        if isinstance(value, str):
            value = value.lower()
            if value in ('true', 'yes', 'y', '1', 't'):
                return True
            elif value in ('false', 'no', 'n', '0', 'f'):
                return False
        
        if isinstance(value, (int, float)):
            return value != 0
        
        return default
    
    @staticmethod
    def to_str(value: Any, default: str = '') -> str:
        """
        转换为字符串
        
        Args:
            value: 要转换的值
            default (str): 转换失败时的默认值
            
        Returns:
            str: 转换后的字符串或默认值
        """
        try:
            if value is None:
                return default
            return str(value)
        except:
            return default
    
    @staticmethod
    def to_list(value: Any, default: List = None) -> List:
        """
        转换为列表
        
        Args:
            value: 要转换的值
            default (List): 转换失败时的默认值
            
        Returns:
            List: 转换后的列表或默认值
        """
        if default is None:
            default = []
        
        if value is None:
            return default
        
        if isinstance(value, list):
            return value
        
        if isinstance(value, (tuple, set)):
            return list(value)
        
        if isinstance(value, str):
            return [value]
        
        return default
    
    @staticmethod
    def to_dict(value: Any, default: Dict = None) -> Dict:
        """
        转换为字典
        
        Args:
            value: 要转换的值
            default (Dict): 转换失败时的默认值
            
        Returns:
            Dict: 转换后的字典或默认值
        """
        if default is None:
            default = {}
        
        if value is None:
            return default
        
        if isinstance(value, dict):
            return value
        
        return default
    
    @staticmethod
    def to_datetime(value: Any, format: str = '%Y-%m-%d', default: datetime = None) -> datetime:
        """
        转换为datetime对象
        
        Args:
            value: 要转换的值
            format (str): 日期格式，默认为'%Y-%m-%d'
            default (datetime): 转换失败时的默认值
            
        Returns:
            datetime: 转换后的datetime对象或默认值
        """
        if value is None:
            return default
        
        if isinstance(value, datetime):
            return value
        
        try:
            return datetime.strptime(str(value), format)
        except (ValueError, TypeError):
            return default
    
    @staticmethod
    def datetime_to_str(dt: datetime, format: str = '%Y-%m-%d %H:%M:%S') -> str:
        """
        将datetime对象转换为字符串
        
        Args:
            dt (datetime): datetime对象
            format (str): 日期格式，默认为'%Y-%m-%d %H:%M:%S'
            
        Returns:
            str: 转换后的字符串
        """
        if not isinstance(dt, datetime):
            return ''
        
        try:
            return dt.strftime(format)
        except:
            return ''
    
    @staticmethod
    def camel_to_snake(name: str) -> str:
        """
        将驼峰命名转换为蛇形命名
        
        Args:
            name (str): 驼峰命名的字符串
            
        Returns:
            str: 蛇形命名的字符串
        """
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    @staticmethod
    def snake_to_camel(name: str, capitalize_first: bool = False) -> str:
        """
        将蛇形命名转换为驼峰命名
        
        Args:
            name (str): 蛇形命名的字符串
            capitalize_first (bool): 是否大写第一个字母，默认为False
            
        Returns:
            str: 驼峰命名的字符串
        """
        parts = name.split('_')
        if capitalize_first:
            return ''.join(part.capitalize() for part in parts)
        else:
            return parts[0] + ''.join(part.capitalize() for part in parts[1:])
