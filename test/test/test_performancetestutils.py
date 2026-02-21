"""测试PerformanceTestUtils类"""
import unittest
import time
from btools.core.test.performancetestutils import PerformanceTestUtils


class TestPerformanceTestUtils(unittest.TestCase):
    """测试PerformanceTestUtils类"""

    def test_measure_time(self):
        """测试测量执行时间"""
        def slow_function():
            time.sleep(0.1)

        result = PerformanceTestUtils.measure_time(slow_function)
        self.assertIn('time', result)
        self.assertGreater(result['time'], 0)

    def test_measure_time_with_iterations(self):
        """测试多次测量"""
        def test_function():
            time.sleep(0.01)

        result = PerformanceTestUtils.measure_time(
            test_function,
            iterations=3,
            warmup=1
        )
        self.assertIn('average_time', result)

    def test_benchmark(self):
        """测试基准测试"""
        def func1():
            time.sleep(0.01)

        def func2():
            time.sleep(0.02)

        results = PerformanceTestUtils.benchmark(
            functions=[func1, func2],
            names=["Func1", "Func2"],
            iterations=2
        )
        self.assertIn("Func1", results)
        self.assertIn("Func2", results)


if __name__ == "__main__":
    unittest.main()
