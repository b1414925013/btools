#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
注解工具类

提供注解相关的操作功能，包括获取类、方法、属性上的注解，检查是否存在某个注解等
"""
import inspect
from typing import Any, Dict, List, Optional, Type, Union, Set


class AnnotationUtil:
    """
    注解工具类
    """

    @staticmethod
    def get_class_annotations(cls: Type[Any]) -> Dict[str, Any]:
        """
        获取类上的所有注解

        Args:
            cls: 类

        Returns:
            Dict[str, Any]: 注解名称到注解值的映射
        """
        return dict(cls.__annotations__) if hasattr(cls, "__annotations__") else {}

    @staticmethod
    def get_method_annotations(method: Any) -> Dict[str, Any]:
        """
        获取方法上的所有注解

        Args:
            method: 方法

        Returns:
            Dict[str, Any]: 注解名称到注解值的映射
        """
        return dict(method.__annotations__) if hasattr(method, "__annotations__") else {}

    @staticmethod
    def get_param_annotations(method: Any) -> Dict[str, Any]:
        """
        获取方法参数的注解

        Args:
            method: 方法

        Returns:
            Dict[str, Any]: 参数名到注解值的映射
        """
        annotations = AnnotationUtil.get_method_annotations(method)
        # 排除返回值注解（如果存在）
        if "return" in annotations:
            annotations = {k: v for k, v in annotations.items() if k != "return"}
        return annotations

    @staticmethod
    def get_return_annotation(method: Any) -> Optional[Any]:
        """
        获取方法返回值的注解

        Args:
            method: 方法

        Returns:
            Optional[Any]: 返回值注解
        """
        annotations = AnnotationUtil.get_method_annotations(method)
        return annotations.get("return")

    @staticmethod
    def get_field_annotations(cls: Type[Any]) -> Dict[str, Dict[str, Any]]:
        """
        获取类所有属性的注解

        Args:
            cls: 类

        Returns:
            Dict[str, Dict[str, Any]]: 属性名到注解的映射
        """
        fields = {}
        
        # 遍历类的所有成员
        for name, member in inspect.getmembers(cls):
            # 跳过特殊成员
            if name.startswith("__") and name.endswith("__"):
                continue
            
            # 检查是否为属性
            if hasattr(member, "__annotations__"):
                fields[name] = dict(member.__annotations__)
            elif hasattr(cls, "__annotations__") and name in cls.__annotations__:
                fields[name] = cls.__annotations__[name]
        
        return fields

    @staticmethod
    def has_annotation(obj: Any, annotation_name: str) -> bool:
        """
        检查对象是否有指定名称的注解

        Args:
            obj: 对象（类、方法、函数）
            annotation_name: 注解名称

        Returns:
            bool: 是否有指定注解
        """
        return hasattr(obj, "__annotations__") and annotation_name in obj.__annotations__

    @staticmethod
    def get_annotation(obj: Any, annotation_name: str, default: Optional[Any] = None) -> Optional[Any]:
        """
        获取对象上指定名称的注解

        Args:
            obj: 对象（类、方法、函数）
            annotation_name: 注解名称
            default: 默认值

        Returns:
            Optional[Any]: 注解值，不存在返回默认值
        """
        if hasattr(obj, "__annotations__") and annotation_name in obj.__annotations__:
            return obj.__annotations__[annotation_name]
        return default

    @staticmethod
    def get_all_annotations(obj: Any) -> Dict[str, Any]:
        """
        获取对象上的所有注解

        Args:
            obj: 对象（类、方法、函数）

        Returns:
            Dict[str, Any]: 注解名称到注解值的映射
        """
        return dict(obj.__annotations__) if hasattr(obj, "__annotations__") else {}

    @staticmethod
    def is_annotation(obj: Any) -> bool:
        """
        检查对象是否为注解

        Args:
            obj: 要检查的对象

        Returns:
            bool: 是否为注解
        """
        # 在Python中，注解可以是任何类型，这里我们检查是否为装饰器
        return callable(obj) and hasattr(obj, "__annotations__")

    @staticmethod
    def get_annotations_by_type(obj: Any, annotation_type: Type[Any]) -> List[Any]:
        """
        获取对象上指定类型的注解

        Args:
            obj: 对象（类、方法、函数）
            annotation_type: 注解类型

        Returns:
            List[Any]: 注解列表
        """
        annotations = []
        if hasattr(obj, "__annotations__"):
            for value in obj.__annotations__.values():
                if isinstance(value, annotation_type):
                    annotations.append(value)
        return annotations

    @staticmethod
    def get_annotated_methods(cls: Type[Any], annotation_name: str) -> List[str]:
        """
        获取类中带有指定注解的方法名列表

        Args:
            cls: 类
            annotation_name: 注解名称

        Returns:
            List[str]: 方法名列表
        """
        annotated_methods = []
        
        # 遍历类的所有成员
        for name, member in inspect.getmembers(cls):
            # 跳过特殊成员
            if name.startswith("__") and name.endswith("__"):
                continue
            
            # 检查是否为方法且带有指定注解
            if inspect.ismethod(member) or inspect.isfunction(member):
                if AnnotationUtil.has_annotation(member, annotation_name):
                    annotated_methods.append(name)
        
        return annotated_methods

    @staticmethod
    def get_annotated_fields(cls: Type[Any], annotation_name: str) -> List[str]:
        """
        获取类中带有指定注解的属性名列表

        Args:
            cls: 类
            annotation_name: 注解名称

        Returns:
            List[str]: 属性名列表
        """
        annotated_fields = []
        field_annotations = AnnotationUtil.get_field_annotations(cls)
        
        for field_name, annotations in field_annotations.items():
            if isinstance(annotations, dict):
                if annotation_name in annotations:
                    annotated_fields.append(field_name)
            elif annotations == annotation_name:
                annotated_fields.append(field_name)
        
        return annotated_fields

    @staticmethod
    def get_method_signature_with_annotations(method: Any) -> str:
        """
        获取带有注解的方法签名

        Args:
            method: 方法

        Returns:
            str: 带有注解的方法签名
        """
        sig = inspect.signature(method)
        params = []
        
        # 获取参数注解
        param_annotations = AnnotationUtil.get_param_annotations(method)
        
        for name, param in sig.parameters.items():
            if name in param_annotations:
                param_str = f"{name}: {param_annotations[name]}"
                if param.default is not inspect.Parameter.empty:
                    param_str += f" = {param.default}"
            else:
                param_str = name
                if param.default is not inspect.Parameter.empty:
                    param_str += f" = {param.default}"
            params.append(param_str)
        
        # 获取返回值注解
        return_annotation = AnnotationUtil.get_return_annotation(method)
        return_str = f" -> {return_annotation}" if return_annotation else ""
        
        # 构建方法签名
        method_name = method.__name__
        signature = f"{method_name}({', '.join(params)}){return_str}"
        
        return signature

    @staticmethod
    def merge_annotations(target: Any, source: Any) -> None:
        """
        将源对象的注解合并到目标对象

        Args:
            target: 目标对象
            source: 源对象
        """
        source_annotations = AnnotationUtil.get_all_annotations(source)
        if not source_annotations:
            return
        
        if not hasattr(target, "__annotations__"):
            target.__annotations__ = {}
        
        target.__annotations__.update(source_annotations)

    @staticmethod
    def copy_annotations(source: Any, target: Any) -> None:
        """
        复制源对象的注解到目标对象

        Args:
            source: 源对象
            target: 目标对象
        """
        source_annotations = AnnotationUtil.get_all_annotations(source)
        if not source_annotations:
            if hasattr(target, "__annotations__"):
                delattr(target, "__annotations__")
            return
        
        target.__annotations__ = source_annotations.copy()