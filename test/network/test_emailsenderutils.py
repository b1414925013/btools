"""测试邮件发送工具类"""
import unittest
import os
import tempfile
from btools.core.network.emailsenderutils import EmailSenderUtils


class TestEmailSenderUtils(unittest.TestCase):
    """测试邮件发送工具类"""

    def test_format_addr(self):
        """测试格式化邮件地址"""
        # 注意：_format_addr 是私有方法，但我们可以通过反射测试
        result = EmailSenderUtils._format_addr("Test <test@example.com>")
        self.assertIsInstance(result, str)
        self.assertIn("Test", result)
        self.assertIn("test@example.com", result)

    def test_get_smtp_server(self):
        """测试根据域名获取SMTP服务器"""
        # 测试已知域名
        self.assertEqual("smtp.qq.com", EmailSenderUtils.get_smtp_server("qq.com"))
        self.assertEqual("smtp.163.com", EmailSenderUtils.get_smtp_server("163.com"))
        self.assertEqual("smtp.gmail.com", EmailSenderUtils.get_smtp_server("gmail.com"))
        
        # 测试未知域名
        self.assertIsNone(EmailSenderUtils.get_smtp_server("unknown.com"))

    def test_send_email_simple(self):
        """测试发送简单邮件（模拟测试）"""
        # 这里我们不实际发送邮件，只测试方法是否能正常调用
        # 实际发送需要配置真实的SMTP服务器
        result = EmailSenderUtils.send_email_simple(
            smtp_server="smtp.qq.com",
            from_addr="test@example.com",
            password="testpassword",
            to_addr="recipient@example.com",
            subject="测试邮件",
            content="这是一封测试邮件"
        )
        # 由于配置是假的，应该返回False
        self.assertFalse(result)

    def test_send_template_email(self):
        """测试发送模板邮件（模拟测试）"""
        template_content = "Hello {{ name }}, welcome to {{ service }}!"
        variables = {"name": "John", "service": "BTools"}
        
        result = EmailSenderUtils.send_template_email(
            smtp_server="smtp.qq.com",
            smtp_port=465,
            from_addr="test@example.com",
            password="testpassword",
            to_addrs=["recipient@example.com"],
            subject="测试模板邮件",
            template_content=template_content,
            variables=variables,
            content_type="plain"
        )
        # 由于配置是假的，应该返回False
        self.assertFalse(result)

    def test_send_html_email(self):
        """测试发送HTML邮件（模拟测试）"""
        html_content = "<h1>测试邮件</h1><p>这是一封HTML测试邮件</p>"
        
        result = EmailSenderUtils.send_html_email(
            smtp_server="smtp.qq.com",
            smtp_port=465,
            from_addr="test@example.com",
            password="testpassword",
            to_addrs=["recipient@example.com"],
            subject="测试HTML邮件",
            html_content=html_content
        )
        # 由于配置是假的，应该返回False
        self.assertFalse(result)

    def test_send_email_with_attachment(self):
        """测试发送带附件的邮件（模拟测试）"""
        # 创建临时附件文件
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("这是一个测试附件")
            temp_file = f.name

        try:
            result = EmailSenderUtils.send_email_with_attachment(
                smtp_server="smtp.qq.com",
                smtp_port=465,
                from_addr="test@example.com",
                password="testpassword",
                to_addrs=["recipient@example.com"],
                subject="测试带附件的邮件",
                content="这是一封带附件的测试邮件",
                attachment_paths=[temp_file]
            )
            # 由于配置是假的，应该返回False
            self.assertFalse(result)
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_validate_email_config(self):
        """测试验证邮件配置"""
        # 测试无效配置
        result = EmailSenderUtils.validate_email_config(
            smtp_server="smtp.qq.com",
            smtp_port=465,
            from_addr="test@example.com",
            password="testpassword"
        )
        # 由于配置是假的，应该返回False
        self.assertFalse(result)

    def test_send_test_email(self):
        """测试发送测试邮件（模拟测试）"""
        result = EmailSenderUtils.send_test_email(
            smtp_server="smtp.qq.com",
            smtp_port=465,
            from_addr="test@example.com",
            password="testpassword",
            test_to_addr="test@example.com"
        )
        # 由于配置是假的，应该返回False
        self.assertFalse(result)

    def test_send_batch_emails(self):
        """测试批量发送邮件（模拟测试）"""
        emails = [
            {
                "to_addrs": ["recipient1@example.com"],
                "subject": "测试邮件1",
                "content": "这是第一封测试邮件"
            },
            {
                "to_addrs": ["recipient2@example.com"],
                "subject": "测试邮件2",
                "content": "这是第二封测试邮件"
            }
        ]
        
        results = EmailSenderUtils.send_batch_emails(
            smtp_server="smtp.qq.com",
            smtp_port=465,
            from_addr="test@example.com",
            password="testpassword",
            emails=emails,
            max_workers=2
        )
        
        # 验证返回结果格式
        self.assertIsInstance(results, dict)
        self.assertIn("recipient1@example.com", results)
        self.assertIn("recipient2@example.com", results)
        # 由于配置是假的，应该返回False
        self.assertFalse(results["recipient1@example.com"])
        self.assertFalse(results["recipient2@example.com"])


if __name__ == '__main__':
    unittest.main()
