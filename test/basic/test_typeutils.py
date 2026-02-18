import unittest
from typing import Any, List, Dict, Tuple, Optional, Union
from btools.core.basic.typeutils import TypeUtils


class TestTypeUtils(unittest.TestCase):
    """
    类型工具类测试
    """

    def test_is_type(self):
        """
        测试检查对象是否为指定类型
        """
        self.assertTrue(TypeUtils.is_type(1, int))
        self.assertTrue(TypeUtils.is_type("test", str))
        self.assertTrue(TypeUtils.is_type([], list))
        self.assertFalse(TypeUtils.is_type(1, str))
        self.assertFalse(TypeUtils.is_type("test", int))

    def test_is_none(self):
        """
        测试检查对象是否为None
        """
        self.assertTrue(TypeUtils.is_none(None))
        self.assertFalse(TypeUtils.is_none(1))
        self.assertFalse(TypeUtils.is_none(""))
        self.assertFalse(TypeUtils.is_none([]))

    def test_is_not_none(self):
        """
        测试检查对象是否不为None
        """
        self.assertFalse(TypeUtils.is_not_none(None))
        self.assertTrue(TypeUtils.is_not_none(1))
        self.assertTrue(TypeUtils.is_not_none(""))
        self.assertTrue(TypeUtils.is_not_none([]))

    def test_is_empty(self):
        """
        测试检查对象是否为空
        """
        self.assertTrue(TypeUtils.is_empty(None))
        self.assertTrue(TypeUtils.is_empty(""))
        self.assertTrue(TypeUtils.is_empty([]))
        self.assertTrue(TypeUtils.is_empty({}))
        self.assertTrue(TypeUtils.is_empty(()))
        self.assertTrue(TypeUtils.is_empty(set()))
        self.assertFalse(TypeUtils.is_empty(1))
        self.assertFalse(TypeUtils.is_empty("test"))
        self.assertFalse(TypeUtils.is_empty([1]))
        self.assertFalse(TypeUtils.is_empty({"a": 1}))

    def test_is_not_empty(self):
        """
        测试检查对象是否不为空
        """
        self.assertFalse(TypeUtils.is_not_empty(None))
        self.assertFalse(TypeUtils.is_not_empty(""))
        self.assertFalse(TypeUtils.is_not_empty([]))
        self.assertFalse(TypeUtils.is_not_empty({}))
        self.assertFalse(TypeUtils.is_not_empty(()))
        self.assertFalse(TypeUtils.is_not_empty(set()))
        self.assertTrue(TypeUtils.is_not_empty(1))
        self.assertTrue(TypeUtils.is_not_empty("test"))
        self.assertTrue(TypeUtils.is_not_empty([1]))
        self.assertTrue(TypeUtils.is_not_empty({"a": 1}))

    def test_cast(self):
        """
        测试将对象转换为指定类型
        """
        self.assertEqual(TypeUtils.cast("1", int), 1)
        self.assertEqual(TypeUtils.cast(1, str), "1")
        self.assertEqual(TypeUtils.cast(None, int), None)
        # 转换失败时返回原对象
        self.assertEqual(TypeUtils.cast("test", int), "test")

    def test_safe_cast(self):
        """
        测试安全地将对象转换为指定类型
        """
        self.assertEqual(TypeUtils.safe_cast("1", int), 1)
        self.assertEqual(TypeUtils.safe_cast(1, str), "1")
        self.assertEqual(TypeUtils.safe_cast(None, int, 0), 0)
        # 转换失败时返回默认值
        self.assertEqual(TypeUtils.safe_cast("test", int, 0), 0)

    def test_get_type(self):
        """
        测试获取对象的类型
        """
        self.assertEqual(TypeUtils.get_type(1), int)
        self.assertEqual(TypeUtils.get_type("test"), str)
        self.assertEqual(TypeUtils.get_type([]), list)

    def test_get_type_name(self):
        """
        测试获取对象的类型名称
        """
        self.assertEqual(TypeUtils.get_type_name(1), "int")
        self.assertEqual(TypeUtils.get_type_name("test"), "str")
        self.assertEqual(TypeUtils.get_type_name([]), "list")
        self.assertEqual(TypeUtils.get_type_name(None), "NoneType")

    def test_get_full_type_name(self):
        """
        测试获取对象的完整类型名称
        """
        self.assertEqual(TypeUtils.get_full_type_name(1), "int")
        self.assertEqual(TypeUtils.get_full_type_name("test"), "str")
        self.assertEqual(TypeUtils.get_full_type_name([]), "list")
        self.assertEqual(TypeUtils.get_full_type_name(None), "NoneType")

    def test_is_generic_type(self):
        """
        测试检查类型是否为泛型类型
        """
        self.assertTrue(TypeUtils.is_generic_type(List[int]))
        self.assertTrue(TypeUtils.is_generic_type(Dict[str, int]))
        self.assertTrue(TypeUtils.is_generic_type(Tuple[int, str]))
        self.assertFalse(TypeUtils.is_generic_type(int))
        self.assertFalse(TypeUtils.is_generic_type(str))
        self.assertFalse(TypeUtils.is_generic_type(list))

    def test_get_generic_type(self):
        """
        测试获取泛型类型的原始类型
        """
        self.assertEqual(TypeUtils.get_generic_type(List[int]), list)
        self.assertEqual(TypeUtils.get_generic_type(Dict[str, int]), dict)
        self.assertEqual(TypeUtils.get_generic_type(Tuple[int, str]), tuple)
        self.assertEqual(TypeUtils.get_generic_type(int), int)

    def test_get_type_args(self):
        """
        测试获取类型的类型参数
        """
        self.assertEqual(TypeUtils.get_type_args(List[int]), (int,))
        self.assertEqual(TypeUtils.get_type_args(Dict[str, int]), (str, int))
        self.assertEqual(TypeUtils.get_type_args(Tuple[int, str]), (int, str))
        self.assertEqual(TypeUtils.get_type_args(int), ())

    def test_is_optional_type(self):
        """
        测试检查类型是否为Optional类型
        """
        self.assertTrue(TypeUtils.is_optional_type(Optional[int]))
        self.assertTrue(TypeUtils.is_optional_type(Optional[str]))
        self.assertFalse(TypeUtils.is_optional_type(int))
        self.assertFalse(TypeUtils.is_optional_type(str))
        self.assertFalse(TypeUtils.is_optional_type(List[int]))

    def test_get_optional_type(self):
        """
        测试获取Optional类型的实际类型
        """
        self.assertEqual(TypeUtils.get_optional_type(Optional[int]), int)
        self.assertEqual(TypeUtils.get_optional_type(Optional[str]), str)
        self.assertEqual(TypeUtils.get_optional_type(int), int)

    def test_is_union_type(self):
        """
        测试检查类型是否为Union类型
        """
        self.assertTrue(TypeUtils.is_union_type(Union[int, str]))
        self.assertTrue(TypeUtils.is_union_type(Optional[int]))  # Optional是Union的特例
        self.assertFalse(TypeUtils.is_union_type(int))
        self.assertFalse(TypeUtils.is_union_type(str))

    def test_get_union_types(self):
        """
        测试获取Union类型的所有类型
        """
        types = TypeUtils.get_union_types(Union[int, str])
        self.assertEqual(len(types), 2)
        self.assertIn(int, types)
        self.assertIn(str, types)

        types = TypeUtils.get_union_types(Optional[int])
        self.assertEqual(len(types), 2)
        self.assertIn(int, types)
        self.assertIn(type(None), types)

        self.assertEqual(TypeUtils.get_union_types(int), (int,))

    def test_is_list_type(self):
        """
        测试检查类型是否为List类型
        """
        self.assertTrue(TypeUtils.is_list_type(List[int]))
        self.assertTrue(TypeUtils.is_list_type(List[str]))
        self.assertFalse(TypeUtils.is_list_type(int))
        self.assertFalse(TypeUtils.is_list_type(str))
        self.assertFalse(TypeUtils.is_list_type(dict))

    def test_get_list_element_type(self):
        """
        测试获取List类型的元素类型
        """
        self.assertEqual(TypeUtils.get_list_element_type(List[int]), int)
        self.assertEqual(TypeUtils.get_list_element_type(List[str]), str)
        self.assertEqual(TypeUtils.get_list_element_type(list), Any)

    def test_is_dict_type(self):
        """
        测试检查类型是否为Dict类型
        """
        self.assertTrue(TypeUtils.is_dict_type(Dict[str, int]))
        self.assertTrue(TypeUtils.is_dict_type(Dict[int, str]))
        self.assertFalse(TypeUtils.is_dict_type(int))
        self.assertFalse(TypeUtils.is_dict_type(str))
        self.assertFalse(TypeUtils.is_dict_type(list))

    def test_get_dict_key_type(self):
        """
        测试获取Dict类型的键类型
        """
        self.assertEqual(TypeUtils.get_dict_key_type(Dict[str, int]), str)
        self.assertEqual(TypeUtils.get_dict_key_type(Dict[int, str]), int)
        self.assertEqual(TypeUtils.get_dict_key_type(dict), Any)

    def test_get_dict_value_type(self):
        """
        测试获取Dict类型的值类型
        """
        self.assertEqual(TypeUtils.get_dict_value_type(Dict[str, int]), int)
        self.assertEqual(TypeUtils.get_dict_value_type(Dict[int, str]), str)
        self.assertEqual(TypeUtils.get_dict_value_type(dict), Any)

    def test_is_tuple_type(self):
        """
        测试检查类型是否为Tuple类型
        """
        self.assertTrue(TypeUtils.is_tuple_type(Tuple[int, str]))
        self.assertTrue(TypeUtils.is_tuple_type(Tuple[str, int]))
        self.assertFalse(TypeUtils.is_tuple_type(int))
        self.assertFalse(TypeUtils.is_tuple_type(str))
        self.assertFalse(TypeUtils.is_tuple_type(list))

    def test_get_tuple_element_types(self):
        """
        测试获取Tuple类型的元素类型
        """
        self.assertEqual(TypeUtils.get_tuple_element_types(Tuple[int, str]), (int, str))
        self.assertEqual(TypeUtils.get_tuple_element_types(Tuple[str, int]), (str, int))
        self.assertEqual(TypeUtils.get_tuple_element_types(tuple), ())

    def test_is_callable_type(self):
        """
        测试检查对象是否为可调用对象
        """
        def test_func():
            pass

        class TestClass:
            def __call__(self):
                pass

        self.assertTrue(TypeUtils.is_callable_type(test_func))
        self.assertTrue(TypeUtils.is_callable_type(TestClass()))
        self.assertFalse(TypeUtils.is_callable_type(1))
        self.assertFalse(TypeUtils.is_callable_type("test"))

    def test_is_function(self):
        """
        测试检查对象是否为函数
        """
        def test_func():
            pass

        class TestClass:
            def method(self):
                pass

        self.assertTrue(TypeUtils.is_function(test_func))
        # 在Python中，类中定义的方法在未绑定到实例时是函数类型
        # 绑定到实例后才是方法类型
        obj = TestClass()
        self.assertTrue(TypeUtils.is_function(TestClass.method))
        self.assertFalse(TypeUtils.is_function(obj.method))
        self.assertFalse(TypeUtils.is_function(1))
        self.assertFalse(TypeUtils.is_function("test"))

    def test_is_method(self):
        """
        测试检查对象是否为方法
        """
        class TestClass:
            def method(self):
                pass

        def test_func():
            pass

        obj = TestClass()
        self.assertTrue(TypeUtils.is_method(obj.method))
        self.assertFalse(TypeUtils.is_method(test_func))
        self.assertFalse(TypeUtils.is_method(1))
        self.assertFalse(TypeUtils.is_method("test"))

    def test_is_class(self):
        """
        测试检查对象是否为类
        """
        class TestClass:
            pass

        self.assertTrue(TypeUtils.is_class(TestClass))
        self.assertFalse(TypeUtils.is_class(TestClass()))
        self.assertFalse(TypeUtils.is_class(1))
        self.assertFalse(TypeUtils.is_class("test"))

    def test_is_instance(self):
        """
        测试检查对象是否为指定类型的实例
        """
        class TestClass:
            pass

        obj = TestClass()
        self.assertTrue(TypeUtils.is_instance(obj, TestClass))
        self.assertTrue(TypeUtils.is_instance(1, int))
        self.assertTrue(TypeUtils.is_instance("test", str))
        self.assertFalse(TypeUtils.is_instance(1, str))
        self.assertFalse(TypeUtils.is_instance("test", int))

    def test_is_subclass(self):
        """
        测试检查类是否为指定类的子类
        """
        class BaseClass:
            pass

        class SubClass(BaseClass):
            pass

        self.assertTrue(TypeUtils.is_subclass(SubClass, BaseClass))
        self.assertTrue(TypeUtils.is_subclass(int, object))
        self.assertTrue(TypeUtils.is_subclass(str, object))
        self.assertFalse(TypeUtils.is_subclass(BaseClass, SubClass))
        self.assertFalse(TypeUtils.is_subclass(int, str))

    def test_get_super_classes(self):
        """
        测试获取类的所有父类
        """
        class BaseClass:
            pass

        class SubClass(BaseClass):
            pass

        super_classes = TypeUtils.get_super_classes(SubClass)
        self.assertEqual(len(super_classes), 2)  # BaseClass 和 object
        self.assertIn(BaseClass, super_classes)
        self.assertIn(object, super_classes)

    def test_get_class_annotations(self):
        """
        测试获取类的注解
        """
        class TestClass:
            a: int
            b: str

        annotations = TypeUtils.get_class_annotations(TestClass)
        self.assertEqual(len(annotations), 2)
        self.assertEqual(annotations["a"], int)
        self.assertEqual(annotations["b"], str)

    def test_get_function_annotations(self):
        """
        测试获取函数的注解
        """
        def test_func(a: int, b: str) -> bool:
            return True

        annotations = TypeUtils.get_function_annotations(test_func)
        self.assertEqual(len(annotations), 3)  # a, b, return
        self.assertEqual(annotations["a"], int)
        self.assertEqual(annotations["b"], str)
        self.assertEqual(annotations["return"], bool)

    def test_get_module_name(self):
        """
        测试获取对象所在的模块名称
        """
        import os
        # 在Windows系统上，os.path实际上是ntpath的别名
        module_name = TypeUtils.get_module_name(os.path.join)
        self.assertTrue(module_name in ["os.path", "ntpath"])
        self.assertEqual(TypeUtils.get_module_name(1), "")
        self.assertEqual(TypeUtils.get_module_name(None), "")

    def test_get_qualified_name(self):
        """
        测试获取对象的限定名称
        """
        def test_func():
            pass

        class TestClass:
            def method(self):
                pass

        # 在方法内部定义的函数和类会包含完整的限定名称
        func_name = TypeUtils.get_qualified_name(test_func)
        self.assertTrue("test_func" in func_name)
        
        method_name = TypeUtils.get_qualified_name(TestClass.method)
        self.assertTrue("TestClass.method" in method_name)
        
        self.assertEqual(TypeUtils.get_qualified_name(1), "1")
        self.assertEqual(TypeUtils.get_qualified_name(None), "")

    def test_is_builtin_type(self):
        """
        测试检查类型是否为内置类型
        """
        self.assertTrue(TypeUtils.is_builtin_type(int))
        self.assertTrue(TypeUtils.is_builtin_type(str))
        self.assertTrue(TypeUtils.is_builtin_type(list))
        self.assertTrue(TypeUtils.is_builtin_type(dict))

        class TestClass:
            pass

        self.assertFalse(TypeUtils.is_builtin_type(TestClass))

    def test_is_custom_type(self):
        """
        测试检查类型是否为自定义类型
        """
        class TestClass:
            pass

        self.assertTrue(TypeUtils.is_custom_type(TestClass))
        self.assertFalse(TypeUtils.is_custom_type(int))
        self.assertFalse(TypeUtils.is_custom_type(str))
        self.assertFalse(TypeUtils.is_custom_type(list))


if __name__ == '__main__':
    unittest.main()
