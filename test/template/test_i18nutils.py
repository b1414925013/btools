"""测试I18nUtils类"""
import unittest
from btools.core.template.i18nutils import I18nUtils


class TestI18nUtils(unittest.TestCase):
    """测试I18nUtils类"""

    def test_load_translations(self):
        """测试加载翻译"""
        translations = {
            "en": {
                "hello": "Hello"
            },
            "zh": {
                "hello": "你好"
            }
        }
        I18nUtils.load_translations(translations)
        # 测试默认语言
        self.assertEqual(I18nUtils.get("hello"), "Hello")
        # 测试切换语言
        I18nUtils.set_locale("zh")
        self.assertEqual(I18nUtils.get("hello"), "你好")

    def test_translate(self):
        """测试翻译"""
        translations = {
            "en": {
                "hello": "Hello"
            },
            "zh": {
                "hello": "你好"
            }
        }
        I18nUtils.load_translations(translations)
        self.assertEqual(I18nUtils.translate("hello", locale="zh"), "你好")


if __name__ == "__main__":
    unittest.main()