"""测试从 AssertEnhancer 合并到 AssertUtil 的方法"""
import unittest
from unittest.mock import Mock
from btools.core.basic.assertutils import AssertUtil


class TestAssertEnhancerMerged(unittest.TestCase):
    """测试从 AssertEnhancer 合并到 AssertUtil 的方法"""

    def test_assert_contains(self):
        """测试 assert_contains 方法"""
        # 测试成功的情况
        AssertUtil.assert_contains("Hello World", "World")
        # 测试失败的情况
        with self.assertRaises(AssertionError):
            AssertUtil.assert_contains("Hello World", "Test")

    def test_assert_json_equals(self):
        """测试 assert_json_equals 方法"""
        # 测试字典比较
        actual = {"name": "John", "age": 30}
        expected = {"name": "John", "age": 30}
        AssertUtil.assert_json_equals(actual, expected)
        
        # 测试JSON字符串比较
        actual_str = '{"name": "John", "age": 30}'
        expected_str = '{"name": "John", "age": 30}'
        AssertUtil.assert_json_equals(actual_str, expected_str)
        
        # 测试失败的情况
        actual = {"name": "John", "age": 30}
        expected = {"name": "John", "age": 25}
        with self.assertRaises(AssertionError):
            AssertUtil.assert_json_equals(actual, expected)

    def test_assert_response_status(self):
        """测试 assert_response_status 方法"""
        # 创建模拟响应对象
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "Success"
        
        # 测试成功的情况
        AssertUtil.assert_response_status(mock_response, 200)
        
        # 测试失败的情况
        with self.assertRaises(AssertionError):
            AssertUtil.assert_response_status(mock_response, 404)

    def test_assert_response_json(self):
        """测试 assert_response_json 方法"""
        # 创建模拟响应对象
        mock_response = Mock()
        mock_response.json.return_value = {"status": "success", "data": {"name": "John"}}
        
        # 测试成功的情况
        expected = {"status": "success", "data": {"name": "John"}}
        AssertUtil.assert_response_json(mock_response, expected)
        
        # 测试部分匹配
        expected_partial = {"status": "success"}
        AssertUtil.assert_response_json(mock_response, expected_partial)


if __name__ == "__main__":
    unittest.main()
