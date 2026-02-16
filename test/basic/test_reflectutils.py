"""测试ReflectUtils类"""
import unittest
from btools.core.basic.reflectutils import ReflectUtils


class TestReflectUtils(unittest.TestCase):
    """测试ReflectUtils类"""

    def test_get_class_name(self):
        """测试获取类名"""
        class TestClass:
            pass
        obj = TestClass()
        self.assertEqual(ReflectUtils.get_class_name(obj), "TestClass")

    def test_get_module_name(self):
        """测试获取模块名"""
        import os
        self.assertEqual(ReflectUtils.get_module_name(os), "os")

    def test_get_base_classes(self):
        """测试获取基类"""
        class BaseClass:
            pass
        class SubClass(BaseClass):
            pass
        result = ReflectUtils.get_base_classes(SubClass)
        self.assertIn(BaseClass, result)

    def test_instantiate(self):
        """测试实例化"""
        class TestClass:
            def __init__(self, name):
                self.name = name
        obj = ReflectUtils.instantiate(TestClass, "test")
        self.assertIsInstance(obj, TestClass)
        self.assertEqual(obj.name, "test")

    def test_call_method(self):
        """测试调用方法"""
        class TestClass:
            def test_method(self, a, b):
                return a + b
        obj = TestClass()
        result = ReflectUtils.call_method(obj, "test_method", 1, 2)
        self.assertEqual(result, 3)

    def test_get_attribute(self):
        """测试获取属性"""
        class TestClass:
            def __init__(self):
                self.name = "test"
        obj = TestClass()
        self.assertEqual(ReflectUtils.get_attribute(obj, "name"), "test")

    def test_set_attribute(self):
        """测试设置属性"""
        class TestClass:
            def __init__(self):
                self.name = "test"
        obj = TestClass()
        ReflectUtils.set_attribute(obj, "name", "new_test")
        self.assertEqual(obj.name, "new_test")

    def test_has_attribute(self):
        """测试是否有属性"""
        class TestClass:
            def __init__(self):
                self.name = "test"
        obj = TestClass()
        self.assertTrue(ReflectUtils.has_attribute(obj, "name"))
        self.assertFalse(ReflectUtils.has_attribute(obj, "age"))

    def test_is_instance(self):
        """测试是否为实例"""
        class TestClass:
            pass
        obj = TestClass()
        self.assertTrue(ReflectUtils.is_instance(obj, TestClass))

    def test_is_subclass(self):
        """测试是否为子类"""
        class BaseClass:
            pass
        class SubClass(BaseClass):
            pass
        self.assertTrue(ReflectUtils.is_subclass(SubClass, BaseClass))

    def test_get_type(self):
        """测试获取类型"""
        obj = "test"
        self.assertEqual(ReflectUtils.get_type(obj), str)

    def test_import_module(self):
        """测试导入模块"""
        module = ReflectUtils.import_module("os")
        self.assertIsNotNone(module)

    def test_is_function(self):
        """测试是否为函数"""
        def test_func():
            pass
        self.assertTrue(ReflectUtils.is_function(test_func))

    def test_is_method(self):
        """测试是否为方法"""
        class TestClass:
            def test_method(self):
                pass
        obj = TestClass()
        self.assertTrue(ReflectUtils.is_method(obj.test_method))

    def test_is_class(self):
        """测试是否为类"""
        class TestClass:
            pass
        self.assertTrue(ReflectUtils.is_class(TestClass))


if __name__ == "__main__":
    unittest.main()