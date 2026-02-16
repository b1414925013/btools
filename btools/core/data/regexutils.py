"""正则工具类"""
import re
from typing import Any, List, Optional, Dict, Union, Match


class RegexUtils:
    """正则工具类"""

    @staticmethod
    def is_match(pattern: str, text: str, flags: int = 0) -> bool:
        """
        检查文本是否匹配正则表达式
        
        Args:
            pattern: 正则表达式模式
            text: 要检查的文本
            flags: 正则表达式标志
            
        Returns:
            bool: 如果匹配则返回True，否则返回False
        """
        return bool(re.match(pattern, text, flags))

    @staticmethod
    def is_full_match(pattern: str, text: str, flags: int = 0) -> bool:
        """
        检查文本是否完全匹配正则表达式
        
        Args:
            pattern: 正则表达式模式
            text: 要检查的文本
            flags: 正则表达式标志
            
        Returns:
            bool: 如果完全匹配则返回True，否则返回False
        """
        return bool(re.fullmatch(pattern, text, flags))

    @staticmethod
    def search(pattern: str, text: str, flags: int = 0) -> Optional[str]:
        """
        在文本中搜索正则表达式匹配
        
        Args:
            pattern: 正则表达式模式
            text: 要搜索的文本
            flags: 正则表达式标志
            
        Returns:
            Optional[str]: 匹配的字符串，如果没有匹配则返回None
        """
        match = re.search(pattern, text, flags)
        return match.group() if match else None

    @staticmethod
    def find_all(pattern: str, text: str, flags: int = 0) -> List[str]:
        """
        查找文本中所有匹配的子串
        
        Args:
            pattern: 正则表达式模式
            text: 要搜索的文本
            flags: 正则表达式标志
            
        Returns:
            List[str]: 匹配的子串列表
        """
        return re.findall(pattern, text, flags)

    @staticmethod
    def find_iter(pattern: str, text: str, flags: int = 0) -> List[Match[str]]:
        """
        查找文本中所有匹配的对象
        
        Args:
            pattern: 正则表达式模式
            text: 要搜索的文本
            flags: 正则表达式标志
            
        Returns:
            List[Match[str]]: 匹配对象列表
        """
        return list(re.finditer(pattern, text, flags))

    @staticmethod
    def split(pattern: str, text: str, maxsplit: int = 0, flags: int = 0) -> List[str]:
        """
        用正则表达式分割文本
        
        Args:
            pattern: 正则表达式模式
            text: 要分割的文本
            maxsplit: 最大分割次数
            flags: 正则表达式标志
            
        Returns:
            List[str]: 分割后的字符串列表
        """
        return re.split(pattern, text, maxsplit, flags)

    @staticmethod
    def sub(pattern: str, repl: Union[str, callable], text: str, count: int = 0, flags: int = 0) -> str:
        """
        替换文本中匹配的子串
        
        Args:
            pattern: 正则表达式模式
            repl: 替换字符串或替换函数
            text: 要处理的文本
            count: 最大替换次数
            flags: 正则表达式标志
            
        Returns:
            str: 替换后的文本
        """
        return re.sub(pattern, repl, text, count, flags)

    @staticmethod
    def subn(pattern: str, repl: Union[str, callable], text: str, count: int = 0, flags: int = 0) -> tuple:
        """
        替换文本中匹配的子串并返回替换次数
        
        Args:
            pattern: 正则表达式模式
            repl: 替换字符串或替换函数
            text: 要处理的文本
            count: 最大替换次数
            flags: 正则表达式标志
            
        Returns:
            tuple: (替换后的文本, 替换次数)
        """
        return re.subn(pattern, repl, text, count, flags)

    @staticmethod
    def escape(text: str) -> str:
        """
        转义文本中的特殊字符
        
        Args:
            text: 要转义的文本
            
        Returns:
            str: 转义后的文本
        """
        return re.escape(text)

    @staticmethod
    def compile(pattern: str, flags: int = 0) -> re.Pattern:
        """
        编译正则表达式模式
        
        Args:
            pattern: 正则表达式模式
            flags: 正则表达式标志
            
        Returns:
            re.Pattern: 编译后的正则表达式对象
        """
        return re.compile(pattern, flags)

    @staticmethod
    def get_groups(match: Match[str]) -> List[str]:
        """
        获取匹配对象的所有分组
        
        Args:
            match: 匹配对象
            
        Returns:
            List[str]: 分组列表
        """
        return list(match.groups())

    @staticmethod
    def get_group_dict(match: Match[str]) -> Dict[str, str]:
        """
        获取匹配对象的命名分组
        
        Args:
            match: 匹配对象
            
        Returns:
            Dict[str, str]: 命名分组字典
        """
        return match.groupdict()

    @staticmethod
    def extract(pattern: str, text: str, flags: int = 0) -> Optional[str]:
        """
        从文本中提取第一个匹配的子串
        
        Args:
            pattern: 正则表达式模式
            text: 要提取的文本
            flags: 正则表达式标志
            
        Returns:
            Optional[str]: 提取的子串，如果没有匹配则返回None
        """
        match = re.search(pattern, text, flags)
        if match:
            return match.group()
        return None

    @staticmethod
    def extract_groups(pattern: str, text: str, flags: int = 0) -> Optional[List[str]]:
        """
        从文本中提取第一个匹配的分组
        
        Args:
            pattern: 正则表达式模式
            text: 要提取的文本
            flags: 正则表达式标志
            
        Returns:
            Optional[List[str]]: 提取的分组列表，如果没有匹配则返回None
        """
        match = re.search(pattern, text, flags)
        if match:
            return list(match.groups())
        return None

    @staticmethod
    def extract_group_dict(pattern: str, text: str, flags: int = 0) -> Optional[Dict[str, str]]:
        """
        从文本中提取第一个匹配的命名分组
        
        Args:
            pattern: 正则表达式模式
            text: 要提取的文本
            flags: 正则表达式标志
            
        Returns:
            Optional[Dict[str, str]]: 提取的命名分组字典，如果没有匹配则返回None
        """
        match = re.search(pattern, text, flags)
        if match:
            return match.groupdict()
        return None

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        验证邮箱地址
        
        Args:
            email: 邮箱地址
            
        Returns:
            bool: 如果是有效的邮箱地址则返回True，否则返回False
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return RegexUtils.is_full_match(pattern, email)

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """
        验证手机号码
        
        Args:
            phone: 手机号码
            
        Returns:
            bool: 如果是有效的手机号码则返回True，否则返回False
        """
        pattern = r'^1[3-9]\d{9}$'
        return RegexUtils.is_full_match(pattern, phone)

    @staticmethod
    def validate_url(url: str) -> bool:
        """
        验证URL
        
        Args:
            url: URL
            
        Returns:
            bool: 如果是有效的URL则返回True，否则返回False
        """
        pattern = r'^https?://[\w\-]+(\.[\w\-]+)+([\w\-.,@?^=%&:/~+#]*[\w\-@?^=%&/~+#])?$'
        return RegexUtils.is_full_match(pattern, url)

    @staticmethod
    def validate_ipv4(ip: str) -> bool:
        """
        验证IPv4地址
        
        Args:
            ip: IPv4地址
            
        Returns:
            bool: 如果是有效的IPv4地址则返回True，否则返回False
        """
        pattern = r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$'
        return RegexUtils.is_full_match(pattern, ip)

    @staticmethod
    def validate_ipv6(ip: str) -> bool:
        """
        验证IPv6地址
        
        Args:
            ip: IPv6地址
            
        Returns:
            bool: 如果是有效的IPv6地址则返回True，否则返回False
        """
        pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        return RegexUtils.is_full_match(pattern, ip)

    @staticmethod
    def validate_id_card(id_card: str) -> bool:
        """
        验证身份证号码
        
        Args:
            id_card: 身份证号码
            
        Returns:
            bool: 如果是有效的身份证号码则返回True，否则返回False
        """
        pattern = r'^[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dXx]$'
        return RegexUtils.is_full_match(pattern, id_card)

    @staticmethod
    def validate_date(date: str) -> bool:
        """
        验证日期格式 (YYYY-MM-DD)
        
        Args:
            date: 日期字符串
            
        Returns:
            bool: 如果是有效的日期格式则返回True，否则返回False
        """
        pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
        return RegexUtils.is_full_match(pattern, date)

    @staticmethod
    def validate_time(time: str) -> bool:
        """
        验证时间格式 (HH:MM:SS)
        
        Args:
            time: 时间字符串
            
        Returns:
            bool: 如果是有效的时间格式则返回True，否则返回False
        """
        pattern = r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$'
        return RegexUtils.is_full_match(pattern, time)

    @staticmethod
    def validate_datetime(datetime: str) -> bool:
        """
        验证日期时间格式 (YYYY-MM-DD HH:MM:SS)
        
        Args:
            datetime: 日期时间字符串
            
        Returns:
            bool: 如果是有效的日期时间格式则返回True，否则返回False
        """
        pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]) ([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$'
        return RegexUtils.is_full_match(pattern, datetime)

    @staticmethod
    def validate_number(number: str) -> bool:
        """
        验证数字（整数或小数）
        
        Args:
            number: 数字字符串
            
        Returns:
            bool: 如果是有效的数字则返回True，否则返回False
        """
        pattern = r'^-?\d+(\.\d+)?$'
        return RegexUtils.is_full_match(pattern, number)

    @staticmethod
    def validate_integer(integer: str) -> bool:
        """
        验证整数
        
        Args:
            integer: 整数字符串
            
        Returns:
            bool: 如果是有效的整数则返回True，否则返回False
        """
        pattern = r'^-?\d+$'
        return RegexUtils.is_full_match(pattern, integer)

    @staticmethod
    def validate_decimal(decimal: str) -> bool:
        """
        验证小数
        
        Args:
            decimal: 小数字符串
            
        Returns:
            bool: 如果是有效的小数则返回True，否则返回False
        """
        pattern = r'^-?\d+\.\d+$'
        return RegexUtils.is_full_match(pattern, decimal)

    @staticmethod
    def validate_hex(hex_str: str) -> bool:
        """
        验证十六进制字符串
        
        Args:
            hex_str: 十六进制字符串
            
        Returns:
            bool: 如果是有效的十六进制字符串则返回True，否则返回False
        """
        pattern = r'^[0-9a-fA-F]+$'
        return RegexUtils.is_full_match(pattern, hex_str)

    @staticmethod
    def validate_alphanumeric(text: str) -> bool:
        """
        验证字母数字字符串
        
        Args:
            text: 字符串
            
        Returns:
            bool: 如果只包含字母和数字则返回True，否则返回False
        """
        pattern = r'^[a-zA-Z0-9]+$'
        return RegexUtils.is_full_match(pattern, text)

    @staticmethod
    def validate_alphabetic(text: str) -> bool:
        """
        验证字母字符串
        
        Args:
            text: 字符串
            
        Returns:
            bool: 如果只包含字母则返回True，否则返回False
        """
        pattern = r'^[a-zA-Z]+$'
        return RegexUtils.is_full_match(pattern, text)

    @staticmethod
    def validate_numeric(text: str) -> bool:
        """
        验证数字字符串
        
        Args:
            text: 字符串
            
        Returns:
            bool: 如果只包含数字则返回True，否则返回False
        """
        pattern = r'^\d+$'
        return RegexUtils.is_full_match(pattern, text)