"""测试StringUtils类"""
import unittest
from btools.core.basic.stringutils import StringUtils


class TestStringUtils(unittest.TestCase):
    """测试StringUtils类"""

    def test_is_empty(self):
        """测试字符串为空检查"""
        self.assertTrue(StringUtils.is_empty(None))
        self.assertTrue(StringUtils.is_empty(""))
        self.assertFalse(StringUtils.is_empty("test"))

    def test_trim(self):
        """测试字符串修剪"""
        self.assertEqual(StringUtils.trim("  test  "), "test")
        self.assertEqual(StringUtils.trim("test"), "test")

    def test_split(self):
        """测试字符串分割"""
        self.assertEqual(StringUtils.split("a,b,c"), ["a", "b", "c"])
        self.assertEqual(StringUtils.split("a-b-c", "-"), ["a", "b", "c"])

    def test_join(self):
        """测试字符串连接"""
        self.assertEqual(StringUtils.join(["a", "b", "c"]), "abc")
        self.assertEqual(StringUtils.join(["a", "b", "c"], ","), "a,b,c")

    def test_replace(self):
        """测试字符串替换"""
        self.assertEqual(StringUtils.replace("test", "t", "T"), "TesT")

    def test_substring(self):
        """测试字符串子串"""
        self.assertEqual(StringUtils.substring("test", 1, 3), "es")

    def test_starts_with(self):
        """测试字符串前缀"""
        self.assertTrue(StringUtils.starts_with("test", "te"))
        self.assertFalse(StringUtils.starts_with("test", "es"))

    def test_ends_with(self):
        """测试字符串后缀"""
        self.assertTrue(StringUtils.ends_with("test", "st"))
        self.assertFalse(StringUtils.ends_with("test", "es"))

    def test_contains(self):
        """测试字符串包含"""
        self.assertTrue(StringUtils.contains("test", "es"))
        self.assertFalse(StringUtils.contains("test", "ab"))

    def test_length(self):
        """测试字符串长度"""
        self.assertEqual(StringUtils.length("test"), 4)
        self.assertEqual(StringUtils.length(None), 0)

    def test_to_upper(self):
        """测试字符串转大写"""
        self.assertEqual(StringUtils.to_upper("test"), "TEST")

    def test_to_lower(self):
        """测试字符串转小写"""
        self.assertEqual(StringUtils.to_lower("TEST"), "test")

    def test_capitalize(self):
        """测试字符串首字母大写"""
        self.assertEqual(StringUtils.capitalize("test"), "Test")

    def test_pad_left(self):
        """测试字符串左填充"""
        self.assertEqual(StringUtils.pad_left("test", 6, "0"), "00test")

    def test_pad_right(self):
        """测试字符串右填充"""
        self.assertEqual(StringUtils.pad_right("test", 6, "0"), "test00")

    def test_remove_whitespace(self):
        """测试移除空白字符"""
        self.assertEqual(StringUtils.remove_whitespace("  t e s t  "), "test")

    def test_is_alpha(self):
        """测试是否为字母"""
        self.assertTrue(StringUtils.is_alpha("test"))
        self.assertFalse(StringUtils.is_alpha("test123"))

    def test_is_digit(self):
        """测试是否为数字"""
        self.assertTrue(StringUtils.is_digit("123"))
        self.assertFalse(StringUtils.is_digit("123test"))

    def test_is_alphanumeric(self):
        """测试是否为字母数字"""
        self.assertTrue(StringUtils.is_alphanumeric("test123"))
        self.assertFalse(StringUtils.is_alphanumeric("test 123"))

    def test_repeat(self):
        """测试字符串重复"""
        self.assertEqual(StringUtils.repeat("test", 3), "testtesttest")

    def test_reverse(self):
        """测试字符串反转"""
        self.assertEqual(StringUtils.reverse("test"), "tset")

    def test_format_template(self):
        """测试模板格式化"""
        template = "Hello, {name}!"
        data = {"name": "World"}
        self.assertEqual(StringUtils.format_template(template, data), "Hello, World!")

    def test_generate_random_string(self):
        """测试生成随机字符串"""
        length = 10
        result = StringUtils.generate_random_string(length)
        self.assertEqual(len(result), length)


if __name__ == "__main__":
    unittest.main()