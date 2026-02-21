"""测试PackagingUtils类"""
import unittest
import os
from btools.core.release.packagingutils import PackagingUtils


class TestPackagingUtils(unittest.TestCase):
    """测试PackagingUtils类"""

    def test_get_project_info(self):
        """测试获取项目信息"""
        info = PackagingUtils.get_project_info(".")
        self.assertIsInstance(info, dict)

    def test_validate_version(self):
        """测试验证版本号"""
        from btools.core.release.releaseutils import ReleaseUtils
        self.assertTrue(ReleaseUtils.validate_version("1.0.0"))
        self.assertTrue(ReleaseUtils.validate_version("1.0.0-beta.1"))
        self.assertFalse(ReleaseUtils.validate_version("invalid"))

    def test_compare_versions(self):
        """测试比较版本号"""
        from btools.core.release.releaseutils import ReleaseUtils
        self.assertEqual(ReleaseUtils.compare_versions("1.0.0", "1.0.0"), 0)
        self.assertEqual(ReleaseUtils.compare_versions("1.1.0", "1.0.0"), 1)
        self.assertEqual(ReleaseUtils.compare_versions("1.0.0", "1.1.0"), -1)


if __name__ == "__main__":
    unittest.main()
