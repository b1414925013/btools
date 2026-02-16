"""测试Validator类"""
import unittest
from btools.core.basic.validatorutils import Validator


class TestValidator(unittest.TestCase):
    """测试Validator类"""

    def test_is_email(self):
        """测试邮箱验证"""
        self.assertTrue(Validator.is_email("test@example.com"))
        self.assertFalse(Validator.is_email("test@"))
        self.assertFalse(Validator.is_email("testexample.com"))

    def test_is_phone(self):
        """测试手机号验证"""
        self.assertTrue(Validator.is_phone("13812345678"))
        self.assertFalse(Validator.is_phone("12345678"))
        self.assertFalse(Validator.is_phone("138123456789"))

    def test_is_url(self):
        """测试URL验证"""
        self.assertTrue(Validator.is_url("https://www.example.com"))
        self.assertTrue(Validator.is_url("http://example.com"))
        self.assertFalse(Validator.is_url("example.com"))

    def test_is_ipv4(self):
        """测试IPv4验证"""
        self.assertTrue(Validator.is_ipv4("192.168.1.1"))
        self.assertFalse(Validator.is_ipv4("256.168.1.1"))
        self.assertFalse(Validator.is_ipv4("192.168.1"))

    def test_is_empty(self):
        """测试空值验证"""
        self.assertTrue(Validator.is_empty(None))
        self.assertTrue(Validator.is_empty(""))
        self.assertTrue(Validator.is_empty([]))
        self.assertTrue(Validator.is_empty({}))
        self.assertFalse(Validator.is_empty("test"))
        self.assertFalse(Validator.is_empty([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()