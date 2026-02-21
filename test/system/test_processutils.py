"""测试ProcessUtils类"""
import unittest
import os
import sys
import time
from btools.core.system.processutils import ProcessUtils


class TestProcessUtils(unittest.TestCase):
    """测试ProcessUtils类"""

    def test_get_current_pid(self):
        """测试获取当前进程ID"""
        pid = ProcessUtils.get_current_pid()
        self.assertIsInstance(pid, int)
        self.assertGreater(pid, 0)

    def test_is_process_running(self):
        """测试检查进程是否运行"""
        current_pid = ProcessUtils.get_current_pid()
        is_running = ProcessUtils.is_process_running(current_pid)
        self.assertTrue(is_running)

    def test_run_process(self):
        """测试运行进程"""
        # 测试运行一个简单的命令
        if sys.platform == 'win32':
            result = ProcessUtils.run_process(['cmd', '/c', 'echo', 'test'], capture_output=True)
        else:
            result = ProcessUtils.run_process(['echo', 'test'], capture_output=True)
        
        self.assertEqual(result.returncode, 0)

    def test_list_processes(self):
        """测试列出进程"""
        processes = ProcessUtils.list_processes()
        self.assertIsInstance(processes, list)
        self.assertGreater(len(processes), 0)

    def test_find_processes_by_name(self):
        """测试按名称查找进程"""
        # 查找当前Python进程
        import psutil
        current_name = psutil.Process().name()
        processes = ProcessUtils.find_processes_by_name(current_name)
        self.assertIsInstance(processes, list)

    def test_get_process_info(self):
        """测试获取进程信息"""
        current_pid = ProcessUtils.get_current_pid()
        info = ProcessUtils.get_process_info(current_pid)
        self.assertIsInstance(info, dict)
        self.assertIn('pid', info)
        self.assertIn('name', info)

    def test_get_resource_usage(self):
        """测试获取资源使用"""
        current_pid = ProcessUtils.get_current_pid()
        usage = ProcessUtils.get_resource_usage(current_pid)
        self.assertIsInstance(usage, dict)


if __name__ == "__main__":
    unittest.main()
