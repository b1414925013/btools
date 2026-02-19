"""测试AIUtils类"""
import unittest
from btools.core.ai.aiutils import AIUtils


class TestAIUtils(unittest.TestCase):
    """测试AIUtils类"""

    def test_chat(self):
        """测试多轮对话"""
        # 这里只是测试方法是否存在，实际调用需要API密钥
        self.assertTrue(hasattr(AIUtils, 'chat'))

    def test_generate(self):
        """测试文本生成"""
        # 这里只是测试方法是否存在，实际调用需要API密钥
        self.assertTrue(hasattr(AIUtils, 'generate'))

    def test_create_openai_client(self):
        """测试创建OpenAI客户端"""
        # 这里只是测试方法是否存在
        self.assertTrue(hasattr(AIUtils, 'create_openai_client'))

    def test_create_deepseek_client(self):
        """测试创建DeepSeek客户端"""
        # 这里只是测试方法是否存在
        self.assertTrue(hasattr(AIUtils, 'create_deepseek_client'))

    def test_create_doubao_client(self):
        """测试创建豆包客户端"""
        # 这里只是测试方法是否存在
        self.assertTrue(hasattr(AIUtils, 'create_doubao_client'))


if __name__ == "__main__":
    unittest.main()