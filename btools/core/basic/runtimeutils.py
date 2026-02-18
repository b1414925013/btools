#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
命令行工具类

提供命令行执行功能，包括执行命令、获取输出、判断执行结果等
"""
import os
import subprocess
import sys
from typing import Dict, Any, Optional, Tuple, Union


class RuntimeUtil:
    """
    命令行工具类
    """

    @staticmethod
    def exec(cmd: str, cwd: Optional[str] = None, shell: bool = True, timeout: Optional[float] = None) -> Tuple[int, str, str]:
        """
        执行命令并返回执行结果

        Args:
            cmd: 要执行的命令
            cwd: 工作目录
            shell: 是否使用shell执行
            timeout: 超时时间（秒）

        Returns:
            Tuple[int, str, str]: (返回码, 标准输出, 标准错误)
        """
        try:
            result = subprocess.run(
                cmd, 
                cwd=cwd, 
                shell=shell, 
                capture_output=True, 
                text=True, 
                timeout=timeout
            )
            return result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return -1, "", f"命令执行超时: {timeout}秒"
        except Exception as e:
            return -1, "", f"命令执行失败: {str(e)}"

    @staticmethod
    def execForStr(cmd: str, cwd: Optional[str] = None, shell: bool = True, timeout: Optional[float] = None) -> str:
        """
        执行命令并返回标准输出

        Args:
            cmd: 要执行的命令
            cwd: 工作目录
            shell: 是否使用shell执行
            timeout: 超时时间（秒）

        Returns:
            str: 命令的标准输出
        """
        _, stdout, _ = RuntimeUtil.exec(cmd, cwd, shell, timeout)
        return stdout.strip()

    @staticmethod
    def execForLines(cmd: str, cwd: Optional[str] = None, shell: bool = True, timeout: Optional[float] = None) -> list:
        """
        执行命令并返回标准输出的行列表

        Args:
            cmd: 要执行的命令
            cwd: 工作目录
            shell: 是否使用shell执行
            timeout: 超时时间（秒）

        Returns:
            list: 命令的标准输出行列表
        """
        stdout = RuntimeUtil.execForStr(cmd, cwd, shell, timeout)
        return stdout.splitlines() if stdout else []

    @staticmethod
    def execWait(cmd: str, cwd: Optional[str] = None, shell: bool = True, timeout: Optional[float] = None) -> bool:
        """
        执行命令并等待完成，返回是否执行成功

        Args:
            cmd: 要执行的命令
            cwd: 工作目录
            shell: 是否使用shell执行
            timeout: 超时时间（秒）

        Returns:
            bool: 是否执行成功（返回码为0）
        """
        returncode, _, _ = RuntimeUtil.exec(cmd, cwd, shell, timeout)
        return returncode == 0

    @staticmethod
    def execAsync(cmd: str, cwd: Optional[str] = None, shell: bool = True) -> Optional[subprocess.Popen]:
        """
        异步执行命令，返回进程对象

        Args:
            cmd: 要执行的命令
            cwd: 工作目录
            shell: 是否使用shell执行

        Returns:
            Optional[subprocess.Popen]: 进程对象，执行失败返回None
        """
        try:
            process = subprocess.Popen(
                cmd, 
                cwd=cwd, 
                shell=shell, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True
            )
            return process
        except Exception:
            return None

    @staticmethod
    def getProcessOutput(process: subprocess.Popen, timeout: Optional[float] = None) -> Tuple[str, str]:
        """
        获取进程的输出

        Args:
            process: 进程对象
            timeout: 超时时间（秒）

        Returns:
            Tuple[str, str]: (标准输出, 标准错误)
        """
        try:
            stdout, stderr = process.communicate(timeout=timeout)
            return stdout.strip(), stderr.strip()
        except subprocess.TimeoutExpired:
            process.kill()
            process.communicate()  # 清理缓冲区
            return "", f"获取输出超时: {timeout}秒"
        except Exception:
            return "", "获取输出失败"

    @staticmethod
    def getSystemInfo() -> Dict[str, Any]:
        """
        获取系统信息

        Returns:
            Dict[str, Any]: 系统信息字典
        """
        import platform
        
        return {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "python_compiler": platform.python_compiler(),
            "os_name": os.name
        }

    @staticmethod
    def getRuntimeInfo() -> Dict[str, Any]:
        """
        获取运行时信息

        Returns:
            Dict[str, Any]: 运行时信息字典
        """
        return {
            "cwd": os.getcwd(),
            "pid": os.getpid(),
            "ppid": os.getppid(),
            "python_path": sys.executable,
            "python_version": sys.version,
            "sys_platform": sys.platform,
            "argv": sys.argv,
            "env": dict(os.environ)
        }

    @staticmethod
    def getEnv(key: str, default: Optional[str] = None) -> Optional[str]:
        """
        获取环境变量

        Args:
            key: 环境变量名
            default: 默认值

        Returns:
            Optional[str]: 环境变量值，不存在返回默认值
        """
        return os.environ.get(key, default)

    @staticmethod
    def setEnv(key: str, value: str) -> None:
        """
        设置环境变量

        Args:
            key: 环境变量名
            value: 环境变量值
        """
        os.environ[key] = value

    @staticmethod
    def unsetEnv(key: str) -> None:
        """
        移除环境变量

        Args:
            key: 环境变量名
        """
        if key in os.environ:
            del os.environ[key]

    @staticmethod
    def getOsName() -> str:
        """
        获取操作系统名称

        Returns:
            str: 操作系统名称
        """
        import platform
        return platform.system()

    @staticmethod
    def isWindows() -> bool:
        """
        是否为Windows系统

        Returns:
            bool: 是否为Windows系统
        """
        return os.name == "nt"

    @staticmethod
    def isLinux() -> bool:
        """
        是否为Linux系统

        Returns:
            bool: 是否为Linux系统
        """
        return os.name == "posix" and "linux" in sys.platform.lower()

    @staticmethod
    def isMac() -> bool:
        """
        是否为Mac系统

        Returns:
            bool: 是否为Mac系统
        """
        return os.name == "posix" and "darwin" in sys.platform.lower()

    @staticmethod
    def runScript(script_path: str, *args: str, cwd: Optional[str] = None) -> Tuple[int, str, str]:
        """
        运行脚本文件

        Args:
            script_path: 脚本文件路径
            *args: 脚本参数
            cwd: 工作目录

        Returns:
            Tuple[int, str, str]: (返回码, 标准输出, 标准错误)
        """
        if not os.path.exists(script_path):
            return -1, "", f"脚本文件不存在: {script_path}"

        # 根据文件扩展名确定执行方式
        ext = os.path.splitext(script_path)[1].lower()
        
        if ext == ".py":
            # Python脚本
            cmd = [sys.executable, script_path] + list(args)
            shell = False
        else:
            # 其他脚本，使用shell执行
            cmd = f"{script_path} {' '.join(args)}"
            shell = True

        try:
            result = subprocess.run(
                cmd, 
                cwd=cwd, 
                shell=shell, 
                capture_output=True, 
                text=True
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return -1, "", f"脚本执行失败: {str(e)}"

    @staticmethod
    def killProcess(pid: int) -> bool:
        """
        终止指定进程

        Args:
            pid: 进程ID

        Returns:
            bool: 是否终止成功
        """
        try:
            if RuntimeUtil.isWindows():
                # Windows系统
                subprocess.run(["taskkill", "/F", "/PID", str(pid)], capture_output=True)
            else:
                # Linux/Mac系统
                os.kill(pid, 9)  # SIGKILL
            return True
        except Exception:
            return False

    @staticmethod
    def sleep(seconds: float) -> None:
        """
        线程休眠

        Args:
            seconds: 休眠时间（秒）
        """
        import time
        time.sleep(seconds)