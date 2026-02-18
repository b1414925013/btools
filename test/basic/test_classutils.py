import unittest
import abc
from btools.core.basic.classutils import ClassUtils


class TestClassUtils(unittest.TestCase):
    """
    类工具类测试
    """

    def test_get_class_name(self):
        """
        测试获取类的名称
        """
        class TestClass:
            pass

        self.assertEqual(ClassUtils.get_class_name(TestClass), "TestClass")
        self.assertEqual(ClassUtils.get_class_name(int), "int")

    def test_get_package_name(self):
        """
        测试获取类所在的包名称
        """
        class TestClass:
            pass

        # 测试本地类（无包）
        package_name = ClassUtils.get_package_name(TestClass)
        self.assertIsInstance(package_name, str)

        # 测试内置类
        package_name = ClassUtils.get_package_name(int)
        self.assertIsInstance(package_name, str)

    def test_get_module_name(self):
        """
        测试获取类所在的模块名称
        """
        class TestClass:
            pass

        # 测试本地类
        module_name = ClassUtils.get_module_name(TestClass)
        self.assertIsInstance(module_name, str)

        # 测试内置类
        module_name = ClassUtils.get_module_name(int)
        self.assertEqual(module_name, "builtins")

    def test_get_full_class_name(self):
        """
        测试获取类的完整名称
        """
        class TestClass:
            pass

        # 测试本地类
        full_name = ClassUtils.get_full_class_name(TestClass)
        self.assertIsInstance(full_name, str)
        self.assertTrue("TestClass" in full_name)

        # 测试内置类
        full_name = ClassUtils.get_full_class_name(int)
        self.assertEqual(full_name, "builtins.int")

    def test_load_class(self):
        """
        测试加载类
        """
        # 测试加载内置类
        cls = ClassUtils.load_class("builtins.int")
        self.assertEqual(cls, int)

        # 测试加载不存在的类
        cls = ClassUtils.load_class("non.existent.Class")
        self.assertIsNone(cls)

    def test_is_abstract(self):
        """
        测试检查类是否为抽象类
        """
        class AbstractClass(metaclass=abc.ABCMeta):
            @abc.abstractmethod
            def method(self):
                pass

        class ConcreteClass:
            pass

        self.assertTrue(ClassUtils.is_abstract(AbstractClass))
        self.assertFalse(ClassUtils.is_abstract(ConcreteClass))
        self.assertFalse(ClassUtils.is_abstract(int))

    def test_is_concrete(self):
        """
        测试检查类是否为具体类
        """
        class AbstractClass(metaclass=abc.ABCMeta):
            @abc.abstractmethod
            def method(self):
                pass

        class ConcreteClass:
            pass

        self.assertFalse(ClassUtils.is_concrete(AbstractClass))
        self.assertTrue(ClassUtils.is_concrete(ConcreteClass))
        self.assertTrue(ClassUtils.is_concrete(int))

    def test_get_super_classes(self):
        """
        测试获取类的所有父类
        """
        class BaseClass:
            pass

        class SubClass(BaseClass):
            pass

        class SubSubClass(SubClass):
            pass

        super_classes = ClassUtils.get_super_classes(SubSubClass)
        self.assertEqual(len(super_classes), 2)
        self.assertIn(SubClass, super_classes)
        self.assertIn(BaseClass, super_classes)

    def test_get_constructors(self):
        """
        测试获取类的所有构造器
        """
        class TestClass:
            def __init__(self):
                pass

        constructors = ClassUtils.get_constructors(TestClass)
        self.assertIsInstance(constructors, list)

    def test_get_methods(self):
        """
        测试获取类的所有方法
        """
        class TestClass:
            def method1(self):
                pass

            def method2(self):
                pass

        methods = ClassUtils.get_methods(TestClass)
        self.assertIsInstance(methods, list)

    def test_get_fields(self):
        """
        测试获取类的所有字段
        """
        class TestClass:
            field1 = "value1"
            field2 = "value2"

            def method(self):
                pass

        fields = ClassUtils.get_fields(TestClass)
        self.assertIsInstance(fields, list)

    def test_get_all_members(self):
        """
        测试获取类的所有成员
        """
        class TestClass:
            field = "value"

            def method(self):
                pass

        members = ClassUtils.get_all_members(TestClass)
        self.assertIsInstance(members, dict)
        self.assertIn('field', members)
        self.assertIn('method', members)

    def test_instantiate(self):
        """
        测试实例化类
        """
        class TestClass:
            def __init__(self, value):
                self.value = value

        # 测试成功实例化
        obj = ClassUtils.instantiate(TestClass, "test")
        self.assertIsInstance(obj, TestClass)
        self.assertEqual(obj.value, "test")

        # 测试实例化失败（参数错误）
        obj = ClassUtils.instantiate(TestClass)
        self.assertIsNone(obj)

    def test_is_subclass(self):
        """
        测试检查类是否为指定类的子类
        """
        class BaseClass:
            pass

        class SubClass(BaseClass):
            pass

        self.assertTrue(ClassUtils.is_subclass(SubClass, BaseClass))
        self.assertFalse(ClassUtils.is_subclass(BaseClass, SubClass))
        self.assertTrue(ClassUtils.is_subclass(int, object))

    def test_implements_interface(self):
        """
        测试检查类是否实现了指定的接口
        """
        class Interface(metaclass=abc.ABCMeta):
            @abc.abstractmethod
            def method(self):
                pass

        class ImplementingClass(Interface):
            def method(self):
                pass

        self.assertTrue(ClassUtils.implements_interface(ImplementingClass, Interface))
        self.assertFalse(ClassUtils.implements_interface(int, Interface))

    def test_get_class_path(self):
        """
        测试获取类的路径
        """
        class TestClass:
            pass

        # 测试本地类
        path = ClassUtils.get_class_path(TestClass)
        self.assertIsInstance(path, (str, type(None)))

        # 测试内置类
        path = ClassUtils.get_class_path(int)
        self.assertIsNone(path)

    def test_is_inner_class(self):
        """
        测试检查类是否为内部类
        """
        class OuterClass:
            class InnerClass:
                pass

        class TopLevelClass:
            pass

        self.assertTrue(ClassUtils.is_inner_class(OuterClass.InnerClass))
        self.assertFalse(ClassUtils.is_inner_class(TopLevelClass))

    def test_get_outer_class(self):
        """
        测试获取内部类的外部类
        """
        class OuterClass:
            class InnerClass:
                pass

        outer_class = ClassUtils.get_outer_class(OuterClass.InnerClass)
        self.assertEqual(outer_class, OuterClass)

        # 测试非内部类
        outer_class = ClassUtils.get_outer_class(OuterClass)
        self.assertIsNone(outer_class)

    def test_get_class_annotations(self):
        """
        测试获取类的注解
        """
        class TestClass:
            field: int
            name: str

        annotations = ClassUtils.get_class_annotations(TestClass)
        self.assertIsInstance(annotations, dict)
        self.assertIn('field', annotations)
        self.assertIn('name', annotations)

    def test_get_method_annotations(self):
        """
        测试获取类方法的注解
        """
        class TestClass:
            def method(self, x: int, y: str) -> bool:
                return True

        annotations = ClassUtils.get_method_annotations(TestClass, "method")
        self.assertIsInstance(annotations, dict)

    def test_get_field_annotations(self):
        """
        测试获取类字段的注解
        """
        class TestClass:
            field: int
            name: str

        annotations = ClassUtils.get_field_annotations(TestClass, "field")
        self.assertIsInstance(annotations, dict)
        self.assertIn('field', annotations)

    def test_is_final(self):
        """
        测试检查类是否为最终类
        """
        class FinalClass:
            __final__ = True

        class NonFinalClass:
            pass

        self.assertTrue(ClassUtils.is_final(FinalClass))
        self.assertFalse(ClassUtils.is_final(NonFinalClass))

    def test_is_static(self):
        """
        测试检查类成员是否为静态成员
        """
        class TestClass:
            static_field = "static"
            
            def instance_method(self):
                pass

        # 测试静态字段
        self.assertTrue(ClassUtils.is_static(TestClass, "static_field"))
        # 测试实例方法
        self.assertFalse(ClassUtils.is_static(TestClass, "instance_method"))
        # 测试不存在的成员
        self.assertFalse(ClassUtils.is_static(TestClass, "non_existent"))

    def test_is_private(self):
        """
        测试检查类成员是否为私有成员
        """
        class TestClass:
            __private_field = "private"
            _protected_field = "protected"
            public_field = "public"

        self.assertTrue(ClassUtils.is_private(TestClass, "__private_field"))
        self.assertFalse(ClassUtils.is_private(TestClass, "_protected_field"))
        self.assertFalse(ClassUtils.is_private(TestClass, "public_field"))

    def test_is_protected(self):
        """
        测试检查类成员是否为保护成员
        """
        class TestClass:
            __private_field = "private"
            _protected_field = "protected"
            public_field = "public"

        self.assertFalse(ClassUtils.is_protected(TestClass, "__private_field"))
        self.assertTrue(ClassUtils.is_protected(TestClass, "_protected_field"))
        self.assertFalse(ClassUtils.is_protected(TestClass, "public_field"))

    def test_get_class_hierarchy(self):
        """
        测试获取类的继承层次结构
        """
        class BaseClass:
            pass

        class SubClass(BaseClass):
            pass

        hierarchy = ClassUtils.get_class_hierarchy(SubClass)
        self.assertIsInstance(hierarchy, list)
        self.assertEqual(len(hierarchy), 3)  # SubClass, BaseClass, object
        self.assertEqual(hierarchy[0], SubClass)
        self.assertEqual(hierarchy[1], BaseClass)
        self.assertEqual(hierarchy[2], object)

    def test_get_common_super_class(self):
        """
        测试获取多个类的共同父类
        """
        class BaseClass:
            pass

        class SubClass1(BaseClass):
            pass

        class SubClass2(BaseClass):
            pass

        # 测试有共同父类的情况
        common = ClassUtils.get_common_super_class([SubClass1, SubClass2])
        self.assertEqual(common, BaseClass)

        # 测试没有共同父类的情况（除了object）
        common = ClassUtils.get_common_super_class([int, str])
        self.assertEqual(common, object)

        # 测试空列表
        common = ClassUtils.get_common_super_class([])
        self.assertIsNone(common)


if __name__ == '__main__':
    unittest.main()
