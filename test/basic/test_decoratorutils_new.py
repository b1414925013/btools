#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试装饰器工具类的新功能
"""

import asyncio
import time
import unittest

from btools.core.basic.decoratorutils import DecoratorUtil


class TestDecoratorUtilNewFeatures(unittest.TestCase):
    """
    测试装饰器工具类的新功能
    """

    def test_async_timer_decorator(self):
        """
        测试异步计时装饰器
        """
        # 记录日志的列表
        logs = []

        # 自定义日志函数
        def custom_logger(msg):
            logs.append(msg)

        # 创建异步计时装饰器
        async_timer_decorator = DecoratorUtil.async_timer(logger=custom_logger)

        # 使用装饰器
        @async_timer_decorator
        async def async_function():
            await asyncio.sleep(0.1)
            return "async_result"

        # 执行异步函数
        async def run_async():
            result = await async_function()
            self.assertEqual(result, "async_result")
            # 检查是否有日志记录
            self.assertTrue(len(logs) > 0)
            # 检查日志格式
            self.assertIn("async_function 执行耗时", logs[0])

        asyncio.run(run_async())

    def test_advanced_cache_decorator(self):
        """
        测试高级缓存装饰器
        """
        # 计数调用次数
        call_count = 0

        # 创建高级缓存装饰器（0.5秒过期）
        advanced_cache_decorator = DecoratorUtil.advanced_cache(ttl=0.5)

        # 使用装饰器
        @advanced_cache_decorator
        def cached_function(x, y):
            nonlocal call_count
            call_count += 1
            return x + y

        # 第一次调用（应该执行）
        result1 = cached_function(1, 2)
        self.assertEqual(result1, 3)
        self.assertEqual(call_count, 1)

        # 第二次调用（应该从缓存获取）
        result2 = cached_function(1, 2)
        self.assertEqual(result2, 3)
        self.assertEqual(call_count, 1)

        # 等待缓存过期
        time.sleep(0.6)

        # 第三次调用（应该重新执行）
        result3 = cached_function(1, 2)
        self.assertEqual(result3, 3)
        self.assertEqual(call_count, 2)

    def test_context_manager_decorator(self):
        """
        测试上下文管理装饰器
        """
        # 记录上下文执行情况
        context_logs = []

        # 创建一个上下文管理器
        class TestContextManager:
            def __enter__(self):
                context_logs.append("enter")
                return self

            def __exit__(self, exc_type, exc_val, exc_tb):
                context_logs.append("exit")

        # 创建上下文管理装饰器
        context_decorator = DecoratorUtil.context_manager(TestContextManager())

        # 使用装饰器
        @context_decorator
        def context_function():
            context_logs.append("function")
            return "success"

        # 执行函数
        result = context_function()
        self.assertEqual(result, "success")
        # 检查上下文执行顺序
        self.assertEqual(context_logs, ["enter", "function", "exit"])

    def test_metric_collector_decorator(self):
        """
        测试指标收集装饰器
        """
        # 记录指标
        metrics = []

        # 自定义指标收集函数
        def custom_metric_logger(msg):
            metrics.append(msg)

        # 临时替换print函数
        import builtins

        original_print = builtins.print
        builtins.print = custom_metric_logger

        try:
            # 创建指标收集装饰器
            metric_decorator = DecoratorUtil.metric_collector(
                "test_metric", tags={"test": "value"}
            )

            # 使用装饰器
            @metric_decorator
            def metric_function():
                time.sleep(0.1)
                return "metric_result"

            # 执行函数
            result = metric_function()
            self.assertEqual(result, "metric_result")

            # 检查指标是否被收集
            self.assertTrue(len(metrics) > 0)
            # 检查指标格式
            self.assertIn("[指标] test_metric", metrics[0])
            self.assertIn("耗时=", metrics[0])
            self.assertIn("成功=True", metrics[0])
            self.assertIn("标签={'test': 'value'}", metrics[0])
        finally:
            # 恢复原始print函数
            builtins.print = original_print

    def test_profiler_decorator(self):
        """
        测试性能分析装饰器
        """
        # 记录性能分析输出
        profiler_output = []

        # 自定义输出函数
        def custom_profiler_output(*args, **kwargs):
            # 只关心第一个参数，即消息内容
            if args:
                profiler_output.append(args[0])

        # 临时替换print函数
        import builtins

        original_print = builtins.print
        builtins.print = custom_profiler_output

        try:
            # 创建性能分析装饰器
            profiler_decorator = DecoratorUtil.profiler(enabled=True)

            # 使用装饰器
            @profiler_decorator
            def profiler_function():
                # 简单的计算
                result = 0
                for i in range(1000):
                    result += i
                return result

            # 执行函数
            result = profiler_function()
            self.assertEqual(result, 499500)

            # 检查性能分析输出
            self.assertTrue(len(profiler_output) > 0)
            # 检查是否有包含性能分析信息的输出
            has_profiler_output = any("[性能分析]" in line for line in profiler_output)
            self.assertTrue(has_profiler_output)
        finally:
            # 恢复原始print函数
            builtins.print = original_print

    def test_profiler_decorator_disabled(self):
        """
        测试禁用的性能分析装饰器
        """
        # 记录输出
        output = []

        # 自定义输出函数
        def custom_output(msg):
            output.append(msg)

        # 临时替换print函数
        import builtins

        original_print = builtins.print
        builtins.print = custom_output

        try:
            # 创建禁用的性能分析装饰器
            profiler_decorator = DecoratorUtil.profiler(enabled=False)

            # 使用装饰器
            @profiler_decorator
            def profiler_function():
                result = 0
                for i in range(1000):
                    result += i
                return result

            # 执行函数
            result = profiler_function()
            self.assertEqual(result, 499500)

            # 检查是否没有性能分析输出
            self.assertEqual(len(output), 0)
        finally:
            # 恢复原始print函数
            builtins.print = original_print


if __name__ == "__main__":
    unittest.main()
