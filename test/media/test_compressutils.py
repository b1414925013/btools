"""测试CompressUtils类"""
import unittest
import os
import tempfile
from btools.core.media.compressutils import CompressUtils


class TestCompressUtils(unittest.TestCase):
    """测试CompressUtils类"""

    def setUp(self):
        """设置测试环境"""
        # 创建临时目录
        self.temp_dir = tempfile.mkdtemp()
        # 创建测试文件
        self.test_files = []
        for i in range(3):
            file_path = os.path.join(self.temp_dir, f"test{i}.txt")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"Test content {i}")
            self.test_files.append(file_path)

    def tearDown(self):
        """清理测试环境"""
        # 删除临时目录及其内容
        if os.path.exists(self.temp_dir):
            import shutil
            shutil.rmtree(self.temp_dir)

    def test_compress_file(self):
        """测试压缩单个文件"""
        # 压缩文件
        input_file = self.test_files[0]
        output_file = os.path.join(self.temp_dir, "compressed.zip")
        CompressUtils.compress_file(input_file, output_file)
        # 检查压缩文件是否创建
        self.assertTrue(os.path.exists(output_file))

    def test_zip_files(self):
        """测试压缩多个文件"""
        # 压缩多个文件
        output_file = os.path.join(self.temp_dir, "compressed_files.zip")
        CompressUtils.zip_files(self.test_files, output_file)
        # 检查压缩文件是否创建
        self.assertTrue(os.path.exists(output_file))

    def test_zip_directory(self):
        """测试压缩目录"""
        # 压缩目录
        output_file = os.path.join(self.temp_dir, "compressed_dir.zip")
        CompressUtils.zip_directory(self.temp_dir, output_file)
        # 检查压缩文件是否创建
        self.assertTrue(os.path.exists(output_file))

    def test_decompress_file(self):
        """测试解压文件"""
        # 先创建压缩文件
        input_file = self.test_files[0]
        zip_file = os.path.join(self.temp_dir, "compressed.zip")
        CompressUtils.compress_file(input_file, zip_file)
        # 创建解压目录
        extract_dir = os.path.join(self.temp_dir, "extract")
        os.makedirs(extract_dir, exist_ok=True)
        # 解压文件
        CompressUtils.decompress_file(zip_file, extract_dir)
        # 检查文件是否解压
        extracted_file = os.path.join(extract_dir, os.path.basename(input_file))
        self.assertTrue(os.path.exists(extracted_file))


if __name__ == "__main__":
    unittest.main()