"""测试SystemUtils类"""
import unittest
from btools.core.system.systemutils import SystemUtils


class TestSystemUtils(unittest.TestCase):
    """测试SystemUtils类"""

    def test_get_os_name(self):
        """测试获取操作系统名称"""
        os_name = SystemUtils.get_os_name()
        self.assertIsInstance(os_name, str)

    def test_get_python_version(self):
        """测试获取Python版本"""
        version = SystemUtils.get_python_version()
        self.assertIsInstance(version, str)

    def test_get_system_architecture(self):
        """测试获取系统架构"""
        arch = SystemUtils.get_system_architecture()
        self.assertIsInstance(arch, str)

    def test_get_hostname(self):
        """测试获取主机名"""
        hostname = SystemUtils.get_hostname()
        self.assertIsInstance(hostname, str)

    def test_get_ip_address(self):
        """测试获取IP地址"""
        ip = SystemUtils.get_ip_address()
        self.assertIsInstance(ip, str)

    def test_get_env(self):
        """测试获取环境变量"""
        # 测试已存在的环境变量
        path = SystemUtils.get_env("PATH")
        self.assertIsInstance(path, str)
        # 测试不存在的环境变量
        self.assertIsNone(SystemUtils.get_env("NON_EXISTENT_VAR"))

    def test_has_env(self):
        """测试是否存在环境变量"""
        self.assertTrue(SystemUtils.has_env("PATH"))
        self.assertFalse(SystemUtils.has_env("NON_EXISTENT_VAR"))

    def test_get_cwd(self):
        """测试获取当前工作目录"""
        cwd = SystemUtils.get_cwd()
        self.assertIsInstance(cwd, str)

    def test_get_temp_dir(self):
        """测试获取临时目录"""
        temp_dir = SystemUtils.get_temp_dir()
        self.assertIsInstance(temp_dir, str)

    def test_get_home_dir(self):
        """测试获取主目录"""
        home_dir = SystemUtils.get_home_dir()
        self.assertIsInstance(home_dir, str)

    def test_get_current_process_id(self):
        """测试获取当前进程ID"""
        pid = SystemUtils.get_current_process_id()
        self.assertIsInstance(pid, int)

    def test_get_current_process_name(self):
        """测试获取当前进程名称"""
        name = SystemUtils.get_current_process_name()
        self.assertIsInstance(name, str)

    def test_get_cpu_count(self):
        """测试获取CPU数量"""
        count = SystemUtils.get_cpu_count()
        self.assertIsInstance(count, int)
        self.assertGreater(count, 0)

    def test_execute_command(self):
        """测试执行命令"""
        if SystemUtils.is_windows():
            result = SystemUtils.execute_command("echo hello")
        else:
            result = SystemUtils.execute_command("echo 'hello'")
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)

    def test_get_system_time(self):
        """测试获取系统时间"""
        time_val = SystemUtils.get_system_time()
        self.assertIsInstance(time_val, float)

    def test_is_windows(self):
        """测试是否为Windows"""
        # 由于我们在Windows环境下运行，应该返回True
        self.assertTrue(SystemUtils.is_windows())

    def test_is_linux(self):
        """测试是否为Linux"""
        # 由于我们在Windows环境下运行，应该返回False
        self.assertFalse(SystemUtils.is_linux())

    def test_is_macos(self):
        """测试是否为macOS"""
        # 由于我们在Windows环境下运行，应该返回False
        self.assertFalse(SystemUtils.is_macos())


if __name__ == "__main__":
    unittest.main()