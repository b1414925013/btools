"""测试ExcelHandler类"""
import unittest
import os
import tempfile
from btools.core.data.excelhandler import ExcelHandler


class TestExcelHandler(unittest.TestCase):
    """测试ExcelHandler类"""

    def setUp(self):
        """设置测试环境"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test.xlsx")
        self.excel_handler = ExcelHandler()

    def tearDown(self):
        """清理测试环境"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)

    def test_write(self):
        """测试写入Excel文件"""
        data = [
            ["Name", "Age", "City"],
            ["John", "30", "New York"],
            ["Alice", "25", "London"]
        ]
        self.excel_handler.write(self.test_file, {"Sheet1": data})
        self.assertTrue(os.path.exists(self.test_file))

    def test_read(self):
        """测试读取Excel文件"""
        data = [
            ["Name", "Age", "City"],
            ["John", "30", "New York"],
            ["Alice", "25", "London"]
        ]
        self.excel_handler.write(self.test_file, {"Sheet1": data})
        read_data = self.excel_handler.read(self.test_file, "Sheet1")
        self.assertEqual(len(read_data), 3)


if __name__ == "__main__":
    unittest.main()