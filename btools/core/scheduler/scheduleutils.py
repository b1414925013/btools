# -*- coding: utf-8 -*-
"""
定时任务工具模块
"""
import sched
import threading
import time
from typing import Callable, Optional, Any


class ScheduleUtils:
    """
    定时任务工具类
    提供定时任务的创建、管理和执行功能
    """

    def __init__(self):
        """
        初始化定时任务工具
        """
        self._scheduler = sched.scheduler(time.time, time.sleep)
        self._running = False
        self._thread = None
        self._tasks = {}
        self._lock = threading.RLock()

    def start(self):
        """
        启动调度器
        """
        with self._lock:
            if not self._running:
                self._running = True
                self._thread = threading.Thread(target=self._run_scheduler, daemon=True)
                self._thread.start()

    def stop(self):
        """
        停止调度器
        """
        with self._lock:
            if self._running:
                self._running = False
                self._scheduler.empty()
                if self._thread:
                    self._thread.join(timeout=1.0)
                self._tasks.clear()

    def _run_scheduler(self):
        """
        运行调度器的线程函数
        """
        while self._running:
            if self._scheduler.queue:
                self._scheduler.run(blocking=False)
            time.sleep(0.1)

    def schedule_once(self, delay: float, func: Callable, *args: Any, **kwargs: Any) -> int:
        """
        安排一次性任务

        Args:
            delay: 延迟时间（秒）
            func: 要执行的函数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            任务ID
        """
        with self._lock:
            task_id = id(func)
            event = self._scheduler.enter(delay, 1, self._wrap_task, (task_id, func, args, kwargs))
            self._tasks[task_id] = event
            return task_id

    def schedule_interval(self, interval: float, func: Callable, *args: Any, **kwargs: Any) -> int:
        """
        安排周期性任务

        Args:
            interval: 执行间隔（秒）
            func: 要执行的函数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            任务ID
        """
        with self._lock:
            task_id = id(func)
            
            def interval_task():
                try:
                    func(*args, **kwargs)
                finally:
                    if self._running and task_id in self._tasks:
                        self._tasks[task_id] = self._scheduler.enter(interval, 1, interval_task)

            event = self._scheduler.enter(interval, 1, interval_task)
            self._tasks[task_id] = event
            return task_id

    def schedule_at_fixed_rate(self, interval: float, func: Callable, *args: Any, **kwargs: Any) -> int:
        """
        按固定速率安排任务（不考虑任务执行时间）

        Args:
            interval: 执行间隔（秒）
            func: 要执行的函数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            任务ID
        """
        return self.schedule_interval(interval, func, *args, **kwargs)

    def schedule_with_fixed_delay(self, delay: float, func: Callable, *args: Any, **kwargs: Any) -> int:
        """
        按固定延迟安排任务（考虑任务执行时间）

        Args:
            delay: 执行延迟（秒）
            func: 要执行的函数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            任务ID
        """
        with self._lock:
            task_id = id(func)
            
            def delay_task():
                start_time = time.time()
                try:
                    func(*args, **kwargs)
                finally:
                    if self._running and task_id in self._tasks:
                        execution_time = time.time() - start_time
                        next_delay = max(0, delay - execution_time)
                        self._tasks[task_id] = self._scheduler.enter(next_delay, 1, delay_task)

            event = self._scheduler.enter(delay, 1, delay_task)
            self._tasks[task_id] = event
            return task_id

    def cancel_task(self, task_id: int):
        """
        取消指定任务

        Args:
            task_id: 任务ID
        """
        with self._lock:
            if task_id in self._tasks:
                try:
                    self._scheduler.cancel(self._tasks[task_id])
                except ValueError:
                    pass  # 任务可能已经执行
                del self._tasks[task_id]

    def cancel_all(self):
        """
        取消所有任务
        """
        with self._lock:
            self._scheduler.empty()
            self._tasks.clear()

    def _wrap_task(self, task_id: int, func: Callable, args: tuple, kwargs: dict):
        """
        包装任务执行

        Args:
            task_id: 任务ID
            func: 要执行的函数
            args: 函数参数
            kwargs: 函数关键字参数
        """
        try:
            func(*args, **kwargs)
        finally:
            with self._lock:
                if task_id in self._tasks:
                    del self._tasks[task_id]

    def is_running(self) -> bool:
        """
        检查调度器是否正在运行

        Returns:
            bool: 调度器运行状态
        """
        return self._running

    def get_task_count(self) -> int:
        """
        获取当前任务数量

        Returns:
            int: 任务数量
        """
        with self._lock:
            return len(self._tasks)


# 全局调度器实例
global_scheduler = ScheduleUtils()


def schedule_once(delay: float, func: Callable, *args: Any, **kwargs: Any) -> int:
    """
    安排一次性任务（使用全局调度器）

    Args:
        delay: 延迟时间（秒）
        func: 要执行的函数
        *args: 函数参数
        **kwargs: 函数关键字参数

    Returns:
        任务ID
    """
    global_scheduler.start()
    return global_scheduler.schedule_once(delay, func, *args, **kwargs)


def schedule_interval(interval: float, func: Callable, *args: Any, **kwargs: Any) -> int:
    """
    安排周期性任务（使用全局调度器）

    Args:
        interval: 执行间隔（秒）
        func: 要执行的函数
        *args: 函数参数
        **kwargs: 函数关键字参数

    Returns:
        任务ID
    """
    global_scheduler.start()
    return global_scheduler.schedule_interval(interval, func, *args, **kwargs)


def schedule_at_fixed_rate(interval: float, func: Callable, *args: Any, **kwargs: Any) -> int:
    """
    按固定速率安排任务（使用全局调度器）

    Args:
        interval: 执行间隔（秒）
        func: 要执行的函数
        *args: 函数参数
        **kwargs: 函数关键字参数

    Returns:
        任务ID
    """
    global_scheduler.start()
    return global_scheduler.schedule_at_fixed_rate(interval, func, *args, **kwargs)


def schedule_with_fixed_delay(delay: float, func: Callable, *args: Any, **kwargs: Any) -> int:
    """
    按固定延迟安排任务（使用全局调度器）

    Args:
        delay: 执行延迟（秒）
        func: 要执行的函数
        *args: 函数参数
        **kwargs: 函数关键字参数

    Returns:
        任务ID
    """
    global_scheduler.start()
    return global_scheduler.schedule_with_fixed_delay(delay, func, *args, **kwargs)


def cancel_task(task_id: int):
    """
    取消指定任务（使用全局调度器）

    Args:
        task_id: 任务ID
    """
    global_scheduler.cancel_task(task_id)


def cancel_all():
    """
    取消所有任务（使用全局调度器）
    """
    global_scheduler.cancel_all()


def start_scheduler():
    """
    启动全局调度器
    """
    global_scheduler.start()


def stop_scheduler():
    """
    停止全局调度器
    """
    global_scheduler.stop()
