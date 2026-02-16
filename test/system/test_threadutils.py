# -*- coding: utf-8 -*-
"""
线程工具测试
"""
import unittest
import time
import threading
from btools.core.system.threadutils import (
    ThreadUtils, ThreadPool, ThreadLocal, create_thread, start_thread,
    wait_for_threads, run_in_threadpool, run_with_timeout,
    get_current_thread_name, get_current_thread_id, sleep
)


class TestThreadUtils(unittest.TestCase):
    """
    线程工具测试类
    """

    def setUp(self):
        """
        测试前设置
        """
        self.counter = 0
        self.lock = threading.Lock()

    def test_create_thread(self):
        """
        测试创建线程
        """
        def test_func():
            with self.lock:
                self.counter += 1

        # 测试创建线程
        thread = ThreadUtils.create_thread(test_func)
        self.assertIsInstance(thread, threading.Thread)

        # 测试启动线程
        thread.start()
        thread.join()
        self.assertEqual(self.counter, 1)

    def test_start_thread(self):
        """
        测试创建并启动线程
        """
        def test_func():
            with self.lock:
                self.counter += 1

        # 测试启动线程
        thread = ThreadUtils.start_thread(test_func)
        self.assertIsInstance(thread, threading.Thread)
        thread.join()
        self.assertEqual(self.counter, 1)

    def test_wait_for_threads(self):
        """
        测试等待多个线程完成
        """
        def test_func():
            time.sleep(0.1)
            with self.lock:
                self.counter += 1

        # 创建多个线程
        threads = []
        for _ in range(3):
            thread = ThreadUtils.start_thread(test_func)
            threads.append(thread)

        # 等待所有线程完成
        result = ThreadUtils.wait_for_threads(threads, timeout=1.0)
        self.assertTrue(result)
        self.assertEqual(self.counter, 3)

    def test_run_in_threadpool(self):
        """
        测试在线程池中运行多个函数
        """
        def test_func(x):
            time.sleep(0.1)
            return x * 2

        # 测试线程池
        funcs = [test_func, test_func, test_func]
        args_list = [(1,), (2,), (3,)]
        results = ThreadUtils.run_in_threadpool(funcs, args_list)
        self.assertEqual(len(results), 3)
        self.assertIn(2, results)
        self.assertIn(4, results)
        self.assertIn(6, results)

    def test_run_with_timeout(self):
        """
        测试带超时的函数执行
        """
        def test_func():
            time.sleep(0.1)
            return "success"

        def test_func_timeout():
            time.sleep(0.5)
            return "success"

        # 测试正常执行
        result = ThreadUtils.run_with_timeout(test_func, timeout=0.2)
        self.assertEqual(result, "success")

        # 测试超时
        with self.assertRaises(TimeoutError):
            ThreadUtils.run_with_timeout(test_func_timeout, timeout=0.2)

    def test_get_current_thread_info(self):
        """
        测试获取当前线程信息
        """
        # 测试获取线程名称
        thread_name = ThreadUtils.get_current_thread_name()
        self.assertIsInstance(thread_name, str)

        # 测试获取线程ID
        thread_id = ThreadUtils.get_current_thread_id()
        self.assertIsInstance(thread_id, int)

    def test_sleep(self):
        """
        测试线程睡眠
        """
        start_time = time.time()
        ThreadUtils.sleep(0.1)
        end_time = time.time()
        self.assertGreaterEqual(end_time - start_time, 0.1)

    def test_thread_pool(self):
        """
        测试线程池
        """
        def test_func(x):
            time.sleep(0.1)
            return x * 2

        # 测试线程池
        pool = ThreadPool(max_workers=2)
        
        # 测试提交任务
        future1 = pool.submit(test_func, 1)
        future2 = pool.submit(test_func, 2)
        
        # 测试获取结果
        result1 = future1.result()
        result2 = future2.result()
        self.assertEqual(result1, 2)
        self.assertEqual(result2, 4)
        
        # 测试map方法
        results = pool.map(test_func, [3, 4])
        self.assertEqual(results, [6, 8])
        
        # 测试关闭线程池
        pool.shutdown()

    def test_thread_local(self):
        """
        测试线程本地存储
        """
        thread_local = ThreadLocal()

        # 测试设置和获取值
        thread_local.set("test_key", "test_value")
        value = thread_local.get("test_key")
        self.assertEqual(value, "test_value")

        # 测试默认值
        default_value = thread_local.get("non_existent_key", "default")
        self.assertEqual(default_value, "default")

        # 测试移除值
        thread_local.remove("test_key")
        value = thread_local.get("test_key")
        self.assertIsNone(value)

        # 测试清空
        thread_local.set("key1", "value1")
        thread_local.set("key2", "value2")
        thread_local.clear()
        value1 = thread_local.get("key1")
        value2 = thread_local.get("key2")
        self.assertIsNone(value1)
        self.assertIsNone(value2)

    def test_convenience_functions(self):
        """
        测试便捷函数
        """
        def test_func():
            with self.lock:
                self.counter += 1

        # 测试create_thread便捷函数
        thread = create_thread(test_func)
        self.assertIsInstance(thread, threading.Thread)

        # 测试start_thread便捷函数
        thread = start_thread(test_func)
        thread.join()
        self.assertEqual(self.counter, 1)

        # 测试get_current_thread_name便捷函数
        thread_name = get_current_thread_name()
        self.assertIsInstance(thread_name, str)

        # 测试get_current_thread_id便捷函数
        thread_id = get_current_thread_id()
        self.assertIsInstance(thread_id, int)

        # 测试sleep便捷函数
        start_time = time.time()
        sleep(0.1)
        end_time = time.time()
        self.assertGreaterEqual(end_time - start_time, 0.1)


if __name__ == '__main__':
    unittest.main()
