#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
装饰器工具类测试文件

测试DecoratorUtil的功能
"""
import unittest
import time
from btools.core.basic.decoratorutils import DecoratorUtil, RateLimitError


class TestDecoratorUtil(unittest.TestCase):
    """
    测试装饰器工具类
    """

    def test_create_timer_decorator(self):
        """
        测试创建计时装饰器
        """
        # 创建计时装饰器
        timer_decorator = DecoratorUtil.createTimerDecorator()
        
        # 使用装饰器
        @timer_decorator
        def test_function():
            time.sleep(0.1)
            return "test"
        
        # 执行函数
        result = test_function()
        self.assertEqual(result, "test")

    def test_create_logging_decorator(self):
        """
        测试创建日志装饰器
        """
        # 收集日志
        logs = []
        def custom_logger(msg):
            logs.append(msg)
        
        # 创建日志装饰器
        logging_decorator = DecoratorUtil.createLoggingDecorator(custom_logger)
        
        # 使用装饰器
        @logging_decorator
        def test_function():
            return "test"
        
        # 执行函数
        result = test_function()
        self.assertEqual(result, "test")
        self.assertTrue(any("[开始]" in log for log in logs))
        self.assertTrue(any("[成功]" in log for log in logs))

    def test_create_cache_decorator(self):
        """
        测试创建缓存装饰器
        """
        # 计数调用次数
        call_count = 0
        
        # 创建缓存装饰器
        cache_decorator = DecoratorUtil.createCacheDecorator()
        
        # 使用装饰器
        @cache_decorator
        def test_function(x):
            nonlocal call_count
            call_count += 1
            return x * 2
        
        # 第一次调用
        result1 = test_function(5)
        self.assertEqual(result1, 10)
        self.assertEqual(call_count, 1)
        
        # 第二次调用（应该从缓存获取）
        result2 = test_function(5)
        self.assertEqual(result2, 10)
        self.assertEqual(call_count, 1)  # 调用次数不应该增加

    def test_create_retry_decorator(self):
        """
        测试创建重试装饰器
        """
        # 计数调用次数
        call_count = 0
        
        # 创建重试装饰器
        retry_decorator = DecoratorUtil.createRetryDecorator(max_retries=3, delay=0.1)
        
        # 使用装饰器
        @retry_decorator
        def test_function():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise Exception("Test exception")
            return "success"
        
        # 执行函数
        result = test_function()
        self.assertEqual(result, "success")
        self.assertEqual(call_count, 3)

    def test_create_singleton_decorator(self):
        """
        测试创建单例装饰器
        """
        # 创建单例装饰器
        singleton_decorator = DecoratorUtil.createSingletonDecorator()
        
        # 使用装饰器
        @singleton_decorator
        class TestClass:
            def __init__(self, value):
                self.value = value
        
        # 创建实例
        instance1 = TestClass(10)
        instance2 = TestClass(20)
        
        # 两个实例应该是同一个
        self.assertEqual(instance1, instance2)
        self.assertEqual(instance1.value, 10)  # 应该保持第一次创建时的值

    def test_create_deprecation_decorator(self):
        """
        测试创建过时警告装饰器
        """
        # 创建过时警告装饰器
        deprecation_decorator = DecoratorUtil.createDeprecationDecorator("此方法已过时，请使用新方法")
        
        # 使用装饰器
        @deprecation_decorator
        def test_function():
            return "test"
        
        # 执行函数，应该发出警告
        import warnings
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            result = test_function()
            self.assertEqual(result, "test")
            self.assertTrue(len(w) > 0)
            self.assertIsInstance(w[0].message, DeprecationWarning)

    def test_create_permission_decorator(self):
        """
        测试创建权限检查装饰器
        """
        # 创建权限检查装饰器
        permission_decorator = DecoratorUtil.createPermissionDecorator("admin")
        
        # 使用装饰器
        @permission_decorator
        def test_function(user):
            return "success"
        
        # 模拟有权限的用户
        class User:
            def __init__(self, permissions):
                self.permissions = permissions
        
        # 测试有权限的情况
        admin_user = User(["admin"])
        result = test_function(admin_user)
        self.assertEqual(result, "success")
        
        # 测试无权限的情况
        regular_user = User(["user"])
        with self.assertRaises(PermissionError):
            test_function(regular_user)

    def test_create_rate_limit_decorator(self):
        """
        测试创建速率限制装饰器
        """
        # 创建速率限制装饰器（1秒内最多调用2次）
        rate_limit_decorator = DecoratorUtil.createRateLimitDecorator(max_calls=2, period=1)
        
        # 使用装饰器
        @rate_limit_decorator
        def test_function():
            return "success"
        
        # 第一次调用
        result1 = test_function()
        self.assertEqual(result1, "success")
        
        # 第二次调用
        result2 = test_function()
        self.assertEqual(result2, "success")
        
        # 第三次调用应该触发速率限制
        with self.assertRaises(RateLimitError):
            test_function()

    def test_combine_decorators(self):
        """
        测试组合多个装饰器
        """
        # 收集日志
        logs = []
        def custom_logger(msg):
            logs.append(msg)
        
        # 创建装饰器
        timer_decorator = DecoratorUtil.createTimerDecorator(custom_logger)
        logging_decorator = DecoratorUtil.createLoggingDecorator(custom_logger)
        
        # 组合装饰器
        combined_decorator = DecoratorUtil.combineDecorators(timer_decorator, logging_decorator)
        
        # 使用装饰器
        @combined_decorator
        def test_function():
            time.sleep(0.05)
            return "test"
        
        # 执行函数
        result = test_function()
        self.assertEqual(result, "test")
        self.assertTrue(any("[开始]" in log for log in logs))
        self.assertTrue(any("[成功]" in log for log in logs))
        self.assertTrue(any("执行耗时" in log for log in logs))

    def test_is_decorator(self):
        """
        测试检查对象是否为装饰器
        """
        # 创建装饰器
        timer_decorator = DecoratorUtil.createTimerDecorator()
        
        # 使用装饰器
        @timer_decorator
        def test_function():
            return "test"
        
        # 测试
        self.assertTrue(DecoratorUtil.isDecorator(test_function))
        self.assertFalse(DecoratorUtil.isDecorator(lambda x: x))

    def test_get_original_function(self):
        """
        测试获取被装饰的原始函数
        """
        # 创建装饰器
        timer_decorator = DecoratorUtil.createTimerDecorator()
        
        # 原始函数
        def original_function():
            return "test"
        
        # 使用装饰器
        decorated_function = timer_decorator(original_function)
        
        # 测试
        retrieved_original = DecoratorUtil.getOriginalFunction(decorated_function)
        self.assertEqual(retrieved_original, original_function)

    def test_get_decorator_chain(self):
        """
        测试获取装饰器链
        """
        # 创建装饰器
        timer_decorator = DecoratorUtil.createTimerDecorator()
        logging_decorator = DecoratorUtil.createLoggingDecorator()
        
        # 使用装饰器
        def test_function():
            return "test"
        
        decorated1 = timer_decorator(test_function)
        decorated2 = logging_decorator(decorated1)
        
        # 测试
        chain = DecoratorUtil.getDecoratorChain(decorated2)
        self.assertEqual(len(chain), 3)  # 装饰器2 -> 装饰器1 -> 原始函数

    def test_create_conditional_decorator(self):
        """
        测试创建条件装饰器
        """
        # 计数调用次数
        call_count = 0
        
        # 创建条件函数
        def condition(args, kwargs):
            return args and args[0] > 5
        
        # 创建装饰器
        def simple_decorator(func):
            def wrapper(*args, **kwargs):
                nonlocal call_count
                call_count += 1
                return func(*args, **kwargs)
            return wrapper
        
        # 创建条件装饰器
        conditional_decorator = DecoratorUtil.createConditionalDecorator(condition, simple_decorator)
        
        # 使用装饰器
        @conditional_decorator
        def test_function(x):
            return x * 2
        
        # 测试不满足条件的情况
        result1 = test_function(3)
        self.assertEqual(result1, 6)
        self.assertEqual(call_count, 0)
        
        # 测试满足条件的情况
        result2 = test_function(7)
        self.assertEqual(result2, 14)
        self.assertEqual(call_count, 1)


if __name__ == '__main__':
    unittest.main()