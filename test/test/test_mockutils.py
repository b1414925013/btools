"""测试MockUtils类"""
import unittest
from btools.core.test.mockutils import MockUtils


class TestMockUtils(unittest.TestCase):
    """测试MockUtils类"""

    def test_create_mock(self):
        """测试创建Mock对象"""
        mock = MockUtils.create_mock()
        self.assertIsNotNone(mock)

    def test_mock_return_value(self):
        """测试Mock返回值"""
        mock = MockUtils.create_mock()
        mock.some_method.return_value = "test"
        self.assertEqual(mock.some_method(), "test")

    def test_mock_side_effect(self):
        """测试Mock副作用"""
        mock = MockUtils.create_mock()
        mock.some_method.side_effect = [1, 2, 3]
        self.assertEqual(mock.some_method(), 1)
        self.assertEqual(mock.some_method(), 2)
        self.assertEqual(mock.some_method(), 3)

    def test_reset_mock(self):
        """测试重置Mock"""
        mock = MockUtils.create_mock()
        mock.some_method()
        MockUtils.reset_mock(mock)
        self.assertFalse(mock.some_method.called)


if __name__ == "__main__":
    unittest.main()
