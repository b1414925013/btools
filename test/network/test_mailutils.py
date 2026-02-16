"""测试MailUtils类"""
import unittest
from btools.core.network.mailutils import MailUtils


class TestMailUtils(unittest.TestCase):
    """测试MailUtils类"""

    def test_validate_email(self):
        """测试验证邮箱"""
        self.assertTrue(MailUtils.validate_email("test@example.com"))
        self.assertFalse(MailUtils.validate_email("test@"))

    def test_parse_email(self):
        """测试解析邮箱"""
        email = "Test User <test@example.com>"
        name, address = MailUtils.parse_email(email)
        self.assertEqual(name, "Test User")
        self.assertEqual(address, "test@example.com")


if __name__ == "__main__":
    unittest.main()