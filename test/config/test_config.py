"""测试Config类"""
import unittest
import os
import tempfile
from btools.core.config.configutils import Config


class TestConfig(unittest.TestCase):
    """测试Config类"""

    def setUp(self):
        """设置测试环境"""
        # 创建临时配置文件
        self.temp_file = tempfile.mktemp(suffix=".json")
        # 写入测试配置
        import json
        with open(self.temp_file, "w", encoding="utf-8") as f:
            json.dump({"database": {"host": "localhost", "port": 3306}, "api": {"key": "test_key"}}, f)

    def tearDown(self):
        """清理测试环境"""
        # 删除临时配置文件
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_load_config(self):
        """测试加载配置"""
        # 加载配置
        config = Config(self.temp_file)
        # 检查配置是否加载成功
        self.assertEqual(config.get("database.host"), "localhost")
        self.assertEqual(config.get("database.port"), 3306)
        self.assertEqual(config.get("api.key"), "test_key")

    def test_get(self):
        """测试获取配置值"""
        config = Config(self.temp_file)
        # 获取存在的配置
        self.assertEqual(config.get("database.host"), "localhost")
        # 获取不存在的配置（使用默认值）
        self.assertEqual(config.get("nonexistent", "default"), "default")

    def test_set(self):
        """测试设置配置值"""
        config = Config(self.temp_file)
        # 设置新配置
        config.set("api.url", "https://api.example.com")
        # 检查配置是否设置成功
        self.assertEqual(config.get("api.url"), "https://api.example.com")

    def test_remove(self):
        """测试删除配置"""
        config = Config(self.temp_file)
        # 删除配置
        config.remove("api.key")
        # 检查配置是否被删除
        self.assertIsNone(config.get("api.key"))

    def test_save(self):
        """测试保存配置"""
        config = Config(self.temp_file)
        # 修改配置
        config.set("database.host", "newhost")
        # 保存配置
        config.save()
        # 重新加载配置
        new_config = Config(self.temp_file)
        # 检查配置是否保存成功
        self.assertEqual(new_config.get("database.host"), "newhost")




if __name__ == "__main__":
    unittest.main()