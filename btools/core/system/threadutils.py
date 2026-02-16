# -*- coding: utf-8 -*-
"""
线程工具类模块
"""
import threading
import time
import concurrent.futures
from typing import Any, Callable, List, Optional, Tuple, Union


class ThreadUtils:
    """
    线程工具类
    提供线程操作的便捷方法
    """

    @staticmethod
    def create_thread(target: Callable, args: tuple = (), kwargs: Optional[dict] = None, 
                     daemon: bool = False, name: Optional[str] = None) -> threading.Thread:
        """
        创建线程

        Args:
            target: 线程目标函数
            args: 函数参数
            kwargs: 函数关键字参数
            daemon: 是否为守护线程
            name: 线程名称

        Returns:
            线程对象
        """
        if kwargs is None:
            kwargs = {}
        thread = threading.Thread(target=target, args=args, kwargs=kwargs, daemon=daemon, name=name)
        return thread

    @staticmethod
    def start_thread(target: Callable, args: tuple = (), kwargs: Optional[dict] = None, 
                    daemon: bool = False, name: Optional[str] = None) -> threading.Thread:
        """
        创建并启动线程

        Args:
            target: 线程目标函数
            args: 函数参数
            kwargs: 函数关键字参数
            daemon: 是否为守护线程
            name: 线程名称

        Returns:
            线程对象
        """
        thread = ThreadUtils.create_thread(target, args, kwargs, daemon, name)
        thread.start()
        return thread

    @staticmethod
    def wait_for_threads(threads: List[threading.Thread], timeout: Optional[float] = None) -> bool:
        """
        等待多个线程完成

        Args:
            threads: 线程列表
            timeout: 超时时间（秒）

        Returns:
            是否所有线程都在超时前完成
        """
        for thread in threads:
            if thread.is_alive():
                thread.join(timeout)
                if thread.is_alive():
                    return False
        return True

    @staticmethod
    def run_in_threadpool(funcs: List[Callable], args_list: Optional[List[tuple]] = None, 
                         max_workers: Optional[int] = None) -> List[Any]:
        """
        在线程池中运行多个函数

        Args:
            funcs: 函数列表
            args_list: 参数列表，每个元素是一个元组
            max_workers: 最大工作线程数

        Returns:
            函数执行结果列表
        """
        if args_list is None:
            args_list = [() for _ in funcs]
        
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_func = {executor.submit(func, *args): func for func, args in zip(funcs, args_list)}
            for future in concurrent.futures.as_completed(future_to_func):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as exc:
                    results.append(None)
        return results

    @staticmethod
    def run_with_timeout(func: Callable, args: tuple = (), kwargs: Optional[dict] = None, 
                        timeout: float = 5.0) -> Any:
        """
        带超时的函数执行

        Args:
            func: 要执行的函数
            args: 函数参数
            kwargs: 函数关键字参数
            timeout: 超时时间（秒）

        Returns:
            函数执行结果

        Raises:
            TimeoutError: 函数执行超时
        """
        if kwargs is None:
            kwargs = {}
        
        result = [None]
        exception = [None]
        
        def wrapper():
            try:
                result[0] = func(*args, **kwargs)
            except Exception as e:
                exception[0] = e
        
        thread = ThreadUtils.start_thread(wrapper, daemon=True)
        thread.join(timeout)
        
        if thread.is_alive():
            raise TimeoutError(f"Function execution timed out after {timeout} seconds")
        
        if exception[0]:
            raise exception[0]
        
        return result[0]

    @staticmethod
    def get_current_thread_name() -> str:
        """
        获取当前线程名称

        Returns:
            线程名称
        """
        return threading.current_thread().name

    @staticmethod
    def get_current_thread_id() -> int:
        """
        获取当前线程ID

        Returns:
            线程ID
        """
        return threading.current_thread().ident

    @staticmethod
    def sleep(seconds: float):
        """
        线程睡眠

        Args:
            seconds: 睡眠时间（秒）
        """
        time.sleep(seconds)


