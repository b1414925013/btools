"""测试Converter类"""

import unittest

from btools.core.basic.convertutils import Converter


class TestConverter(unittest.TestCase):
    """测试Converter类"""

    def test_to_int(self):
        """测试转换为整数"""
        self.assertEqual(Converter.to_int("123"), 123)
        self.assertEqual(Converter.to_int(123), 123)
        self.assertEqual(Converter.to_int("abc", default=0), 0)

    def test_to_float(self):
        """测试转换为浮点数"""
        self.assertEqual(Converter.to_float("123.45"), 123.45)
        self.assertEqual(Converter.to_float(123.45), 123.45)
        self.assertEqual(Converter.to_float("abc", default=0.0), 0.0)

    def test_to_bool(self):
        """测试转换为布尔值"""
        self.assertTrue(Converter.to_bool("True"))
        self.assertTrue(Converter.to_bool(1))
        self.assertFalse(Converter.to_bool("False"))
        self.assertFalse(Converter.to_bool(0))

    def test_to_str(self):
        """测试转换为字符串"""
        self.assertEqual(Converter.to_str(123), "123")
        self.assertEqual(Converter.to_str(123.45), "123.45")
        self.assertEqual(Converter.to_str(None), "")

    def test_parse_to_words(self):
        """测试解析为单词列表"""
        # 测试驼峰命名
        self.assertEqual(Converter.parse_to_words("camelCase"), ["camel", "case"])
        # 测试帕斯卡命名
        self.assertEqual(Converter.parse_to_words("PascalCase"), ["pascal", "case"])
        # 测试蛇形命名
        self.assertEqual(Converter.parse_to_words("snake_case"), ["snake", "case"])
        # 测试短横线命名
        self.assertEqual(Converter.parse_to_words("kebab-case"), ["kebab", "case"])
        # 测试空格分隔
        self.assertEqual(Converter.parse_to_words("hello world"), ["hello", "world"])
        # 测试空字符串
        self.assertEqual(Converter.parse_to_words(""), [])

    def test_to_pascal_case(self):
        """测试转换为帕斯卡命名"""
        self.assertEqual(Converter.to_pascal_case(["hello", "world"]), "HelloWorld")
        self.assertEqual(Converter.to_pascal_case(["test"]), "Test")
        self.assertEqual(Converter.to_pascal_case([]), "")

    def test_to_snake_case_upper(self):
        """测试转换为大写蛇形命名"""
        self.assertEqual(Converter.to_snake_case_upper(["hello", "world"]), "HELLO_WORLD")
        self.assertEqual(Converter.to_snake_case_upper(["test"]), "TEST")
        self.assertEqual(Converter.to_snake_case_upper([]), "")

    def test_to_package_name(self):
        """测试转换为包命名"""
        self.assertEqual(Converter.to_package_name(["com", "example", "test"]), "com.example.test")
        self.assertEqual(Converter.to_package_name(["test"]), "test")
        self.assertEqual(Converter.to_package_name([]), "")

    def test_to_kebab_case(self):
        """测试转换为短横线命名"""
        self.assertEqual(Converter.to_kebab_case(["hello", "world"]), "hello-world")
        self.assertEqual(Converter.to_kebab_case(["test"]), "test")
        self.assertEqual(Converter.to_kebab_case([]), "")


if __name__ == "__main__":
    unittest.main()
