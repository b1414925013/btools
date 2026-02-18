#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
切面代理工具类

提供代理相关功能，包括动态代理创建、切面增强、方法拦截等
"""
import inspect
import types
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union


class ProxyUtil:
    """
    切面代理工具类
    """

    @staticmethod
    def createProxy(target: Any, **kwargs) -> Any:
        """
        创建动态代理

        Args:
            target: 目标对象
            **kwargs: 代理配置
                - before: 方法执行前的回调函数
                - after: 方法执行后的回调函数
                - around: 方法执行环绕的回调函数
                - on_exception: 方法执行异常时的回调函数

        Returns:
            Any: 代理对象
        """
        # 检查目标对象是否为类
        if inspect.isclass(target):
            # 创建类的代理
            return ProxyUtil._createClassProxy(target, **kwargs)
        else:
            # 创建实例的代理
            return ProxyUtil._createInstanceProxy(target, **kwargs)

    @staticmethod
    def _createClassProxy(cls: Type[Any], **kwargs) -> Type[Any]:
        """
        创建类的代理

        Args:
            cls: 目标类
            **kwargs: 代理配置

        Returns:
            Type[Any]: 代理类
        """
        # 创建代理类
        class ProxyClass(cls):
            """代理类"""

            def __init__(self, *args, **init_kwargs):
                """初始化"""
                super().__init__(*args, **init_kwargs)
                self._proxy_config = kwargs

        # 重命名代理类
        ProxyClass.__name__ = f"Proxy_{cls.__name__}"
        
        # 为代理类添加方法
        for name, method in inspect.getmembers(cls, inspect.isfunction):
            if name.startswith("__") and name.endswith("__"):
                continue
            
            # 创建代理方法
            def create_proxy_method(method_name, original_method):
                def proxy_method(self, *args, **proxy_kwargs):
                    return ProxyUtil._invokeMethod(self, method_name, original_method, args, proxy_kwargs, self._proxy_config)
                return proxy_method
            
            # 绑定代理方法
            setattr(ProxyClass, name, create_proxy_method(name, method))
        
        return ProxyClass

    @staticmethod
    def _createInstanceProxy(instance: Any, **kwargs) -> Any:
        """
        创建实例的代理

        Args:
            instance: 目标实例
            **kwargs: 代理配置

        Returns:
            Any: 代理实例
        """
        # 获取实例的类
        cls = type(instance)
        
        # 创建代理类
        class ProxyClass:
            """代理类"""

            def __init__(self, target):
                """初始化"""
                self._proxy_target = target
                self._proxy_config = kwargs

        # 重命名代理类
        ProxyClass.__name__ = f"Proxy_{cls.__name__}"
        
        # 为代理类添加方法
        for name, method in inspect.getmembers(cls, inspect.isfunction):
            if name.startswith("__") and name.endswith("__"):
                continue
            
            # 创建代理方法
            def create_proxy_method(method_name):
                def proxy_method(self, *args, **proxy_kwargs):
                    target_method = getattr(self._proxy_target, method_name)
                    return ProxyUtil._invokeMethod(self._proxy_target, method_name, target_method, args, proxy_kwargs, self._proxy_config)
                return proxy_method
            
            # 绑定代理方法
            setattr(ProxyClass, name, create_proxy_method(name))
        
        # 创建并返回代理实例
        return ProxyClass(instance)

    @staticmethod
    def _invokeMethod(target: Any, method_name: str, method: Callable, args: Tuple[Any], kwargs: Dict[str, Any], config: Dict[str, Any]) -> Any:
        """
        调用方法并应用切面

        Args:
            target: 目标对象
            method_name: 方法名
            method: 要调用的方法
            args: 位置参数
            kwargs: 关键字参数
            config: 代理配置

        Returns:
            Any: 方法返回值
        """
        # 执行前回调
        if "before" in config:
            config["before"](target, method_name, args, kwargs)
        
        # 执行环绕回调
        if "around" in config:
            try:
                # 检查方法是否已经绑定到实例
                if hasattr(method, "__self__") and method.__self__ is not None:
                    # 实例方法，已经绑定了self
                    result = config["around"](target, method_name, args, kwargs, lambda: method(*args, **kwargs))
                else:
                    # 类方法或未绑定方法，需要传递self参数
                    result = config["around"](target, method_name, args, kwargs, lambda: method(target, *args, **kwargs))
                # 执行后回调
                if "after" in config:
                    config["after"](target, method_name, args, kwargs, result)
                return result
            except Exception as e:
                # 执行异常回调
                if "on_exception" in config:
                    config["on_exception"](target, method_name, args, kwargs, e)
                raise
        else:
            # 直接执行方法
            try:
                # 检查方法是否已经绑定到实例
                if hasattr(method, "__self__") and method.__self__ is not None:
                    # 实例方法，已经绑定了self
                    result = method(*args, **kwargs)
                else:
                    # 类方法或未绑定方法，需要传递self参数
                    result = method(target, *args, **kwargs)
                # 执行后回调
                if "after" in config:
                    config["after"](target, method_name, args, kwargs, result)
                return result
            except Exception as e:
                # 执行异常回调
                if "on_exception" in config:
                    config["on_exception"](target, method_name, args, kwargs, e)
                raise

    @staticmethod
    def createAspect(target: Any, before: Optional[Callable] = None, after: Optional[Callable] = None, 
                   around: Optional[Callable] = None, on_exception: Optional[Callable] = None) -> Any:
        """
        创建切面

        Args:
            target: 目标对象或类
            before: 方法执行前的回调函数
            after: 方法执行后的回调函数
            around: 方法执行环绕的回调函数
            on_exception: 方法执行异常时的回调函数

        Returns:
            Any: 代理对象
        """
        config = {}
        if before:
            config["before"] = before
        if after:
            config["after"] = after
        if around:
            config["around"] = around
        if on_exception:
            config["on_exception"] = on_exception
        
        return ProxyUtil.createProxy(target, **config)

    @staticmethod
    def createTimerAspect(target: Any, logger: Optional[Callable] = print) -> Any:
        """
        创建计时切面

        Args:
            target: 目标对象或类
            logger: 日志函数

        Returns:
            Any: 代理对象
        """
        import time
        
        def before(target, method_name, args, kwargs):
            """执行前"""
            logger(f"开始执行 {method_name}...")
            setattr(target, f"_start_time_{method_name}", time.time())
        
        def after(target, method_name, args, kwargs, result):
            """执行后"""
            start_time = getattr(target, f"_start_time_{method_name}", time.time())
            end_time = time.time()
            logger(f"{method_name} 执行完成，耗时 {end_time - start_time:.4f} 秒")
        
        def on_exception(target, method_name, args, kwargs, e):
            """执行异常"""
            start_time = getattr(target, f"_start_time_{method_name}", time.time())
            end_time = time.time()
            logger(f"{method_name} 执行异常，耗时 {end_time - start_time:.4f} 秒，异常: {e}")
        
        return ProxyUtil.createAspect(target, before=before, after=after, on_exception=on_exception)

    @staticmethod
    def createLoggingAspect(target: Any, logger: Optional[Callable] = print) -> Any:
        """
        创建日志切面

        Args:
            target: 目标对象或类
            logger: 日志函数

        Returns:
            Any: 代理对象
        """
        def before(target, method_name, args, kwargs):
            """执行前"""
            logger(f"[BEFORE] {method_name} 被调用，参数: args={args}, kwargs={kwargs}")
        
        def after(target, method_name, args, kwargs, result):
            """执行后"""
            logger(f"[AFTER] {method_name} 执行完成，返回值: {result}")
        
        def on_exception(target, method_name, args, kwargs, e):
            """执行异常"""
            logger(f"[EXCEPTION] {method_name} 执行异常，异常: {e}")
        
        return ProxyUtil.createAspect(target, before=before, after=after, on_exception=on_exception)

    @staticmethod
    def createTransactionAspect(target: Any, begin_transaction: Callable, commit_transaction: Callable, 
                              rollback_transaction: Callable) -> Any:
        """
        创建事务切面

        Args:
            target: 目标对象或类
            begin_transaction: 开始事务的函数
            commit_transaction: 提交事务的函数
            rollback_transaction: 回滚事务的函数

        Returns:
            Any: 代理对象
        """
        def around(target, method_name, args, kwargs, proceed):
            """执行环绕"""
            # 开始事务
            tx = begin_transaction()
            try:
                # 执行方法
                result = proceed()
                # 提交事务
                commit_transaction(tx)
                return result
            except Exception as e:
                # 回滚事务
                rollback_transaction(tx)
                raise
        
        return ProxyUtil.createAspect(target, around=around)

    @staticmethod
    def isProxy(obj: Any) -> bool:
        """
        检查对象是否为代理对象

        Args:
            obj: 要检查的对象

        Returns:
            bool: 是否为代理对象
        """
        return hasattr(obj, "_proxy_target") or hasattr(obj, "_proxy_config")

    @staticmethod
    def getTarget(obj: Any) -> Any:
        """
        获取代理对象的目标对象

        Args:
            obj: 代理对象

        Returns:
            Any: 目标对象
        """
        if hasattr(obj, "_proxy_target"):
            return obj._proxy_target
        return obj

    @staticmethod
    def getProxyConfig(obj: Any) -> Dict[str, Any]:
        """
        获取代理对象的配置

        Args:
            obj: 代理对象

        Returns:
            Dict[str, Any]: 代理配置
        """
        if hasattr(obj, "_proxy_config"):
            return obj._proxy_config
        return {}

    @staticmethod
    def addAspect(obj: Any, **kwargs) -> Any:
        """
        为对象添加切面

        Args:
            obj: 目标对象
            **kwargs: 代理配置

        Returns:
            Any: 代理对象
        """
        if ProxyUtil.isProxy(obj):
            # 如果已经是代理对象，合并配置
            if hasattr(obj, "_proxy_config"):
                obj._proxy_config.update(kwargs)
            return obj
        else:
            # 创建新的代理对象
            return ProxyUtil.createProxy(obj, **kwargs)

    @staticmethod
    def removeAspect(obj: Any) -> Any:
        """
        移除对象的切面

        Args:
            obj: 代理对象

        Returns:
            Any: 目标对象
        """
        return ProxyUtil.getTarget(obj)