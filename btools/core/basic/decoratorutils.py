#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
装饰器工具类

提供装饰器相关的操作功能，包括创建、管理和使用装饰器
"""
import functools
import inspect
import time
from typing import Any, Callable, Dict, List, Optional, Type, Union


class DecoratorUtil:
    """
    装饰器工具类
    """

    @staticmethod
    def createDecorator(func: Callable) -> Callable:
        """
        创建一个简单的装饰器

        Args:
            func: 装饰器函数

        Returns:
            Callable: 装饰器
        """
        @functools.wraps(func)
        def decorator(*args, **kwargs):
            return func(*args, **kwargs)
        return decorator

    @staticmethod
    def createTimerDecorator(logger: Optional[Callable] = print) -> Callable:
        """
        创建一个计时装饰器

        Args:
            logger: 日志函数

        Returns:
            Callable: 计时装饰器
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                logger(f"{func.__name__} 执行耗时: {end_time - start_time:.4f} 秒")
                return result
            return wrapper
        return decorator

    @staticmethod
    def createLoggingDecorator(logger: Optional[Callable] = print) -> Callable:
        """
        创建一个日志装饰器

        Args:
            logger: 日志函数

        Returns:
            Callable: 日志装饰器
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                logger(f"[开始] {func.__name__}")
                try:
                    result = func(*args, **kwargs)
                    logger(f"[成功] {func.__name__}")
                    return result
                except Exception as e:
                    logger(f"[失败] {func.__name__}: {e}")
                    raise
            return wrapper
        return decorator

    @staticmethod
    def createCacheDecorator() -> Callable:
        """
        创建一个缓存装饰器

        Returns:
            Callable: 缓存装饰器
        """
        def decorator(func: Callable) -> Callable:
            cache = {}
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                key = str(args) + str(kwargs)
                if key not in cache:
                    cache[key] = func(*args, **kwargs)
                return cache[key]
            return wrapper
        return decorator

    @staticmethod
    def createRetryDecorator(max_retries: int = 3, delay: float = 1.0) -> Callable:
        """
        创建一个重试装饰器

        Args:
            max_retries: 最大重试次数
            delay: 重试延迟（秒）

        Returns:
            Callable: 重试装饰器
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None
                for i in range(max_retries):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_exception = e
                        if i < max_retries - 1:
                            time.sleep(delay)
                raise last_exception
            return wrapper
        return decorator

    @staticmethod
    def createSingletonDecorator() -> Callable:
        """
        创建一个单例装饰器

        Returns:
            Callable: 单例装饰器
        """
        def decorator(cls: Type[Any]) -> Type[Any]:
            instances = {}
            
            @functools.wraps(cls)
            def get_instance(*args, **kwargs):
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
                return instances[cls]
            
            return get_instance
        return decorator

    @staticmethod
    def createDeprecationDecorator(message: str = "此方法已过时") -> Callable:
        """
        创建一个过时警告装饰器

        Args:
            message: 警告消息

        Returns:
            Callable: 过时警告装饰器
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                import warnings
                warnings.warn(message, DeprecationWarning, stacklevel=2)
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def createPermissionDecorator(required_permission: str) -> Callable:
        """
        创建一个权限检查装饰器

        Args:
            required_permission: 所需权限

        Returns:
            Callable: 权限检查装饰器
        """
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 这里可以根据实际情况实现权限检查逻辑
                # 例如从用户会话中获取权限信息
                user_permissions = getattr(args[0], "permissions", []) if args else []
                
                if required_permission not in user_permissions:
                    raise PermissionError(f"缺少权限: {required_permission}")
                
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def createRateLimitDecorator(max_calls: int, period: float) -> Callable:
        """
        创建一个速率限制装饰器

        Args:
            max_calls: 最大调用次数
            period: 时间周期（秒）

        Returns:
            Callable: 速率限制装饰器
        """
        def decorator(func: Callable) -> Callable:
            calls = []
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                current_time = time.time()
                # 清理过期的调用记录
                calls[:] = [t for t in calls if current_time - t < period]
                
                if len(calls) >= max_calls:
                    raise RateLimitError(f"超过速率限制: {max_calls} 次/ {period} 秒")
                
                calls.append(current_time)
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def combineDecorators(*decorators: Callable) -> Callable:
        """
        组合多个装饰器

        Args:
            *decorators: 装饰器列表

        Returns:
            Callable: 组合后的装饰器
        """
        def decorator(func: Callable) -> Callable:
            for decorator in reversed(decorators):
                func = decorator(func)
            return func
        return decorator

    @staticmethod
    def isDecorator(obj: Any) -> bool:
        """
        检查对象是否为装饰器

        Args:
            obj: 要检查的对象

        Returns:
            bool: 是否为装饰器
        """
        return callable(obj) and hasattr(obj, "__wrapped__")

    @staticmethod
    def getOriginalFunction(decorated_func: Callable) -> Optional[Callable]:
        """
        获取被装饰的原始函数

        Args:
            decorated_func: 被装饰的函数

        Returns:
            Optional[Callable]: 原始函数
        """
        if hasattr(decorated_func, "__wrapped__"):
            return decorated_func.__wrapped__
        return None

    @staticmethod
    def getDecoratorChain(decorated_func: Callable) -> List[Callable]:
        """
        获取装饰器链

        Args:
            decorated_func: 被装饰的函数

        Returns:
            List[Callable]: 装饰器链
        """
        chain = []
        current = decorated_func
        
        while hasattr(current, "__wrapped__"):
            chain.append(current)
            current = current.__wrapped__
        
        chain.append(current)
        return chain

    @staticmethod
    def createConditionalDecorator(condition: Callable[[Any], bool], decorator: Callable) -> Callable:
        """
        创建一个条件装饰器

        Args:
            condition: 条件函数
            decorator: 装饰器

        Returns:
            Callable: 条件装饰器
        """
        def conditional_decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if condition(args, kwargs):
                    return decorator(func)(*args, **kwargs)
                else:
                    return func(*args, **kwargs)
            return wrapper
        return conditional_decorator


class RateLimitError(Exception):
    """
    速率限制异常
    """
    pass