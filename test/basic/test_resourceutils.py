import unittest
import os
import tempfile
from btools.core.basic.resourceutils import ResourceUtils


class TestResourceUtils(unittest.TestCase):
    """
    资源工具类测试
    """

    def setUp(self):
        """
        测试前准备
        """
        # 在当前目录创建临时文件用于测试
        self.temp_file_name = 'test_resource.txt'
        self.temp_file_path = os.path.join(os.getcwd(), self.temp_file_name)
        with open(self.temp_file_path, 'w') as f:
            f.write('Hello, ResourceUtils!')

    def tearDown(self):
        """
        测试后清理
        """
        if os.path.exists(self.temp_file_path):
            os.unlink(self.temp_file_path)

    def test_get_resource_path(self):
        """
        测试获取资源路径
        """
        # 测试从文件系统获取
        path = ResourceUtils.get_resource_path(self.temp_file_name)
        self.assertIsNotNone(path)
        self.assertTrue(os.path.exists(path))

        # 测试不存在的资源
        path = ResourceUtils.get_resource_path('non_existent_file.txt')
        self.assertIsNone(path)

    def test_get_resource_stream(self):
        """
        测试获取资源输入流
        """
        # 测试从文件系统获取
        stream = ResourceUtils.get_resource_stream(self.temp_file_name)
        self.assertIsNotNone(stream)
        if stream:
            content = stream.read().decode('utf-8')
            self.assertEqual(content, 'Hello, ResourceUtils!')
            stream.close()

        # 测试不存在的资源
        stream = ResourceUtils.get_resource_stream('non_existent_file.txt')
        self.assertIsNone(stream)

    def test_read_resource(self):
        """
        测试读取资源内容
        """
        # 测试从文件系统获取
        content = ResourceUtils.read_resource(self.temp_file_name)
        self.assertIsNotNone(content)
        self.assertEqual(content, 'Hello, ResourceUtils!')

        # 测试不存在的资源
        content = ResourceUtils.read_resource('non_existent_file.txt')
        self.assertIsNone(content)

    def test_read_resource_bytes(self):
        """
        测试读取资源字节内容
        """
        # 测试从文件系统获取
        content = ResourceUtils.read_resource_bytes(self.temp_file_name)
        self.assertIsNotNone(content)
        self.assertEqual(content, b'Hello, ResourceUtils!')

        # 测试不存在的资源
        content = ResourceUtils.read_resource_bytes('non_existent_file.txt')
        self.assertIsNone(content)

    def test_get_resource_url(self):
        """
        测试获取资源URL
        """
        # 测试从文件系统获取
        url = ResourceUtils.get_resource_url(self.temp_file_name)
        self.assertIsNotNone(url)
        self.assertTrue(url.startswith('file://'))

        # 测试绝对URL
        test_url = 'http://example.com/test.txt'
        url = ResourceUtils.get_resource_url(test_url)
        self.assertEqual(url, test_url)

        # 测试不存在的资源
        url = ResourceUtils.get_resource_url('non_existent_file.txt')
        self.assertIsNone(url)

    def test_exists(self):
        """
        测试检查资源是否存在
        """
        # 测试存在的资源
        exists = ResourceUtils.exists(self.temp_file_name)
        self.assertTrue(exists)

        # 测试不存在的资源
        exists = ResourceUtils.exists('non_existent_file.txt')
        self.assertFalse(exists)

    def test_load_from_url(self):
        """
        测试从URL加载资源
        """
        # 测试有效的URL
        # 注意：这里使用一个稳定的测试URL
        url = 'https://httpbin.org/get'
        content = ResourceUtils.load_from_url(url)
        self.assertIsNotNone(content)
        self.assertIsInstance(content, str)

        # 测试无效的URL
        invalid_url = 'http://non_existent_domain_123456.com/test.txt'
        content = ResourceUtils.load_from_url(invalid_url)
        self.assertIsNone(content)

    def test_get_resource_as_stream(self):
        """
        测试获取资源作为输入流（别名方法）
        """
        # 测试从文件系统获取
        stream = ResourceUtils.get_resource_as_stream(self.temp_file_name)
        self.assertIsNotNone(stream)
        if stream:
            content = stream.read().decode('utf-8')
            self.assertEqual(content, 'Hello, ResourceUtils!')
            stream.close()

    def test_get_resource_bytes(self):
        """
        测试获取资源字节内容（别名方法）
        """
        # 测试从文件系统获取
        content = ResourceUtils.get_resource_bytes(self.temp_file_name)
        self.assertIsNotNone(content)
        self.assertEqual(content, b'Hello, ResourceUtils!')

    def test_get_resource_text(self):
        """
        测试获取资源文本内容（别名方法）
        """
        # 测试从文件系统获取
        content = ResourceUtils.get_resource_text(self.temp_file_name)
        self.assertIsNotNone(content)
        self.assertEqual(content, 'Hello, ResourceUtils!')


if __name__ == '__main__':
    unittest.main()
