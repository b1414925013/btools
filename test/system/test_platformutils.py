"""测试PlatformUtils类"""
import unittest
from btools.core.system.platformutils import PlatformUtils


class TestPlatformUtils(unittest.TestCase):
    """测试PlatformUtils类"""

    def test_get_os_name(self):
        """测试获取操作系统名称"""
        os_name = PlatformUtils.get_os_name()
        self.assertIn(os_name, ["Windows", "Linux", "Darwin"])

    def test_get_architecture(self):
        """测试获取架构"""
        arch = PlatformUtils.get_architecture()
        self.assertIsNotNone(arch)

    def test_is_windows(self):
        """测试检查是否为Windows"""
        result = PlatformUtils.is_windows()
        self.assertIsInstance(result, bool)

    def test_is_linux(self):
        """测试检查是否为Linux"""
        result = PlatformUtils.is_linux()
        self.assertIsInstance(result, bool)

    def test_is_macos(self):
        """测试检查是否为macOS"""
        result = PlatformUtils.is_macos()
        self.assertIsInstance(result, bool)

    def test_is_unix(self):
        """测试检查是否为Unix-like"""
        result = PlatformUtils.is_unix()
        self.assertIsInstance(result, bool)

    def test_get_path_separator(self):
        """测试获取路径分隔符"""
        sep = PlatformUtils.get_path_separator()
        self.assertIn(sep, ["\\", "/"])

    def test_get_newline(self):
        """测试获取换行符"""
        newline = PlatformUtils.get_newline()
        self.assertIn(newline, ["\r\n", "\n"])

    def test_get_temp_dir(self):
        """测试获取临时目录"""
        temp_dir = PlatformUtils.get_temp_dir()
        self.assertIsNotNone(temp_dir)

    def test_get_home_dir(self):
        """测试获取用户主目录"""
        home = PlatformUtils.get_home_dir()
        self.assertIsNotNone(home)


if __name__ == "__main__":
    unittest.main()
