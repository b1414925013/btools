# -*- coding: utf-8 -*-
"""
JSONPath工具类模块
"""
from jsonpath_ng import parse as jsonpath_parse
from jsonpath_ng.ext import parse as jsonpath_ext_parse
from typing import Any, Dict, List, Optional, Union


class JSONPathUtils:
    """
    JSONPath工具类
    提供JSONPath的解析和查询功能
    """

    @staticmethod
    def parse(jsonpath: str, extended: bool = False) -> Any:
        """
        解析JSONPath表达式

        Args:
            jsonpath: JSONPath表达式
            extended: 是否使用扩展语法，默认False

        Returns:
            解析后的JSONPath对象
        """
        if extended:
            return jsonpath_ext_parse(jsonpath)
        return jsonpath_parse(jsonpath)

    @staticmethod
    def find(data: Any, jsonpath: Union[str, Any]) -> List[Any]:
        """
        根据JSONPath查询数据

        Args:
            data: 要查询的数据
            jsonpath: JSONPath表达式或解析后的JSONPath对象

        Returns:
            查询结果列表
        """
        if isinstance(jsonpath, str):
            jsonpath_obj = JSONPathUtils.parse(jsonpath)
        else:
            jsonpath_obj = jsonpath
        
        matches = jsonpath_obj.find(data)
        return [match.value for match in matches]

    @staticmethod
    def find_first(data: Any, jsonpath: Union[str, Any]) -> Optional[Any]:
        """
        根据JSONPath查询第一个匹配的数据

        Args:
            data: 要查询的数据
            jsonpath: JSONPath表达式或解析后的JSONPath对象

        Returns:
            第一个匹配的结果，不存在则返回None
        """
        results = JSONPathUtils.find(data, jsonpath)
        return results[0] if results else None

    @staticmethod
    def exists(data: Any, jsonpath: Union[str, Any]) -> bool:
        """
        检查JSONPath是否存在

        Args:
            data: 要检查的数据
            jsonpath: JSONPath表达式或解析后的JSONPath对象

        Returns:
            是否存在匹配
        """
        results = JSONPathUtils.find(data, jsonpath)
        return len(results) > 0

    @staticmethod
    def update(data: Dict[str, Any], jsonpath: Union[str, Any], value: Any) -> Dict[str, Any]:
        """
        根据JSONPath更新数据

        Args:
            data: 要更新的数据
            jsonpath: JSONPath表达式或解析后的JSONPath对象
            value: 要设置的值

        Returns:
            更新后的数据
        """
        if isinstance(jsonpath, str):
            jsonpath_obj = JSONPathUtils.parse(jsonpath)
        else:
            jsonpath_obj = jsonpath
        
        # 对于简单的JSONPath，直接更新
        if isinstance(data, dict):
            keys = jsonpath.strip('$').strip('.').split('.')
            current = data
            for i, key in enumerate(keys[:-1]):
                if key not in current:
                    current[key] = {}
                current = current[key]
            current[keys[-1]] = value
        return data

    @staticmethod
    def delete(data: Dict[str, Any], jsonpath: Union[str, Any]) -> Dict[str, Any]:
        """
        根据JSONPath删除数据

        Args:
            data: 要删除的数据
            jsonpath: JSONPath表达式或解析后的JSONPath对象

        Returns:
            删除后的数据
        """
        if isinstance(jsonpath, str):
            jsonpath_obj = JSONPathUtils.parse(jsonpath)
        else:
            jsonpath_obj = jsonpath
        
        # 对于简单的JSONPath，直接删除
        if isinstance(data, dict):
            keys = jsonpath.strip('$').strip('.').split('.')
            current = data
            for i, key in enumerate(keys[:-1]):
                if key not in current:
                    return data
                current = current[key]
            if keys[-1] in current:
                del current[keys[-1]]
        return data

    @staticmethod
    def extract(data: Any, jsonpath_map: Dict[str, str]) -> Dict[str, Any]:
        """
        根据JSONPath映射提取数据

        Args:
            data: 要提取的数据
            jsonpath_map: JSONPath映射，键为目标键，值为JSONPath表达式

        Returns:
            提取后的数据
        """
        result = {}
        for key, jsonpath in jsonpath_map.items():
            value = JSONPathUtils.find_first(data, jsonpath)
            result[key] = value
        return result

    @staticmethod
    def apply(data: Any, jsonpath: Union[str, Any], func: callable) -> Dict[str, Any]:
        """
        对JSONPath匹配的数据应用函数

        Args:
            data: 要处理的数据
            jsonpath: JSONPath表达式或解析后的JSONPath对象
            func: 要应用的函数

        Returns:
            处理后的数据
        """
        if isinstance(jsonpath, str):
            jsonpath_obj = JSONPathUtils.parse(jsonpath)
        else:
            jsonpath_obj = jsonpath
        
        # 对于简单的JSONPath，直接应用函数
        if isinstance(data, dict):
            keys = jsonpath.strip('$').strip('.').split('.')
            current = data
            for i, key in enumerate(keys[:-1]):
                if key not in current:
                    return data
                current = current[key]
            if keys[-1] in current:
                current[keys[-1]] = func(current[keys[-1]])
        return data


