"""测试Logger类"""
import unittest
import os
import tempfile
from btools.core.log.logger import Logger


class TestLogger(unittest.TestCase):
    """测试Logger类"""

    def setUp(self):
        """设置测试环境"""
        # 创建临时目录作为日志目录
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """清理测试环境"""
        # 删除临时目录
        if os.path.exists(self.temp_dir):
            import shutil
            shutil.rmtree(self.temp_dir)

    def test_create_logger(self):
        """测试创建Logger实例"""
        # 创建Logger实例
        logger = Logger(name="test_logger", level=Logger.INFO, log_dir=self.temp_dir)
        # 检查Logger是否创建成功
        self.assertIsNotNone(logger)

    def test_log_methods(self):
        """测试日志方法"""
        logger = Logger(name="test_logger", level=Logger.INFO, log_dir=self.temp_dir)
        # 测试不同级别的日志方法
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")
        # 这里只是测试方法是否存在，实际日志输出会写入文件

    def test_log_to_file(self):
        """测试日志写入文件"""
        # 创建带文件输出的Logger
        logger = Logger(name="test_logger", level=Logger.INFO, log_dir=self.temp_dir, log_file="test.log")
        # 记录日志
        test_message = "Test log message"
        logger.info(test_message)
        # 检查日志文件是否创建
        log_file_path = os.path.join(self.temp_dir, "test.log")
        self.assertTrue(os.path.exists(log_file_path))
        # 检查日志是否写入文件
        with open(log_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn(test_message, content)

    def test_log_level(self):
        """测试日志级别"""
        # 创建只记录ERROR及以上级别的Logger
        logger = Logger(name="test_logger", level=Logger.ERROR, log_dir=self.temp_dir, log_file="test.log")
        # 记录不同级别的日志
        logger.info("Info message")  # 不会被记录
        logger.error("Error message")  # 会被记录
        # 检查日志文件
        log_file_path = os.path.join(self.temp_dir, "test.log")
        with open(log_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertNotIn("Info message", content)
        self.assertIn("Error message", content)


if __name__ == "__main__":
    unittest.main()