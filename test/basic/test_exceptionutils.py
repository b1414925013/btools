"""测试ExceptionUtils类"""
import unittest
from btools.core.basic.exceptionutils import ExceptionUtils


class TestExceptionUtils(unittest.TestCase):
    """测试ExceptionUtils类"""

    def test_get_stack_trace(self):
        """测试获取堆栈跟踪"""
        try:
            raise ValueError("Test error")
        except Exception as e:
            stack_trace = ExceptionUtils.get_stack_trace(e)
            self.assertIsInstance(stack_trace, str)
            self.assertIn("Test error", stack_trace)

    def test_get_exception_message(self):
        """测试获取异常消息"""
        try:
            raise ValueError("Test error")
        except Exception as e:
            message = ExceptionUtils.get_exception_message(e)
            self.assertEqual(message, "Test error")

    def test_get_exception_type(self):
        """测试获取异常类型"""
        try:
            raise ValueError("Test error")
        except Exception as e:
            exception_type = ExceptionUtils.get_exception_type(e)
            self.assertEqual(exception_type, "ValueError")

    def test_safe_call(self):
        """测试安全调用"""
        def test_func():
            return "Success"
        def error_func():
            raise ValueError("Test error")
        result = ExceptionUtils.safe_call(test_func)
        self.assertEqual(result, "Success")
        result = ExceptionUtils.safe_call(error_func)
        self.assertIsNone(result)

    def test_safe_call_with_default(self):
        """测试带默认值的安全调用"""
        def error_func():
            raise ValueError("Test error")
        result = ExceptionUtils.safe_call_with_default(error_func, "Default")
        self.assertEqual(result, "Default")


if __name__ == "__main__":
    unittest.main()