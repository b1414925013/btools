"""测试FileUtils类"""
import unittest
import os
import tempfile
from btools.core.data.fileutils import FileUtils


class TestFileUtils(unittest.TestCase):
    """测试FileUtils类"""

    def setUp(self):
        """设置测试环境"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test.txt")

    def tearDown(self):
        """清理测试环境"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.temp_dir):
            # 递归删除所有子目录和文件
            for root, dirs, files in os.walk(self.temp_dir, topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    os.rmdir(os.path.join(root, dir))
            os.rmdir(self.temp_dir)

    def test_write_file(self):
        """测试写入文件"""
        content = "Hello, World!"
        FileUtils.write_file(self.test_file, content)
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), content)

    def test_read_file(self):
        """测试读取文件"""
        content = "Hello, World!"
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write(content)
        self.assertEqual(FileUtils.read_file(self.test_file), content)

    def test_exists(self):
        """测试文件是否存在"""
        self.assertFalse(FileUtils.exists(self.test_file))
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("test")
        self.assertTrue(FileUtils.exists(self.test_file))

    def test_create_dir(self):
        """测试创建目录"""
        new_dir = os.path.join(self.temp_dir, "new_dir")
        self.assertFalse(os.path.exists(new_dir))
        FileUtils.create_dir(new_dir)
        self.assertTrue(os.path.exists(new_dir))

    def test_delete_file(self):
        """测试删除文件"""
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("test")
        self.assertTrue(os.path.exists(self.test_file))
        FileUtils.delete_file(self.test_file)
        self.assertFalse(os.path.exists(self.test_file))


if __name__ == "__main__":
    unittest.main()