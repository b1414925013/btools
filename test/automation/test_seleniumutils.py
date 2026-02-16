"""测试SeleniumUtils类"""
import unittest
from btools.core.automation.seleniumutils import SeleniumUtils


class TestSeleniumUtils(unittest.TestCase):
    """测试SeleniumUtils类"""

    def test_get_driver(self):
        """测试获取WebDriver"""
        # 跳过测试，因为需要网络连接下载chromedriver
        self.skipTest("需要网络连接下载chromedriver")
        selenium = SeleniumUtils()
        driver = selenium.get_driver(headless=True)
        self.assertIsNotNone(driver)
        driver.quit()


if __name__ == "__main__":
    unittest.main()