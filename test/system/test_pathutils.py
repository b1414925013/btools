"""测试PathUtils类"""
import unittest
import os
from btools.core.system.pathutils import PathUtils


class TestPathUtils(unittest.TestCase):
    """测试PathUtils类"""

    def test_normalize(self):
        """测试路径规范化"""
        path = PathUtils.normalize("path//to///file.txt")
        self.assertNotIn("///", path)

    def test_join(self):
        """测试路径拼接"""
        path = PathUtils.join("path", "to", "file.txt")
        self.assertTrue("path" in path)
        self.assertTrue("to" in path)
        self.assertTrue("file.txt" in path)

    def test_get_filename(self):
        """测试获取文件名"""
        filename = PathUtils.get_filename("/path/to/file.txt")
        self.assertEqual(filename, "file.txt")

    def test_get_extension(self):
        """测试获取扩展名"""
        ext = PathUtils.get_extension("/path/to/file.txt")
        self.assertEqual(ext, "txt")

    def test_get_dirname(self):
        """测试获取目录名"""
        dirname = PathUtils.get_dirname("/path/to/file.txt")
        self.assertIn("path", dirname)

    def test_get_basename(self):
        """测试获取文件名（不含扩展名）"""
        basename = PathUtils.get_basename("/path/to/file.txt")
        self.assertEqual(basename, "file")

    def test_change_extension(self):
        """测试修改扩展名"""
        new_path = PathUtils.change_extension("/path/to/file.txt", "md")
        self.assertTrue(new_path.endswith(".md"))

    def test_is_absolute(self):
        """测试检查是否为绝对路径"""
        if os.name == 'nt':  # Windows
            self.assertTrue(PathUtils.is_absolute("C:\\path\\to\\file.txt"))
        else:  # Unix
            self.assertTrue(PathUtils.is_absolute("/path/to/file.txt"))
        self.assertFalse(PathUtils.is_absolute("relative/path"))

    def test_get_temp_dir(self):
        """测试获取临时目录"""
        temp_dir = PathUtils.get_temp_dir()
        self.assertTrue(os.path.exists(temp_dir))

    def test_get_home_dir(self):
        """测试获取用户主目录"""
        home = PathUtils.get_home_dir()
        self.assertTrue(os.path.exists(home))


if __name__ == "__main__":
    unittest.main()
