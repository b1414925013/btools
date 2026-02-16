import logging
import os
import inspect
import sys
from datetime import datetime

class Logger:
    """
    日志记录器类，提供简单的日志记录功能
    
    Attributes:
        name (str): 日志记录器名称
        level (int): 日志级别
        file_path (str): 日志文件路径
        logger (logging.Logger): 内部logging模块的Logger实例
    """
    
    # 日志级别常量
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL
    
    def __init__(self, name=None, level=logging.INFO, file_path=None):
        """
        初始化Logger实例
        
        Args:
            name (str): 日志记录器名称，默认为当前调用方的项目名称
            level (int): 日志级别，默认为logging.INFO
            file_path (str): 日志文件路径，默认为None（仅输出到控制台）
        """
        # 如果未指定name，自动获取当前调用方的项目名称
        if name is None:
            # 获取调用栈
            stack = inspect.stack()
            # 找到调用方的帧（跳过Logger.__init__和Logger的其他方法）
            caller_frame = None
            for frame_info in stack[1:]:  # 从栈的第二个元素开始查找
                frame_file = frame_info.filename
                # 跳过当前文件和Python标准库文件
                if __file__ not in frame_file and 'site-packages' not in frame_file:
                    caller_frame = frame_info
                    break
            
            if caller_frame:
                # 获取调用方文件的目录路径
                caller_dir = os.path.dirname(os.path.abspath(caller_frame.filename))
                # 尝试获取项目根目录（寻找常见的项目文件如setup.py、pyproject.toml等）
                project_root = caller_dir
                while project_root and project_root != os.path.dirname(project_root):
                    if any(os.path.exists(os.path.join(project_root, f)) for f in ['setup.py', 'pyproject.toml', 'requirements.txt', 'README.md']):
                        break
                    project_root = os.path.dirname(project_root)
                # 使用项目根目录名称作为name
                name = os.path.basename(project_root) if project_root else os.path.basename(caller_dir)
            else:
                # 如果无法获取调用方信息，使用默认值
                name = "Default_AppName"
        
        self.name = name
        self.level = level
        self.file_path = file_path
        
        # 创建logger实例
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # 清除已有的handler
        self.logger.handlers.clear()
        
        # 创建formatter，添加文件路径、行号等信息
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')
        
        # 创建控制台handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # 如果指定了文件路径，创建文件handler
        if file_path:
            # 确保目录存在
            os.makedirs(os.path.dirname(file_path) if os.path.dirname(file_path) else '.', exist_ok=True)
            
            file_handler = logging.FileHandler(file_path, encoding='utf-8')
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
    
    def debug(self, message):
        """记录调试级别日志"""
        self.logger.debug(message, stacklevel=2)
    
    def info(self, message):
        """记录信息级别日志"""
        self.logger.info(message, stacklevel=2)
    
    def warning(self, message):
        """记录警告级别日志"""
        self.logger.warning(message, stacklevel=2)
    
    def error(self, message):
        """记录错误级别日志"""
        self.logger.error(message, stacklevel=2)
    
    def critical(self, message):
        """记录严重错误级别日志"""
        self.logger.critical(message, stacklevel=2)
