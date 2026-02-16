# -*- coding: utf-8 -*-
"""
JSON工具测试
"""
import unittest
import tempfile
import os
import decimal
from btools.core.data.jsonutils import (
    JSONUtils, to_json, from_json, from_file, to_file, pretty_print,
    merge, get_value, set_value, remove_value, is_valid, size, flatten, unflatten
)


class TestJSONUtils(unittest.TestCase):
    """
    JSON工具测试类
    """

    def setUp(self):
        """
        测试前设置
        """
        self.test_data = {
            "name": "测试",
            "age": 25,
            "address": {
                "city": "北京",
                "district": "朝阳区"
            },
            "hobbies": ["读书", "编程", "旅游"],
            "is_student": False
        }

    def test_to_json(self):
        """
        测试对象转JSON字符串
        """
        json_str = JSONUtils.to_json(self.test_data)
        self.assertIsInstance(json_str, str)
        self.assertIn("测试", json_str)  # 确保中文正确处理

        # 测试带缩进的JSON
        pretty_json = JSONUtils.to_json(self.test_data, indent=2)
        self.assertIn("\n", pretty_json)

        # 测试排序键
        sorted_json = JSONUtils.to_json(self.test_data, sort_keys=True)
        self.assertTrue(sorted_json.index('"address"') < sorted_json.index('"age"'))

    def test_from_json(self):
        """
        测试JSON字符串转对象
        """
        json_str = '{"name": "测试", "age": 25}'
        obj = JSONUtils.from_json(json_str)
        self.assertIsInstance(obj, dict)
        self.assertEqual(obj["name"], "测试")
        self.assertEqual(obj["age"], 25)

    def test_file_operations(self):
        """
        测试文件操作
        """
        # 创建临时文件
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_file = f.name

        try:
            # 测试写入文件
            JSONUtils.to_file(self.test_data, temp_file, indent=2)
            self.assertTrue(os.path.exists(temp_file))

            # 测试读取文件
            loaded_data = JSONUtils.from_file(temp_file)
            self.assertEqual(loaded_data["name"], self.test_data["name"])
            self.assertEqual(loaded_data["address"]["city"], self.test_data["address"]["city"])
        finally:
            # 清理临时文件
            if os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_merge(self):
        """
        测试合并JSON对象
        """
        json1 = {"a": 1, "b": {"c": 2, "d": 3}}
        json2 = {"b": {"d": 4, "e": 5}, "f": 6}

        # 测试深度合并
        merged = JSONUtils.merge(json1, json2)
        self.assertEqual(merged["a"], 1)
        self.assertEqual(merged["b"]["c"], 2)
        self.assertEqual(merged["b"]["d"], 4)  # 被覆盖
        self.assertEqual(merged["b"]["e"], 5)  # 新增
        self.assertEqual(merged["f"], 6)  # 新增

        # 测试浅合并
        merged_shallow = JSONUtils.merge(json1, json2, deep=False)
        self.assertEqual(merged_shallow["a"], 1)
        self.assertEqual(merged_shallow["b"]["d"], 4)
        self.assertEqual(merged_shallow["b"]["e"], 5)
        self.assertNotIn("c", merged_shallow["b"])  # 浅合并会覆盖整个b对象

    def test_get_value(self):
        """
        测试根据路径获取值
        """
        # 测试存在的路径
        name = JSONUtils.get_value(self.test_data, "name")
        self.assertEqual(name, "测试")

        # 测试嵌套路径
        city = JSONUtils.get_value(self.test_data, "address.city")
        self.assertEqual(city, "北京")

        # 测试不存在的路径
        nonexistent = JSONUtils.get_value(self.test_data, "nonexistent", "默认值")
        self.assertEqual(nonexistent, "默认值")

        # 测试自定义分隔符
        city_custom = JSONUtils.get_value(self.test_data, "address|city", separator="|")
        self.assertEqual(city_custom, "北京")

    def test_set_value(self):
        """
        测试根据路径设置值
        """
        data = {}

        # 测试设置简单值
        JSONUtils.set_value(data, "name", "测试")
        self.assertEqual(data["name"], "测试")

        # 测试设置嵌套值
        JSONUtils.set_value(data, "address.city", "北京")
        self.assertEqual(data["address"]["city"], "北京")

        # 测试覆盖值
        JSONUtils.set_value(data, "name", "新测试")
        self.assertEqual(data["name"], "新测试")

    def test_remove_value(self):
        """
        测试根据路径移除值
        """
        data = {"a": 1, "b": {"c": 2, "d": 3}}

        # 测试移除嵌套值
        JSONUtils.remove_value(data, "b.c")
        self.assertNotIn("c", data["b"])
        self.assertIn("d", data["b"])

        # 测试移除顶级值
        JSONUtils.remove_value(data, "a")
        self.assertNotIn("a", data)

        # 测试移除不存在的路径
        JSONUtils.remove_value(data, "nonexistent")  # 应该不会报错
        self.assertIn("b", data)

    def test_is_valid(self):
        """
        测试JSON有效性检查
        """
        # 测试有效JSON
        valid_json = '{"name": "测试", "age": 25}'
        self.assertTrue(JSONUtils.is_valid(valid_json))

        # 测试无效JSON
        invalid_json = '{"name": "测试", "age": 25'  # 缺少结束括号
        self.assertFalse(JSONUtils.is_valid(invalid_json))

        # 测试非字符串
        self.assertFalse(JSONUtils.is_valid(123))

    def test_size(self):
        """
        测试JSON大小计算
        """
        # 测试简单对象
        simple_obj = {"a": 1, "b": 2}
        self.assertEqual(JSONUtils.size(simple_obj), 2)

        # 测试嵌套对象
        nested_obj = {"a": 1, "b": {"c": 2, "d": 3}}
        self.assertEqual(JSONUtils.size(nested_obj), 4)  # 2 + 2

        # 测试包含列表的对象
        list_obj = {"a": 1, "b": [2, 3, 4]}
        self.assertEqual(JSONUtils.size(list_obj), 4)  # 1 + 3

    def test_flatten(self):
        """
        测试JSON扁平化
        """
        nested_obj = {"a": 1, "b": {"c": 2, "d": 3}}
        flattened = JSONUtils.flatten(nested_obj)
        self.assertEqual(flattened["a"], 1)
        self.assertEqual(flattened["b.c"], 2)
        self.assertEqual(flattened["b.d"], 3)

        # 测试自定义前缀和分隔符
        flattened_custom = JSONUtils.flatten(nested_obj, prefix="root", separator="_")
        self.assertEqual(flattened_custom["root_a"], 1)
        self.assertEqual(flattened_custom["root_b_c"], 2)

    def test_unflatten(self):
        """
        测试JSON反扁平化
        """
        flattened = {"a": 1, "b.c": 2, "b.d": 3}
        nested = JSONUtils.unflatten(flattened)
        self.assertEqual(nested["a"], 1)
        self.assertEqual(nested["b"]["c"], 2)
        self.assertEqual(nested["b"]["d"], 3)

        # 测试自定义分隔符
        flattened_custom = {"a": 1, "b_c": 2, "b_d": 3}
        nested_custom = JSONUtils.unflatten(flattened_custom, separator="_")
        self.assertEqual(nested_custom["a"], 1)
        self.assertEqual(nested_custom["b"]["c"], 2)

    def test_special_types(self):
        """
        测试特殊类型处理
        """
        # 测试Decimal类型
        from decimal import Decimal
        data_with_decimal = {"price": Decimal("19.99")}
        json_str = JSONUtils.to_json(data_with_decimal)
        self.assertIn("19.99", json_str)

        # 测试set类型
        data_with_set = {"tags": {"python", "json", "test"}}
        json_str = JSONUtils.to_json(data_with_set)
        self.assertIn("python", json_str)
        self.assertIn("json", json_str)

        # 测试bytes类型
        data_with_bytes = {"content": b"hello world"}
        json_str = JSONUtils.to_json(data_with_bytes)
        self.assertIn("hello world", json_str)

    def test_convenience_functions(self):
        """
        测试便捷函数
        """
        # 测试to_json便捷函数
        json_str = to_json(self.test_data)
        self.assertIsInstance(json_str, str)

        # 测试from_json便捷函数
        obj = from_json('{"name": "测试"}')
        self.assertEqual(obj["name"], "测试")

        # 测试merge便捷函数
        merged = merge({"a": 1}, {"b": 2})
        self.assertEqual(merged["a"], 1)
        self.assertEqual(merged["b"], 2)

        # 测试get_value便捷函数
        value = get_value(self.test_data, "name")
        self.assertEqual(value, "测试")

        # 测试set_value便捷函数
        data = {}
        set_value(data, "name", "测试")
        self.assertEqual(data["name"], "测试")

        # 测试remove_value便捷函数
        remove_value(data, "name")
        self.assertNotIn("name", data)

        # 测试is_valid便捷函数
        self.assertTrue(is_valid('{"name": "测试"}'))

        # 测试size便捷函数
        self.assertEqual(size({"a": 1, "b": 2}), 2)

        # 测试flatten便捷函数
        flattened = flatten({"a": {"b": 1}})
        self.assertEqual(flattened["a.b"], 1)

        # 测试unflatten便捷函数
        nested = unflatten({"a.b": 1})
        self.assertEqual(nested["a"]["b"], 1)


if __name__ == '__main__':
    unittest.main()
