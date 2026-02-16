"""集合工具类"""
from typing import Any, Dict, List, Optional, Set, Tuple, Union, Callable


class CollectionUtils:
    """集合工具类"""

    @staticmethod
    def is_empty(collection: Any) -> bool:
        """
        判断集合是否为空
        
        Args:
            collection: 要判断的集合
            
        Returns:
            bool: 如果为空则返回True，否则返回False
        """
        if collection is None:
            return True
        if hasattr(collection, '__len__'):
            return len(collection) == 0
        return True

    @staticmethod
    def is_not_empty(collection: Any) -> bool:
        """
        判断集合是否不为空
        
        Args:
            collection: 要判断的集合
            
        Returns:
            bool: 如果不为空则返回True，否则返回False
        """
        return not CollectionUtils.is_empty(collection)

    @staticmethod
    def size(collection: Any) -> int:
        """
        获取集合大小
        
        Args:
            collection: 要获取大小的集合
            
        Returns:
            int: 集合大小
        """
        if collection is None:
            return 0
        if hasattr(collection, '__len__'):
            return len(collection)
        return 0

    @staticmethod
    def add_all(target: Union[List, Set], source: Union[List, Set]) -> None:
        """
        将源集合中的所有元素添加到目标集合中
        
        Args:
            target: 目标集合
            source: 源集合
        """
        if target is not None and source is not None:
            if isinstance(target, list):
                target.extend(source)
            elif isinstance(target, set):
                target.update(source)

    @staticmethod
    def remove_all(target: Union[List, Set], source: Union[List, Set]) -> None:
        """
        从目标集合中移除源集合中的所有元素
        
        Args:
            target: 目标集合
            source: 源集合
        """
        if target is not None and source is not None:
            if isinstance(target, list):
                for item in source:
                    while item in target:
                        target.remove(item)
            elif isinstance(target, set):
                target.difference_update(source)

    @staticmethod
    def retain_all(target: Union[List, Set], source: Union[List, Set]) -> None:
        """
        保留目标集合中与源集合共有的元素
        
        Args:
            target: 目标集合
            source: 源集合
        """
        if target is not None and source is not None:
            if isinstance(target, list):
                target[:] = [item for item in target if item in source]
            elif isinstance(target, set):
                target.intersection_update(source)

    @staticmethod
    def contains_all(collection: Union[List, Set], items: Union[List, Set]) -> bool:
        """
        判断集合是否包含所有指定元素
        
        Args:
            collection: 要判断的集合
            items: 要检查的元素集合
            
        Returns:
            bool: 如果包含所有指定元素则返回True，否则返回False
        """
        if collection is None or items is None:
            return False
        for item in items:
            if item not in collection:
                return False
        return True

    @staticmethod
    def contains_any(collection: Union[List, Set], items: Union[List, Set]) -> bool:
        """
        判断集合是否包含任意指定元素
        
        Args:
            collection: 要判断的集合
            items: 要检查的元素集合
            
        Returns:
            bool: 如果包含任意指定元素则返回True，否则返回False
        """
        if collection is None or items is None:
            return False
        for item in items:
            if item in collection:
                return True
        return False

    @staticmethod
    def find(collection: Union[List, Set], predicate: Callable[[Any], bool]) -> Optional[Any]:
        """
        查找集合中符合条件的第一个元素
        
        Args:
            collection: 要查找的集合
            predicate: 条件函数
            
        Returns:
            Any: 符合条件的第一个元素，如果没有找到则返回None
        """
        if collection is None:
            return None
        for item in collection:
            if predicate(item):
                return item
        return None

    @staticmethod
    def filter(collection: Union[List, Set], predicate: Callable[[Any], bool]) -> Union[List, Set]:
        """
        过滤集合中符合条件的元素
        
        Args:
            collection: 要过滤的集合
            predicate: 条件函数
            
        Returns:
            Union[List, Set]: 符合条件的元素集合
        """
        if collection is None:
            return [] if isinstance(collection, list) else set()
        if isinstance(collection, list):
            return [item for item in collection if predicate(item)]
        elif isinstance(collection, set):
            return {item for item in collection if predicate(item)}
        return collection

    @staticmethod
    def map(collection: Union[List, Set], mapper: Callable[[Any], Any]) -> Union[List, Set]:
        """
        映射集合中的元素
        
        Args:
            collection: 要映射的集合
            mapper: 映射函数
            
        Returns:
            Union[List, Set]: 映射后的元素集合
        """
        if collection is None:
            return [] if isinstance(collection, list) else set()
        if isinstance(collection, list):
            return [mapper(item) for item in collection]
        elif isinstance(collection, set):
            return {mapper(item) for item in collection}
        return collection

    @staticmethod
    def reduce(collection: Union[List, Set], reducer: Callable[[Any, Any], Any], initial_value: Any = None) -> Any:
        """
        归约集合中的元素
        
        Args:
            collection: 要归约的集合
            reducer: 归约函数
            initial_value: 初始值
            
        Returns:
            Any: 归约结果
        """
        if collection is None:
            return initial_value
        iterator = iter(collection)
        if initial_value is None:
            try:
                initial_value = next(iterator)
            except StopIteration:
                return None
        accumulator = initial_value
        for item in iterator:
            accumulator = reducer(accumulator, item)
        return accumulator

    @staticmethod
    def sort(collection: List, key: Optional[Callable[[Any], Any]] = None, reverse: bool = False) -> None:
        """
        排序集合
        
        Args:
            collection: 要排序的集合
            key: 排序键函数
            reverse: 是否倒序
        """
        if collection is not None:
            collection.sort(key=key, reverse=reverse)

    @staticmethod
    def reverse(collection: List) -> None:
        """
        反转集合
        
        Args:
            collection: 要反转的集合
        """
        if collection is not None:
            collection.reverse()

    @staticmethod
    def distinct(collection: Union[List, Set]) -> Union[List, Set]:
        """
        去重集合
        
        Args:
            collection: 要去重的集合
            
        Returns:
            Union[List, Set]: 去重后的集合
        """
        if collection is None:
            return [] if isinstance(collection, list) else set()
        if isinstance(collection, list):
            seen = set()
            return [item for item in collection if not (item in seen or seen.add(item))]
        elif isinstance(collection, set):
            return collection.copy()
        return collection

    @staticmethod
    def union(a: Union[List, Set], b: Union[List, Set]) -> Union[List, Set]:
        """
        计算两个集合的并集
        
        Args:
            a: 第一个集合
            b: 第二个集合
            
        Returns:
            Union[List, Set]: 并集
        """
        if a is None:
            return b.copy() if b is not None else [] if isinstance(a, list) else set()
        if b is None:
            return a.copy()
        if isinstance(a, list) and isinstance(b, list):
            return a + [item for item in b if item not in a]
        elif isinstance(a, set) and isinstance(b, set):
            return a.union(b)
        return a.copy()

    @staticmethod
    def intersection(a: Union[List, Set], b: Union[List, Set]) -> Union[List, Set]:
        """
        计算两个集合的交集
        
        Args:
            a: 第一个集合
            b: 第二个集合
            
        Returns:
            Union[List, Set]: 交集
        """
        if a is None or b is None:
            return [] if isinstance(a, list) else set()
        if isinstance(a, list) and isinstance(b, list):
            return [item for item in a if item in b]
        elif isinstance(a, set) and isinstance(b, set):
            return a.intersection(b)
        return [] if isinstance(a, list) else set()

    @staticmethod
    def difference(a: Union[List, Set], b: Union[List, Set]) -> Union[List, Set]:
        """
        计算两个集合的差集
        
        Args:
            a: 第一个集合
            b: 第二个集合
            
        Returns:
            Union[List, Set]: 差集
        """
        if a is None:
            return [] if isinstance(a, list) else set()
        if b is None:
            return a.copy()
        if isinstance(a, list) and isinstance(b, list):
            return [item for item in a if item not in b]
        elif isinstance(a, set) and isinstance(b, set):
            return a.difference(b)
        return a.copy()

    @staticmethod
    def to_list(collection: Any) -> List:
        """
        将集合转换为列表
        
        Args:
            collection: 要转换的集合
            
        Returns:
            List: 转换后的列表
        """
        if collection is None:
            return []
        if isinstance(collection, list):
            return collection.copy()
        if hasattr(collection, '__iter__'):
            return list(collection)
        return [collection]

    @staticmethod
    def to_set(collection: Any) -> Set:
        """
        将集合转换为集合
        
        Args:
            collection: 要转换的集合
            
        Returns:
            Set: 转换后的集合
        """
        if collection is None:
            return set()
        if isinstance(collection, set):
            return collection.copy()
        if hasattr(collection, '__iter__'):
            return set(collection)
        return {collection}

    @staticmethod
    def to_dict(*args) -> Dict:
        """
        将集合转换为字典
        
        支持两种调用方式：
        1. to_dict([(key1, value1), (key2, value2), ...])
        2. to_dict([key1, key2, ...], [value1, value2, ...])
        
        Args:
            *args: 可以是一个包含键值对元组的列表，或者两个分别包含键和值的列表
            
        Returns:
            Dict: 转换后的字典
        """
        if not args:
            return {}
        
        # 第一种情况：单个参数，包含键值对元组的列表
        if len(args) == 1:
            items = args[0]
            if items is None:
                return {}
            if isinstance(items, dict):
                return items.copy()
            if hasattr(items, '__iter__'):
                try:
                    return dict(items)
                except (TypeError, ValueError):
                    return {}
            return {}
        
        # 第二种情况：两个参数，分别是键列表和值列表
        elif len(args) == 2:
            keys, values = args
            if keys is None or values is None:
                return {}
            return dict(zip(keys, values))
        
        return {}

    @staticmethod
    def zip(*args) -> List[Tuple]:
        """
        压缩多个可迭代对象
        
        支持两种调用方式：
        1. zip([iterable1, iterable2, ...])
        2. zip(iterable1, iterable2, ...)
        
        Args:
            *args: 可以是一个包含多个可迭代对象的列表，或者多个独立的可迭代对象
            
        Returns:
            List[Tuple]: 压缩后的列表
        """
        if not args:
            return []
        
        # 第一种情况：单个参数，包含多个可迭代对象的列表
        if len(args) == 1:
            iterables = args[0]
            if iterables is None:
                return []
            return list(zip(*iterables))
        
        # 第二种情况：多个参数，每个都是可迭代对象
        return list(zip(*args))

    @staticmethod
    def unzip(collection: Union[List, Tuple]) -> Tuple[List, ...]:
        """
        解压缩集合
        
        Args:
            collection: 要解压缩的集合
            
        Returns:
            Tuple[List, ...]: 解压缩后的元组
        """
        if collection is None:
            return ()
        return tuple(map(list, zip(*collection)))

    @staticmethod
    def chunk(collection: List, size: int) -> List[List]:
        """
        将列表分块
        
        Args:
            collection: 要分块的列表
            size: 块大小
            
        Returns:
            List[List]: 分块后的列表
        """
        if collection is None:
            return []
        if size <= 0:
            return [collection]
        return [collection[i:i+size] for i in range(0, len(collection), size)]

    @staticmethod
    def flatten(collection: Union[List, Tuple]) -> List:
        """
        扁平化集合
        
        Args:
            collection: 要扁平化的集合
            
        Returns:
            List: 扁平化后的列表
        """
        if collection is None:
            return []
        result = []
        for item in collection:
            if isinstance(item, (list, tuple)):
                result.extend(CollectionUtils.flatten(item))
            else:
                result.append(item)
        return result

    @staticmethod
    def frequency(collection: Union[List, Set], item: Any) -> int:
        """
        计算元素在集合中出现的频率
        
        Args:
            collection: 要计算的集合
            item: 要计算频率的元素
            
        Returns:
            int: 元素出现的频率
        """
        if collection is None:
            return 0
        return collection.count(item) if hasattr(collection, 'count') else 0

    @staticmethod
    def max(collection: Union[List, Set], key: Optional[Callable[[Any], Any]] = None) -> Any:
        """
        获取集合中的最大值
        
        Args:
            collection: 要获取最大值的集合
            key: 比较键函数
            
        Returns:
            Any: 最大值
        """
        if collection is None or len(collection) == 0:
            return None
        return max(collection, key=key) if key else max(collection)

    @staticmethod
    def min(collection: Union[List, Set], key: Optional[Callable[[Any], Any]] = None) -> Any:
        """
        获取集合中的最小值
        
        Args:
            collection: 要获取最小值的集合
            key: 比较键函数
            
        Returns:
            Any: 最小值
        """
        if collection is None or len(collection) == 0:
            return None
        return min(collection, key=key) if key else min(collection)

    @staticmethod
    def sum(collection: Union[List, Set]) -> Any:
        """
        计算集合中元素的和
        
        Args:
            collection: 要计算和的集合
            
        Returns:
            Any: 元素的和
        """
        if collection is None or len(collection) == 0:
            return 0
        return sum(collection)

    @staticmethod
    def average(collection: Union[List, Set]) -> float:
        """
        计算集合中元素的平均值
        
        Args:
            collection: 要计算平均值的集合
            
        Returns:
            float: 元素的平均值
        """
        if collection is None or len(collection) == 0:
            return 0.0
        return sum(collection) / len(collection)
