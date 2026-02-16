"""测试NetUtils类"""
import unittest
from btools.core.network.netutils import NetUtils


class TestNetUtils(unittest.TestCase):
    """测试NetUtils类"""

    def test_get_hostname(self):
        """测试获取主机名"""
        hostname = NetUtils.get_hostname()
        self.assertIsInstance(hostname, str)

    def test_get_ip_address(self):
        """测试获取IP地址"""
        ip = NetUtils.get_ip_address()
        self.assertIsInstance(ip, str)

    def test_is_ipv4(self):
        """测试是否为IPv4"""
        self.assertTrue(NetUtils.is_ipv4("192.168.1.1"))
        self.assertFalse(NetUtils.is_ipv4("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))

    def test_is_ipv6(self):
        """测试是否为IPv6"""
        self.assertTrue(NetUtils.is_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
        self.assertFalse(NetUtils.is_ipv6("192.168.1.1"))

    def test_is_private_ip(self):
        """测试是否为私有IP"""
        self.assertTrue(NetUtils.is_private_ip("192.168.1.1"))
        self.assertFalse(NetUtils.is_private_ip("8.8.8.8"))

    def test_is_loopback_ip(self):
        """测试是否为回环IP"""
        self.assertTrue(NetUtils.is_loopback_ip("127.0.0.1"))
        self.assertFalse(NetUtils.is_loopback_ip("192.168.1.1"))

    def test_ping(self):
        """测试ping"""
        # 测试ping本地主机
        result = NetUtils.ping("127.0.0.1", count=1, timeout=1)
        self.assertTrue(result)

    def test_url_encode_decode(self):
        """测试URL编解码"""
        data = "Hello World!"
        encoded = NetUtils.url_encode(data)
        decoded = NetUtils.url_decode(encoded)
        self.assertEqual(decoded, data)


if __name__ == "__main__":
    unittest.main()