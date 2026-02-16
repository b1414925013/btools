import re
from typing import Union, List, Dict, Any

class Validator:
    """
    数据验证类，提供常用的数据验证方法
    """
    
    @staticmethod
    def is_email(email: str) -> bool:
        """
        验证邮箱地址格式
        
        Args:
            email (str): 邮箱地址
            
        Returns:
            bool: 如果格式正确返回True，否则返回False
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def is_phone(phone: str) -> bool:
        """
        验证手机号码格式（中国大陆）
        
        Args:
            phone (str): 手机号码
            
        Returns:
            bool: 如果格式正确返回True，否则返回False
        """
        pattern = r'^1[3-9]\d{9}$'
        return re.match(pattern, phone) is not None
    
    @staticmethod
    def is_url(url: str) -> bool:
        """
        验证URL格式
        
        Args:
            url (str): URL地址
            
        Returns:
            bool: 如果格式正确返回True，否则返回False
        """
        pattern = r'^https?://[\w\-]+(\.[\w\-]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?$'
        return re.match(pattern, url) is not None
    
    @staticmethod
    def is_ipv4(ip: str) -> bool:
        """
        验证IPv4地址格式
        
        Args:
            ip (str): IPv4地址
            
        Returns:
            bool: 如果格式正确返回True，否则返回False
        """
        pattern = r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$'
        return re.match(pattern, ip) is not None
    
    @staticmethod
    def is_date(date_str: str, format: str = '%Y-%m-%d') -> bool:
        """
        验证日期格式
        
        Args:
            date_str (str): 日期字符串
            format (str): 日期格式，默认为'%Y-%m-%d'
            
        Returns:
            bool: 如果格式正确返回True，否则返回False
        """
        try:
            from datetime import datetime
            datetime.strptime(date_str, format)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def is_number(value: Union[str, int, float]) -> bool:
        """
        验证是否为数字
        
        Args:
            value: 要验证的值
            
        Returns:
            bool: 如果是数字返回True，否则返回False
        """
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def is_integer(value: Union[str, int, float]) -> bool:
        """
        验证是否为整数
        
        Args:
            value: 要验证的值
            
        Returns:
            bool: 如果是整数返回True，否则返回False
        """
        try:
            int(value)
            return True
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def is_positive(value: Union[str, int, float]) -> bool:
        """
        验证是否为正数
        
        Args:
            value: 要验证的值
            
        Returns:
            bool: 如果是正数返回True，否则返回False
        """
        try:
            return float(value) > 0
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def is_negative(value: Union[str, int, float]) -> bool:
        """
        验证是否为负数
        
        Args:
            value: 要验证的值
            
        Returns:
            bool: 如果是负数返回True，否则返回False
        """
        try:
            return float(value) < 0
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def is_empty(value: Any) -> bool:
        """
        验证是否为空
        
        Args:
            value: 要验证的值
            
        Returns:
            bool: 如果为空返回True，否则返回False
        """
        if value is None:
            return True
        if isinstance(value, str):
            return len(value.strip()) == 0
        if isinstance(value, (list, tuple, dict, set)):
            return len(value) == 0
        return False
    
    @staticmethod
    def is_length_between(value: str, min_length: int, max_length: int) -> bool:
        """
        验证字符串长度是否在指定范围内
        
        Args:
            value (str): 要验证的字符串
            min_length (int): 最小长度
            max_length (int): 最大长度
            
        Returns:
            bool: 如果长度在范围内返回True，否则返回False
        """
        if not isinstance(value, str):
            return False
        return min_length <= len(value) <= max_length
