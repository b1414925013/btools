"""测试RegexUtils类"""
import unittest
from btools.core.data.regexutils import RegexUtils


class TestRegexUtils(unittest.TestCase):
    """测试RegexUtils类"""

    def test_is_match(self):
        """测试是否匹配"""
        self.assertTrue(RegexUtils.is_match(r"\d+", "123"))
        self.assertFalse(RegexUtils.is_match(r"\d+", "abc"))

    def test_is_full_match(self):
        """测试是否完全匹配"""
        self.assertTrue(RegexUtils.is_full_match(r"\d+", "123"))
        self.assertFalse(RegexUtils.is_full_match(r"\d+", "123abc"))

    def test_search(self):
        """测试搜索"""
        result = RegexUtils.search(r"\d+", "abc123def")
        self.assertEqual(result, "123")

    def test_find_all(self):
        """测试查找所有"""
        result = RegexUtils.find_all(r"\d+", "abc123def456")
        self.assertEqual(result, ["123", "456"])

    def test_split(self):
        """测试分割"""
        result = RegexUtils.split(r"\s+", "abc  def  ghi")
        self.assertEqual(result, ["abc", "def", "ghi"])

    def test_sub(self):
        """测试替换"""
        result = RegexUtils.sub(r"\d+", "x", "abc123def456")
        self.assertEqual(result, "abcxdefx")

    def test_validate_email(self):
        """测试验证邮箱"""
        self.assertTrue(RegexUtils.validate_email("test@example.com"))
        self.assertFalse(RegexUtils.validate_email("test@"))

    def test_validate_phone(self):
        """测试验证手机号"""
        self.assertTrue(RegexUtils.validate_phone("13812345678"))
        self.assertFalse(RegexUtils.validate_phone("12345678"))

    def test_validate_url(self):
        """测试验证URL"""
        self.assertTrue(RegexUtils.validate_url("https://www.example.com"))
        self.assertFalse(RegexUtils.validate_url("example.com"))

    def test_validate_ipv4(self):
        """测试验证IPv4"""
        self.assertTrue(RegexUtils.validate_ipv4("192.168.1.1"))
        self.assertFalse(RegexUtils.validate_ipv4("256.168.1.1"))


if __name__ == "__main__":
    unittest.main()