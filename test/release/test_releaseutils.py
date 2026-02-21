"""测试ReleaseUtils类"""
import unittest
from btools.core.release.releaseutils import ReleaseUtils


class TestReleaseUtils(unittest.TestCase):
    """测试ReleaseUtils类"""

    def test_validate_version(self):
        """测试验证版本号"""
        self.assertTrue(ReleaseUtils.validate_version("1.0.0"))
        self.assertTrue(ReleaseUtils.validate_version("2.3.4"))
        self.assertTrue(ReleaseUtils.validate_version("1.0.0-alpha.1"))
        self.assertTrue(ReleaseUtils.validate_version("1.0.0-beta.2"))
        self.assertTrue(ReleaseUtils.validate_version("1.0.0-rc.3"))
        self.assertFalse(ReleaseUtils.validate_version("invalid"))
        self.assertFalse(ReleaseUtils.validate_version("1.0"))

    def test_compare_versions(self):
        """测试比较版本号"""
        self.assertEqual(ReleaseUtils.compare_versions("1.0.0", "1.0.0"), 0)
        self.assertEqual(ReleaseUtils.compare_versions("1.1.0", "1.0.0"), 1)
        self.assertEqual(ReleaseUtils.compare_versions("1.0.0", "1.1.0"), -1)
        self.assertEqual(ReleaseUtils.compare_versions("2.0.0", "1.9.9"), 1)

    def test_is_prerelease(self):
        """测试检查是否为预发布"""
        self.assertTrue(ReleaseUtils.is_prerelease("1.0.0-alpha.1"))
        self.assertTrue(ReleaseUtils.is_prerelease("1.0.0-beta.1"))
        self.assertTrue(ReleaseUtils.is_prerelease("1.0.0-rc.1"))
        self.assertFalse(ReleaseUtils.is_prerelease("1.0.0"))


if __name__ == "__main__":
    unittest.main()
