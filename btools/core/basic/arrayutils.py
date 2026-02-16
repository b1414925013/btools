"""数组工具类"""
from typing import Any, List, Optional, Tuple, Union, Callable
import numpy as np


class ArrayUtils:
    """数组工具类"""

    @staticmethod
    def is_empty(array: Any) -> bool:
        """
        判断数组是否为空
        
        Args:
            array: 要判断的数组
            
        Returns:
            bool: 如果为空则返回True，否则返回False
        """
        if array is None:
            return True
        if isinstance(array, (list, tuple, np.ndarray)):
            return len(array) == 0
        return True

    @staticmethod
    def is_not_empty(array: Any) -> bool:
        """
        判断数组是否不为空
        
        Args:
            array: 要判断的数组
            
        Returns:
            bool: 如果不为空则返回True，否则返回False
        """
        return not ArrayUtils.is_empty(array)

    @staticmethod
    def size(array: Any) -> int:
        """
        获取数组大小
        
        Args:
            array: 要获取大小的数组
            
        Returns:
            int: 数组大小
        """
        if array is None:
            return 0
        if isinstance(array, (list, tuple, np.ndarray)):
            return len(array)
        return 0

    @staticmethod
    def add(array: List, element: Any) -> None:
        """
        向数组添加元素
        
        Args:
            array: 要添加元素的数组
            element: 要添加的元素
        """
        if array is not None:
            array.append(element)

    @staticmethod
    def add_all(array: List, elements: Union[List, Tuple]) -> None:
        """
        向数组添加多个元素
        
        Args:
            array: 要添加元素的数组
            elements: 要添加的元素集合
        """
        if array is not None and elements is not None:
            array.extend(elements)

    @staticmethod
    def remove(array: List, element: Any) -> bool:
        """
        从数组中移除元素
        
        Args:
            array: 要移除元素的数组
            element: 要移除的元素
            
        Returns:
            bool: 如果移除成功则返回True，否则返回False
        """
        if array is not None:
            try:
                array.remove(element)
                return True
            except ValueError:
                return False
        return False

    @staticmethod
    def remove_at(array: List, index: int) -> Any:
        """
        从数组中移除指定位置的元素
        
        Args:
            array: 要移除元素的数组
            index: 要移除的元素位置
            
        Returns:
            Any: 被移除的元素，如果移除失败则返回None
        """
        if array is not None and 0 <= index < len(array):
            return array.pop(index)
        return None

    @staticmethod
    def get(array: Union[List, Tuple], index: int) -> Any:
        """
        获取数组指定位置的元素
        
        Args:
            array: 要获取元素的数组
            index: 元素位置
            
        Returns:
            Any: 数组元素，如果位置无效则返回None
        """
        if array is not None and 0 <= index < len(array):
            return array[index]
        return None

    @staticmethod
    def set(array: List, index: int, element: Any) -> bool:
        """
        设置数组指定位置的元素
        
        Args:
            array: 要设置元素的数组
            index: 元素位置
            element: 要设置的元素
            
        Returns:
            bool: 如果设置成功则返回True，否则返回False
        """
        if array is not None and 0 <= index < len(array):
            array[index] = element
            return True
        return False

    @staticmethod
    def index_of(array: Union[List, Tuple], element: Any) -> int:
        """
        查找元素在数组中第一次出现的位置
        
        Args:
            array: 要查找的数组
            element: 要查找的元素
            
        Returns:
            int: 元素在数组中第一次出现的位置，如果没有找到则返回-1
        """
        if array is not None:
            try:
                return array.index(element)
            except ValueError:
                return -1
        return -1

    @staticmethod
    def last_index_of(array: Union[List, Tuple], element: Any) -> int:
        """
        查找元素在数组中最后一次出现的位置
        
        Args:
            array: 要查找的数组
            element: 要查找的元素
            
        Returns:
            int: 元素在数组中最后一次出现的位置，如果没有找到则返回-1
        """
        if array is not None:
            try:
                return len(array) - 1 - array[::-1].index(element)
            except ValueError:
                return -1
        return -1

    @staticmethod
    def contains(array: Union[List, Tuple], element: Any) -> bool:
        """
        判断数组是否包含指定元素
        
        Args:
            array: 要判断的数组
            element: 要检查的元素
            
        Returns:
            bool: 如果包含指定元素则返回True，否则返回False
        """
        if array is not None:
            return element in array
        return False

    @staticmethod
    def sort(array: List, key: Optional[Callable[[Any], Any]] = None, reverse: bool = False) -> None:
        """
        排序数组
        
        Args:
            array: 要排序的数组
            key: 排序键函数
            reverse: 是否倒序
        """
        if array is not None:
            array.sort(key=key, reverse=reverse)

    @staticmethod
    def sorted(array: Union[List, Tuple], key: Optional[Callable[[Any], Any]] = None, reverse: bool = False) -> List:
        """
        排序数组并返回新数组
        
        Args:
            array: 要排序的数组
            key: 排序键函数
            reverse: 是否倒序
            
        Returns:
            List: 排序后的新数组
        """
        if array is None:
            return []
        sorted_array = list(array)
        sorted_array.sort(key=key, reverse=reverse)
        return sorted_array

    @staticmethod
    def reverse(array: List) -> None:
        """
        反转数组
        
        Args:
            array: 要反转的数组
        """
        if array is not None:
            array.reverse()

    @staticmethod
    def reversed(array: Union[List, Tuple]) -> List:
        """
        反转数组并返回新数组
        
        Args:
            array: 要反转的数组
            
        Returns:
            List: 反转后的新数组
        """
        if array is None:
            return []
        return list(reversed(array))

    @staticmethod
    def copy(array: Union[List, Tuple]) -> List:
        """
        复制数组
        
        Args:
            array: 要复制的数组
            
        Returns:
            List: 复制后的新数组
        """
        if array is None:
            return []
        return list(array)

    @staticmethod
    def sub_array(array: Union[List, Tuple], start: int, end: Optional[int] = None) -> List:
        """
        截取数组
        
        Args:
            array: 要截取的数组
            start: 起始位置
            end: 结束位置
            
        Returns:
            List: 截取后的新数组
        """
        if array is None:
            return []
        return list(array[start:end])

    @staticmethod
    def concat(*arrays: Union[List, Tuple]) -> List:
        """
        合并多个数组
        
        Args:
            *arrays: 要合并的数组
            
        Returns:
            List: 合并后的新数组
        """
        result = []
        for array in arrays:
            if array is not None:
                result.extend(array)
        return result

    @staticmethod
    def flatten(array: Union[List, Tuple]) -> List:
        """
        扁平化数组
        
        Args:
            array: 要扁平化的数组
            
        Returns:
            List: 扁平化后的新数组
        """
        if array is None:
            return []
        result = []
        for item in array:
            if isinstance(item, (list, tuple)):
                result.extend(ArrayUtils.flatten(item))
            else:
                result.append(item)
        return result

    @staticmethod
    def distinct(array: Union[List, Tuple]) -> List:
        """
        去重数组
        
        Args:
            array: 要去重的数组
            
        Returns:
            List: 去重后的新数组
        """
        if array is None:
            return []
        seen = set()
        return [item for item in array if not (item in seen or seen.add(item))]

    @staticmethod
    def chunk(array: Union[List, Tuple], size: int) -> List[List]:
        """
        将数组分块
        
        Args:
            array: 要分块的数组
            size: 块大小
            
        Returns:
            List[List]: 分块后的新数组
        """
        if array is None:
            return []
        if size <= 0:
            return [list(array)]
        return [list(array[i:i+size]) for i in range(0, len(array), size)]

    @staticmethod
    def fill(array: List, value: Any, start: int = 0, end: Optional[int] = None) -> None:
        """
        填充数组
        
        Args:
            array: 要填充的数组
            value: 填充值
            start: 起始位置
            end: 结束位置
        """
        if array is not None:
            if end is None:
                end = len(array)
            array[start:end] = [value] * (end - start)

    @staticmethod
    def to_list(array: Any) -> List:
        """
        将对象转换为数组
        
        Args:
            array: 要转换的对象
            
        Returns:
            List: 转换后的数组
        """
        if array is None:
            return []
        if isinstance(array, list):
            return array
        if isinstance(array, (tuple, np.ndarray)):
            return list(array)
        if hasattr(array, '__iter__'):
            return list(array)
        return [array]

    @staticmethod
    def to_tuple(array: Any) -> Tuple:
        """
        将对象转换为元组
        
        Args:
            array: 要转换的对象
            
        Returns:
            Tuple: 转换后的元组
        """
        if array is None:
            return ()
        if isinstance(array, tuple):
            return array
        if isinstance(array, (list, np.ndarray)):
            return tuple(array)
        if hasattr(array, '__iter__'):
            return tuple(array)
        return (array,)

    @staticmethod
    def to_numpy(array: Any) -> np.ndarray:
        """
        将对象转换为NumPy数组
        
        Args:
            array: 要转换的对象
            
        Returns:
            np.ndarray: 转换后的NumPy数组
        """
        if array is None:
            return np.array([])
        if isinstance(array, np.ndarray):
            return array
        return np.array(array)

    @staticmethod
    def max(array: Union[List, Tuple]) -> Any:
        """
        获取数组中的最大值
        
        Args:
            array: 要获取最大值的数组
            
        Returns:
            Any: 最大值，如果数组为空则返回None
        """
        if array is None or len(array) == 0:
            return None
        return max(array)

    @staticmethod
    def min(array: Union[List, Tuple]) -> Any:
        """
        获取数组中的最小值
        
        Args:
            array: 要获取最小值的数组
            
        Returns:
            Any: 最小值，如果数组为空则返回None
        """
        if array is None or len(array) == 0:
            return None
        return min(array)

    @staticmethod
    def sum(array: Union[List, Tuple]) -> Any:
        """
        计算数组中元素的和
        
        Args:
            array: 要计算和的数组
            
        Returns:
            Any: 元素的和，如果数组为空则返回0
        """
        if array is None or len(array) == 0:
            return 0
        return sum(array)

    @staticmethod
    def average(array: Union[List, Tuple]) -> float:
        """
        计算数组中元素的平均值
        
        Args:
            array: 要计算平均值的数组
            
        Returns:
            float: 元素的平均值，如果数组为空则返回0.0
        """
        if array is None or len(array) == 0:
            return 0.0
        return sum(array) / len(array)

    @staticmethod
    def median(array: Union[List, Tuple]) -> float:
        """
        计算数组中元素的中位数
        
        Args:
            array: 要计算中位数的数组
            
        Returns:
            float: 元素的中位数，如果数组为空则返回0.0
        """
        if array is None or len(array) == 0:
            return 0.0
        sorted_array = sorted(array)
        n = len(sorted_array)
        if n % 2 == 0:
            return (sorted_array[n//2 - 1] + sorted_array[n//2]) / 2
        else:
            return sorted_array[n//2]

    @staticmethod
    def frequency(array: Union[List, Tuple], element: Any) -> int:
        """
        计算元素在数组中出现的频率
        
        Args:
            array: 要计算的数组
            element: 要计算频率的元素
            
        Returns:
            int: 元素出现的频率
        """
        if array is None:
            return 0
        return array.count(element)

    @staticmethod
    def filter(array: Union[List, Tuple], predicate: Callable[[Any], bool]) -> List:
        """
        过滤数组中符合条件的元素
        
        Args:
            array: 要过滤的数组
            predicate: 条件函数
            
        Returns:
            List: 符合条件的元素数组
        """
        if array is None:
            return []
        return [item for item in array if predicate(item)]

    @staticmethod
    def map(array: Union[List, Tuple], mapper: Callable[[Any], Any]) -> List:
        """
        映射数组中的元素
        
        Args:
            array: 要映射的数组
            mapper: 映射函数
            
        Returns:
            List: 映射后的元素数组
        """
        if array is None:
            return []
        return [mapper(item) for item in array]

    @staticmethod
    def for_each(array: Union[List, Tuple], action: Callable[[Any], None]) -> None:
        """
        遍历数组中的元素并执行操作
        
        Args:
            array: 要遍历的数组
            action: 操作函数
        """
        if array is not None:
            for item in array:
                action(item)

    @staticmethod
    def any_match(array: Union[List, Tuple], predicate: Callable[[Any], bool]) -> bool:
        """
        判断数组中是否存在符合条件的元素
        
        Args:
            array: 要判断的数组
            predicate: 条件函数
            
        Returns:
            bool: 如果存在符合条件的元素则返回True，否则返回False
        """
        if array is not None:
            for item in array:
                if predicate(item):
                    return True
        return False

    @staticmethod
    def all_match(array: Union[List, Tuple], predicate: Callable[[Any], bool]) -> bool:
        """
        判断数组中是否所有元素都符合条件
        
        Args:
            array: 要判断的数组
            predicate: 条件函数
            
        Returns:
            bool: 如果所有元素都符合条件则返回True，否则返回False
        """
        if array is not None:
            for item in array:
                if not predicate(item):
                    return False
            return len(array) > 0
        return False

    @staticmethod
    def none_match(array: Union[List, Tuple], predicate: Callable[[Any], bool]) -> bool:
        """
        判断数组中是否没有符合条件的元素
        
        Args:
            array: 要判断的数组
            predicate: 条件函数
            
        Returns:
            bool: 如果没有符合条件的元素则返回True，否则返回False
        """
        if array is not None:
            for item in array:
                if predicate(item):
                    return False
        return True
