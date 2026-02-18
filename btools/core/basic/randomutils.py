#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
随机工具类

提供随机数生成功能，包括随机整数、浮点数、字符串、列表元素等
"""
import random
import string
from typing import Any, List, Optional, Sequence, Tuple, Union


class RandomUtil:
    """
    随机工具类
    """

    @staticmethod
    def randomInt(min_val: int = 0, max_val: int = 999999999) -> int:
        """
        生成随机整数

        Args:
            min_val: 最小值（包含）
            max_val: 最大值（包含）

        Returns:
            int: 随机整数
        """
        return random.randint(min_val, max_val)

    @staticmethod
    def randomFloat(min_val: float = 0.0, max_val: float = 1.0) -> float:
        """
        生成随机浮点数

        Args:
            min_val: 最小值（包含）
            max_val: 最大值（不包含）

        Returns:
            float: 随机浮点数
        """
        return random.uniform(min_val, max_val)

    @staticmethod
    def randomBool() -> bool:
        """
        生成随机布尔值

        Returns:
            bool: 随机布尔值
        """
        return random.choice([True, False])

    @staticmethod
    def randomStr(length: int = 8, charset: str = string.ascii_letters + string.digits) -> str:
        """
        生成随机字符串

        Args:
            length: 字符串长度
            charset: 字符集，默认为大小写字母和数字

        Returns:
            str: 随机字符串
        """
        return ''.join(random.choices(charset, k=length))

    @staticmethod
    def randomLowerStr(length: int = 8) -> str:
        """
        生成随机小写字符串

        Args:
            length: 字符串长度

        Returns:
            str: 随机小写字符串
        """
        return RandomUtil.randomStr(length, string.ascii_lowercase)

    @staticmethod
    def randomUpperStr(length: int = 8) -> str:
        """
        生成随机大写字符串

        Args:
            length: 字符串长度

        Returns:
            str: 随机大写字符串
        """
        return RandomUtil.randomStr(length, string.ascii_uppercase)

    @staticmethod
    def randomNumberStr(length: int = 8) -> str:
        """
        生成随机数字字符串

        Args:
            length: 字符串长度

        Returns:
            str: 随机数字字符串
        """
        return RandomUtil.randomStr(length, string.digits)

    @staticmethod
    def randomHexStr(length: int = 8) -> str:
        """
        生成随机十六进制字符串

        Args:
            length: 字符串长度

        Returns:
            str: 随机十六进制字符串
        """
        return RandomUtil.randomStr(length, string.hexdigits)

    @staticmethod
    def randomChar(charset: str = string.ascii_letters + string.digits) -> str:
        """
        生成随机字符

        Args:
            charset: 字符集，默认为大小写字母和数字

        Returns:
            str: 随机字符
        """
        return random.choice(charset)

    @staticmethod
    def randomChoice(sequence: Sequence[Any]) -> Any:
        """
        从序列中随机选择一个元素

        Args:
            sequence: 序列

        Returns:
            Any: 随机选择的元素
        """
        return random.choice(sequence)

    @staticmethod
    def randomChoices(sequence: Sequence[Any], k: int = 1, weights: Optional[Sequence[float]] = None) -> List[Any]:
        """
        从序列中随机选择多个元素（可重复）

        Args:
            sequence: 序列
            k: 选择数量
            weights: 权重序列

        Returns:
            List[Any]: 随机选择的元素列表
        """
        return random.choices(sequence, weights=weights, k=k)

    @staticmethod
    def randomSample(sequence: Sequence[Any], k: int) -> List[Any]:
        """
        从序列中随机选择多个元素（不可重复）

        Args:
            sequence: 序列
            k: 选择数量

        Returns:
            List[Any]: 随机选择的元素列表
        """
        return random.sample(sequence, k)

    @staticmethod
    def shuffle(sequence: List[Any]) -> None:
        """
        打乱序列

        Args:
            sequence: 序列（会被原地修改）
        """
        random.shuffle(sequence)

    @staticmethod
    def randomBytes(length: int = 8) -> bytes:
        """
        生成随机字节串

        Args:
            length: 字节串长度

        Returns:
            bytes: 随机字节串
        """
        return bytes(random.getrandbits(8) for _ in range(length))

    @staticmethod
    def randomUUID() -> str:
        """
        生成随机UUID

        Returns:
            str: 随机UUID
        """
        import uuid
        return str(uuid.uuid4())

    @staticmethod
    def randomColor(alpha: bool = False) -> str:
        """
        生成随机颜色（十六进制）

        Args:
            alpha: 是否包含透明度

        Returns:
            str: 随机颜色
        """
        r = RandomUtil.randomInt(0, 255)
        g = RandomUtil.randomInt(0, 255)
        b = RandomUtil.randomInt(0, 255)
        
        if alpha:
            a = RandomUtil.randomInt(0, 255)
            return f'#{r:02x}{g:02x}{b:02x}{a:02x}'
        else:
            return f'#{r:02x}{g:02x}{b:02x}'

    @staticmethod
    def randomEmail(domain: str = "example.com") -> str:
        """
        生成随机邮箱地址

        Args:
            domain: 域名

        Returns:
            str: 随机邮箱地址
        """
        username = RandomUtil.randomStr(10, string.ascii_lowercase + string.digits)
        return f"{username}@{domain}"

    @staticmethod
    def randomPhone(prefix: str = "138") -> str:
        """
        生成随机手机号

        Args:
            prefix: 手机号前缀

        Returns:
            str: 随机手机号
        """
        suffix = RandomUtil.randomNumberStr(8)
        return f"{prefix}{suffix}"

    @staticmethod
    def randomPassword(length: int = 12) -> str:
        """
        生成随机密码（包含大小写字母、数字和特殊字符）

        Args:
            length: 密码长度

        Returns:
            str: 随机密码
        """
        # 确保包含至少一个大写字母、一个小写字母、一个数字和一个特殊字符
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        digits = string.digits
        special = string.punctuation
        
        # 至少各取一个
        password = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(digits),
            random.choice(special)
        ]
        
        # 填充剩余长度
        if length > 4:
            all_chars = uppercase + lowercase + digits + special
            password.extend(random.choices(all_chars, k=length-4))
        
        # 打乱顺序
        random.shuffle(password)
        
        return ''.join(password)

    @staticmethod
    def randomDate(start_year: int = 1970, end_year: int = 2030) -> Tuple[int, int, int]:
        """
        生成随机日期

        Args:
            start_year: 开始年份
            end_year: 结束年份

        Returns:
            Tuple[int, int, int]: (年, 月, 日)
        """
        import calendar
        
        year = RandomUtil.randomInt(start_year, end_year)
        month = RandomUtil.randomInt(1, 12)
        
        # 获取当月天数
        _, last_day = calendar.monthrange(year, month)
        day = RandomUtil.randomInt(1, last_day)
        
        return year, month, day

    @staticmethod
    def randomTime() -> Tuple[int, int, int]:
        """
        生成随机时间

        Returns:
            Tuple[int, int, int]: (时, 分, 秒)
        """
        hour = RandomUtil.randomInt(0, 23)
        minute = RandomUtil.randomInt(0, 59)
        second = RandomUtil.randomInt(0, 59)
        
        return hour, minute, second

    @staticmethod
    def setSeed(seed: int) -> None:
        """
        设置随机种子

        Args:
            seed: 随机种子
        """
        random.seed(seed)

    @staticmethod
    def getRandom() -> random.Random:
        """
        获取随机数生成器实例

        Returns:
            random.Random: 随机数生成器实例
        """
        return random

    @staticmethod
    def randomGaussian(mu: float = 0.0, sigma: float = 1.0) -> float:
        """
        生成高斯分布的随机数

        Args:
            mu: 均值
            sigma: 标准差

        Returns:
            float: 高斯分布的随机数
        """
        return random.gauss(mu, sigma)

    @staticmethod
    def randomTriangular(low: float = 0.0, high: float = 1.0, mode: Optional[float] = None) -> float:
        """
        生成三角形分布的随机数

        Args:
            low: 最小值
            high: 最大值
            mode: 众数

        Returns:
            float: 三角形分布的随机数
        """
        return random.triangular(low, high, mode)

    @staticmethod
    def randomExpovariate(lambd: float = 1.0) -> float:
        """
        生成指数分布的随机数

        Args:
            lambd: 速率参数

        Returns:
            float: 指数分布的随机数
        """
        return random.expovariate(lambd)