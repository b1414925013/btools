"""测试CSVHandler类"""
import unittest
import os
import tempfile
from btools.core.data.csvhandler import CSVHandler


class TestCSVHandler(unittest.TestCase):
    """测试CSVHandler类"""

    def setUp(self):
        """设置测试环境"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test.csv")

    def tearDown(self):
        """清理测试环境"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)

    def test_write_csv(self):
        """测试写入CSV文件"""
        data = [
            ["Name", "Age", "City"],
            ["John", "30", "New York"],
            ["Alice", "25", "London"]
        ]
        CSVHandler.write_csv(self.test_file, data)
        self.assertTrue(os.path.exists(self.test_file))

    def test_read_csv(self):
        """测试读取CSV文件"""
        data = [
            ["Name", "Age", "City"],
            ["John", "30", "New York"],
            ["Alice", "25", "London"]
        ]
        CSVHandler.write_csv(self.test_file, data)
        read_data = CSVHandler.read_csv(self.test_file)
        self.assertEqual(len(read_data), 3)
        self.assertEqual(read_data[0], ["Name", "Age", "City"])


if __name__ == "__main__":
    unittest.main()