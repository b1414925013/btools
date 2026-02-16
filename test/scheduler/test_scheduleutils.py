# -*- coding: utf-8 -*-
"""
定时任务工具测试
"""
import unittest
import time
from btools.core.scheduler.scheduleutils import (
    ScheduleUtils, schedule_once, schedule_interval, schedule_at_fixed_rate,
    schedule_with_fixed_delay, cancel_task, cancel_all, start_scheduler, stop_scheduler
)


class TestScheduleUtils(unittest.TestCase):
    """
    定时任务工具测试类
    """

    def setUp(self):
        """
        测试前设置
        """
        self.scheduler = ScheduleUtils()
        self.scheduler.start()
        self.counter = 0
        self.last_execution_time = 0

    def tearDown(self):
        """
        测试后清理
        """
        self.scheduler.stop()
        stop_scheduler()  # 停止全局调度器

    def test_schedule_once(self):
        """
        测试一次性任务
        """
        def test_func():
            self.counter += 1

        # 安排一次性任务，延迟0.1秒
        task_id = self.scheduler.schedule_once(0.1, test_func)
        self.assertIsInstance(task_id, int)
        
        # 等待任务执行
        time.sleep(0.2)
        self.assertEqual(self.counter, 1)
        self.assertEqual(self.scheduler.get_task_count(), 0)

    def test_schedule_interval(self):
        """
        测试周期性任务
        """
        def test_func():
            self.counter += 1

        # 安排周期性任务，间隔0.1秒
        task_id = self.scheduler.schedule_interval(0.1, test_func)
        
        # 等待执行几次
        time.sleep(0.35)
        
        # 取消任务
        self.scheduler.cancel_task(task_id)
        
        # 确保任务被取消
        time.sleep(0.15)
        final_counter = self.counter
        time.sleep(0.15)
        self.assertEqual(self.counter, final_counter)

    def test_schedule_at_fixed_rate(self):
        """
        测试固定速率任务
        """
        def test_func():
            self.counter += 1

        # 安排固定速率任务，间隔0.1秒
        task_id = self.scheduler.schedule_at_fixed_rate(0.1, test_func)
        
        # 等待执行几次
        time.sleep(0.35)
        
        # 取消任务
        self.scheduler.cancel_task(task_id)
        
        # 确保任务被取消
        time.sleep(0.15)
        final_counter = self.counter
        time.sleep(0.15)
        self.assertEqual(self.counter, final_counter)

    def test_schedule_with_fixed_delay(self):
        """
        测试固定延迟任务
        """
        def test_func():
            self.counter += 1
            # 模拟任务执行时间
            time.sleep(0.05)

        # 安排固定延迟任务，延迟0.1秒
        task_id = self.scheduler.schedule_with_fixed_delay(0.1, test_func)
        
        # 等待执行几次
        time.sleep(0.4)
        
        # 取消任务
        self.scheduler.cancel_task(task_id)
        
        # 确保任务被取消
        time.sleep(0.15)
        final_counter = self.counter
        time.sleep(0.15)
        self.assertEqual(self.counter, final_counter)

    def test_cancel_task(self):
        """
        测试取消任务
        """
        def test_func():
            self.counter += 1

        # 安排任务
        task_id = self.scheduler.schedule_once(0.2, test_func)
        self.assertEqual(self.scheduler.get_task_count(), 1)
        
        # 取消任务
        self.scheduler.cancel_task(task_id)
        self.assertEqual(self.scheduler.get_task_count(), 0)
        
        # 等待足够时间，确保任务未执行
        time.sleep(0.3)
        self.assertEqual(self.counter, 0)

    def test_cancel_all(self):
        """
        测试取消所有任务
        """
        def test_func1():
            self.counter += 1

        def test_func2():
            self.counter += 1

        # 安排多个任务
        self.scheduler.schedule_once(0.2, test_func1)
        self.scheduler.schedule_once(0.3, test_func2)
        self.assertEqual(self.scheduler.get_task_count(), 2)
        
        # 取消所有任务
        self.scheduler.cancel_all()
        self.assertEqual(self.scheduler.get_task_count(), 0)
        
        # 等待足够时间，确保任务未执行
        time.sleep(0.4)
        self.assertEqual(self.counter, 0)

    def test_is_running(self):
        """
        测试调度器运行状态
        """
        self.assertTrue(self.scheduler.is_running())
        self.scheduler.stop()
        self.assertFalse(self.scheduler.is_running())

    def test_get_task_count(self):
        """
        测试获取任务数量
        """
        def test_func():
            pass

        # 初始任务数量
        self.assertEqual(self.scheduler.get_task_count(), 0)
        
        # 安排任务
        self.scheduler.schedule_once(0.1, test_func)
        self.assertEqual(self.scheduler.get_task_count(), 1)
        
        # 等待任务执行
        time.sleep(0.2)
        self.assertEqual(self.scheduler.get_task_count(), 0)

    def test_global_scheduler(self):
        """
        测试全局调度器
        """
        def test_func():
            self.counter += 1

        # 使用全局调度器安排任务
        task_id = schedule_once(0.1, test_func)
        self.assertIsInstance(task_id, int)
        
        # 等待任务执行
        time.sleep(0.2)
        self.assertEqual(self.counter, 1)

    def test_global_schedule_interval(self):
        """
        测试全局调度器的周期性任务
        """
        def test_func():
            self.counter += 1

        # 使用全局调度器安排周期性任务
        task_id = schedule_interval(0.1, test_func)
        
        # 等待执行几次
        time.sleep(0.35)
        
        # 取消任务
        cancel_task(task_id)
        
        # 确保任务被取消
        time.sleep(0.15)
        final_counter = self.counter
        time.sleep(0.15)
        self.assertEqual(self.counter, final_counter)

    def test_global_cancel_all(self):
        """
        测试全局调度器取消所有任务
        """
        def test_func():
            self.counter += 1

        # 使用全局调度器安排任务
        schedule_once(0.2, test_func)
        schedule_once(0.3, test_func)
        
        # 取消所有任务
        cancel_all()
        
        # 等待足够时间，确保任务未执行
        time.sleep(0.4)
        self.assertEqual(self.counter, 0)

    def test_start_stop_scheduler(self):
        """
        测试启动和停止全局调度器
        """
        start_scheduler()
        # 这里不需要断言，只要不报错即可
        stop_scheduler()

    def test_task_with_arguments(self):
        """
        测试带参数的任务
        """
        def test_func(a, b, c=0):
            self.counter = a + b + c

        # 安排带参数的任务
        self.scheduler.schedule_once(0.1, test_func, 1, 2, c=3)
        
        # 等待任务执行
        time.sleep(0.2)
        self.assertEqual(self.counter, 6)

    def test_task_execution_time(self):
        """
        测试任务执行时间（用于固定延迟任务）
        """
        def test_func():
            current_time = time.time()
            if self.last_execution_time > 0:
                execution_interval = current_time - self.last_execution_time
                # 确保执行间隔合理
                self.assertGreaterEqual(execution_interval, 0.08)  # 允许一定误差
            self.last_execution_time = current_time
            self.counter += 1
            # 模拟任务执行时间
            time.sleep(0.05)

        # 安排固定延迟任务
        task_id = self.scheduler.schedule_with_fixed_delay(0.1, test_func)
        
        # 等待执行几次
        time.sleep(0.4)
        
        # 取消任务
        self.scheduler.cancel_task(task_id)


if __name__ == '__main__':
    unittest.main()
