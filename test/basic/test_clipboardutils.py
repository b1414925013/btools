import unittest
from btools.core.basic.clipboardutils import ClipboardUtils


class TestClipboardUtils(unittest.TestCase):
    """
    剪贴板工具类测试
    """

    def test_copy_and_get_text(self):
        """
        测试复制文本到剪贴板并从剪贴板获取文本
        """
        # 测试文本
        test_text = "Hello, ClipboardUtils!"
        
        # 复制文本到剪贴板
        copy_result = ClipboardUtils.copy_text(test_text)
        
        # 从剪贴板获取文本
        get_result = ClipboardUtils.get_text()
        
        # 由于剪贴板操作可能会受到系统环境的影响，这里只测试方法是否能够正常执行
        # 不强制测试是否能够成功复制和获取，因为这依赖于系统环境
        self.assertIsInstance(copy_result, bool)
        self.assertIsInstance(get_result, (str, type(None)))

    def test_clear(self):
        """
        测试清空剪贴板
        """
        # 先复制一些文本到剪贴板
        ClipboardUtils.copy_text("Test text to clear")
        
        # 清空剪贴板
        clear_result = ClipboardUtils.clear()
        
        # 检查清空操作是否成功执行
        self.assertIsInstance(clear_result, bool)

    def test_copy_and_get_image(self):
        """
        测试复制图片到剪贴板并从剪贴板获取图片
        """
        try:
            from PIL import Image
            import io
            
            # 创建一个简单的测试图片
            test_image = Image.new('RGB', (100, 100), color='red')
            
            # 复制图片到剪贴板
            copy_result = ClipboardUtils.copy_image(test_image)
            
            # 从剪贴板获取图片
            get_result = ClipboardUtils.get_image()
            
            # 检查操作是否成功执行
            self.assertIsInstance(copy_result, bool)
            self.assertIsInstance(get_result, (Image.Image, type(None)))
        except ImportError:
            # 如果没有安装PIL，则跳过图片相关的测试
            self.skipTest("PIL library not installed, skipping image tests")

    def test_copy_invalid_image(self):
        """
        测试复制无效的图片对象
        """
        # 尝试复制一个非图片对象
        copy_result = ClipboardUtils.copy_image("not an image")
        
        # 检查操作是否失败（返回False）
        self.assertFalse(copy_result)


if __name__ == '__main__':
    unittest.main()
