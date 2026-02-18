#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
枚举工具类

提供枚举相关的操作功能，包括获取枚举值、根据名称获取枚举、枚举转列表等
"""
import enum
from typing import List, Dict, Any, Type, Optional, Union


class EnumUtil:
    """
    枚举工具类
    """

    @staticmethod
    def get_enum_list(enum_class: Type[enum.Enum]) -> List[enum.Enum]:
        """
        获取枚举类的所有枚举值列表

        Args:
            enum_class: 枚举类

        Returns:
            List[enum.Enum]: 枚举值列表
        """
        return list(enum_class)

    @staticmethod
    def get_enum_names(enum_class: Type[enum.Enum]) -> List[str]:
        """
        获取枚举类的所有枚举名称列表

        Args:
            enum_class: 枚举类

        Returns:
            List[str]: 枚举名称列表
        """
        return [member.name for member in enum_class]

    @staticmethod
    def get_enum_values(enum_class: Type[enum.Enum]) -> List[Any]:
        """
        获取枚举类的所有枚举值列表

        Args:
            enum_class: 枚举类

        Returns:
            List[Any]: 枚举值列表
        """
        return [member.value for member in enum_class]

    @staticmethod
    def get_enum_map(enum_class: Type[enum.Enum]) -> Dict[str, Any]:
        """
        获取枚举类的名称到值的映射

        Args:
            enum_class: 枚举类

        Returns:
            Dict[str, Any]: 名称到值的映射
        """
        return {member.name: member.value for member in enum_class}

    @staticmethod
    def get_enum_by_name(enum_class: Type[enum.Enum], name: str, default: Optional[enum.Enum] = None) -> Optional[enum.Enum]:
        """
        根据名称获取枚举

        Args:
            enum_class: 枚举类
            name: 枚举名称
            default: 默认值，当找不到时返回

        Returns:
            Optional[enum.Enum]: 枚举对象，找不到时返回默认值
        """
        try:
            return enum_class[name]
        except KeyError:
            return default

    @staticmethod
    def get_enum_by_value(enum_class: Type[enum.Enum], value: Any, default: Optional[enum.Enum] = None) -> Optional[enum.Enum]:
        """
        根据值获取枚举

        Args:
            enum_class: 枚举类
            value: 枚举值
            default: 默认值，当找不到时返回

        Returns:
            Optional[enum.Enum]: 枚举对象，找不到时返回默认值
        """
        for member in enum_class:
            if member.value == value:
                return member
        return default

    @staticmethod
    def contains_name(enum_class: Type[enum.Enum], name: str) -> bool:
        """
        检查枚举类是否包含指定名称的枚举

        Args:
            enum_class: 枚举类
            name: 枚举名称

        Returns:
            bool: 是否包含
        """
        return name in enum_class.__members__

    @staticmethod
    def contains_value(enum_class: Type[enum.Enum], value: Any) -> bool:
        """
        检查枚举类是否包含指定值的枚举

        Args:
            enum_class: 枚举类
            value: 枚举值

        Returns:
            bool: 是否包含
        """
        return value in [member.value for member in enum_class]

    @staticmethod
    def get_enum_count(enum_class: Type[enum.Enum]) -> int:
        """
        获取枚举类的枚举数量

        Args:
            enum_class: 枚举类

        Returns:
            int: 枚举数量
        """
        return len(enum_class)

    @staticmethod
    def to_dict(enum_member: enum.Enum) -> Dict[str, Any]:
        """
        将枚举对象转换为字典

        Args:
            enum_member: 枚举对象

        Returns:
            Dict[str, Any]: 包含名称和值的字典
        """
        return {
            'name': enum_member.name,
            'value': enum_member.value
        }

    @staticmethod
    def from_dict(enum_class: Type[enum.Enum], data: Dict[str, Any]) -> Optional[enum.Enum]:
        """
        从字典创建枚举对象

        Args:
            enum_class: 枚举类
            data: 包含名称或值的字典

        Returns:
            Optional[enum.Enum]: 枚举对象，创建失败返回None
        """
        if 'name' in data:
            return EnumUtil.get_enum_by_name(enum_class, data['name'])
        elif 'value' in data:
            return EnumUtil.get_enum_by_value(enum_class, data['value'])
        return None

    @staticmethod
    def is_enum(obj: Any) -> bool:
        """
        检查对象是否为枚举类或枚举值

        Args:
            obj: 要检查的对象

        Returns:
            bool: 是否为枚举
        """
        return isinstance(obj, enum.Enum) or (isinstance(obj, type) and issubclass(obj, enum.Enum))

    @staticmethod
    def get_enum_class(enum_member: enum.Enum) -> Type[enum.Enum]:
        """
        获取枚举对象所属的枚举类

        Args:
            enum_member: 枚举对象

        Returns:
            Type[enum.Enum]: 枚举类
        """
        return type(enum_member)

    @staticmethod
    def get_enum_ordinal(enum_member: enum.Enum) -> int:
        """
        获取枚举对象的序号

        Args:
            enum_member: 枚举对象

        Returns:
            int: 序号
        """
        return list(type(enum_member)).index(enum_member)