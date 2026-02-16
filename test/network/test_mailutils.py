"""测试MailUtils类"""
import unittest
from btools.core.network.mailutils import MailUtils


class TestMailUtils(unittest.TestCase):
    """测试MailUtils类"""

    def test_validate_email_format(self):
        """测试验证邮箱格式"""
        self.assertTrue(MailUtils.validate_email_format("test@example.com"))
        self.assertFalse(MailUtils.validate_email_format("test@"))


if __name__ == "__main__":
    unittest.main()