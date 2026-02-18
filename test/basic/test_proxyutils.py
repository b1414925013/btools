#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ProxyUtil 测试文件

测试 ProxyUtil 工具类的功能
"""
import unittest
from btools.core.basic.proxyutils import ProxyUtil


class TestProxyUtil(unittest.TestCase):
    """
    测试 ProxyUtil 工具类
    """

    def setUp(self):
        """
        测试前置方法
        """
        # 定义一个测试类
        class Calculator:
            def __init__(self, name="default"):
                self.name = name
                self.calls = 0
            
            def add(self, a, b):
                self.calls += 1
                return a + b
            
            def subtract(self, a, b):
                self.calls += 1
                return a - b
            
            def multiply(self, a, b):
                self.calls += 1
                return a * b
            
            def divide(self, a, b):
                self.calls += 1
                if b == 0:
                    raise ZeroDivisionError("除数不能为零")
                return a / b
        
        self.Calculator = Calculator
        self.calculator = Calculator()

    def test_create_proxy_instance(self):
        """
        测试创建实例代理
        """
        # 创建代理
        proxy = ProxyUtil.createProxy(self.calculator)
        
        # 测试代理功能
        result = proxy.add(1, 2)
        self.assertEqual(result, 3)
        self.assertEqual(self.calculator.calls, 1)
        
        # 测试多个方法
        result = proxy.subtract(5, 2)
        self.assertEqual(result, 3)
        self.assertEqual(self.calculator.calls, 2)

    def test_create_proxy_class(self):
        """
        测试创建类代理
        """
        # 创建类代理
        ProxyCalculator = ProxyUtil.createProxy(self.Calculator)
        
        # 使用代理类创建实例
        calculator = ProxyCalculator("test")
        self.assertEqual(calculator.name, "test")
        
        # 测试方法调用
        result = calculator.add(1, 2)
        self.assertEqual(result, 3)
        self.assertEqual(calculator.calls, 1)

    def test_before_after_callbacks(self):
        """
        测试前置和后置回调
        """
        before_called = False
        after_called = False
        after_result = None
        
        def before_callback(target, method_name, args, kwargs):
            nonlocal before_called
            before_called = True
            self.assertEqual(method_name, "add")
            self.assertEqual(args, (1, 2))
        
        def after_callback(target, method_name, args, kwargs, result):
            nonlocal after_called, after_result
            after_called = True
            after_result = result
            self.assertEqual(method_name, "add")
            self.assertEqual(args, (1, 2))
            self.assertEqual(result, 3)
        
        # 创建带回调的代理
        proxy = ProxyUtil.createProxy(
            self.calculator,
            before=before_callback,
            after=after_callback
        )
        
        # 调用方法
        result = proxy.add(1, 2)
        self.assertEqual(result, 3)
        self.assertTrue(before_called)
        self.assertTrue(after_called)
        self.assertEqual(after_result, 3)

    def test_around_callback(self):
        """
        测试环绕回调
        """
        around_called = False
        proceed_called = False
        
        def around_callback(target, method_name, args, kwargs, proceed):
            nonlocal around_called, proceed_called
            around_called = True
            self.assertEqual(method_name, "add")
            # 调用原始方法
            result = proceed()
            proceed_called = True
            return result * 2  # 增强返回值
        
        # 创建带环绕回调的代理
        proxy = ProxyUtil.createProxy(
            self.calculator,
            around=around_callback
        )
        
        # 调用方法
        result = proxy.add(1, 2)
        self.assertEqual(result, 6)  # 应该是增强后的值
        self.assertTrue(around_called)
        self.assertTrue(proceed_called)

    def test_on_exception_callback(self):
        """
        测试异常回调
        """
        exception_called = False
        exception_value = None
        
        def on_exception_callback(target, method_name, args, kwargs, e):
            nonlocal exception_called, exception_value
            exception_called = True
            exception_value = e
            self.assertEqual(method_name, "divide")
            self.assertEqual(args, (1, 0))
        
        # 创建带异常回调的代理
        proxy = ProxyUtil.createProxy(
            self.calculator,
            on_exception=on_exception_callback
        )
        
        # 调用会抛出异常的方法
        with self.assertRaises(ZeroDivisionError):
            proxy.divide(1, 0)
        
        self.assertTrue(exception_called)
        self.assertIsInstance(exception_value, ZeroDivisionError)

    def test_create_aspect(self):
        """
        测试创建切面
        """
        before_called = False
        after_called = False
        
        def before_callback(target, method_name, args, kwargs):
            nonlocal before_called
            before_called = True
        
        def after_callback(target, method_name, args, kwargs, result):
            nonlocal after_called
            after_called = True
        
        # 创建切面
        aspect = ProxyUtil.createAspect(
            self.calculator,
            before=before_callback,
            after=after_callback
        )
        
        # 调用方法
        result = aspect.add(1, 2)
        self.assertEqual(result, 3)
        self.assertTrue(before_called)
        self.assertTrue(after_called)

    def test_create_timer_aspect(self):
        """
        测试创建计时切面
        """
        # 创建计时切面
        timer_proxy = ProxyUtil.createTimerAspect(self.calculator)
        
        # 调用方法
        result = timer_proxy.add(1, 2)
        self.assertEqual(result, 3)

    def test_create_logging_aspect(self):
        """
        测试创建日志切面
        """
        # 创建日志切面
        log_proxy = ProxyUtil.createLoggingAspect(self.calculator)
        
        # 调用方法
        result = log_proxy.add(1, 2)
        self.assertEqual(result, 3)

    def test_create_transaction_aspect(self):
        """
        测试创建事务切面
        """
        tx_started = False
        tx_committed = False
        tx_rolled_back = False
        tx_value = None
        
        def begin_transaction():
            nonlocal tx_started, tx_value
            tx_started = True
            tx_value = "tx123"
            return tx_value
        
        def commit_transaction(tx):
            nonlocal tx_committed
            tx_committed = True
            self.assertEqual(tx, tx_value)
        
        def rollback_transaction(tx):
            nonlocal tx_rolled_back
            tx_rolled_back = True
            self.assertEqual(tx, tx_value)
        
        # 创建事务切面
        tx_proxy = ProxyUtil.createTransactionAspect(
            self.calculator,
            begin_transaction=begin_transaction,
            commit_transaction=commit_transaction,
            rollback_transaction=rollback_transaction
        )
        
        # 测试正常执行（应该提交事务）
        result = tx_proxy.add(1, 2)
        self.assertEqual(result, 3)
        self.assertTrue(tx_started)
        self.assertTrue(tx_committed)
        self.assertFalse(tx_rolled_back)

    def test_is_proxy(self):
        """
        测试检查是否为代理对象
        """
        # 创建代理
        proxy = ProxyUtil.createProxy(self.calculator)
        
        # 检查
        self.assertTrue(ProxyUtil.isProxy(proxy))
        self.assertFalse(ProxyUtil.isProxy(self.calculator))

    def test_get_target(self):
        """
        测试获取目标对象
        """
        # 创建代理
        proxy = ProxyUtil.createProxy(self.calculator)
        
        # 获取目标对象
        target = ProxyUtil.getTarget(proxy)
        self.assertEqual(target, self.calculator)
        
        # 非代理对象应该返回自身
        self.assertEqual(ProxyUtil.getTarget(self.calculator), self.calculator)

    def test_get_proxy_config(self):
        """
        测试获取代理配置
        """
        # 创建带配置的代理
        def before_callback(target, method_name, args, kwargs):
            pass
        
        proxy = ProxyUtil.createProxy(self.calculator, before=before_callback)
        
        # 获取配置
        config = ProxyUtil.getProxyConfig(proxy)
        self.assertIn("before", config)
        
        # 非代理对象应该返回空字典
        self.assertEqual(ProxyUtil.getProxyConfig(self.calculator), {})

    def test_add_aspect(self):
        """
        测试添加切面
        """
        # 创建初始代理
        proxy = ProxyUtil.createProxy(self.calculator)
        
        # 添加额外的切面
        after_called = False
        
        def after_callback(target, method_name, args, kwargs, result):
            nonlocal after_called
            after_called = True
        
        enhanced_proxy = ProxyUtil.addAspect(proxy, after=after_callback)
        
        # 调用方法
        result = enhanced_proxy.add(1, 2)
        self.assertEqual(result, 3)
        self.assertTrue(after_called)

    def test_remove_aspect(self):
        """
        测试移除切面
        """
        # 创建代理
        proxy = ProxyUtil.createProxy(self.calculator)
        
        # 移除切面
        original = ProxyUtil.removeAspect(proxy)
        
        # 检查是否为原始对象
        self.assertEqual(original, self.calculator)

    def test_chain_aspects(self):
        """
        测试链式添加切面
        """
        # 创建原始对象
        calculator = self.Calculator()
        
        # 添加多个切面
        proxy = ProxyUtil.createTimerAspect(calculator)
        proxy = ProxyUtil.createLoggingAspect(proxy)
        
        # 调用方法
        result = proxy.add(1, 2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()