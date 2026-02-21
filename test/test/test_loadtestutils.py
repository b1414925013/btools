"""测试LoadTestUtils类"""
import unittest
import time
from btools.core.test.loadtestutils import LoadTestUtils


class TestLoadTestUtils(unittest.TestCase):
    """测试LoadTestUtils类"""

    def test_simple_load_test(self):
        """测试简单负载测试"""
        def test_func():
            time.sleep(0.01)
            return True

        # 快速测试，不使用长时间运行
        results = LoadTestUtils.run_load_test(
            func=test_func,
            concurrent_users=2,
            duration=1,
            ramp_up=0
        )
        self.assertIsInstance(results, dict)
        self.assertIn('total_requests', results)

    def test_check_thresholds(self):
        """测试检查阈值"""
        results = {
            'success_rate': 95.0,
            'average_response_time': 1.5
        }
        thresholds = {
            'min_success_rate': 90.0,
            'max_response_time': 2.0
        }
        check_result = LoadTestUtils.check_thresholds(results, thresholds)
        self.assertTrue(check_result['passed'])


if __name__ == "__main__":
    unittest.main()
