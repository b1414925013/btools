"""异常工具类"""
import traceback
import sys
import inspect
import datetime
from typing import Optional, List, Dict, Any


class ExceptionUtils:
    """异常工具类"""

    @staticmethod
    def get_stack_trace(exception: Exception) -> str:
        """
        获取异常堆栈信息
        
        Args:
            exception: 异常对象
            
        Returns:
            str: 堆栈信息字符串
        """
        return traceback.format_exc()

    @staticmethod
    def get_stack_trace_list(exception: Exception) -> List[str]:
        """
        获取异常堆栈信息列表
        
        Args:
            exception: 异常对象
            
        Returns:
            List[str]: 堆栈信息列表
        """
        return traceback.format_exception(type(exception), exception, exception.__traceback__)

    @staticmethod
    def get_exception_message(exception: Exception) -> str:
        """
        获取异常信息
        
        Args:
            exception: 异常对象
            
        Returns:
            str: 异常信息
        """
        return str(exception)

    @staticmethod
    def get_exception_type(exception: Exception) -> str:
        """
        获取异常类型
        
        Args:
            exception: 异常对象
            
        Returns:
            str: 异常类型
        """
        return exception.__class__.__name__

    @staticmethod
    def get_exception_module(exception: Exception) -> str:
        """
        获取异常模块
        
        Args:
            exception: 异常对象
            
        Returns:
            str: 异常模块
        """
        return exception.__class__.__module__

    @staticmethod
    def get_cause(exception: Exception) -> Optional[Exception]:
        """
        获取异常原因
        
        Args:
            exception: 异常对象
            
        Returns:
            Optional[Exception]: 异常原因
        """
        if hasattr(exception, '__cause__') and exception.__cause__:
            return exception.__cause__
        if hasattr(exception, 'cause') and exception.cause:
            return exception.cause
        return None

    @staticmethod
    def get_suppressed(exception: Exception) -> List[Exception]:
        """
        获取被抑制的异常
        
        Args:
            exception: 异常对象
            
        Returns:
            List[Exception]: 被抑制的异常列表
        """
        if hasattr(exception, '__suppressed__'):
            return list(exception.__suppressed__)
        return []

    @staticmethod
    def wrap_exception(exception: Exception, wrapper_class: type) -> Exception:
        """
        包装异常
        
        Args:
            exception: 原始异常
            wrapper_class: 包装异常类
            
        Returns:
            Exception: 包装后的异常
        """
        try:
            wrapper = wrapper_class(str(exception))
            wrapper.__cause__ = exception
            return wrapper
        except Exception:
            return exception

    @staticmethod
    def unwrap_exception(exception: Exception) -> Exception:
        """
        解包异常
        
        Args:
            exception: 包装异常
            
        Returns:
            Exception: 原始异常
        """
        cause = ExceptionUtils.get_cause(exception)
        if cause:
            return cause
        return exception

    @staticmethod
    def is_instance(exception: Exception, exception_type: type) -> bool:
        """
        检查异常类型
        
        Args:
            exception: 异常对象
            exception_type: 异常类型
            
        Returns:
            bool: 如果是指定类型则返回True，否则返回False
        """
        return isinstance(exception, exception_type)

    @staticmethod
    def contains_instance(exception: Exception, exception_type: type) -> bool:
        """
        检查异常链中是否包含指定类型
        
        Args:
            exception: 异常对象
            exception_type: 异常类型
            
        Returns:
            bool: 如果包含则返回True，否则返回False
        """
        current = exception
        while current:
            if isinstance(current, exception_type):
                return True
            current = ExceptionUtils.get_cause(current)
        return False

    @staticmethod
    def get_stack_frame_info(frame_index: int = 0) -> Dict[str, Any]:
        """
        获取堆栈帧信息
        
        Args:
            frame_index: 帧索引，0表示当前帧
            
        Returns:
            Dict[str, Any]: 堆栈帧信息
        """
        try:
            frames = inspect.stack()
            if frame_index < len(frames):
                frame = frames[frame_index + 1]  # +1 跳过当前函数
                return {
                    'filename': frame.filename,
                    'line_number': frame.lineno,
                    'function': frame.function,
                    'code_context': frame.code_context
                }
        except Exception:
            pass
        return {}

    @staticmethod
    def get_caller_info() -> Dict[str, Any]:
        """
        获取调用者信息
        
        Returns:
            Dict[str, Any]: 调用者信息
        """
        return ExceptionUtils.get_stack_frame_info(1)

    @staticmethod
    def log_exception(exception: Exception, logger: Optional[Any] = None) -> None:
        """
        记录异常
        
        Args:
            exception: 异常对象
            logger: 日志对象，默认为None（使用print）
        """
        stack_trace = ExceptionUtils.get_stack_trace(exception)
        if logger and hasattr(logger, 'error'):
            logger.error(stack_trace)
        else:
            print(stack_trace, file=sys.stderr)

    @staticmethod
    def format_exception(exception: Exception, include_stack: bool = True) -> str:
        """
        格式化异常信息
        
        Args:
            exception: 异常对象
            include_stack: 是否包含堆栈信息
            
        Returns:
            str: 格式化后的异常信息
        """
        parts = []
        parts.append(f"Exception Type: {ExceptionUtils.get_exception_type(exception)}")
        parts.append(f"Exception Message: {ExceptionUtils.get_exception_message(exception)}")
        parts.append(f"Exception Module: {ExceptionUtils.get_exception_module(exception)}")
        
        cause = ExceptionUtils.get_cause(exception)
        if cause:
            parts.append(f"Cause: {ExceptionUtils.get_exception_type(cause)}: {ExceptionUtils.get_exception_message(cause)}")
        
        suppressed = ExceptionUtils.get_suppressed(exception)
        if suppressed:
            parts.append(f"Suppressed Exceptions: {len(suppressed)}")
            for i, sup in enumerate(suppressed):
                parts.append(f"  {i+1}. {ExceptionUtils.get_exception_type(sup)}: {ExceptionUtils.get_exception_message(sup)}")
        
        if include_stack:
            parts.append("Stack Trace:")
            parts.append(ExceptionUtils.get_stack_trace(exception))
        
        return '\n'.join(parts)

    @staticmethod
    def get_exception_chain(exception: Exception) -> List[Exception]:
        """
        获取异常链
        
        Args:
            exception: 异常对象
            
        Returns:
            List[Exception]: 异常链列表
        """
        chain = []
        current = exception
        while current:
            chain.append(current)
            current = ExceptionUtils.get_cause(current)
        return chain

    @staticmethod
    def get_exception_chain_strings(exception: Exception) -> List[str]:
        """
        获取异常链字符串
        
        Args:
            exception: 异常对象
            
        Returns:
            List[str]: 异常链字符串列表
        """
        chain = ExceptionUtils.get_exception_chain(exception)
        return [f"{ExceptionUtils.get_exception_type(ex)}: {ExceptionUtils.get_exception_message(ex)}" for ex in chain]

    @staticmethod
    def retry_on_exception(func: callable, max_attempts: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)) -> Any:
        """
        异常重试
        
        Args:
            func: 要执行的函数
            max_attempts: 最大尝试次数
            delay: 重试延迟（秒）
            exceptions: 要捕获的异常类型
            
        Returns:
            Any: 函数返回值
            
        Raises:
            Exception: 如果所有尝试都失败则抛出最后一个异常
        """
        last_exception = None
        
        for attempt in range(max_attempts):
            try:
                return func()
            except exceptions as e:
                last_exception = e
                if attempt < max_attempts - 1:
                    import time
                    time.sleep(delay)
        
        if last_exception:
            raise last_exception
        raise Exception("Unknown error")

    @staticmethod
    def safe_call(func: callable, *args, **kwargs) -> Optional[Any]:
        """
        安全调用函数
        
        Args:
            func: 要执行的函数
            *args: 位置参数
            **kwargs: 关键字参数
            
        Returns:
            Optional[Any]: 函数返回值，如果发生异常则返回None
        """
        try:
            return func(*args, **kwargs)
        except Exception:
            return None

    @staticmethod
    def safe_call_with_default(func: callable, default: Any, *args, **kwargs) -> Any:
        """
        安全调用函数，带默认值
        
        Args:
            func: 要执行的函数
            default: 默认返回值
            *args: 位置参数
            **kwargs: 关键字参数
            
        Returns:
            Any: 函数返回值，如果发生异常则返回默认值
        """
        try:
            return func(*args, **kwargs)
        except Exception:
            return default

    @staticmethod
    def catch_and_log(func: callable, logger: Optional[Any] = None, *args, **kwargs) -> Optional[Any]:
        """
        捕获并记录异常
        
        Args:
            func: 要执行的函数
            logger: 日志对象
            *args: 位置参数
            **kwargs: 关键字参数
            
        Returns:
            Optional[Any]: 函数返回值，如果发生异常则返回None
        """
        try:
            return func(*args, **kwargs)
        except Exception as e:
            ExceptionUtils.log_exception(e, logger)
            return None

    @staticmethod
    def get_exception_time(exception: Exception) -> datetime.datetime:
        """
        获取异常发生时间
        
        Args:
            exception: 异常对象
            
        Returns:
            datetime.datetime: 异常发生时间
        """
        # 简单实现，实际应该在异常发生时记录时间
        return datetime.datetime.now()

    @staticmethod
    def serialize_exception(exception: Exception) -> Dict[str, Any]:
        """
        序列化异常
        
        Args:
            exception: 异常对象
            
        Returns:
            Dict[str, Any]: 序列化后的异常
        """
        return {
            'type': ExceptionUtils.get_exception_type(exception),
            'message': ExceptionUtils.get_exception_message(exception),
            'module': ExceptionUtils.get_exception_module(exception),
            'stack_trace': ExceptionUtils.get_stack_trace(exception),
            'cause': ExceptionUtils.serialize_exception(ExceptionUtils.get_cause(exception)) if ExceptionUtils.get_cause(exception) else None,
            'suppressed': [ExceptionUtils.serialize_exception(sup) for sup in ExceptionUtils.get_suppressed(exception)]
        }

    @staticmethod
    def deserialize_exception(data: Dict[str, Any]) -> Exception:
        """
        反序列化异常
        
        Args:
            data: 序列化数据
            
        Returns:
            Exception: 反序列化后的异常
        """
        try:
            # 简单实现，实际应该根据类型创建具体异常
            exception = Exception(data.get('message', ''))
            return exception
        except Exception:
            return Exception('Failed to deserialize exception')

    @staticmethod
    def get_line_number(exception: Exception) -> int:
        """
        获取异常发生行号
        
        Args:
            exception: 异常对象
            
        Returns:
            int: 行号
        """
        try:
            tb_lines = traceback.format_exc().split('\n')
            for line in tb_lines:
                if ', line ' in line:
                    parts = line.split(', line ')
                    if len(parts) > 1:
                        line_num = parts[1].split(',')[0]
                        if line_num.isdigit():
                            return int(line_num)
        except Exception:
            pass
        return 0

    @staticmethod
    def get_file_name(exception: Exception) -> str:
        """
        获取异常发生文件名
        
        Args:
            exception: 异常对象
            
        Returns:
            str: 文件名
        """
        try:
            tb_lines = traceback.format_exc().split('\n')
            for line in tb_lines:
                if 'File "' in line:
                    parts = line.split('File "')
                    if len(parts) > 1:
                        file_name = parts[1].split('",')[0]
                        return file_name
        except Exception:
            pass
        return ''

    @staticmethod
    def get_function_name(exception: Exception) -> str:
        """
        获取异常发生函数名
        
        Args:
            exception: 异常对象
            
        Returns:
            str: 函数名
        """
        try:
            tb_lines = traceback.format_exc().split('\n')
            for line in tb_lines:
                if 'in ' in line and line.strip().startswith('in '):
                    func_name = line.strip().split('in ')[1]
                    return func_name
        except Exception:
            pass
        return ''