"""测试EncodeUtils类"""
import unittest
from btools.core.data.encodeutils import EncodeUtils


class TestEncodeUtils(unittest.TestCase):
    """测试EncodeUtils类"""

    def test_base64_encode_decode(self):
        """测试Base64编解码"""
        data = "Hello, World!"
        encoded = EncodeUtils.base64_encode(data)
        decoded = EncodeUtils.base64_decode(encoded)
        self.assertEqual(decoded, data)

    def test_base64_url_encode_decode(self):
        """测试Base64 URL编解码"""
        data = "Hello, World!"
        encoded = EncodeUtils.base64_url_encode(data)
        decoded = EncodeUtils.base64_url_decode(encoded)
        self.assertEqual(decoded, data)

    def test_url_encode_decode(self):
        """测试URL编解码"""
        data = "Hello World!"
        encoded = EncodeUtils.url_encode(data)
        decoded = EncodeUtils.url_decode(encoded)
        self.assertEqual(decoded, data)

    def test_html_encode_decode(self):
        """测试HTML编解码"""
        data = "<html>Hello</html>"
        encoded = EncodeUtils.html_encode(data)
        decoded = EncodeUtils.html_decode(encoded)
        self.assertEqual(decoded, data)

    def test_json_encode_decode(self):
        """测试JSON编解码"""
        data = {"name": "test", "age": 25}
        encoded = EncodeUtils.json_encode(data)
        decoded = EncodeUtils.json_decode(encoded)
        self.assertEqual(decoded, data)

    def test_hex_encode_decode(self):
        """测试十六进制编解码"""
        data = "Hello"
        encoded = EncodeUtils.hex_encode(data)
        decoded = EncodeUtils.hex_decode(encoded)
        self.assertEqual(decoded, data)

    def test_utf8_encode_decode(self):
        """测试UTF-8编解码"""
        data = "Hello, 世界!"
        encoded = EncodeUtils.utf8_encode(data)
        decoded = EncodeUtils.utf8_decode(encoded)
        self.assertEqual(decoded, data)


if __name__ == "__main__":
    unittest.main()