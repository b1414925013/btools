"""数学工具类"""
import math
import random
from typing import Any, List, Optional, Tuple, Union


class MathUtils:
    """数学工具类"""

    # 常量
    PI = math.pi
    E = math.e
    INF = float('inf')
    NAN = float('nan')

    @staticmethod
    def abs(x: Union[int, float]) -> Union[int, float]:
        """
        获取绝对值
        
        Args:
            x: 数值
            
        Returns:
            Union[int, float]: 绝对值
        """
        return abs(x)

    @staticmethod
    def sqrt(x: Union[int, float]) -> float:
        """
        计算平方根
        
        Args:
            x: 数值
            
        Returns:
            float: 平方根
        """
        return math.sqrt(x)

    @staticmethod
    def pow(x: Union[int, float], y: Union[int, float]) -> float:
        """
        计算幂
        
        Args:
            x: 底数
            y: 指数
            
        Returns:
            float: 幂结果
        """
        return math.pow(x, y)

    @staticmethod
    def exp(x: Union[int, float]) -> float:
        """
        计算自然指数
        
        Args:
            x: 数值
            
        Returns:
            float: 自然指数结果
        """
        return math.exp(x)

    @staticmethod
    def log(x: Union[int, float], base: Optional[Union[int, float]] = None) -> float:
        """
        计算对数
        
        Args:
            x: 数值
            base: 底数，默认为自然对数
            
        Returns:
            float: 对数结果
        """
        if base is None:
            return math.log(x)
        return math.log(x, base)

    @staticmethod
    def log10(x: Union[int, float]) -> float:
        """
        计算以10为底的对数
        
        Args:
            x: 数值
            
        Returns:
            float: 以10为底的对数结果
        """
        return math.log10(x)

    @staticmethod
    def sin(x: Union[int, float]) -> float:
        """
        计算正弦值
        
        Args:
            x: 角度（弧度）
            
        Returns:
            float: 正弦值
        """
        return math.sin(x)

    @staticmethod
    def cos(x: Union[int, float]) -> float:
        """
        计算余弦值
        
        Args:
            x: 角度（弧度）
            
        Returns:
            float: 余弦值
        """
        return math.cos(x)

    @staticmethod
    def tan(x: Union[int, float]) -> float:
        """
        计算正切值
        
        Args:
            x: 角度（弧度）
            
        Returns:
            float: 正切值
        """
        return math.tan(x)

    @staticmethod
    def asin(x: Union[int, float]) -> float:
        """
        计算反正弦值
        
        Args:
            x: 数值
            
        Returns:
            float: 反正弦值（弧度）
        """
        return math.asin(x)

    @staticmethod
    def acos(x: Union[int, float]) -> float:
        """
        计算反余弦值
        
        Args:
            x: 数值
            
        Returns:
            float: 反余弦值（弧度）
        """
        return math.acos(x)

    @staticmethod
    def atan(x: Union[int, float]) -> float:
        """
        计算反正切值
        
        Args:
            x: 数值
            
        Returns:
            float: 反正切值（弧度）
        """
        return math.atan(x)

    @staticmethod
    def atan2(y: Union[int, float], x: Union[int, float]) -> float:
        """
        计算坐标的反正切值
        
        Args:
            y: y坐标
            x: x坐标
            
        Returns:
            float: 反正切值（弧度）
        """
        return math.atan2(y, x)

    @staticmethod
    def radians(degrees: Union[int, float]) -> float:
        """
        角度转弧度
        
        Args:
            degrees: 角度
            
        Returns:
            float: 弧度
        """
        return math.radians(degrees)

    @staticmethod
    def degrees(radians: Union[int, float]) -> float:
        """
        弧度转角度
        
        Args:
            radians: 弧度
            
        Returns:
            float: 角度
        """
        return math.degrees(radians)

    @staticmethod
    def ceil(x: Union[int, float]) -> int:
        """
        向上取整
        
        Args:
            x: 数值
            
        Returns:
            int: 向上取整结果
        """
        return math.ceil(x)

    @staticmethod
    def floor(x: Union[int, float]) -> int:
        """
        向下取整
        
        Args:
            x: 数值
            
        Returns:
            int: 向下取整结果
        """
        return math.floor(x)

    @staticmethod
    def round(x: Union[int, float], ndigits: Optional[int] = None) -> Union[int, float]:
        """
        四舍五入
        
        Args:
            x: 数值
            ndigits: 小数位数
            
        Returns:
            Union[int, float]: 四舍五入结果
        """
        return round(x, ndigits)

    @staticmethod
    def trunc(x: Union[int, float]) -> int:
        """
        截断小数部分
        
        Args:
            x: 数值
            
        Returns:
            int: 截断结果
        """
        return math.trunc(x)

    @staticmethod
    def sign(x: Union[int, float]) -> int:
        """
        获取符号
        
        Args:
            x: 数值
            
        Returns:
            int: 符号（-1, 0, 1）
        """
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

    @staticmethod
    def max(*args: Union[int, float]) -> Union[int, float]:
        """
        获取最大值
        
        Args:
            *args: 数值
            
        Returns:
            Union[int, float]: 最大值
        """
        return max(args)

    @staticmethod
    def min(*args: Union[int, float]) -> Union[int, float]:
        """
        获取最小值
        
        Args:
            *args: 数值
            
        Returns:
            Union[int, float]: 最小值
        """
        return min(args)

    @staticmethod
    def sum(*args: Union[int, float]) -> Union[int, float]:
        """
        计算和
        
        Args:
            *args: 数值
            
        Returns:
            Union[int, float]: 和
        """
        return sum(args)

    @staticmethod
    def average(*args: Union[int, float]) -> float:
        """
        计算平均值
        
        Args:
            *args: 数值
            
        Returns:
            float: 平均值
        """
        if not args:
            return 0.0
        return sum(args) / len(args)

    @staticmethod
    def median(*args: Union[int, float]) -> float:
        """
        计算中位数
        
        Args:
            *args: 数值
            
        Returns:
            float: 中位数
        """
        if not args:
            return 0.0
        sorted_args = sorted(args)
        n = len(sorted_args)
        if n % 2 == 0:
            return (sorted_args[n//2 - 1] + sorted_args[n//2]) / 2
        else:
            return sorted_args[n//2]

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """
        计算最大公约数
        
        Args:
            a: 整数
            b: 整数
            
        Returns:
            int: 最大公约数
        """
        return math.gcd(a, b)

    @staticmethod
    def lcm(a: int, b: int) -> int:
        """
        计算最小公倍数
        
        Args:
            a: 整数
            b: 整数
            
        Returns:
            int: 最小公倍数
        """
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // math.gcd(a, b)

    @staticmethod
    def is_integer(x: Union[int, float]) -> bool:
        """
        判断是否为整数
        
        Args:
            x: 数值
            
        Returns:
            bool: 如果是整数则返回True，否则返回False
        """
        return isinstance(x, int) or (isinstance(x, float) and x.is_integer())

    @staticmethod
    def is_even(x: int) -> bool:
        """
        判断是否为偶数
        
        Args:
            x: 整数
            
        Returns:
            bool: 如果是偶数则返回True，否则返回False
        """
        return x % 2 == 0

    @staticmethod
    def is_odd(x: int) -> bool:
        """
        判断是否为奇数
        
        Args:
            x: 整数
            
        Returns:
            bool: 如果是奇数则返回True，否则返回False
        """
        return x % 2 != 0

    @staticmethod
    def is_prime(x: int) -> bool:
        """
        判断是否为质数
        
        Args:
            x: 整数
            
        Returns:
            bool: 如果是质数则返回True，否则返回False
        """
        if x <= 1:
            return False
        if x <= 3:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False
        i = 5
        while i * i <= x:
            if x % i == 0 or x % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def generate_random_integer(min_value: int, max_value: int) -> int:
        """
        生成随机整数
        
        Args:
            min_value: 最小值
            max_value: 最大值
            
        Returns:
            int: 随机整数
        """
        return random.randint(min_value, max_value)

    @staticmethod
    def generate_random_float(min_value: float = 0.0, max_value: float = 1.0) -> float:
        """
        生成随机浮点数
        
        Args:
            min_value: 最小值
            max_value: 最大值
            
        Returns:
            float: 随机浮点数
        """
        return random.uniform(min_value, max_value)

    @staticmethod
    def generate_random_choice(sequence: List[Any]) -> Any:
        """
        从序列中随机选择一个元素
        
        Args:
            sequence: 序列
            
        Returns:
            Any: 随机选择的元素
        """
        return random.choice(sequence)

    @staticmethod
    def generate_random_sample(sequence: List[Any], k: int) -> List[Any]:
        """
        从序列中随机选择k个不重复元素
        
        Args:
            sequence: 序列
            k: 选择的元素数量
            
        Returns:
            List[Any]: 随机选择的元素列表
        """
        return random.sample(sequence, k)

    @staticmethod
    def shuffle(sequence: List[Any]) -> None:
        """
        打乱序列
        
        Args:
            sequence: 序列
        """
        random.shuffle(sequence)

    @staticmethod
    def set_random_seed(seed: int) -> None:
        """
        设置随机种子
        
        Args:
            seed: 种子值
        """
        random.seed(seed)

    @staticmethod
    def distance(x1: float, y1: float, x2: float, y2: float) -> float:
        """
        计算两点之间的距离
        
        Args:
            x1: 第一个点的x坐标
            y1: 第一个点的y坐标
            x2: 第二个点的x坐标
            y2: 第二个点的y坐标
            
        Returns:
            float: 距离
        """
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    @staticmethod
    def clamp(value: Union[int, float], min_value: Union[int, float], max_value: Union[int, float]) -> Union[int, float]:
        """
        限制值在指定范围内
        
        Args:
            value: 数值
            min_value: 最小值
            max_value: 最大值
            
        Returns:
            Union[int, float]: 限制后的值
        """
        return max(min(value, max_value), min_value)

    @staticmethod
    def lerp(start: Union[int, float], end: Union[int, float], t: float) -> Union[int, float]:
        """
        线性插值
        
        Args:
            start: 起始值
            end: 结束值
            t: 插值参数（0-1）
            
        Returns:
            Union[int, float]: 插值结果
        """
        return start + (end - start) * t

    @staticmethod
    def factorial(n: int) -> int:
        """
        计算阶乘
        
        Args:
            n: 整数
            
        Returns:
            int: 阶乘结果
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        return math.factorial(n)

    @staticmethod
    def combinations(n: int, k: int) -> int:
        """
        计算组合数
        
        Args:
            n: 总数
            k: 选择数
            
        Returns:
            int: 组合数
        """
        if k < 0 or k > n:
            return 0
        return math.comb(n, k)

    @staticmethod
    def permutations(n: int, k: int) -> int:
        """
        计算排列数
        
        Args:
            n: 总数
            k: 选择数
            
        Returns:
            int: 排列数
        """
        if k < 0 or k > n:
            return 0
        return math.perm(n, k)
