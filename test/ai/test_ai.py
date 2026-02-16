"""测试AIUtils类"""
import unittest
from btools.core.ai.ai import AIUtils


class TestAIUtils(unittest.TestCase):
    """测试AIUtils类"""

    def test_call_model(self):
        """测试调用AI模型"""
        # 这里只是测试方法是否存在，实际调用需要API密钥
        # 可以根据实际情况添加mock测试
        self.assertTrue(hasattr(AIUtils, 'call_model'))

    def test_summarize_text(self):
        """测试文本摘要"""
        # 这里只是测试方法是否存在，实际调用需要API密钥
        # 可以根据实际情况添加mock测试
        self.assertTrue(hasattr(AIUtils, 'summarize_text'))

    def test_classify_text(self):
        """测试文本分类"""
        # 这里只是测试方法是否存在，实际调用需要API密钥
        # 可以根据实际情况添加mock测试
        self.assertTrue(hasattr(AIUtils, 'classify_text'))

    def test_analyze_sentiment(self):
        """测试情感分析"""
        # 这里只是测试方法是否存在，实际调用需要API密钥
        # 可以根据实际情况添加mock测试
        self.assertTrue(hasattr(AIUtils, 'analyze_sentiment'))

    def test_chat(self):
        """测试多轮对话"""
        # 这里只是测试方法是否存在，实际调用需要API密钥
        # 可以根据实际情况添加mock测试
        self.assertTrue(hasattr(AIUtils, 'chat'))

    def test_translate_text(self):
        """测试文本翻译"""
        # 这里只是测试方法是否存在，实际调用需要API密钥
        # 可以根据实际情况添加mock测试
        self.assertTrue(hasattr(AIUtils, 'translate_text'))


if __name__ == "__main__":
    unittest.main()