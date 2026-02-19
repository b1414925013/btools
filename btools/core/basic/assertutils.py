"""断言工具类"""
from typing import Any, List, Dict, Optional, Union, Callable
import re


class AssertUtil:
    """断言工具类，提供丰富的断言方法"""

    @staticmethod
    def is_true(expression: bool, message: Optional[str] = None) -> None:
        """
        断言表达式为真

        Args:
            expression: 布尔表达式
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当表达式为False时抛出
        """
        if not expression:
            raise AssertionError(message or "表达式不为真")

    @staticmethod
    def is_false(expression: bool, message: Optional[str] = None) -> None:
        """
        断言表达式为假

        Args:
            expression: 布尔表达式
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当表达式为True时抛出
        """
        if expression:
            raise AssertionError(message or "表达式不为假")

    @staticmethod
    def is_none(obj: Any, message: Optional[str] = None) -> None:
        """
        断言对象为None

        Args:
            obj: 待检查的对象
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当对象不为None时抛出
        """
        if obj is not None:
            raise AssertionError(message or f"对象不为None: {obj}")

    @staticmethod
    def is_not_none(obj: Any, message: Optional[str] = None) -> None:
        """
        断言对象不为None

        Args:
            obj: 待检查的对象
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当对象为None时抛出
        """
        if obj is None:
            raise AssertionError(message or "对象为None")

    @staticmethod
    def equals(expected: Any, actual: Any, message: Optional[str] = None) -> None:
        """
        断言两个对象相等

        Args:
            expected: 期望值
            actual: 实际值
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当两个对象不相等时抛出
        """
        if expected != actual:
            raise AssertionError(message or f"期望值: {expected}, 实际值: {actual}")

    @staticmethod
    def not_equals(expected: Any, actual: Any, message: Optional[str] = None) -> None:
        """
        断言两个对象不相等

        Args:
            expected: 期望值
            actual: 实际值
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当两个对象相等时抛出
        """
        if expected == actual:
            raise AssertionError(message or f"期望值与实际值相等: {expected}")

    @staticmethod
    def is_empty(obj: Any, message: Optional[str] = None) -> None:
        """
        断言对象为空

        支持的类型：str, list, tuple, set, dict, None

        Args:
            obj: 待检查的对象
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当对象不为空时抛出
        """
        is_empty_obj = False
        if obj is None:
            is_empty_obj = True
        elif isinstance(obj, (str, list, tuple, set, dict)):
            is_empty_obj = len(obj) == 0

        if not is_empty_obj:
            raise AssertionError(message or f"对象不为空: {obj}")

    @staticmethod
    def is_not_empty(obj: Any, message: Optional[str] = None) -> None:
        """
        断言对象不为空

        支持的类型：str, list, tuple, set, dict

        Args:
            obj: 待检查的对象
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当对象为空时抛出
        """
        is_empty_obj = False
        if obj is None:
            is_empty_obj = True
        elif isinstance(obj, (str, list, tuple, set, dict)):
            is_empty_obj = len(obj) == 0

        if is_empty_obj:
            raise AssertionError(message or "对象为空")

    @staticmethod
    def is_zero(number: Union[int, float], message: Optional[str] = None) -> None:
        """
        断言数字为0

        Args:
            number: 待检查的数字
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当数字不为0时抛出
        """
        if number != 0:
            raise AssertionError(message or f"数字不为0: {number}")

    @staticmethod
    def is_not_zero(number: Union[int, float], message: Optional[str] = None) -> None:
        """
        断言数字不为0

        Args:
            number: 待检查的数字
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当数字为0时抛出
        """
        if number == 0:
            raise AssertionError(message or "数字为0")

    @staticmethod
    def is_positive(number: Union[int, float], message: Optional[str] = None) -> None:
        """
        断言数字为正数

        Args:
            number: 待检查的数字
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当数字不为正数时抛出
        """
        if number <= 0:
            raise AssertionError(message or f"数字不为正数: {number}")

    @staticmethod
    def is_negative(number: Union[int, float], message: Optional[str] = None) -> None:
        """
        断言数字为负数

        Args:
            number: 待检查的数字
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当数字不为负数时抛出
        """
        if number >= 0:
            raise AssertionError(message or f"数字不为负数: {number}")

    @staticmethod
    def is_instance(obj: Any, cls: type, message: Optional[str] = None) -> None:
        """
        断言对象是指定类型的实例

        Args:
            obj: 待检查的对象
            cls: 期望的类型
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当对象不是指定类型的实例时抛出
        """
        if not isinstance(obj, cls):
            raise AssertionError(message or f"对象不是 {cls.__name__} 类型: {type(obj)}")

    @staticmethod
    def is_not_instance(obj: Any, cls: type, message: Optional[str] = None) -> None:
        """
        断言对象不是指定类型的实例

        Args:
            obj: 待检查的对象
            cls: 不期望的类型
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当对象是指定类型的实例时抛出
        """
        if isinstance(obj, cls):
            raise AssertionError(message or f"对象是 {cls.__name__} 类型")

    @staticmethod
    def contains(container: Any, item: Any, message: Optional[str] = None) -> None:
        """
        断言容器包含指定元素

        支持的容器类型：str, list, tuple, set, dict

        Args:
            container: 容器对象
            item: 要检查的元素
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当容器不包含元素时抛出
        """
        if item not in container:
            raise AssertionError(message or f"容器不包含元素: {item}")

    @staticmethod
    def not_contains(container: Any, item: Any, message: Optional[str] = None) -> None:
        """
        断言容器不包含指定元素

        支持的容器类型：str, list, tuple, set, dict

        Args:
            container: 容器对象
            item: 要检查的元素
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当容器包含元素时抛出
        """
        if item in container:
            raise AssertionError(message or f"容器包含元素: {item}")

    @staticmethod
    def is_subset(subset: Any, superset: Any, message: Optional[str] = None) -> None:
        """
        断言一个集合是另一个集合的子集

        Args:
            subset: 子集
            superset: 超集
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当不是子集时抛出
        """
        if not set(subset).issubset(set(superset)):
            raise AssertionError(message or f"{subset} 不是 {superset} 的子集")

    @staticmethod
    def is_superset(superset: Any, subset: Any, message: Optional[str] = None) -> None:
        """
        断言一个集合是另一个集合的超集

        Args:
            superset: 超集
            subset: 子集
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当不是超集时抛出
        """
        if not set(superset).issuperset(set(subset)):
            raise AssertionError(message or f"{superset} 不是 {subset} 的超集")

    @staticmethod
    def matches(pattern: str, string: str, message: Optional[str] = None) -> None:
        """
        断言字符串匹配正则表达式

        Args:
            pattern: 正则表达式
            string: 待检查的字符串
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当字符串不匹配正则表达式时抛出
        """
        if not re.match(pattern, string):
            raise AssertionError(message or f"字符串 '{string}' 不匹配正则表达式 '{pattern}'")

    @staticmethod
    def not_matches(pattern: str, string: str, message: Optional[str] = None) -> None:
        """
        断言字符串不匹配正则表达式

        Args:
            pattern: 正则表达式
            string: 待检查的字符串
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当字符串匹配正则表达式时抛出
        """
        if re.match(pattern, string):
            raise AssertionError(message or f"字符串 '{string}' 匹配正则表达式 '{pattern}'")

    @staticmethod
    def raises(expected_exception: type, func: Callable, *args, **kwargs) -> None:
        """
        断言函数调用抛出指定异常

        Args:
            expected_exception: 期望的异常类型
            func: 要调用的函数
            *args: 函数位置参数
            **kwargs: 函数关键字参数

        Raises:
            AssertionError: 当未抛出期望的异常时抛出
        """
        try:
            func(*args, **kwargs)
            raise AssertionError(f"未抛出期望的异常: {expected_exception.__name__}")
        except AssertionError:
            raise
        except Exception as e:
            if not isinstance(e, expected_exception):
                raise AssertionError(f"抛出了异常 {type(e).__name__}，但期望的是 {expected_exception.__name__}")

    @staticmethod
    def does_not_raise(func: Callable, *args, **kwargs) -> None:
        """
        断言函数调用不抛出任何异常

        Args:
            func: 要调用的函数
            *args: 函数位置参数
            **kwargs: 函数关键字参数

        Raises:
            AssertionError: 当函数抛出异常时抛出
        """
        try:
            func(*args, **kwargs)
        except Exception as e:
            raise AssertionError(f"函数抛出了异常: {type(e).__name__}: {e}")

    @staticmethod
    def greater(a: Union[int, float], b: Union[int, float], message: Optional[str] = None) -> None:
        """
        断言 a 大于 b

        Args:
            a: 第一个数字
            b: 第二个数字
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当 a 不大于 b 时抛出
        """
        if not a > b:
            raise AssertionError(message or f"{a} 不大于 {b}")

    @staticmethod
    def greater_or_equal(a: Union[int, float], b: Union[int, float], message: Optional[str] = None) -> None:
        """
        断言 a 大于等于 b

        Args:
            a: 第一个数字
            b: 第二个数字
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当 a 小于 b 时抛出
        """
        if not a >= b:
            raise AssertionError(message or f"{a} 小于 {b}")

    @staticmethod
    def less(a: Union[int, float], b: Union[int, float], message: Optional[str] = None) -> None:
        """
        断言 a 小于 b

        Args:
            a: 第一个数字
            b: 第二个数字
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当 a 不小于 b 时抛出
        """
        if not a < b:
            raise AssertionError(message or f"{a} 不小于 {b}")

    @staticmethod
    def less_or_equal(a: Union[int, float], b: Union[int, float], message: Optional[str] = None) -> None:
        """
        断言 a 小于等于 b

        Args:
            a: 第一个数字
            b: 第二个数字
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当 a 大于 b 时抛出
        """
        if not a <= b:
            raise AssertionError(message or f"{a} 大于 {b}")

    @staticmethod
    def between(value: Union[int, float], min_val: Union[int, float], max_val: Union[int, float],
                message: Optional[str] = None) -> None:
        """
        断言值在指定范围内（包含边界）

        Args:
            value: 待检查的值
            min_val: 最小值
            max_val: 最大值
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当值不在指定范围内时抛出
        """
        if not (min_val <= value <= max_val):
            raise AssertionError(message or f"{value} 不在 [{min_val}, {max_val}] 范围内")

    @staticmethod
    def is_same(obj1: Any, obj2: Any, message: Optional[str] = None) -> None:
        """
        断言两个对象是同一个对象（身份相等）

        Args:
            obj1: 第一个对象
            obj2: 第二个对象
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当两个对象不是同一个对象时抛出
        """
        if obj1 is not obj2:
            raise AssertionError(message or f"对象不是同一个: {obj1} vs {obj2}")

    @staticmethod
    def is_not_same(obj1: Any, obj2: Any, message: Optional[str] = None) -> None:
        """
        断言两个对象不是同一个对象（身份不相等）

        Args:
            obj1: 第一个对象
            obj2: 第二个对象
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当两个对象是同一个对象时抛出
        """
        if obj1 is obj2:
            raise AssertionError(message or f"对象是同一个: {obj1}")

    @staticmethod
    def has_length(collection: Any, length: int, message: Optional[str] = None) -> None:
        """
        断言集合具有指定长度

        Args:
            collection: 集合对象
            length: 期望的长度
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当集合长度不匹配时抛出
        """
        if len(collection) != length:
            raise AssertionError(message or f"集合长度为 {len(collection)}，期望为 {length}")

    @staticmethod
    def starts_with(string: str, prefix: str, message: Optional[str] = None) -> None:
        """
        断言字符串以指定前缀开头

        Args:
            string: 待检查的字符串
            prefix: 前缀
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当字符串不以指定前缀开头时抛出
        """
        if not string.startswith(prefix):
            raise AssertionError(message or f"字符串 '{string}' 不以 '{prefix}' 开头")

    @staticmethod
    def ends_with(string: str, suffix: str, message: Optional[str] = None) -> None:
        """
        断言字符串以指定后缀结尾

        Args:
            string: 待检查的字符串
            suffix: 后缀
            message: 断言失败时的错误信息

        Raises:
            AssertionError: 当字符串不以指定后缀结尾时抛出
        """
        if not string.endswith(suffix):
            raise AssertionError(message or f"字符串 '{string}' 不以 '{suffix}' 结尾")

    @staticmethod
    def assert_contains(actual: str, expected: str, message: str = None):
        """
        断言字符串包含

        Args:
            actual (str): 实际值
            expected (str): 期望值
            message (str): 断言失败消息

        Raises:
            AssertionError: 断言失败时抛出
        """
        if expected not in actual:
            msg = message or f"字符串 '{actual}' 不包含 '{expected}'"
            raise AssertionError(msg)

    @staticmethod
    def assert_json_equals(actual: Union[Dict, str], expected: Union[Dict, str], message: str = None):
        """
        断言JSON相等

        Args:
            actual (dict或str): 实际JSON
            expected (dict或str): 期望JSON
            message (str): 断言失败消息

        Raises:
            AssertionError: 断言失败时抛出
        """
        import json
        
        def to_dict(obj):
            if isinstance(obj, str):
                return json.loads(obj)
            return obj
        
        actual_dict = to_dict(actual)
        expected_dict = to_dict(expected)
        
        if actual_dict != expected_dict:
            msg = message or f"JSON不相等: 实际={actual_dict}, 期望={expected_dict}"
            raise AssertionError(msg)

    @staticmethod
    def assert_response_status(response, expected_status: int, message: str = None):
        """
        断言HTTP响应状态码

        Args:
            response: HTTP响应对象
            expected_status (int): 期望状态码
            message (str): 断言失败消息

        Raises:
            AssertionError: 断言失败时抛出
        """
        if hasattr(response, 'status_code'):
            actual_status = response.status_code
        else:
            raise ValueError("响应对象没有status_code属性")
        
        if actual_status != expected_status:
            msg = message or f"状态码不匹配: 实际={actual_status}, 期望={expected_status}"
            # 尝试获取响应内容作为错误信息的一部分
            try:
                if hasattr(response, 'text'):
                    msg += f"\n响应内容: {response.text[:500]}..."
            except:
                pass
            raise AssertionError(msg)

    @staticmethod
    def assert_response_json(response, expected_json: Dict, message: str = None):
        """
        断言HTTP响应JSON

        Args:
            response: HTTP响应对象
            expected_json (dict): 期望JSON
            message (str): 断言失败消息

        Raises:
            AssertionError: 断言失败时抛出
        """
        import json
        
        try:
            actual_json = response.json()
        except Exception as e:
            raise AssertionError(f"无法解析响应为JSON: {e}")
        
        # 递归比较JSON
        def compare_json(actual, expected, path=""):
            if isinstance(expected, dict):
                if not isinstance(actual, dict):
                    return f"路径 '{path}' 期望dict，实际是 {type(actual)}"
                
                for key, value in expected.items():
                    new_path = f"{path}.{key}" if path else key
                    if key not in actual:
                        return f"路径 '{new_path}' 在实际JSON中不存在"
                    
                    error = compare_json(actual[key], value, new_path)
                    if error:
                        return error
            elif isinstance(expected, list):
                if not isinstance(actual, list):
                    return f"路径 '{path}' 期望list，实际是 {type(actual)}"
                
                if len(actual) != len(expected):
                    return f"路径 '{path}' 列表长度不匹配: 实际={len(actual)}, 期望={len(expected)}"
                
                for i, (a, e) in enumerate(zip(actual, expected)):
                    new_path = f"{path}[{i}]"
                    error = compare_json(a, e, new_path)
                    if error:
                        return error
            else:
                if actual != expected:
                    return f"路径 '{path}' 值不匹配: 实际={actual}, 期望={expected}"
            
            return None
        
        error = compare_json(actual_json, expected_json)
        if error:
            msg = message or f"响应JSON不匹配: {error}"
            raise AssertionError(msg)
