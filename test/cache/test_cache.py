"""测试CacheUtils类"""
import unittest
import os
import tempfile
from btools.core.cache.cache import CacheUtils


class TestCacheUtils(unittest.TestCase):
    """测试CacheUtils类"""

    def setUp(self):
        """设置测试环境"""
        # 创建临时目录作为缓存目录
        self.temp_dir = tempfile.mkdtemp()
        CacheUtils.set_cache_dir(self.temp_dir)

    def tearDown(self):
        """清理测试环境"""
        # 清空缓存
        CacheUtils.clear()
        CacheUtils.clear_file()
        # 删除临时目录
        if os.path.exists(self.temp_dir):
            import shutil
            shutil.rmtree(self.temp_dir)

    def test_set_and_get(self):
        """测试设置和获取内存缓存"""
        # 设置缓存
        CacheUtils.set("key1", "value1")
        # 获取缓存
        self.assertEqual(CacheUtils.get("key1"), "value1")

    def test_exists(self):
        """测试检查缓存是否存在"""
        # 设置缓存
        CacheUtils.set("key1", "value1")
        # 检查存在的缓存
        self.assertTrue(CacheUtils.exists("key1"))
        # 检查不存在的缓存
        self.assertFalse(CacheUtils.exists("nonexistent"))

    def test_delete(self):
        """测试删除内存缓存"""
        # 设置缓存
        CacheUtils.set("key1", "value1")
        # 删除缓存
        CacheUtils.delete("key1")
        # 检查缓存是否被删除
        self.assertIsNone(CacheUtils.get("key1"))

    def test_clear(self):
        """测试清空内存缓存"""
        # 设置多个缓存
        CacheUtils.set("key1", "value1")
        CacheUtils.set("key2", "value2")
        # 清空缓存
        CacheUtils.clear()
        # 检查缓存是否被清空
        self.assertIsNone(CacheUtils.get("key1"))
        self.assertIsNone(CacheUtils.get("key2"))

    def test_set_file_and_get_file(self):
        """测试设置和获取文件缓存"""
        # 设置文件缓存
        CacheUtils.set_file("file_key1", "file_value1")
        # 获取文件缓存
        self.assertEqual(CacheUtils.get_file("file_key1"), "file_value1")

    def test_exists_file(self):
        """测试检查文件缓存是否存在"""
        # 设置文件缓存
        CacheUtils.set_file("file_key1", "file_value1")
        # 检查存在的文件缓存
        self.assertTrue(CacheUtils.exists_file("file_key1"))
        # 检查不存在的文件缓存
        self.assertFalse(CacheUtils.exists_file("nonexistent"))

    def test_delete_file(self):
        """测试删除文件缓存"""
        # 设置文件缓存
        CacheUtils.set_file("file_key1", "file_value1")
        # 删除文件缓存
        CacheUtils.delete_file("file_key1")
        # 检查文件缓存是否被删除
        self.assertIsNone(CacheUtils.get_file("file_key1"))

    def test_clear_file(self):
        """测试清空文件缓存"""
        # 设置多个文件缓存
        CacheUtils.set_file("file_key1", "file_value1")
        CacheUtils.set_file("file_key2", "file_value2")
        # 清空文件缓存
        CacheUtils.clear_file()
        # 检查文件缓存是否被清空
        self.assertIsNone(CacheUtils.get_file("file_key1"))
        self.assertIsNone(CacheUtils.get_file("file_key2"))

    def test_set_cache_dir(self):
        """测试设置缓存目录"""
        # 创建新的临时目录
        new_temp_dir = tempfile.mkdtemp()
        try:
            # 设置缓存目录
            CacheUtils.set_cache_dir(new_temp_dir)
            # 获取缓存目录
            self.assertEqual(CacheUtils.get_cache_dir(), new_temp_dir)
        finally:
            # 清理临时目录
            if os.path.exists(new_temp_dir):
                import shutil
                shutil.rmtree(new_temp_dir)


if __name__ == "__main__":
    unittest.main()