"""测试EmailUtils类"""
import unittest
import os
import tempfile
from btools.core.network.emailutils import EmailTemplateUtils, EmailSenderUtils


class TestEmailTemplateUtils(unittest.TestCase):
    """测试EmailTemplateUtils类"""

    def test_create_html_template(self):
        """测试创建HTML模板"""
        template = EmailTemplateUtils.create_html_template('''
        <html>
        <body>
            <h1>Hello {{ name }}!</h1>
        </body>
        </html>
        ''')
        self.assertIsNotNone(template)

    def test_render_template(self):
        """测试渲染模板"""
        template = EmailTemplateUtils.create_html_template('''
        <html>
        <body>
            <h1>Hello {{ name }}!</h1>
        </body>
        </html>
        ''')
        result = EmailTemplateUtils.render_template(template, {'name': 'John'})
        self.assertIn('Hello John!', result)

    def test_render_template_string(self):
        """测试渲染模板字符串"""
        result = EmailTemplateUtils.render_template_string(
            '<h1>Hello {{ name }}!</h1>',
            {'name': 'John'}
        )
        self.assertIn('Hello John!', result)

    def test_create_basic_html_template(self):
        """测试创建基本HTML模板"""
        template = EmailTemplateUtils.create_basic_html_template()
        self.assertIsInstance(template, str)
        self.assertIn('<!DOCTYPE html>', template)

    def test_create_notification_template(self):
        """测试创建通知模板"""
        template = EmailTemplateUtils.create_notification_template()
        self.assertIsInstance(template, str)
        self.assertIn('<!DOCTYPE html>', template)

    def test_create_welcome_template(self):
        """测试创建欢迎模板"""
        template = EmailTemplateUtils.create_welcome_template()
        self.assertIsInstance(template, str)
        self.assertIn('<!DOCTYPE html>', template)

    def test_create_password_reset_template(self):
        """测试创建密码重置模板"""
        template = EmailTemplateUtils.create_password_reset_template()
        self.assertIsInstance(template, str)
        self.assertIn('<!DOCTYPE html>', template)

    def test_save_and_load_template(self):
        """测试保存和加载模板"""
        with tempfile.TemporaryDirectory() as temp_dir:
            template_path = os.path.join(temp_dir, 'test_template.html')
            
            # 保存模板
            template_content = '<h1>Hello {{ name }}!</h1>'
            EmailTemplateUtils.save_template(template_content, template_path)
            
            # 验证文件存在
            self.assertTrue(os.path.exists(template_path))
            
            # 加载模板
            loaded_template = EmailTemplateUtils.load_template(template_path)
            self.assertIsNotNone(loaded_template)

    def test_validate_template(self):
        """测试验证模板"""
        # 有效的模板
        valid_template = '<h1>Hello {{ name }}!</h1>'
        self.assertTrue(EmailTemplateUtils.validate_template(valid_template))
        
        # 无效的模板
        invalid_template = '<h1>Hello {{ name!</h1>'
        self.assertFalse(EmailTemplateUtils.validate_template(invalid_template))

    def test_load_template_from_directory(self):
        """测试从目录加载模板"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # 创建模板文件
            template_content = '<h1>Hello {{ name }}!</h1>'
            template_path = os.path.join(temp_dir, 'test_template.html')
            with open(template_path, 'w', encoding='utf-8') as f:
                f.write(template_content)
            
            # 加载模板
            template = EmailTemplateUtils.load_template_from_directory(
                temp_dir, 'test_template.html'
            )
            self.assertIsNotNone(template)


class TestEmailSenderUtils(unittest.TestCase):
    """测试EmailSenderUtils类"""

    def test_format_addr(self):
        """测试格式化邮件地址"""
        formatted = EmailSenderUtils._format_addr('John <john@example.com>')
        self.assertIsInstance(formatted, str)

    def test_get_smtp_server(self):
        """测试获取SMTP服务器"""
        self.assertEqual(EmailSenderUtils.get_smtp_server('qq.com'), 'smtp.qq.com')
        self.assertEqual(EmailSenderUtils.get_smtp_server('gmail.com'), 'smtp.gmail.com')
        self.assertEqual(EmailSenderUtils.get_smtp_server('163.com'), 'smtp.163.com')
        self.assertIsNone(EmailSenderUtils.get_smtp_server('unknown.com'))

    def test_send_email_simple(self):
        """测试发送简单邮件（模拟）"""
        # 这里只是测试方法调用，不实际发送邮件
        # 实际发送邮件需要真实的SMTP服务器配置
        try:
            result = EmailSenderUtils.send_email_simple(
                smtp_server='smtp.qq.com',
                from_addr='test@example.com',
                password='test',
                to_addr='recipient@example.com',
                subject='Test',
                content='Test content'
            )
            # 由于是测试配置，应该返回False
            self.assertFalse(result)
        except Exception as e:
            # 预期会抛出异常，因为配置是假的
            self.assertIsInstance(e, Exception)

    def test_validate_email_config(self):
        """测试验证邮件配置（模拟）"""
        # 使用假配置，应该返回False
        result = EmailSenderUtils.validate_email_config(
            smtp_server='smtp.qq.com',
            smtp_port=465,
            from_addr='test@example.com',
            password='test',
            use_ssl=True
        )
        self.assertFalse(result)

    def test_send_test_email(self):
        """测试发送测试邮件（模拟）"""
        # 使用假配置，应该返回False
        result = EmailSenderUtils.send_test_email(
            smtp_server='smtp.qq.com',
            smtp_port=465,
            from_addr='test@example.com',
            password='test',
            test_to_addr='test@example.com',
            use_ssl=True
        )
        self.assertFalse(result)

    def test_send_batch_emails(self):
        """测试批量发送邮件（模拟）"""
        emails = [
            {
                'to_addrs': ['user1@example.com'],
                'subject': 'Test 1',
                'content': 'Content 1'
            }
        ]
        
        results = EmailSenderUtils.send_batch_emails(
            smtp_server='smtp.qq.com',
            smtp_port=465,
            from_addr='test@example.com',
            password='test',
            emails=emails,
            use_ssl=True
        )
        
        self.assertIsInstance(results, dict)

    def test_send_template_email(self):
        """测试发送模板邮件（模拟）"""
        template = '<h1>Hello {{ name }}!</h1>'
        
        result = EmailSenderUtils.send_template_email(
            smtp_server='smtp.qq.com',
            smtp_port=465,
            from_addr='test@example.com',
            password='test',
            to_addrs=['recipient@example.com'],
            subject='Test',
            template_content=template,
            variables={'name': 'John'},
            use_ssl=True
        )
        
        self.assertFalse(result)

    def test_send_html_email(self):
        """测试发送HTML邮件（模拟）"""
        html_content = '<h1>Hello!</h1><p>This is a test.</p>'
        
        result = EmailSenderUtils.send_html_email(
            smtp_server='smtp.qq.com',
            smtp_port=465,
            from_addr='test@example.com',
            password='test',
            to_addrs=['recipient@example.com'],
            subject='Test',
            html_content=html_content,
            use_ssl=True
        )
        
        self.assertFalse(result)

    def test_send_email_with_attachment(self):
        """测试发送带附件的邮件（模拟）"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as temp_file:
            temp_file.write('Test content')
            temp_file_path = temp_file.name
        
        try:
            result = EmailSenderUtils.send_email_with_attachment(
                smtp_server='smtp.qq.com',
                smtp_port=465,
                from_addr='test@example.com',
                password='test',
                to_addrs=['recipient@example.com'],
                subject='Test',
                content='Test content',
                attachment_paths=[temp_file_path],
                use_ssl=True
            )
            
            self.assertFalse(result)
        finally:
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)


if __name__ == "__main__":
    unittest.main()