class ThreadPool:
    """
    线程池类
    提供线程池的创建和管理
    """

    def __init__(self, max_workers: Optional[int] = None):
        """
        初始化线程池

        Args:
            max_workers: 最大工作线程数
        """
        self._executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)
        self._futures = []

    def submit(self, func: Callable, *args: Any, **kwargs: Any) -> concurrent.futures.Future:
        """
        提交任务到线程池

        Args:
            func: 要执行的函数
            *args: 函数参数
            **kwargs: 函数关键字参数

        Returns:
            任务未来对象
        """
        future = self._executor.submit(func, *args, **kwargs)
        self._futures.append(future)
        return future

    def map(self, func: Callable, *iterables: Any) -> List[Any]:
        """
        映射函数到可迭代对象

        Args:
            func: 要执行的函数
            *iterables: 可迭代对象

        Returns:
            函数执行结果列表
        """
        return list(self._executor.map(func, *iterables))

    def shutdown(self, wait: bool = True):
        """
        关闭线程池

        Args:
            wait: 是否等待所有任务完成
        """
        self._executor.shutdown(wait=wait)

    def wait_completion(self, timeout: Optional[float] = None) -> bool:
        """
        等待所有任务完成

        Args:
            timeout: 超时时间（秒）

        Returns:
            是否所有任务都在超时前完成
        """
        try:
            for future in concurrent.futures.as_completed(self._futures, timeout=timeout):
                pass
            return True
        except concurrent.futures.TimeoutError:
            return False


class ThreadLocal:
    """
    线程本地存储类
    提供线程本地变量的便捷访问
    """

    def __init__(self):
        """
        初始化线程本地存储
        """
        self._local = threading.local()

    def set(self, key: str, value: Any):
        """
        设置线程本地变量

        Args:
            key: 变量名
            value: 变量值
        """
        setattr(self._local, key, value)

    def get(self, key: str, default: Any = None) -> Any:
        """
        获取线程本地变量

        Args:
            key: 变量名
            default: 默认值

        Returns:
            变量值或默认值
        """
        return getattr(self._local, key, default)

    def remove(self, key: str):
        """
        移除线程本地变量

        Args:
            key: 变量名
        """
        if hasattr(self._local, key):
            delattr(self._local, key)

    def clear(self):
        """
        清空线程本地变量
        """
        for attr in dir(self._local):
            if not attr.startswith('__'):
                delattr(self._local, attr)


# 全局线程本地存储
thread_local = ThreadLocal()


# 便捷函数

def create_thread(target: Callable, args: tuple = (), kwargs: Optional[dict] = None, 
                 daemon: bool = False, name: Optional[str] = None) -> threading.Thread:
    """
    创建线程

    Args:
        target: 线程目标函数
        args: 函数参数
        kwargs: 函数关键字参数
        daemon: 是否为守护线程
        name: 线程名称

    Returns:
        线程对象
    """
    return ThreadUtils.create_thread(target, args, kwargs, daemon, name)


def start_thread(target: Callable, args: tuple = (), kwargs: Optional[dict] = None, 
                daemon: bool = False, name: Optional[str] = None) -> threading.Thread:
    """
    创建并启动线程

    Args:
        target: 线程目标函数
        args: 函数参数
        kwargs: 函数关键字参数
        daemon: 是否为守护线程
        name: 线程名称

    Returns:
        线程对象
    """
    return ThreadUtils.start_thread(target, args, kwargs, daemon, name)


def wait_for_threads(threads: List[threading.Thread], timeout: Optional[float] = None) -> bool:
    """
    等待多个线程完成

    Args:
        threads: 线程列表
        timeout: 超时时间（秒）

    Returns:
        是否所有线程都在超时前完成
    """
    return ThreadUtils.wait_for_threads(threads, timeout)


def run_in_threadpool(funcs: List[Callable], args_list: Optional[List[tuple]] = None, 
                     max_workers: Optional[int] = None) -> List[Any]:
    """
    在线程池中运行多个函数

    Args:
        funcs: 函数列表
        args_list: 参数列表，每个元素是一个元组
        max_workers: 最大工作线程数

    Returns:
        函数执行结果列表
    """
    return ThreadUtils.run_in_threadpool(funcs, args_list, max_workers)


def run_with_timeout(func: Callable, args: tuple = (), kwargs: Optional[dict] = None, 
                    timeout: float = 5.0) -> Any:
    """
    带超时的函数执行

    Args:
        func: 要执行的函数
        args: 函数参数
        kwargs: 函数关键字参数
        timeout: 超时时间（秒）

    Returns:
        函数执行结果

    Raises:
        TimeoutError: 函数执行超时
    """
    return ThreadUtils.run_with_timeout(func, args, kwargs, timeout)


def get_current_thread_name() -> str:
    """
    获取当前线程名称

    Returns:
        线程名称
    """
    return ThreadUtils.get_current_thread_name()


def get_current_thread_id() -> int:
    """
    获取当前线程ID

    Returns:
        线程ID
    """
    return ThreadUtils.get_current_thread_id()


def sleep(seconds: float):
    """
    线程睡眠

    Args:
        seconds: 睡眠时间（秒）
    """
    ThreadUtils.sleep(seconds)
