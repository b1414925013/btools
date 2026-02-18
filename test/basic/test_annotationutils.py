#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AnnotationUtil 测试文件
"""
import unittest
from btools.core.basic import AnnotationUtil


# 测试用的注解类
class TestAnnotation:
    """测试注解类"""
    pass


# 测试用的类
class TestClass:
    """测试类"""
    
    # 类属性注解
    name: str
    age: int
    
    def __init__(self, name: str, age: int):
        """构造方法"""
        self.name = name
        self.age = age
    
    def get_name(self) -> str:
        """获取名称"""
        return self.name
    
    def set_name(self, name: str) -> None:
        """设置名称"""
        self.name = name
    
    def get_age(self) -> int:
        """获取年龄"""
        return self.age
    
    def set_age(self, age: int) -> None:
        """设置年龄"""
        self.age = age
    
    def get_info(self, prefix: str = "Info") -> str:
        """获取信息"""
        return f"{prefix}: {self.name}, {self.age}"


class TestAnnotationUtil(unittest.TestCase):
    """
    AnnotationUtil 测试类
    """

    def test_get_class_annotations(self):
        """
        测试获取类上的所有注解
        """
        annotations = AnnotationUtil.get_class_annotations(TestClass)
        self.assertIsInstance(annotations, dict)
        # 检查是否包含类属性注解
        self.assertIn("name", annotations)
        self.assertIn("age", annotations)

    def test_get_method_annotations(self):
        """
        测试获取方法上的所有注解
        """
        # 测试 get_name 方法
        get_name_method = TestClass.get_name
        annotations = AnnotationUtil.get_method_annotations(get_name_method)
        self.assertIsInstance(annotations, dict)
        self.assertIn("return", annotations)
        self.assertEqual(annotations["return"], str)

        # 测试 set_name 方法
        set_name_method = TestClass.set_name
        annotations = AnnotationUtil.get_method_annotations(set_name_method)
        self.assertIsInstance(annotations, dict)
        self.assertIn("name", annotations)
        self.assertEqual(annotations["name"], str)
        self.assertIn("return", annotations)
        self.assertEqual(annotations["return"], None)

    def test_get_param_annotations(self):
        """
        测试获取方法参数的注解
        """
        # 测试 set_name 方法
        set_name_method = TestClass.set_name
        param_annotations = AnnotationUtil.get_param_annotations(set_name_method)
        self.assertIsInstance(param_annotations, dict)
        self.assertIn("name", param_annotations)
        self.assertEqual(param_annotations["name"], str)
        # 确保不包含返回值注解
        self.assertNotIn("return", param_annotations)

        # 测试 get_info 方法
        get_info_method = TestClass.get_info
        param_annotations = AnnotationUtil.get_param_annotations(get_info_method)
        self.assertIsInstance(param_annotations, dict)
        self.assertIn("prefix", param_annotations)
        self.assertEqual(param_annotations["prefix"], str)

    def test_get_return_annotation(self):
        """
        测试获取方法返回值的注解
        """
        # 测试 get_name 方法
        get_name_method = TestClass.get_name
        return_annotation = AnnotationUtil.get_return_annotation(get_name_method)
        self.assertEqual(return_annotation, str)

        # 测试 set_name 方法
        set_name_method = TestClass.set_name
        return_annotation = AnnotationUtil.get_return_annotation(set_name_method)
        self.assertEqual(return_annotation, None)

    def test_get_field_annotations(self):
        """
        测试获取类所有属性的注解
        """
        field_annotations = AnnotationUtil.get_field_annotations(TestClass)
        self.assertIsInstance(field_annotations, dict)
        # 检查是否包含类属性注解
        self.assertIn("name", field_annotations)
        self.assertIn("age", field_annotations)

    def test_has_annotation(self):
        """
        测试检查对象是否有指定名称的注解
        """
        # 测试 get_name 方法
        get_name_method = TestClass.get_name
        # 检查是否有 return 注解
        has_return_annotation = AnnotationUtil.has_annotation(get_name_method, "return")
        self.assertTrue(has_return_annotation)
        # 检查是否有不存在的注解
        has_nonexistent_annotation = AnnotationUtil.has_annotation(get_name_method, "nonexistent")
        self.assertFalse(has_nonexistent_annotation)

    def test_get_annotation(self):
        """
        测试获取对象上指定名称的注解
        """
        # 测试 get_name 方法
        get_name_method = TestClass.get_name
        # 获取 return 注解
        return_annotation = AnnotationUtil.get_annotation(get_name_method, "return")
        self.assertEqual(return_annotation, str)
        # 获取不存在的注解，使用默认值
        nonexistent_annotation = AnnotationUtil.get_annotation(get_name_method, "nonexistent", "default")
        self.assertEqual(nonexistent_annotation, "default")

    def test_get_all_annotations(self):
        """
        测试获取对象上的所有注解
        """
        # 测试 get_name 方法
        get_name_method = TestClass.get_name
        annotations = AnnotationUtil.get_all_annotations(get_name_method)
        self.assertIsInstance(annotations, dict)
        self.assertIn("return", annotations)

    def test_is_annotation(self):
        """
        测试检查对象是否为注解
        """
        # 测试 TestAnnotation 类
        is_annotation = AnnotationUtil.is_annotation(TestAnnotation)
        # 由于 TestAnnotation 是可调用的且有 __annotations__ 属性，应该返回 True
        self.assertTrue(is_annotation)

        # 测试普通函数
        def test_function():
            pass
        is_annotation = AnnotationUtil.is_annotation(test_function)
        self.assertTrue(is_annotation)

        # 测试普通对象
        test_obj = {}
        is_annotation = AnnotationUtil.is_annotation(test_obj)
        self.assertFalse(is_annotation)

    def test_get_annotations_by_type(self):
        """
        测试获取对象上指定类型的注解
        """
        # 测试 get_name 方法
        get_name_method = TestClass.get_name
        str_annotations = AnnotationUtil.get_annotations_by_type(get_name_method, type)
        self.assertIsInstance(str_annotations, list)
        self.assertIn(str, str_annotations)

    def test_get_annotated_methods(self):
        """
        测试获取类中带有指定注解的方法名列表
        """
        # 获取带有 return 注解的方法
        annotated_methods = AnnotationUtil.get_annotated_methods(TestClass, "return")
        self.assertIsInstance(annotated_methods, list)
        # 检查是否包含 get_name, get_age, get_info 方法
        self.assertIn("get_name", annotated_methods)
        self.assertIn("get_age", annotated_methods)
        self.assertIn("get_info", annotated_methods)

    def test_get_annotated_fields(self):
        """
        测试获取类中带有指定注解的属性名列表
        """
        # 获取带有 str 注解的属性
        annotated_fields = AnnotationUtil.get_annotated_fields(TestClass, str)
        self.assertIsInstance(annotated_fields, list)
        self.assertIn("name", annotated_fields)

        # 获取带有 int 注解的属性
        annotated_fields = AnnotationUtil.get_annotated_fields(TestClass, int)
        self.assertIsInstance(annotated_fields, list)
        self.assertIn("age", annotated_fields)

    def test_get_method_signature_with_annotations(self):
        """
        测试获取带有注解的方法签名
        """
        # 测试 get_info 方法
        get_info_method = TestClass.get_info
        signature = AnnotationUtil.get_method_signature_with_annotations(get_info_method)
        self.assertIsInstance(signature, str)
        # 检查签名是否包含参数注解和返回值注解
        self.assertIn("prefix: str", signature)
        self.assertIn("= Info", signature)
        self.assertIn("-> str", signature)

    def test_merge_annotations(self):
        """
        测试将源对象的注解合并到目标对象
        """
        # 创建测试函数
        def target_function():
            pass

        def source_function(name: str, age: int) -> str:
            pass

        # 合并注解
        AnnotationUtil.merge_annotations(target_function, source_function)

        # 检查目标函数是否包含源函数的注解
        target_annotations = AnnotationUtil.get_all_annotations(target_function)
        self.assertIn("name", target_annotations)
        self.assertIn("age", target_annotations)
        self.assertIn("return", target_annotations)

    def test_copy_annotations(self):
        """
        测试复制源对象的注解到目标对象
        """
        # 创建测试函数
        def target_function():
            pass

        def source_function(name: str, age: int) -> str:
            pass

        # 复制注解
        AnnotationUtil.copy_annotations(source_function, target_function)

        # 检查目标函数是否包含源函数的注解
        target_annotations = AnnotationUtil.get_all_annotations(target_function)
        source_annotations = AnnotationUtil.get_all_annotations(source_function)
        self.assertEqual(target_annotations, source_annotations)


if __name__ == '__main__':
    unittest.main()