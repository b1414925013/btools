"""测试TemplateUtils类"""
import unittest
from btools.core.template.templateutils import TemplateUtils


class TestTemplateUtils(unittest.TestCase):
    """测试TemplateUtils类"""

    def test_render_template(self):
        """测试渲染模板"""
        template = "Hello, {{ name }}!"
        data = {"name": "World"}
        result = TemplateUtils.render_template(template, data)
        self.assertEqual(result, "Hello, World!")

    def test_escape_html(self):
        """测试HTML转义"""
        data = "<html>Hello</html>"
        escaped = TemplateUtils.escape_html(data)
        self.assertEqual(escaped, "&lt;html&gt;Hello&lt;/html&gt;")


if __name__ == "__main__":
    unittest.main()