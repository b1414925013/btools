# -*- coding: utf-8 -*-
"""
JSONPath工具测试
"""
import unittest
from btools.core.data.jsonpathutils import (
    JSONPathUtils, parse, find, find_first, exists, update, delete, extract, apply
)


class TestJSONPathUtils(unittest.TestCase):
    """
    JSONPath工具测试类
    """

    def setUp(self):
        """
        测试前设置
        """
        self.test_data = {
            "name": "John",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "New York",
                "zip": "10001"
            },
            "phone_numbers": [
                {
                    "type": "home",
                    "number": "555-1234"
                },
                {
                    "type": "work",
                    "number": "555-5678"
                }
            ],
            "email": "john@example.com"
        }

    def test_parse(self):
        """
        测试解析JSONPath表达式
        """
        # 测试基本JSONPath解析
        jsonpath_obj = JSONPathUtils.parse("$.name")
        self.assertIsNotNone(jsonpath_obj)

        # 测试扩展JSONPath解析
        jsonpath_obj_ext = JSONPathUtils.parse("$.address.city", extended=True)
        self.assertIsNotNone(jsonpath_obj_ext)

    def test_find(self):
        """
        测试根据JSONPath查询数据
        """
        # 测试查询单个值
        result = JSONPathUtils.find(self.test_data, "$.name")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "John")

        # 测试查询嵌套值
        result = JSONPathUtils.find(self.test_data, "$.address.city")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "New York")

        # 测试查询数组
        result = JSONPathUtils.find(self.test_data, "$.phone_numbers[*].type")
        self.assertEqual(len(result), 2)
        self.assertIn("home", result)
        self.assertIn("work", result)

    def test_find_first(self):
        """
        测试根据JSONPath查询第一个匹配的数据
        """
        # 测试查询存在的值
        result = JSONPathUtils.find_first(self.test_data, "$.name")
        self.assertEqual(result, "John")

        # 测试查询不存在的值
        result = JSONPathUtils.find_first(self.test_data, "$.non_existent")
        self.assertIsNone(result)

    def test_exists(self):
        """
        测试检查JSONPath是否存在
        """
        # 测试存在的路径
        result = JSONPathUtils.exists(self.test_data, "$.name")
        self.assertTrue(result)

        # 测试不存在的路径
        result = JSONPathUtils.exists(self.test_data, "$.non_existent")
        self.assertFalse(result)

    def test_update(self):
        """
        测试根据JSONPath更新数据
        """
        # 测试更新简单值
        data = self.test_data.copy()
        updated_data = JSONPathUtils.update(data, "$.name", "Jane")
        self.assertEqual(updated_data["name"], "Jane")

        # 测试更新嵌套值
        data = self.test_data.copy()
        updated_data = JSONPathUtils.update(data, "$.address.city", "Los Angeles")
        self.assertEqual(updated_data["address"]["city"], "Los Angeles")

    def test_delete(self):
        """
        测试根据JSONPath删除数据
        """
        # 测试删除简单值
        data = self.test_data.copy()
        updated_data = JSONPathUtils.delete(data, "$.email")
        self.assertNotIn("email", updated_data)

        # 测试删除嵌套值
        data = self.test_data.copy()
        updated_data = JSONPathUtils.delete(data, "$.address.zip")
        self.assertNotIn("zip", updated_data["address"])

    def test_extract(self):
        """
        测试根据JSONPath映射提取数据
        """
        jsonpath_map = {
            "person_name": "$.name",
            "person_age": "$.age",
            "city": "$.address.city"
        }
        result = JSONPathUtils.extract(self.test_data, jsonpath_map)
        self.assertEqual(result["person_name"], "John")
        self.assertEqual(result["person_age"], 30)
        self.assertEqual(result["city"], "New York")

    def test_apply(self):
        """
        测试对JSONPath匹配的数据应用函数
        """
        # 测试应用函数到简单值
        data = self.test_data.copy()
        updated_data = JSONPathUtils.apply(data, "$.age", lambda x: x + 1)
        self.assertEqual(updated_data["age"], 31)

        # 测试应用函数到嵌套值
        data = self.test_data.copy()
        updated_data = JSONPathUtils.apply(data, "$.address.city", lambda x: x.upper())
        self.assertEqual(updated_data["address"]["city"], "NEW YORK")

    def test_convenience_functions(self):
        """
        测试便捷函数
        """
        # 测试parse便捷函数
        jsonpath_obj = parse("$.name")
        self.assertIsNotNone(jsonpath_obj)

        # 测试find便捷函数
        result = find(self.test_data, "$.name")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "John")

        # 测试find_first便捷函数
        result = find_first(self.test_data, "$.name")
        self.assertEqual(result, "John")

        # 测试exists便捷函数
        result = exists(self.test_data, "$.name")
        self.assertTrue(result)

        # 测试update便捷函数
        data = self.test_data.copy()
        updated_data = update(data, "$.name", "Jane")
        self.assertEqual(updated_data["name"], "Jane")

        # 测试delete便捷函数
        data = self.test_data.copy()
        updated_data = delete(data, "$.email")
        self.assertNotIn("email", updated_data)

        # 测试extract便捷函数
        jsonpath_map = {
            "person_name": "$.name",
            "person_age": "$.age"
        }
        result = extract(self.test_data, jsonpath_map)
        self.assertEqual(result["person_name"], "John")
        self.assertEqual(result["person_age"], 30)

        # 测试apply便捷函数
        data = self.test_data.copy()
        updated_data = apply(data, "$.age", lambda x: x + 1)
        self.assertEqual(updated_data["age"], 31)


if __name__ == '__main__':
    unittest.main()