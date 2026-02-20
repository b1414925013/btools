#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
性能测试工具类

提供性能测试工具，测量执行时间、内存使用等功能
"""
import time
import psutil
import gc
from typing import Callable, Optional, Dict, Any, Union
from functools import wraps


class PerformanceTestUtils:
    """
    性能测试工具类
    """

    @staticmethod
    def measure_execution_time(func: Callable, *args, **kwargs) -> Dict[str, Any]:
        """
        测量函数执行时间

        Args:
            func: 要测量的函数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            包含执行时间和结果的字典
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        return {
            'execution_time': execution_time,
            'result': result
        }

    @staticmethod
    def measure_memory_usage(func: Callable, *args, **kwargs) -> Dict[str, Any]:
        """
        测量函数内存使用

        Args:
            func: 要测量的函数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            包含内存使用和结果的字典
        """
        # 清理垃圾回收
        gc.collect()
        
        # 获取初始内存使用
        process = psutil.Process()
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB

        result = func(*args, **kwargs)

        # 清理垃圾回收
        gc.collect()
        
        # 获取最终内存使用
        final_memory = process.memory_info().rss / 1024 / 1024  # MB
        memory_used = final_memory - initial_memory

        return {
            'initial_memory': initial_memory,
            'final_memory': final_memory,
            'memory_used': memory_used,
            'result': result
        }

    @staticmethod
    def measure_performance(func: Callable, *args, **kwargs) -> Dict[str, Any]:
        """
        测量函数性能（时间和内存）

        Args:
            func: 要测量的函数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            包含性能数据和结果的字典
        """
        # 清理垃圾回收
        gc.collect()
        
        # 获取初始状态
        start_time = time.time()
        process = psutil.Process()
        initial_memory = process.memory_info().rss / 1024 / 1024  # MB

        result = func(*args, **kwargs)

        # 清理垃圾回收
        gc.collect()
        
        # 获取最终状态
        end_time = time.time()
        final_memory = process.memory_info().rss / 1024 / 1024  # MB

        execution_time = end_time - start_time
        memory_used = final_memory - initial_memory

        return {
            'execution_time': execution_time,
            'initial_memory': initial_memory,
            'final_memory': final_memory,
            'memory_used': memory_used,
            'result': result
        }

    @staticmethod
    def benchmark(func: Callable, iterations: int = 1000, *args, **kwargs) -> Dict[str, Any]:
        """
        基准测试函数

        Args:
            func: 要测试的函数
            iterations: 执行次数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            包含基准测试结果的字典
        """
        times = []
        results = []

        for _ in range(iterations):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            times.append(end_time - start_time)
            results.append(result)

        avg_time = sum(times) / len(times)
        min_time = min(times)
        max_time = max(times)

        return {
            'iterations': iterations,
            'avg_time': avg_time,
            'min_time': min_time,
            'max_time': max_time,
            'total_time': sum(times),
            'times': times,
            'results': results
        }

    @staticmethod
    def performance_decorator(measure_memory: bool = False):
        """
        性能测试装饰器

        Args:
            measure_memory: 是否测量内存使用

        Returns:
            装饰器函数
        """
        def decorator(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if measure_memory:
                    result = PerformanceTestUtils.measure_performance(func, *args, **kwargs)
                    print(f"{func.__name__} 执行时间: {result['execution_time']:.6f}s")
                    print(f"{func.__name__} 内存使用: {result['memory_used']:.2f}MB")
                    return result['result']
                else:
                    result = PerformanceTestUtils.measure_execution_time(func, *args, **kwargs)
                    print(f"{func.__name__} 执行时间: {result['execution_time']:.6f}s")
                    return result['result']
            return wrapper
        return decorator

    @staticmethod
    def profile_function(func: Callable, *args, **kwargs) -> Dict[str, Any]:
        """
        分析函数性能

        Args:
            func: 要分析的函数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            包含分析结果的字典
        """
        try:
            import cProfile
            import pstats
            import io

            pr = cProfile.Profile()
            pr.enable()

            result = func(*args, **kwargs)

            pr.disable()
            s = io.StringIO()
            ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
            ps.print_stats()

            profile_output = s.getvalue()

            return {
                'result': result,
                'profile_output': profile_output
            }
        except ImportError:
            # 如果没有 cProfile，回退到基本测量
            return PerformanceTestUtils.measure_performance(func, *args, **kwargs)

    @staticmethod
    def measure_cpu_usage(func: Callable, *args, **kwargs) -> Dict[str, Any]:
        """
        测量函数CPU使用

        Args:
            func: 要测量的函数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            包含CPU使用和结果的字典
        """
        import psutil

        process = psutil.Process()
        cpu_percentages = []

        # 开始监控CPU使用
        def monitor_cpu():
            while True:
                cpu_percentages.append(process.cpu_percent(interval=0.1))

        import threading
        monitor_thread = threading.Thread(target=monitor_cpu, daemon=True)
        monitor_thread.start()

        # 执行函数
        result = func(*args, **kwargs)

        # 等待监控线程结束
        import time
        time.sleep(0.2)  # 给监控线程一点时间

        # 计算平均CPU使用
        avg_cpu_usage = sum(cpu_percentages) / len(cpu_percentages) if cpu_percentages else 0

        return {
            'avg_cpu_usage': avg_cpu_usage,
            'cpu_percentages': cpu_percentages,
            'result': result
        }

    @staticmethod
    def compare_functions(functions: Dict[str, Callable], *args, **kwargs) -> Dict[str, Any]:
        """
        比较多个函数的性能

        Args:
            functions: 函数字典，键为函数名称，值为函数对象
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            包含比较结果的字典
        """
        comparisons = {}

        for name, func in functions.items():
            result = PerformanceTestUtils.measure_performance(func, *args, **kwargs)
            comparisons[name] = result

        # 找出最快的函数
        fastest = min(comparisons.items(), key=lambda x: x[1]['execution_time'])

        return {
            'comparisons': comparisons,
            'fastest': fastest[0],
            'fastest_time': fastest[1]['execution_time']
        }

    @staticmethod
    def memory_leak_test(func: Callable, iterations: int = 100, *args, **kwargs) -> Dict[str, Any]:
        """
        内存泄漏测试

        Args:
            func: 要测试的函数
            iterations: 执行次数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            包含内存泄漏测试结果的字典
        """
        import psutil

        process = psutil.Process()
        memory_usages = []

        for i in range(iterations):
            # 清理垃圾回收
            gc.collect()
            
            # 获取内存使用
            memory = process.memory_info().rss / 1024 / 1024  # MB
            memory_usages.append(memory)

            # 执行函数
            func(*args, **kwargs)

        # 清理垃圾回收
        gc.collect()
        final_memory = process.memory_info().rss / 1024 / 1024  # MB

        # 检查内存是否持续增长
        is_leaking = memory_usages[-1] > memory_usages[0] * 1.1  # 增长超过10%认为有泄漏

        return {
            'iterations': iterations,
            'initial_memory': memory_usages[0],
            'final_memory': final_memory,
            'memory_growth': final_memory - memory_usages[0],
            'memory_usages': memory_usages,
            'is_leaking': is_leaking
        }