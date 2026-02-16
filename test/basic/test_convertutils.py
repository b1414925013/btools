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

    def test_to_string(self):
        """测试转换为字符串"""
        self.assertEqual(Converter.to_string(123), "123")
        self.assertEqual(Converter.to_string(123.45), "123.45")
        self.assertEqual(Converter.to_string(None), "")


if __name__ == "__main__":
    unittest.main()