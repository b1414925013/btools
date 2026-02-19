"""测试CacheUtils类"""
import unittest
import os
import tempfile
from btools.core.cache.cacheutils import CacheUtils


class TestCacheUtils(unittest.TestCase):
    """测试CacheUtils类"""

    def setUp(self):
        """设置测试环境"""
        # 创建临时目录作为缓存目录
        self.temp_dir = tempfile.mkdtemp()
        # 创建缓存实例
        self.memory_cache = CacheUtils.create_memory_cache()
        self.file_cache = CacheUtils.create_file_cache(self.temp_dir)

    def tearDown(self):
        """清理测试环境"""
        # 删除临时目录
        if os.path.exists(self.temp_dir):
            import shutil
            shutil.rmtree(self.temp_dir)

    def test_memory_cache_set_and_get(self):
        """测试设置和获取内存缓存"""
        # 设置缓存
        self.memory_cache.set("key1", "value1")
        # 获取缓存
        self.assertEqual(self.memory_cache.get("key1"), "value1")

    def test_memory_cache_exists(self):
        """测试检查缓存是否存在"""
        # 设置缓存
        self.memory_cache.set("key1", "value1")
        # 检查存在的缓存
        self.assertTrue(self.memory_cache.exists("key1"))
        # 检查不存在的缓存
        self.assertFalse(self.memory_cache.exists("nonexistent"))

    def test_memory_cache_delete(self):
        """测试删除内存缓存"""
        # 设置缓存
        self.memory_cache.set("key1", "value1")
        # 删除缓存
        self.memory_cache.delete("key1")
        # 检查缓存是否被删除
        self.assertIsNone(self.memory_cache.get("key1"))

    def test_memory_cache_clear(self):
        """测试清空内存缓存"""
        # 设置多个缓存
        self.memory_cache.set("key1", "value1")
        self.memory_cache.set("key2", "value2")
        # 清空缓存
        self.memory_cache.clear()
        # 检查缓存是否被清空
        self.assertIsNone(self.memory_cache.get("key1"))
        self.assertIsNone(self.memory_cache.get("key2"))

    def test_file_cache_set_and_get(self):
        """测试设置和获取文件缓存"""
        # 设置文件缓存
        self.file_cache.set("file_key1", "file_value1")
        # 获取文件缓存
        self.assertEqual(self.file_cache.get("file_key1"), "file_value1")

    def test_file_cache_exists(self):
        """测试检查文件缓存是否存在"""
        # 设置文件缓存
        self.file_cache.set("file_key1", "file_value1")
        # 检查存在的文件缓存
        self.assertTrue(self.file_cache.exists("file_key1"))
        # 检查不存在的文件缓存
        self.assertFalse(self.file_cache.exists("nonexistent"))

    def test_file_cache_delete(self):
        """测试删除文件缓存"""
        # 设置文件缓存
        self.file_cache.set("file_key1", "file_value1")
        # 删除文件缓存
        self.file_cache.delete("file_key1")
        # 检查文件缓存是否被删除
        self.assertIsNone(self.file_cache.get("file_key1"))

    def test_file_cache_clear(self):
        """测试清空文件缓存"""
        # 设置多个文件缓存
        self.file_cache.set("file_key1", "file_value1")
        self.file_cache.set("file_key2", "file_value2")
        # 清空文件缓存
        self.file_cache.clear()
        # 检查文件缓存是否被清空
        self.assertIsNone(self.file_cache.get("file_key1"))
        self.assertIsNone(self.file_cache.get("file_key2"))


if __name__ == "__main__":
    unittest.main()