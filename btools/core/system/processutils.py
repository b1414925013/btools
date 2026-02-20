#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
跨平台进程管理工具类

提供跨平台进程管理，启动、监控、终止进程等功能
"""
import os
import subprocess
import signal
import time
from typing import Dict, Any, Optional, List, Tuple


class ProcessUtils:
    """
    跨平台进程管理工具类
    """

    @staticmethod
    def run_command(command: str, cwd: Optional[str] = None, shell: bool = False, timeout: Optional[int] = None) -> Dict[str, Any]:
        """
        运行命令

        Args:
            command: 命令
            cwd: 工作目录
            shell: 是否使用 shell
            timeout: 超时时间

        Returns:
            包含命令执行结果的字典
        """
        try:
            result = subprocess.run(
                command, 
                cwd=cwd, 
                shell=shell, 
                capture_output=True, 
                text=True, 
                timeout=timeout
            )
            return {
                'success': result.returncode == 0,
                'returncode': result.returncode,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'error': None
            }
        except subprocess.TimeoutExpired as e:
            return {
                'success': False,
                'returncode': None,
                'stdout': e.stdout.decode() if e.stdout else '',
                'stderr': e.stderr.decode() if e.stderr else '',
                'error': f'Timeout expired: {timeout} seconds'
            }
        except Exception as e:
            return {
                'success': False,
                'returncode': None,
                'stdout': '',
                'stderr': '',
                'error': str(e)
            }

    @staticmethod
    def start_process(command: str, cwd: Optional[str] = None, shell: bool = False) -> Optional[subprocess.Popen]:
        """
        启动进程

        Args:
            command: 命令
            cwd: 工作目录
            shell: 是否使用 shell

        Returns:
            进程对象
        """
        try:
            process = subprocess.Popen(
                command, 
                cwd=cwd, 
                shell=shell, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True
            )
            return process
        except Exception as e:
            return None

    @staticmethod
    def stop_process(process: subprocess.Popen) -> bool:
        """
        停止进程

        Args:
            process: 进程对象

        Returns:
            是否成功
        """
        try:
            if process.poll() is None:  # 进程仍在运行
                if os.name == 'nt':  # Windows
                    process.terminate()
                    process.wait(timeout=5)
                else:  # Unix-like
                    process.send_signal(signal.SIGTERM)
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.send_signal(signal.SIGKILL)
                        process.wait(timeout=2)
            return True
        except Exception as e:
            return False

    @staticmethod
    def kill_process(process: subprocess.Popen) -> bool:
        """
        强制终止进程

        Args:
            process: 进程对象

        Returns:
            是否成功
        """
        try:
            if process.poll() is None:  # 进程仍在运行
                if os.name == 'nt':  # Windows
                    process.kill()
                else:  # Unix-like
                    process.send_signal(signal.SIGKILL)
                process.wait(timeout=5)
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_process_status(process: subprocess.Popen) -> Dict[str, Any]:
        """
        获取进程状态

        Args:
            process: 进程对象

        Returns:
            进程状态字典
        """
        try:
            returncode = process.poll()
            is_running = returncode is None
            return {
                'is_running': is_running,
                'returncode': returncode,
                'pid': process.pid
            }
        except Exception as e:
            return {
                'is_running': False,
                'returncode': None,
                'pid': None,
                'error': str(e)
            }

    @staticmethod
    def get_process_output(process: subprocess.Popen, timeout: Optional[int] = None) -> Dict[str, Any]:
        """
        获取进程输出

        Args:
            process: 进程对象
            timeout: 超时时间

        Returns:
            包含进程输出的字典
        """
        try:
            stdout, stderr = process.communicate(timeout=timeout)
            return {
                'stdout': stdout,
                'stderr': stderr,
                'returncode': process.returncode
            }
        except subprocess.TimeoutExpired as e:
            return {
                'stdout': e.stdout,
                'stderr': e.stderr,
                'returncode': None,
                'error': f'Timeout expired: {timeout} seconds'
            }
        except Exception as e:
            return {
                'stdout': '',
                'stderr': '',
                'returncode': None,
                'error': str(e)
            }

    @staticmethod
    def wait_for_process(process: subprocess.Popen, timeout: Optional[int] = None) -> int:
        """
        等待进程结束

        Args:
            process: 进程对象
            timeout: 超时时间

        Returns:
            进程返回码
        """
        try:
            return process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            return -1
        except Exception:
            return -1

    @staticmethod
    def get_process_list() -> List[Dict[str, Any]]:
        """
        获取进程列表

        Returns:
            进程列表
        """
        processes = []
        try:
            if os.name == 'nt':  # Windows
                result = subprocess.run(
                    ['tasklist', '/fo', 'csv', '/nh'],
                    capture_output=True,
                    text=True
                )
                for line in result.stdout.split('\n'):
                    if line.strip():
                        parts = line.strip().split(',')
                        if len(parts) >= 2:
                            processes.append({
                                'name': parts[0].strip('"'),
                                'pid': int(parts[1].strip('"')),
                                'mem usage': parts[4].strip('"') if len(parts) > 4 else ''
                            })
            else:  # Unix-like
                result = subprocess.run(
                    ['ps', 'aux'],
                    capture_output=True,
                    text=True
                )
                for line in result.stdout.split('\n')[1:]:  # 跳过表头
                    if line.strip():
                        parts = line.strip().split()
                        if len(parts) >= 10:
                            processes.append({
                                'user': parts[0],
                                'pid': int(parts[1]),
                                'cpu': parts[2],
                                'mem': parts[3],
                                'command': ' '.join(parts[10:])
                            })
        except Exception as e:
            pass
        return processes

    @staticmethod
    def find_process_by_name(name: str) -> List[Dict[str, Any]]:
        """
        根据名称查找进程

        Args:
            name: 进程名称

        Returns:
            进程列表
        """
        processes = ProcessUtils.get_process_list()
        return [p for p in processes if name.lower() in str(p.get('name', '')).lower() or name.lower() in str(p.get('command', '')).lower()]

    @staticmethod
    def find_process_by_pid(pid: int) -> Optional[Dict[str, Any]]:
        """
        根据 PID 查找进程

        Args:
            pid: 进程 ID

        Returns:
            进程信息
        """
        processes = ProcessUtils.get_process_list()
        for p in processes:
            if p.get('pid') == pid:
                return p
        return None

    @staticmethod
    def kill_process_by_pid(pid: int) -> bool:
        """
        根据 PID 终止进程

        Args:
            pid: 进程 ID

        Returns:
            是否成功
        """
        try:
            if os.name == 'nt':  # Windows
                subprocess.run(['taskkill', '/F', '/PID', str(pid)], capture_output=True)
            else:  # Unix-like
                os.kill(pid, signal.SIGTERM)
                # 等待进程终止
                for _ in range(5):
                    try:
                        os.kill(pid, 0)  # 检查进程是否存在
                        time.sleep(1)
                    except OSError:
                        return True
                # 如果进程仍在运行，强制终止
                os.kill(pid, signal.SIGKILL)
            return True
        except Exception as e:
            return False

    @staticmethod
    def kill_processes_by_name(name: str) -> int:
        """
        根据名称终止进程

        Args:
            name: 进程名称

        Returns:
            终止的进程数
        """
        processes = ProcessUtils.find_process_by_name(name)
        count = 0
        for process in processes:
            pid = process.get('pid')
            if pid:
                if ProcessUtils.kill_process_by_pid(pid):
                    count += 1
        return count

    @staticmethod
    def get_current_process_id() -> int:
        """
        获取当前进程 ID

        Returns:
            当前进程 ID
        """
        return os.getpid()

    @staticmethod
    def get_parent_process_id() -> int:
        """
        获取父进程 ID

        Returns:
            父进程 ID
        """
        if os.name == 'nt':  # Windows
            try:
                import psutil
                return psutil.Process().ppid()
            except:
                return 0
        else:  # Unix-like
            return os.getppid()

    @staticmethod
    def get_process_memory_usage(pid: int) -> Optional[int]:
        """
        获取进程内存使用

        Args:
            pid: 进程 ID

        Returns:
            内存使用量（字节）
        """
        try:
            if os.name == 'nt':  # Windows
                result = subprocess.run(
                    ['tasklist', '/fi', f'PID eq {pid}', '/fo', 'csv', '/nh'],
                    capture_output=True,
                    text=True
                )
                for line in result.stdout.split('\n'):
                    if line.strip():
                        parts = line.strip().split(',')
                        if len(parts) > 4:
                            mem_str = parts[4].strip('"').replace(',', '')
                            # 转换为字节
                            if mem_str.endswith('K'):
                                return int(mem_str[:-1]) * 1024
                            elif mem_str.endswith('M'):
                                return int(mem_str[:-1]) * 1024 * 1024
            else:  # Unix-like
                result = subprocess.run(
                    ['ps', 'o', 'rss=', '-p', str(pid)],
                    capture_output=True,
                    text=True
                )
                mem_str = result.stdout.strip()
                if mem_str:
                    return int(mem_str) * 1024  # 转换为字节
        except Exception:
            pass
        return None

    @staticmethod
    def get_process_cpu_usage(pid: int) -> Optional[float]:
        """
        获取进程 CPU 使用

        Args:
            pid: 进程 ID

        Returns:
            CPU 使用率
        """
        try:
            if os.name == 'nt':  # Windows
                # Windows 没有直接的命令获取 CPU 使用率
                # 这里使用 psutil 作为备选
                try:
                    import psutil
                    process = psutil.Process(pid)
                    return process.cpu_percent(interval=1)
                except:
                    pass
            else:  # Unix-like
                result = subprocess.run(
                    ['ps', 'o', '%cpu=', '-p', str(pid)],
                    capture_output=True,
                    text=True
                )
                cpu_str = result.stdout.strip()
                if cpu_str:
                    return float(cpu_str)
        except Exception:
            pass
        return None

    @staticmethod
    def create_process_group() -> bool:
        """
        创建进程组

        Returns:
            是否成功
        """
        try:
            if os.name != 'nt':  # Unix-like
                os.setpgid(0, 0)
            return True
        except Exception:
            return False

    @staticmethod
    def kill_process_group(pgid: int) -> bool:
        """
        终止进程组

        Args:
            pgid: 进程组 ID

        Returns:
            是否成功
        """
        try:
            if os.name != 'nt':  # Unix-like
                os.killpg(pgid, signal.SIGTERM)
                return True
        except Exception:
            pass
        return False

    @staticmethod
    def run_in_background(command: str, cwd: Optional[str] = None, shell: bool = False) -> Optional[int]:
        """
        在后台运行命令

        Args:
            command: 命令
            cwd: 工作目录
            shell: 是否使用 shell

        Returns:
            进程 ID
        """
        try:
            if os.name == 'nt':  # Windows
                # Windows 后台运行
                process = subprocess.Popen(
                    command, 
                    cwd=cwd, 
                    shell=shell,
                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
                )
            else:  # Unix-like
                # Unix 后台运行
                process = subprocess.Popen(
                    command, 
                    cwd=cwd, 
                    shell=shell,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    preexec_fn=os.setpgid
                )
            return process.pid
        except Exception:
            return None

    @staticmethod
    def monitor_process(pid: int, interval: int = 1, duration: int = 60) -> List[Dict[str, Any]]:
        """
        监控进程

        Args:
            pid: 进程 ID
            interval: 监控间隔（秒）
            duration: 监控持续时间（秒）

        Returns:
            监控数据列表
        """
        monitoring_data = []
        start_time = time.time()

        while time.time() - start_time < duration:
            process_info = ProcessUtils.find_process_by_pid(pid)
            if not process_info:
                break

            mem_usage = ProcessUtils.get_process_memory_usage(pid)
            cpu_usage = ProcessUtils.get_process_cpu_usage(pid)

            monitoring_data.append({
                'timestamp': time.time(),
                'pid': pid,
                'memory_usage': mem_usage,
                'cpu_usage': cpu_usage,
                'process_info': process_info
            })

            time.sleep(interval)

        return monitoring_data

    @staticmethod
    def execute_with_retry(command: str, max_retries: int = 3, retry_delay: int = 1, **kwargs) -> Dict[str, Any]:
        """
        带重试的命令执行

        Args:
            command: 命令
            max_retries: 最大重试次数
            retry_delay: 重试延迟（秒）
            **kwargs: 其他参数

        Returns:
            命令执行结果
        """
        for attempt in range(max_retries):
            result = ProcessUtils.run_command(command, **kwargs)
            if result['success']:
                return result
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
        return result

    @staticmethod
    def get_process_environment(pid: int) -> Optional[Dict[str, str]]:
        """
        获取进程环境变量

        Args:
            pid: 进程 ID

        Returns:
            环境变量字典
        """
        try:
            if os.name == 'nt':  # Windows
                # Windows 没有直接的命令获取进程环境变量
                # 这里使用 psutil 作为备选
                try:
                    import psutil
                    process = psutil.Process(pid)
                    return process.environ()
                except:
                    pass
            else:  # Unix-like
                with open(f'/proc/{pid}/environ', 'r') as f:
                    env_str = f.read()
                env_vars = {}
                for var in env_str.split('\0'):
                    if '=' in var:
                        key, value = var.split('=', 1)
                        env_vars[key] = value
                return env_vars
        except Exception:
            pass
        return None

    @staticmethod
    def set_process_priority(pid: int, priority: int) -> bool:
        """
        设置进程优先级

        Args:
            pid: 进程 ID
            priority: 优先级

        Returns:
            是否成功
        """
        try:
            if os.name == 'nt':  # Windows
                import psutil
                process = psutil.Process(pid)
                process.nice(priority)
            else:  # Unix-like
                os.nice(priority)
            return True
        except Exception:
            return False

    @staticmethod
    def get_process_priority(pid: int) -> Optional[int]:
        """
        获取进程优先级

        Args:
            pid: 进程 ID

        Returns:
            优先级
        """
        try:
            if os.name == 'nt':  # Windows
                import psutil
                process = psutil.Process(pid)
                return process.nice()
            else:  # Unix-like
                return os.nice(0)
        except Exception:
            return None

    @staticmethod
    def is_process_running(pid: int) -> bool:
        """
        检查进程是否在运行

        Args:
            pid: 进程 ID

        Returns:
            是否在运行
        """
        try:
            if os.name == 'nt':  # Windows
                result = subprocess.run(
                    ['tasklist', '/fi', f'PID eq {pid}'],
                    capture_output=True,
                    text=True
                )
                return f'PID {pid}' in result.stdout
            else:  # Unix-like
                os.kill(pid, 0)  # 发送空信号检查进程是否存在
                return True
        except:
            return False

    @staticmethod
    def wait_for_process_start(pid: int, timeout: int = 10) -> bool:
        """
        等待进程启动

        Args:
            pid: 进程 ID
            timeout: 超时时间

        Returns:
            是否成功
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            if ProcessUtils.is_process_running(pid):
                return True
            time.sleep(0.5)
        return False

    @staticmethod
    def wait_for_process_stop(pid: int, timeout: int = 10) -> bool:
        """
        等待进程停止

        Args:
            pid: 进程 ID
            timeout: 超时时间

        Returns:
            是否成功
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            if not ProcessUtils.is_process_running(pid):
                return True
            time.sleep(0.5)
        return False

    @staticmethod
    def run_with_timeout(command: str, timeout: int, **kwargs) -> Dict[str, Any]:
        """
        带超时的命令执行

        Args:
            command: 命令
            timeout: 超时时间
            **kwargs: 其他参数

        Returns:
            命令执行结果
        """
        return ProcessUtils.run_command(command, timeout=timeout, **kwargs)

    @staticmethod
    def run_interactive(command: str, cwd: Optional[str] = None) -> Optional[subprocess.Popen]:
        """
        运行交互式命令

        Args:
            command: 命令
            cwd: 工作目录

        Returns:
            进程对象
        """
        try:
            process = subprocess.Popen(
                command, 
                cwd=cwd, 
                shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return process
        except Exception:
            return None

    @staticmethod
    def send_input_to_process(process: subprocess.Popen, input_str: str) -> bool:
        """
        向进程发送输入

        Args:
            process: 进程对象
            input_str: 输入字符串

        Returns:
            是否成功
        """
        try:
            process.stdin.write(input_str)
            process.stdin.flush()
            return True
        except Exception:
            return False

    @staticmethod
    def get_system_processes() -> List[Dict[str, Any]]:
        """
        获取系统进程列表

        Returns:
            系统进程列表
        """
        return ProcessUtils.get_process_list()

    @staticmethod
    def get_process_info(pid: int) -> Optional[Dict[str, Any]]:
        """
        获取进程详细信息

        Args:
            pid: 进程 ID

        Returns:
            进程详细信息
        """
        process_info = ProcessUtils.find_process_by_pid(pid)
        if not process_info:
            return None

        mem_usage = ProcessUtils.get_process_memory_usage(pid)
        cpu_usage = ProcessUtils.get_process_cpu_usage(pid)
        environment = ProcessUtils.get_process_environment(pid)

        return {
            **process_info,
            'memory_usage': mem_usage,
            'cpu_usage': cpu_usage,
            'environment': environment,
            'is_running': ProcessUtils.is_process_running(pid)
        }

    @staticmethod
    def terminate_all_processes() -> int:
        """
        终止所有子进程

        Returns:
            终止的进程数
        """
        # 注意：此功能需要谨慎使用
        count = 0
        try:
            if os.name == 'nt':  # Windows
                # Windows 不支持进程组，需要其他方式
                pass
            else:  # Unix-like
                # 终止当前进程组
                pgid = os.getpgid(0)
                if ProcessUtils.kill_process_group(pgid):
                    count += 1
        except Exception:
            pass
        return count

    @staticmethod
    def get_process_children(pid: int) -> List[int]:
        """
        获取进程的子进程

        Args:
            pid: 进程 ID

        Returns:
            子进程 PID 列表
        """
        children = []
        try:
            if os.name == 'nt':  # Windows
                try:
                    import psutil
                    process = psutil.Process(pid)
                    for child in process.children(recursive=True):
                        children.append(child.pid)
                except:
                    pass
            else:  # Unix-like
                import psutil
                process = psutil.Process(pid)
                for child in process.children(recursive=True):
                    children.append(child.pid)
        except Exception:
            pass
        return children

    @staticmethod
    def kill_process_tree(pid: int) -> int:
        """
        终止进程树

        Args:
            pid: 进程 ID

        Returns:
            终止的进程数
        """
        count = 0
        try:
            # 获取所有子进程
            children = ProcessUtils.get_process_children(pid)
            # 先终止子进程
            for child_pid in children:
                if ProcessUtils.kill_process_by_pid(child_pid):
                    count += 1
            # 再终止父进程
            if ProcessUtils.kill_process_by_pid(pid):
                count += 1
        except Exception:
            pass
        return count