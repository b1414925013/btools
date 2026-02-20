"""测试邮件模板工具类"""
import unittest
import os
import tempfile
from btools.core.network.emailtemplateutils import EmailTemplateUtils
from jinja2 import Template


class TestEmailTemplateUtils(unittest.TestCase):
    """测试邮件模板工具类"""

    def test_create_html_template(self):
        """测试创建HTML邮件模板"""
        template_content = "<h1>{{ title }}</h1><p>{{ content }}</p>"
        template = EmailTemplateUtils.create_html_template(template_content)
        self.assertIsInstance(template, Template)

    def test_render_template(self):
        """测试渲染邮件模板"""
        template_content = "<h1>{{ title }}</h1><p>{{ content }}</p>"
        template = EmailTemplateUtils.create_html_template(template_content)
        variables = {"title": "测试邮件", "content": "这是一封测试邮件"}
        rendered = EmailTemplateUtils.render_template(template, variables)
        self.assertIn("测试邮件", rendered)
        self.assertIn("这是一封测试邮件", rendered)

    def test_render_template_string(self):
        """测试渲染模板字符串"""
        template_str = "Hello {{ name }}, welcome to {{ service }}!"
        variables = {"name": "John", "service": "BTools"}
        rendered = EmailTemplateUtils.render_template_string(template_str, variables)
        self.assertEqual("Hello John, welcome to BTools!", rendered)

    def test_load_template_from_file(self):
        """测试从文件加载模板"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write("<h1>{{ title }}</h1><p>{{ content }}</p>")
            temp_file = f.name

        try:
            template = EmailTemplateUtils.load_template_from_file(temp_file)
            self.assertIsInstance(template, Template)
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_create_basic_html_template(self):
        """测试创建基本HTML邮件模板"""
        template = EmailTemplateUtils.create_basic_html_template()
        self.assertIsInstance(template, str)
        self.assertIn("<!DOCTYPE html>", template)
        self.assertIn("{{ title }}", template)
        self.assertIn("{{ content }}", template)

    def test_create_notification_template(self):
        """测试创建通知邮件模板"""
        template = EmailTemplateUtils.create_notification_template()
        self.assertIsInstance(template, str)
        self.assertIn("<!DOCTYPE html>", template)
        self.assertIn("{{ subject }}", template)
        self.assertIn("{{ message }}", template)

    def test_create_welcome_template(self):
        """测试创建欢迎邮件模板"""
        template = EmailTemplateUtils.create_welcome_template()
        self.assertIsInstance(template, str)
        self.assertIn("<!DOCTYPE html>", template)
        self.assertIn("{{ username }}", template)
        self.assertIn("{{ service_name }}", template)

    def test_create_password_reset_template(self):
        """测试创建密码重置邮件模板"""
        template = EmailTemplateUtils.create_password_reset_template()
        self.assertIsInstance(template, str)
        self.assertIn("<!DOCTYPE html>", template)
        self.assertIn("{{ username }}", template)
        self.assertIn("{{ reset_url }}", template)

    def test_save_and_load_template(self):
        """测试保存和加载模板"""
        with tempfile.TemporaryDirectory() as temp_dir:
            template_path = os.path.join(temp_dir, "test_template.html")
            template_content = "<h1>{{ title }}</h1><p>{{ content }}</p>"
            
            # 保存模板
            EmailTemplateUtils.save_template(template_content, template_path)
            self.assertTrue(os.path.exists(template_path))
            
            # 加载模板
            template = EmailTemplateUtils.load_template(template_path)
            self.assertIsInstance(template, Template)

    def test_validate_template(self):
        """测试验证模板语法"""
        # 有效的模板
        valid_template = "Hello {{ name }}"
        self.assertTrue(EmailTemplateUtils.validate_template(valid_template))
        
        # 无效的模板（缺少结束标记）
        invalid_template = "Hello {{ name"
        self.assertFalse(EmailTemplateUtils.validate_template(invalid_template))


if __name__ == '__main__':
    unittest.main()
