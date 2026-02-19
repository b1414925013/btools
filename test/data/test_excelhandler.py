"""测试ExcelHandler类"""
import unittest
import os
import tempfile
from btools.core.data.excelhandlerutils import ExcelHandler


class TestExcelHandler(unittest.TestCase):
    """测试ExcelHandler类"""

    def setUp(self):
        """设置测试环境"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test.xlsx")

    def tearDown(self):
        """清理测试环境"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)

    def test_write_excel(self):
        """测试写入Excel文件"""
        data = [
            ["John", "30", "New York"],
            ["Alice", "25", "London"]
        ]
        header = ["Name", "Age", "City"]
        ExcelHandler.write_excel(self.test_file, data, sheet_name="Sheet1", header=header)
        self.assertTrue(os.path.exists(self.test_file))

    def test_read_excel(self):
        """测试读取Excel文件"""
        data = [
            ["John", "30", "New York"],
            ["Alice", "25", "London"]
        ]
        header = ["Name", "Age", "City"]
        ExcelHandler.write_excel(self.test_file, data, sheet_name="Sheet1", header=header)
        read_data = ExcelHandler.read_excel(self.test_file, sheet_name="Sheet1", skip_header=True)
        self.assertEqual(len(read_data), 2)


if __name__ == "__main__":
    unittest.main()