"""测试TestUtils类"""
import unittest
from btools.core.automation.testutils import TestUtils


class TestTestUtils(unittest.TestCase):
    """测试TestUtils类"""

    def test_generate_random_string(self):
        """测试生成随机字符串"""
        length = 10
        result = TestUtils.generate_random_string(length)
        self.assertEqual(len(result), length)


if __name__ == "__main__":
    unittest.main()