#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模拟工具类

提供高级模拟工具，支持复杂对象和行为模拟等功能
"""
import unittest.mock
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union

T = TypeVar('T')


class MockUtils:
    """
    模拟工具类
    """

    @staticmethod
    def create_mock(spec: Optional[Type] = None, **kwargs) -> unittest.mock.Mock:
        """
        创建模拟对象

        Args:
            spec: 模拟对象的规格
            **kwargs: 模拟对象的属性

        Returns:
            模拟对象
        """
        if spec:
            mock = unittest.mock.Mock(spec=spec, **kwargs)
        else:
            mock = unittest.mock.Mock(**kwargs)
        return mock

    @staticmethod
    def create_magic_mock(spec: Optional[Type] = None, **kwargs) -> unittest.mock.MagicMock:
        """
        创建魔术模拟对象

        Args:
            spec: 模拟对象的规格
            **kwargs: 模拟对象的属性

        Returns:
            魔术模拟对象
        """
        if spec:
            mock = unittest.mock.MagicMock(spec=spec, **kwargs)
        else:
            mock = unittest.mock.MagicMock(**kwargs)
        return mock

    @staticmethod
    def create_spy(obj: Any, name: str) -> unittest.mock.MagicMock:
        """
        创建间谍对象

        Args:
            obj: 要监视的对象
            name: 要监视的方法名

        Returns:
            间谍对象
        """
        return unittest.mock.spy(obj, name)

    @staticmethod
    def patch(target: str, **kwargs) -> unittest.mock._patch:
        """
        补丁装饰器/上下文管理器

        Args:
            target: 要补丁的目标
            **kwargs: 补丁参数

        Returns:
            补丁对象
        """
        return unittest.mock.patch(target, **kwargs)

    @staticmethod
    def patch_object(target: Any, attribute: str, **kwargs) -> unittest.mock._patch_object:
        """
        补丁对象的属性

        Args:
            target: 目标对象
            attribute: 属性名
            **kwargs: 补丁参数

        Returns:
            补丁对象
        """
        return unittest.mock.patch.object(target, attribute, **kwargs)

    @staticmethod
    def patch_multiple(target: Any, **kwargs) -> unittest.mock._patch_multiple:
        """
        补丁对象的多个属性

        Args:
            target: 目标对象
            **kwargs: 补丁参数

        Returns:
            补丁对象
        """
        return unittest.mock.patch.multiple(target, **kwargs)

    @staticmethod
    def mock_returns(mock_obj: unittest.mock.Mock, returns: Any) -> unittest.mock.Mock:
        """
        设置模拟对象的返回值

        Args:
            mock_obj: 模拟对象
            returns: 返回值

        Returns:
            模拟对象
        """
        mock_obj.return_value = returns
        return mock_obj

    @staticmethod
    def mock_side_effect(mock_obj: unittest.mock.Mock, side_effect: Union[Callable, List, Exception]) -> unittest.mock.Mock:
        """
        设置模拟对象的副作用

        Args:
            mock_obj: 模拟对象
            side_effect: 副作用

        Returns:
            模拟对象
        """
        mock_obj.side_effect = side_effect
        return mock_obj

    @staticmethod
    def mock_raises(mock_obj: unittest.mock.Mock, exception: Exception) -> unittest.mock.Mock:
        """
        设置模拟对象抛出异常

        Args:
            mock_obj: 模拟对象
            exception: 异常对象

        Returns:
            模拟对象
        """
        mock_obj.side_effect = exception
        return mock_obj

    @staticmethod
    def mock_returns_iterable(mock_obj: unittest.mock.Mock, iterable: List[Any]) -> unittest.mock.Mock:
        """
        设置模拟对象返回可迭代对象

        Args:
            mock_obj: 模拟对象
            iterable: 可迭代对象

        Returns:
            模拟对象
        """
        mock_obj.side_effect = iterable
        return mock_obj

    @staticmethod
    def assert_called(mock_obj: unittest.mock.Mock) -> None:
        """
        断言模拟对象被调用过

        Args:
            mock_obj: 模拟对象

        Raises:
            AssertionError: 如果模拟对象未被调用
        """
        mock_obj.assert_called()

    @staticmethod
    def assert_called_once(mock_obj: unittest.mock.Mock) -> None:
        """
        断言模拟对象只被调用过一次

        Args:
            mock_obj: 模拟对象

        Raises:
            AssertionError: 如果模拟对象未被调用或被调用多次
        """
        mock_obj.assert_called_once()

    @staticmethod
    def assert_called_with(mock_obj: unittest.mock.Mock, *args, **kwargs) -> None:
        """
        断言模拟对象以指定参数被调用

        Args:
            mock_obj: 模拟对象
            *args: 预期的位置参数
            **kwargs: 预期的关键字参数

        Raises:
            AssertionError: 如果模拟对象未以指定参数被调用
        """
        mock_obj.assert_called_with(*args, **kwargs)

    @staticmethod
    def assert_called_once_with(mock_obj: unittest.mock.Mock, *args, **kwargs) -> None:
        """
        断言模拟对象只以指定参数被调用过一次

        Args:
            mock_obj: 模拟对象
            *args: 预期的位置参数
            **kwargs: 预期的关键字参数

        Raises:
            AssertionError: 如果模拟对象未以指定参数被调用或被调用多次
        """
        mock_obj.assert_called_once_with(*args, **kwargs)

    @staticmethod
    def assert_any_call(mock_obj: unittest.mock.Mock, *args, **kwargs) -> None:
        """
        断言模拟对象曾经以指定参数被调用

        Args:
            mock_obj: 模拟对象
            *args: 预期的位置参数
            **kwargs: 预期的关键字参数

        Raises:
            AssertionError: 如果模拟对象从未以指定参数被调用
        """
        mock_obj.assert_any_call(*args, **kwargs)

    @staticmethod
    def assert_not_called(mock_obj: unittest.mock.Mock) -> None:
        """
        断言模拟对象未被调用

        Args:
            mock_obj: 模拟对象

        Raises:
            AssertionError: 如果模拟对象被调用过
        """
        mock_obj.assert_not_called()

    @staticmethod
    def reset_mock(mock_obj: unittest.mock.Mock) -> unittest.mock.Mock:
        """
        重置模拟对象

        Args:
            mock_obj: 模拟对象

        Returns:
            重置后的模拟对象
        """
        mock_obj.reset_mock()
        return mock_obj

    @staticmethod
    def create_complex_mock(spec: Type, behavior: Dict[str, Any]) -> unittest.mock.Mock:
        """
        创建复杂的模拟对象

        Args:
            spec: 模拟对象的规格
            behavior: 模拟对象的行为定义

        Returns:
            复杂模拟对象
        """
        mock = MockUtils.create_mock(spec=spec)

        for attr_name, attr_value in behavior.items():
            if isinstance(attr_value, dict) and 'return_value' in attr_value:
                # 处理方法模拟
                method_mock = MockUtils.create_mock()
                method_mock.return_value = attr_value['return_value']
                if 'side_effect' in attr_value:
                    method_mock.side_effect = attr_value['side_effect']
                setattr(mock, attr_name, method_mock)
            else:
                # 处理属性模拟
                setattr(mock, attr_name, attr_value)

        return mock

    @staticmethod
    def mock_context_manager(mock_obj: unittest.mock.Mock, enter_return: Any = None, exit_return: bool = False) -> unittest.mock.Mock:
        """
        模拟上下文管理器

        Args:
            mock_obj: 模拟对象
            enter_return: __enter__ 方法的返回值
            exit_return: __exit__ 方法的返回值

        Returns:
            模拟上下文管理器
        """
        mock_obj.__enter__.return_value = enter_return
        mock_obj.__exit__.return_value = exit_return
        return mock_obj

    @staticmethod
    def mock_iterator(mock_obj: unittest.mock.Mock, items: List[Any]) -> unittest.mock.Mock:
        """
        模拟迭代器

        Args:
            mock_obj: 模拟对象
            items: 迭代的项目列表

        Returns:
            模拟迭代器
        """
        mock_obj.__iter__.return_value = iter(items)
        return mock_obj

    @staticmethod
    def create_autospec(spec: Type, **kwargs) -> Any:
        """
        创建自动规格的模拟对象

        Args:
            spec: 模拟对象的规格
            **kwargs: 模拟对象的属性

        Returns:
            自动规格的模拟对象
        """
        return unittest.mock.create_autospec(spec, **kwargs)

    @staticmethod
    def patch_dict(target: Dict, values: Dict, clear: bool = False) -> unittest.mock._patch_dict:
        """
        补丁字典

        Args:
            target: 要补丁的字典
            values: 补丁值
            clear: 是否清除原字典

        Returns:
            补丁对象
        """
        return unittest.mock.patch.dict(target, values, clear=clear)

    @staticmethod
    def mock_open(read_data: str = '') -> unittest.mock.MagicMock:
        """
        模拟 open 函数

        Args:
            read_data: 读取的数据

        Returns:
            模拟的 open 函数
        """
        return unittest.mock.mock_open(read_data=read_data)

    @staticmethod
    def get_call_args(mock_obj: unittest.mock.Mock) -> List[unittest.mock._Call]:
        """
        获取模拟对象的调用参数

        Args:
            mock_obj: 模拟对象

        Returns:
            调用参数列表
        """
        return mock_obj.call_args_list

    @staticmethod
    def get_call_count(mock_obj: unittest.mock.Mock) -> int:
        """
        获取模拟对象的调用次数

        Args:
            mock_obj: 模拟对象

        Returns:
            调用次数
        """
        return mock_obj.call_count