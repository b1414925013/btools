"""字符串工具类"""
import re
import string
from typing import Any, List, Optional, Union, Dict


class StringUtils:
    """字符串工具类"""

    @staticmethod
    def is_empty(s: Any) -> bool:
        """
        判断字符串是否为空
        
        Args:
            s: 要判断的值
            
        Returns:
            bool: 如果为空则返回True，否则返回False
        """
        return s is None or (isinstance(s, str) and len(s.strip()) == 0)

    @staticmethod
    def is_not_empty(s: Any) -> bool:
        """
        判断字符串是否不为空
        
        Args:
            s: 要判断的值
            
        Returns:
            bool: 如果不为空则返回True，否则返回False
        """
        return not StringUtils.is_empty(s)

    @staticmethod
    def trim(s: str) -> str:
        """
        去除字符串两端的空白字符
        
        Args:
            s: 要处理的字符串
            
        Returns:
            str: 去除空白字符后的字符串
        """
        return s.strip() if s else s

    @staticmethod
    def trim_start(s: str) -> str:
        """
        去除字符串开头的空白字符
        
        Args:
            s: 要处理的字符串
            
        Returns:
            str: 去除开头空白字符后的字符串
        """
        return s.lstrip() if s else s

    @staticmethod
    def trim_end(s: str) -> str:
        """
        去除字符串结尾的空白字符
        
        Args:
            s: 要处理的字符串
            
        Returns:
            str: 去除结尾空白字符后的字符串
        """
        return s.rstrip() if s else s

    @staticmethod
    def split(s: str, separator: Optional[str] = ",", maxsplit: int = -1) -> List[str]:
        """
        分割字符串
        
        Args:
            s: 要分割的字符串
            separator: 分隔符，默认为逗号
            maxsplit: 最大分割次数
            
        Returns:
            List[str]: 分割后的字符串列表
        """
        if not s:
            return []
        return s.split(separator, maxsplit)

    @staticmethod
    def join(strings: List[str], separator: str = "") -> str:
        """
        连接字符串列表
        
        Args:
            strings: 字符串列表
            separator: 连接符
            
        Returns:
            str: 连接后的字符串
        """
        return separator.join(strings)

    @staticmethod
    def replace(s: str, old: str, new: str, count: int = -1) -> str:
        """
        替换字符串
        
        Args:
            s: 要处理的字符串
            old: 要替换的子串
            new: 替换后的子串
            count: 替换次数，-1表示全部替换
            
        Returns:
            str: 替换后的字符串
        """
        return s.replace(old, new, count) if s else s

    @staticmethod
    def substring(s: str, start: int, end: Optional[int] = None) -> str:
        """
        截取字符串
        
        Args:
            s: 要处理的字符串
            start: 起始位置
            end: 结束位置
            
        Returns:
            str: 截取后的字符串
        """
        return s[start:end] if s else s

    @staticmethod
    def starts_with(s: str, prefix: str, start: int = 0, end: Optional[int] = None) -> bool:
        """
        判断字符串是否以指定前缀开头
        
        Args:
            s: 要判断的字符串
            prefix: 前缀
            start: 起始位置
            end: 结束位置
            
        Returns:
            bool: 如果以指定前缀开头则返回True，否则返回False
        """
        return s.startswith(prefix, start, end) if s else False

    @staticmethod
    def ends_with(s: str, suffix: str, start: int = 0, end: Optional[int] = None) -> bool:
        """
        判断字符串是否以指定后缀结尾
        
        Args:
            s: 要判断的字符串
            suffix: 后缀
            start: 起始位置
            end: 结束位置
            
        Returns:
            bool: 如果以指定后缀结尾则返回True，否则返回False
        """
        return s.endswith(suffix, start, end) if s else False

    @staticmethod
    def contains(s: str, substr: str, start: int = 0, end: Optional[int] = None) -> bool:
        """
        判断字符串是否包含指定子串
        
        Args:
            s: 要判断的字符串
            substr: 子串
            start: 起始位置
            end: 结束位置
            
        Returns:
            bool: 如果包含指定子串则返回True，否则返回False
        """
        if not s:
            return False
        return substr in s[start:end]

    @staticmethod
    def index_of(s: str, substr: str, start: int = 0, end: Optional[int] = None) -> int:
        """
        查找子串在字符串中第一次出现的位置
        
        Args:
            s: 要查找的字符串
            substr: 子串
            start: 起始位置
            end: 结束位置
            
        Returns:
            int: 子串在字符串中第一次出现的位置，如果没有找到则返回-1
        """
        if not s:
            return -1
        return s.find(substr, start, end)

    @staticmethod
    def last_index_of(s: str, substr: str, start: int = 0, end: Optional[int] = None) -> int:
        """
        查找子串在字符串中最后一次出现的位置
        
        Args:
            s: 要查找的字符串
            substr: 子串
            start: 起始位置
            end: 结束位置
            
        Returns:
            int: 子串在字符串中最后一次出现的位置，如果没有找到则返回-1
        """
        if not s:
            return -1
        return s.rfind(substr, start, end)

    @staticmethod
    def length(s: str) -> int:
        """
        获取字符串长度
        
        Args:
            s: 要处理的字符串
            
        Returns:
            int: 字符串长度
        """
        return len(s) if s else 0

    @staticmethod
    def to_upper(s: str) -> str:
        """
        将字符串转换为大写
        
        Args:
            s: 要处理的字符串
            
        Returns:
            str: 转换后的大写字符串
        """
        return s.upper() if s else s

    @staticmethod
    def to_lower(s: str) -> str:
        """
        将字符串转换为小写
        
        Args:
            s: 要处理的字符串
            
        Returns:
            str: 转换后的小写字符串
        """
        return s.lower() if s else s

    @staticmethod
    def capitalize(s: str) -> str:
        """
        将字符串首字母大写
        
        Args:
            s: 要处理的字符串
            
        Returns:
            str: 首字母大写后的字符串
        """
        return s.capitalize() if s else s

    @staticmethod
    def title(s: str) -> str:
        """
        将字符串每个单词的首字母大写
        
        Args:
            s: 要处理的字符串
            
        Returns:
            str: 每个单词首字母大写后的字符串
        """
        return s.title() if s else s

    @staticmethod
    def pad_left(s: str, width: int, fillchar: str = ' ') -> str:
        """
        在字符串左侧填充指定字符
        
        Args:
            s: 要处理的字符串
            width: 填充后的宽度
            fillchar: 填充字符
            
        Returns:
            str: 左侧填充后的字符串
        """
        return s.rjust(width, fillchar) if s else fillchar * width

    @staticmethod
    def pad_right(s: str, width: int, fillchar: str = ' ') -> str:
        """
        在字符串右侧填充指定字符
        
        Args:
            s: 要处理的字符串
            width: 填充后的宽度
            fillchar: 填充字符
            
        Returns:
            str: 右侧填充后的字符串
        """
        return s.ljust(width, fillchar) if s else fillchar * width

    @staticmethod
    def pad_center(s: str, width: int, fillchar: str = ' ') -> str:
        """
        在字符串两侧填充指定字符
        
        Args:
            s: 要处理的字符串
            width: 填充后的宽度
            fillchar: 填充字符
            
        Returns:
            str: 两侧填充后的字符串
        """
        return s.center(width, fillchar) if s else fillchar * width

    @staticmethod
    def remove_whitespace(s: str) -> str:
        """
        移除字符串中的所有空白字符
        
        Args:
            s: 要处理的字符串
            
        Returns:
            str: 移除空白字符后的字符串
        """
        return ''.join(s.split()) if s else s

    @staticmethod
    def replace_whitespace(s: str, replacement: str = ' ') -> str:
        """
        替换字符串中的所有空白字符
        
        Args:
            s: 要处理的字符串
            replacement: 替换字符
            
        Returns:
            str: 替换空白字符后的字符串
        """
        return re.sub(r'\s+', replacement, s) if s else s

    @staticmethod
    def is_alpha(s: str) -> bool:
        """
        判断字符串是否只包含字母
        
        Args:
            s: 要判断的字符串
            
        Returns:
            bool: 如果只包含字母则返回True，否则返回False
        """
        return s.isalpha() if s else False

    @staticmethod
    def is_digit(s: str) -> bool:
        """
        判断字符串是否只包含数字
        
        Args:
            s: 要判断的字符串
            
        Returns:
            bool: 如果只包含数字则返回True，否则返回False
        """
        return s.isdigit() if s else False

    @staticmethod
    def is_alphanumeric(s: str) -> bool:
        """
        判断字符串是否只包含字母和数字
        
        Args:
            s: 要判断的字符串
            
        Returns:
            bool: 如果只包含字母和数字则返回True，否则返回False
        """
        return s.isalnum() if s else False

    @staticmethod
    def is_numeric(s: str) -> bool:
        """
        判断字符串是否只包含数字字符
        
        Args:
            s: 要判断的字符串
            
        Returns:
            bool: 如果只包含数字字符则返回True，否则返回False
        """
        return s.isnumeric() if s else False

    @staticmethod
    def is_blank(s: str) -> bool:
        """
        判断字符串是否为空白
        
        Args:
            s: 要判断的字符串
            
        Returns:
            bool: 如果为空白则返回True，否则返回False
        """
        return StringUtils.is_empty(s)

    @staticmethod
    def is_not_blank(s: str) -> bool:
        """
        判断字符串是否不为空白
        
        Args:
            s: 要判断的字符串
            
        Returns:
            bool: 如果不为空白则返回True，否则返回False
        """
        return StringUtils.is_not_empty(s)

    @staticmethod
    def repeat(s: str, times: int) -> str:
        """
        重复字符串
        
        Args:
            s: 要重复的字符串
            times: 重复次数
            
        Returns:
            str: 重复后的字符串
        """
        return s * times if s else ''

    @staticmethod
    def reverse(s: str) -> str:
        """
        反转字符串
        
        Args:
            s: 要反转的字符串
            
        Returns:
            str: 反转后的字符串
        """
        return s[::-1] if s else s

    @staticmethod
    def format_template(template: str, data: Optional[Dict] = None, **kwargs) -> str:
        """
        格式化模板字符串
        
        支持两种调用方式：
        1. format_template(template, data)
        2. format_template(template, **kwargs)
        
        Args:
            template: 模板字符串
            data: 模板参数字典
            **kwargs: 模板参数
            
        Returns:
            str: 格式化后的字符串
        """
        if not template:
            return ''
        
        # 如果提供了data参数，则使用data
        if data is not None:
            return template.format(**data)
        
        # 否则使用kwargs
        return template.format(**kwargs)

    @staticmethod
    def generate_random_string(length: int, chars: str = string.ascii_letters + string.digits) -> str:
        """
        生成随机字符串
        
        Args:
            length: 字符串长度
            chars: 字符集
            
        Returns:
            str: 随机字符串
        """
        import random
        return ''.join(random.choice(chars) for _ in range(length))
