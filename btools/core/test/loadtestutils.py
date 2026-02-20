#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
负载测试工具类

提供负载测试工具，模拟并发请求等功能
"""
import concurrent.futures
import time
import threading
from typing import Callable, List, Dict, Any, Optional


class LoadTestUtils:
    """
    负载测试工具类
    """

    @staticmethod
    def concurrent_execution(func: Callable, concurrency: int, iterations: int = 1, *args, **kwargs) -> Dict[str, Any]:
        """
        并发执行函数

        Args:
            func: 要执行的函数
            concurrency: 并发数
            iterations: 每个线程执行次数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            包含执行结果的字典
        """
        results = []
        errors = []
        execution_times = []

        def worker():
            for _ in range(iterations):
                start_time = time.time()
                try:
                    result = func(*args, **kwargs)
                    results.append(result)
                except Exception as e:
                    errors.append(str(e))
                finally:
                    end_time = time.time()
                    execution_times.append(end_time - start_time)

        # 使用线程池执行
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
            futures = [executor.submit(worker) for _ in range(concurrency)]
            concurrent.futures.wait(futures)

        total_requests = concurrency * iterations
        success_requests = len(results)
        error_requests = len(errors)

        return {
            'concurrency': concurrency,
            'iterations': iterations,
            'total_requests': total_requests,
            'success_requests': success_requests,
            'error_requests': error_requests,
            'execution_times': execution_times,
            'avg_response_time': sum(execution_times) / len(execution_times) if execution_times else 0,
            'min_response_time': min(execution_times) if execution_times else 0,
            'max_response_time': max(execution_times) if execution_times else 0,
            'results': results,
            'errors': errors
        }

    @staticmethod
    def load_test(func: Callable, concurrency: int, duration: int = 10, *args, **kwargs) -> Dict[str, Any]:
        """
        负载测试

        Args:
            func: 要测试的函数
            concurrency: 并发数
            duration: 测试持续时间（秒）
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            包含测试结果的字典
        """
        results = []
        errors = []
        execution_times = []
        start_time = time.time()
        stop_event = threading.Event()

        def worker():
            while not stop_event.is_set():
                worker_start_time = time.time()
                try:
                    result = func(*args, **kwargs)
                    results.append(result)
                except Exception as e:
                    errors.append(str(e))
                finally:
                    worker_end_time = time.time()
                    execution_times.append(worker_end_time - worker_start_time)

        # 启动线程
        threads = []
        for _ in range(concurrency):
            thread = threading.Thread(target=worker, daemon=True)
            threads.append(thread)
            thread.start()

        # 等待指定时间
        time.sleep(duration)

        # 停止测试
        stop_event.set()
        for thread in threads:
            thread.join(timeout=1)

        end_time = time.time()
        actual_duration = end_time - start_time
        total_requests = len(results) + len(errors)
        rps = total_requests / actual_duration if actual_duration > 0 else 0

        return {
            'concurrency': concurrency,
            'duration': duration,
            'actual_duration': actual_duration,
            'total_requests': total_requests,
            'requests_per_second': rps,
            'success_requests': len(results),
            'error_requests': len(errors),
            'execution_times': execution_times,
            'avg_response_time': sum(execution_times) / len(execution_times) if execution_times else 0,
            'min_response_time': min(execution_times) if execution_times else 0,
            'max_response_time': max(execution_times) if execution_times else 0,
            'results': results,
            'errors': errors
        }

    @staticmethod
    def step_load_test(func: Callable, start_concurrency: int, max_concurrency: int, step: int, duration_per_step: int = 5, *args, **kwargs) -> List[Dict[str, Any]]:
        """
        阶梯负载测试

        Args:
            func: 要测试的函数
            start_concurrency: 起始并发数
            max_concurrency: 最大并发数
            step: 步长
            duration_per_step: 每步持续时间（秒）
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            各阶梯测试结果列表
        """
        results = []

        for concurrency in range(start_concurrency, max_concurrency + 1, step):
            print(f"Running load test with concurrency: {concurrency}")
            test_result = LoadTestUtils.load_test(
                func, concurrency, duration_per_step, *args, **kwargs
            )
            results.append(test_result)

        return results

    @staticmethod
    def stress_test(func: Callable, initial_concurrency: int = 10, increment: int = 10, duration_per_level: int = 10, max_errors: int = 5, *args, **kwargs) -> Dict[str, Any]:
        """
        压力测试

        Args:
            func: 要测试的函数
            initial_concurrency: 初始并发数
            increment: 每次增加的并发数
            duration_per_level: 每个并发级别持续时间（秒）
            max_errors: 最大错误数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            压力测试结果
        """
        concurrency = initial_concurrency
        test_results = []
        total_errors = 0

        while total_errors < max_errors:
            print(f"Running stress test with concurrency: {concurrency}")
            test_result = LoadTestUtils.load_test(
                func, concurrency, duration_per_level, *args, **kwargs
            )
            test_results.append(test_result)

            total_errors += test_result['error_requests']
            if total_errors >= max_errors:
                break

            concurrency += increment

        # 找出最大处理能力
        max_throughput_result = max(test_results, key=lambda x: x['requests_per_second'])

        return {
            'test_results': test_results,
            'max_concurrency_reached': concurrency,
            'max_throughput': max_throughput_result['requests_per_second'],
            'max_throughput_concurrency': max_throughput_result['concurrency'],
            'total_errors': total_errors
        }

    @staticmethod
    def benchmark_throughput(func: Callable, concurrency_levels: List[int], iterations: int = 100, *args, **kwargs) -> List[Dict[str, Any]]:
        """
        基准测试吞吐量

        Args:
            func: 要测试的函数
            concurrency_levels: 并发级别列表
            iterations: 每个并发级别执行次数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            各并发级别测试结果列表
        """
        results = []

        for concurrency in concurrency_levels:
            print(f"Benchmarking throughput with concurrency: {concurrency}")
            
            start_time = time.time()
            test_result = LoadTestUtils.concurrent_execution(
                func, concurrency, iterations // concurrency, *args, **kwargs
            )
            end_time = time.time()

            total_time = end_time - start_time
            throughput = test_result['total_requests'] / total_time if total_time > 0 else 0

            result = test_result.copy()
            result['throughput'] = throughput
            result['total_time'] = total_time
            results.append(result)

        return results

    @staticmethod
    def simulate_api_load(url: str, concurrency: int, duration: int, method: str = 'GET', headers: Dict = None, data: Dict = None) -> Dict[str, Any]:
        """
        模拟 API 负载

        Args:
            url: API URL
            concurrency: 并发数
            duration: 持续时间（秒）
            method: HTTP 方法
            headers: 请求头
            data: 请求数据

        Returns:
            负载测试结果
        """
        import requests

        def make_request():
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers, timeout=30)
            elif method.upper() == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=30)
            elif method.upper() == 'PUT':
                response = requests.put(url, json=data, headers=headers, timeout=30)
            elif method.upper() == 'DELETE':
                response = requests.delete(url, headers=headers, timeout=30)
            else:
                raise ValueError(f"Unsupported method: {method}")
            response.raise_for_status()
            return response.status_code

        return LoadTestUtils.load_test(make_request, concurrency, duration)

    @staticmethod
    def distributed_load_test(func: Callable, workers: List[str], concurrency_per_worker: int, duration: int, *args, **kwargs) -> Dict[str, Any]:
        """
        分布式负载测试

        Args:
            func: 要测试的函数
            workers: 工作节点列表
            concurrency_per_worker: 每个工作节点的并发数
            duration: 测试持续时间（秒）
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            分布式测试结果
        """
        # 注意：此功能需要在分布式环境中实现
        # 这里仅提供框架，实际实现需要根据具体的分布式架构调整
        results = []

        # 模拟分布式执行
        for worker in workers:
            print(f"Running load test on worker: {worker}")
            # 在实际实现中，这里应该通过网络调用远程执行测试
            # 这里仅模拟结果
            worker_result = LoadTestUtils.load_test(
                func, concurrency_per_worker, duration, *args, **kwargs
            )
            worker_result['worker'] = worker
            results.append(worker_result)

        # 汇总结果
        total_requests = sum(r['total_requests'] for r in results)
        total_success = sum(r['success_requests'] for r in results)
        total_errors = sum(r['error_requests'] for r in results)
        all_execution_times = [t for r in results for t in r['execution_times']]

        return {
            'workers': workers,
            'concurrency_per_worker': concurrency_per_worker,
            'duration': duration,
            'total_requests': total_requests,
            'total_success': total_success,
            'total_errors': total_errors,
            'avg_response_time': sum(all_execution_times) / len(all_execution_times) if all_execution_times else 0,
            'min_response_time': min(all_execution_times) if all_execution_times else 0,
            'max_response_time': max(all_execution_times) if all_execution_times else 0,
            'requests_per_second': total_requests / duration if duration > 0 else 0,
            'worker_results': results
        }

    @staticmethod
    def calculate_percentiles(times: List[float], percentiles: List[float]) -> Dict[str, float]:
        """
        计算响应时间百分位

        Args:
            times: 响应时间列表
            percentiles: 要计算的百分位列表（如 [50, 90, 95, 99]）

        Returns:
            百分位结果字典
        """
        if not times:
            return {}

        sorted_times = sorted(times)
        results = {}

        for p in percentiles:
            index = int(len(sorted_times) * p / 100)
            if index >= len(sorted_times):
                index = len(sorted_times) - 1
            results[f'p{p}'] = sorted_times[index]

        return results