# 便捷函数

def parse(jsonpath: str, extended: bool = False) -> Any:
    """
    解析JSONPath表达式

    Args:
        jsonpath: JSONPath表达式
        extended: 是否使用扩展语法，默认False

    Returns:
        解析后的JSONPath对象
    """
    return JSONPathUtils.parse(jsonpath, extended)


def find(data: Any, jsonpath: Union[str, Any]) -> List[Any]:
    """
    根据JSONPath查询数据

    Args:
        data: 要查询的数据
        jsonpath: JSONPath表达式或解析后的JSONPath对象

    Returns:
        查询结果列表
    """
    return JSONPathUtils.find(data, jsonpath)


def find_first(data: Any, jsonpath: Union[str, Any]) -> Optional[Any]:
    """
    根据JSONPath查询第一个匹配的数据

    Args:
        data: 要查询的数据
        jsonpath: JSONPath表达式或解析后的JSONPath对象

    Returns:
        第一个匹配的结果，不存在则返回None
    """
    return JSONPathUtils.find_first(data, jsonpath)


def exists(data: Any, jsonpath: Union[str, Any]) -> bool:
    """
    检查JSONPath是否存在

    Args:
        data: 要检查的数据
        jsonpath: JSONPath表达式或解析后的JSONPath对象

    Returns:
        是否存在匹配
    """
    return JSONPathUtils.exists(data, jsonpath)


def update(data: Dict[str, Any], jsonpath: Union[str, Any], value: Any) -> Dict[str, Any]:
    """
    根据JSONPath更新数据

    Args:
        data: 要更新的数据
        jsonpath: JSONPath表达式或解析后的JSONPath对象
        value: 要设置的值

    Returns:
        更新后的数据
    """
    return JSONPathUtils.update(data, jsonpath, value)


def delete(data: Dict[str, Any], jsonpath: Union[str, Any]) -> Dict[str, Any]:
    """
    根据JSONPath删除数据

    Args:
        data: 要删除的数据
        jsonpath: JSONPath表达式或解析后的JSONPath对象

    Returns:
        删除后的数据
    """
    return JSONPathUtils.delete(data, jsonpath)


def extract(data: Any, jsonpath_map: Dict[str, str]) -> Dict[str, Any]:
    """
    根据JSONPath映射提取数据

    Args:
        data: 要提取的数据
        jsonpath_map: JSONPath映射，键为目标键，值为JSONPath表达式

    Returns:
        提取后的数据
    """
    return JSONPathUtils.extract(data, jsonpath_map)


def apply(data: Any, jsonpath: Union[str, Any], func: callable) -> Dict[str, Any]:
    """
    对JSONPath匹配的数据应用函数

    Args:
        data: 要处理的数据
        jsonpath: JSONPath表达式或解析后的JSONPath对象
        func: 要应用的函数

    Returns:
        处理后的数据
    """
    return JSONPathUtils.apply(data, jsonpath, func)
