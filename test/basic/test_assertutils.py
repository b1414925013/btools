"""断言工具类测试"""
import unittest
from unittest.mock import Mock
from btools.core.basic import AssertUtil


class TestAssertUtil(unittest.TestCase):
    """AssertUtil 测试类"""

    def test_is_true(self):
        """测试 is_true 方法"""
        AssertUtil.is_true(True)
        with self.assertRaises(AssertionError):
            AssertUtil.is_true(False)

    def test_is_false(self):
        """测试 is_false 方法"""
        AssertUtil.is_false(False)
        with self.assertRaises(AssertionError):
            AssertUtil.is_false(True)

    def test_is_none(self):
        """测试 is_none 方法"""
        AssertUtil.is_none(None)
        with self.assertRaises(AssertionError):
            AssertUtil.is_none(123)

    def test_is_not_none(self):
        """测试 is_not_none 方法"""
        AssertUtil.is_not_none(123)
        with self.assertRaises(AssertionError):
            AssertUtil.is_not_none(None)

    def test_equals(self):
        """测试 equals 方法"""
        AssertUtil.equals(1, 1)
        AssertUtil.equals("test", "test")
        with self.assertRaises(AssertionError):
            AssertUtil.equals(1, 2)

    def test_not_equals(self):
        """测试 not_equals 方法"""
        AssertUtil.not_equals(1, 2)
        AssertUtil.not_equals("test", "test2")
        with self.assertRaises(AssertionError):
            AssertUtil.not_equals(1, 1)

    def test_is_empty(self):
        """测试 is_empty 方法"""
        AssertUtil.is_empty(None)
        AssertUtil.is_empty("")
        AssertUtil.is_empty([])
        AssertUtil.is_empty(())
        AssertUtil.is_empty(set())
        AssertUtil.is_empty({})
        with self.assertRaises(AssertionError):
            AssertUtil.is_empty("test")
        with self.assertRaises(AssertionError):
            AssertUtil.is_empty([1, 2, 3])

    def test_is_not_empty(self):
        """测试 is_not_empty 方法"""
        AssertUtil.is_not_empty("test")
        AssertUtil.is_not_empty([1, 2, 3])
        AssertUtil.is_not_empty({"a": 1})
        with self.assertRaises(AssertionError):
            AssertUtil.is_not_empty(None)
        with self.assertRaises(AssertionError):
            AssertUtil.is_not_empty("")

    def test_is_zero(self):
        """测试 is_zero 方法"""
        AssertUtil.is_zero(0)
        AssertUtil.is_zero(0.0)
        with self.assertRaises(AssertionError):
            AssertUtil.is_zero(1)
        with self.assertRaises(AssertionError):
            AssertUtil.is_zero(-1)

    def test_is_not_zero(self):
        """测试 is_not_zero 方法"""
        AssertUtil.is_not_zero(1)
        AssertUtil.is_not_zero(-1)
        AssertUtil.is_not_zero(0.5)
        with self.assertRaises(AssertionError):
            AssertUtil.is_not_zero(0)

    def test_is_positive(self):
        """测试 is_positive 方法"""
        AssertUtil.is_positive(1)
        AssertUtil.is_positive(0.5)
        with self.assertRaises(AssertionError):
            AssertUtil.is_positive(0)
        with self.assertRaises(AssertionError):
            AssertUtil.is_positive(-1)

    def test_is_negative(self):
        """测试 is_negative 方法"""
        AssertUtil.is_negative(-1)
        AssertUtil.is_negative(-0.5)
        with self.assertRaises(AssertionError):
            AssertUtil.is_negative(0)
        with self.assertRaises(AssertionError):
            AssertUtil.is_negative(1)

    def test_is_instance(self):
        """测试 is_instance 方法"""
        AssertUtil.is_instance(123, int)
        AssertUtil.is_instance("test", str)
        AssertUtil.is_instance([1, 2], list)
        with self.assertRaises(AssertionError):
            AssertUtil.is_instance(123, str)

    def test_is_not_instance(self):
        """测试 is_not_instance 方法"""
        AssertUtil.is_not_instance(123, str)
        AssertUtil.is_not_instance("test", int)
        with self.assertRaises(AssertionError):
            AssertUtil.is_not_instance(123, int)

    def test_contains(self):
        """测试 contains 方法"""
        AssertUtil.contains("hello world", "world")
        AssertUtil.contains([1, 2, 3], 2)
        AssertUtil.contains({"a": 1, "b": 2}, "a")
        with self.assertRaises(AssertionError):
            AssertUtil.contains("hello world", "test")
        with self.assertRaises(AssertionError):
            AssertUtil.contains([1, 2, 3], 4)

    def test_not_contains(self):
        """测试 not_contains 方法"""
        AssertUtil.not_contains("hello world", "test")
        AssertUtil.not_contains([1, 2, 3], 4)
        with self.assertRaises(AssertionError):
            AssertUtil.not_contains("hello world", "world")

    def test_is_subset(self):
        """测试 is_subset 方法"""
        AssertUtil.is_subset([1, 2], [1, 2, 3])
        AssertUtil.is_subset({1, 2}, {1, 2, 3})
        with self.assertRaises(AssertionError):
            AssertUtil.is_subset([1, 4], [1, 2, 3])

    def test_is_superset(self):
        """测试 is_superset 方法"""
        AssertUtil.is_superset([1, 2, 3], [1, 2])
        AssertUtil.is_superset({1, 2, 3}, {1, 2})
        with self.assertRaises(AssertionError):
            AssertUtil.is_superset([1, 2, 3], [1, 4])

    def test_matches(self):
        """测试 matches 方法"""
        AssertUtil.matches(r'^\d+$', '12345')
        AssertUtil.matches(r'^[a-zA-Z]+$', 'hello')
        with self.assertRaises(AssertionError):
            AssertUtil.matches(r'^\d+$', 'abc123')

    def test_not_matches(self):
        """测试 not_matches 方法"""
        AssertUtil.not_matches(r'^\d+$', 'abc123')
        AssertUtil.not_matches(r'^[a-zA-Z]+$', '123')
        with self.assertRaises(AssertionError):
            AssertUtil.not_matches(r'^\d+$', '12345')

    def test_raises(self):
        """测试 raises 方法"""
        def raise_value_error():
            raise ValueError("test error")

        def no_error():
            return 123

        AssertUtil.raises(ValueError, raise_value_error)
        with self.assertRaises(AssertionError):
            AssertUtil.raises(ValueError, no_error)

    def test_does_not_raise(self):
        """测试 does_not_raise 方法"""
        def no_error():
            return 123

        def raise_value_error():
            raise ValueError("test error")

        AssertUtil.does_not_raise(no_error)
        with self.assertRaises(AssertionError):
            AssertUtil.does_not_raise(raise_value_error)

    def test_greater(self):
        """测试 greater 方法"""
        AssertUtil.greater(5, 3)
        AssertUtil.greater(0.5, 0.3)
        with self.assertRaises(AssertionError):
            AssertUtil.greater(3, 5)
        with self.assertRaises(AssertionError):
            AssertUtil.greater(5, 5)

    def test_greater_or_equal(self):
        """测试 greater_or_equal 方法"""
        AssertUtil.greater_or_equal(5, 3)
        AssertUtil.greater_or_equal(5, 5)
        AssertUtil.greater_or_equal(0.5, 0.3)
        with self.assertRaises(AssertionError):
            AssertUtil.greater_or_equal(3, 5)

    def test_less(self):
        """测试 less 方法"""
        AssertUtil.less(3, 5)
        AssertUtil.less(0.3, 0.5)
        with self.assertRaises(AssertionError):
            AssertUtil.less(5, 3)
        with self.assertRaises(AssertionError):
            AssertUtil.less(5, 5)

    def test_less_or_equal(self):
        """测试 less_or_equal 方法"""
        AssertUtil.less_or_equal(3, 5)
        AssertUtil.less_or_equal(5, 5)
        AssertUtil.less_or_equal(0.3, 0.5)
        with self.assertRaises(AssertionError):
            AssertUtil.less_or_equal(5, 3)

    def test_between(self):
        """测试 between 方法"""
        AssertUtil.between(5, 1, 10)
        AssertUtil.between(1, 1, 10)
        AssertUtil.between(10, 1, 10)
        AssertUtil.between(0.5, 0.1, 1.0)
        with self.assertRaises(AssertionError):
            AssertUtil.between(0, 1, 10)
        with self.assertRaises(AssertionError):
            AssertUtil.between(11, 1, 10)

    def test_is_same(self):
        """测试 is_same 方法"""
        a = [1, 2, 3]
        b = a
        AssertUtil.is_same(a, b)
        c = [1, 2, 3]
        with self.assertRaises(AssertionError):
            AssertUtil.is_same(a, c)

    def test_is_not_same(self):
        """测试 is_not_same 方法"""
        a = [1, 2, 3]
        b = [1, 2, 3]
        AssertUtil.is_not_same(a, b)
        c = a
        with self.assertRaises(AssertionError):
            AssertUtil.is_not_same(a, c)

    def test_has_length(self):
        """测试 has_length 方法"""
        AssertUtil.has_length([1, 2, 3], 3)
        AssertUtil.has_length("hello", 5)
        AssertUtil.has_length({"a": 1, "b": 2}, 2)
        with self.assertRaises(AssertionError):
            AssertUtil.has_length([1, 2, 3], 2)
        with self.assertRaises(AssertionError):
            AssertUtil.has_length("hello", 4)

    def test_starts_with(self):
        """测试 starts_with 方法"""
        AssertUtil.starts_with("hello world", "hello")
        AssertUtil.starts_with("python", "py")
        with self.assertRaises(AssertionError):
            AssertUtil.starts_with("hello world", "world")

    def test_ends_with(self):
        """测试 ends_with 方法"""
        AssertUtil.ends_with("hello world", "world")
        AssertUtil.ends_with("python", "thon")
        with self.assertRaises(AssertionError):
            AssertUtil.ends_with("hello world", "hello")

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
