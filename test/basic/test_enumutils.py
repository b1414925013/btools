#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EnumUtil 测试文件
"""
import enum
import unittest
from btools.core.basic import EnumUtil


# 测试用枚举类
class TestEnum(enum.Enum):
    """测试枚举类"""
    FIRST = 1
    SECOND = 2
    THIRD = 3


class TestEnumUtil(unittest.TestCase):
    """
    EnumUtil 测试类
    """

    def test_get_enum_list(self):
        """
        测试获取枚举列表
        """
        enum_list = EnumUtil.get_enum_list(TestEnum)
        self.assertEqual(len(enum_list), 3)
        self.assertIn(TestEnum.FIRST, enum_list)
        self.assertIn(TestEnum.SECOND, enum_list)
        self.assertIn(TestEnum.THIRD, enum_list)

    def test_get_enum_names(self):
        """
        测试获取枚举名称列表
        """
        names = EnumUtil.get_enum_names(TestEnum)
        self.assertEqual(len(names), 3)
        self.assertIn("FIRST", names)
        self.assertIn("SECOND", names)
        self.assertIn("THIRD", names)

    def test_get_enum_values(self):
        """
        测试获取枚举值列表
        """
        values = EnumUtil.get_enum_values(TestEnum)
        self.assertEqual(len(values), 3)
        self.assertIn(1, values)
        self.assertIn(2, values)
        self.assertIn(3, values)

    def test_get_enum_map(self):
        """
        测试获取枚举映射
        """
        enum_map = EnumUtil.get_enum_map(TestEnum)
        self.assertEqual(len(enum_map), 3)
        self.assertEqual(enum_map["FIRST"], 1)
        self.assertEqual(enum_map["SECOND"], 2)
        self.assertEqual(enum_map["THIRD"], 3)

    def test_get_enum_by_name(self):
        """
        测试根据名称获取枚举
        """
        # 测试存在的名称
        enum_obj = EnumUtil.get_enum_by_name(TestEnum, "FIRST")
        self.assertEqual(enum_obj, TestEnum.FIRST)

        # 测试不存在的名称，使用默认值
        enum_obj = EnumUtil.get_enum_by_name(TestEnum, "NOT_EXIST", TestEnum.FIRST)
        self.assertEqual(enum_obj, TestEnum.FIRST)

        # 测试不存在的名称，不使用默认值
        enum_obj = EnumUtil.get_enum_by_name(TestEnum, "NOT_EXIST")
        self.assertIsNone(enum_obj)

    def test_get_enum_by_value(self):
        """
        测试根据值获取枚举
        """
        # 测试存在的值
        enum_obj = EnumUtil.get_enum_by_value(TestEnum, 1)
        self.assertEqual(enum_obj, TestEnum.FIRST)

        # 测试不存在的值，使用默认值
        enum_obj = EnumUtil.get_enum_by_value(TestEnum, 999, TestEnum.FIRST)
        self.assertEqual(enum_obj, TestEnum.FIRST)

        # 测试不存在的值，不使用默认值
        enum_obj = EnumUtil.get_enum_by_value(TestEnum, 999)
        self.assertIsNone(enum_obj)

    def test_contains_name(self):
        """
        测试是否包含指定名称
        """
        self.assertTrue(EnumUtil.contains_name(TestEnum, "FIRST"))
        self.assertFalse(EnumUtil.contains_name(TestEnum, "NOT_EXIST"))

    def test_contains_value(self):
        """
        测试是否包含指定值
        """
        self.assertTrue(EnumUtil.contains_value(TestEnum, 1))
        self.assertFalse(EnumUtil.contains_value(TestEnum, 999))

    def test_get_enum_count(self):
        """
        测试获取枚举数量
        """
        count = EnumUtil.get_enum_count(TestEnum)
        self.assertEqual(count, 3)

    def test_to_dict(self):
        """
        测试枚举转字典
        """
        enum_dict = EnumUtil.to_dict(TestEnum.FIRST)
        self.assertEqual(enum_dict["name"], "FIRST")
        self.assertEqual(enum_dict["value"], 1)

    def test_from_dict(self):
        """
        测试从字典创建枚举
        """
        # 测试通过名称创建
        enum_obj = EnumUtil.from_dict(TestEnum, {"name": "FIRST"})
        self.assertEqual(enum_obj, TestEnum.FIRST)

        # 测试通过值创建
        enum_obj = EnumUtil.from_dict(TestEnum, {"value": 1})
        self.assertEqual(enum_obj, TestEnum.FIRST)

        # 测试创建失败
        enum_obj = EnumUtil.from_dict(TestEnum, {"other": "value"})
        self.assertIsNone(enum_obj)

    def test_is_enum(self):
        """
        测试是否为枚举
        """
        # 测试枚举对象
        self.assertTrue(EnumUtil.is_enum(TestEnum.FIRST))

        # 测试枚举类
        self.assertTrue(EnumUtil.is_enum(TestEnum))

        # 测试非枚举
        self.assertFalse(EnumUtil.is_enum(1))
        self.assertFalse(EnumUtil.is_enum("string"))
        self.assertFalse(EnumUtil.is_enum({}))

    def test_get_enum_class(self):
        """
        测试获取枚举类
        """
        enum_class = EnumUtil.get_enum_class(TestEnum.FIRST)
        self.assertEqual(enum_class, TestEnum)

    def test_get_enum_ordinal(self):
        """
        测试获取枚举序号
        """
        ordinal = EnumUtil.get_enum_ordinal(TestEnum.FIRST)
        self.assertEqual(ordinal, 0)

        ordinal = EnumUtil.get_enum_ordinal(TestEnum.SECOND)
        self.assertEqual(ordinal, 1)

        ordinal = EnumUtil.get_enum_ordinal(TestEnum.THIRD)
        self.assertEqual(ordinal, 2)


if __name__ == '__main__':
    unittest.main()