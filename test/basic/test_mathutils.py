"""测试MathUtils类"""
import unittest
from btools.core.basic.mathutils import MathUtils


class TestMathUtils(unittest.TestCase):
    """测试MathUtils类"""

    def test_abs(self):
        """测试绝对值"""
        self.assertEqual(MathUtils.abs(-1), 1)
        self.assertEqual(MathUtils.abs(1), 1)

    def test_sqrt(self):
        """测试平方根"""
        self.assertAlmostEqual(MathUtils.sqrt(4), 2.0)

    def test_pow(self):
        """测试幂运算"""
        self.assertEqual(MathUtils.pow(2, 3), 8)

    def test_exp(self):
        """测试指数运算"""
        self.assertAlmostEqual(MathUtils.exp(1), 2.718281828459045)

    def test_log(self):
        """测试自然对数"""
        self.assertAlmostEqual(MathUtils.log(1), 0.0)

    def test_log10(self):
        """测试以10为底的对数"""
        self.assertAlmostEqual(MathUtils.log10(10), 1.0)

    def test_sin(self):
        """测试正弦"""
        self.assertAlmostEqual(MathUtils.sin(0), 0.0)

    def test_cos(self):
        """测试余弦"""
        self.assertAlmostEqual(MathUtils.cos(0), 1.0)

    def test_tan(self):
        """测试正切"""
        self.assertAlmostEqual(MathUtils.tan(0), 0.0)

    def test_radians(self):
        """测试角度转弧度"""
        self.assertAlmostEqual(MathUtils.radians(180), 3.141592653589793)

    def test_degrees(self):
        """测试弧度转角度"""
        self.assertAlmostEqual(MathUtils.degrees(3.141592653589793), 180.0)

    def test_ceil(self):
        """测试向上取整"""
        self.assertEqual(MathUtils.ceil(1.2), 2)

    def test_floor(self):
        """测试向下取整"""
        self.assertEqual(MathUtils.floor(1.8), 1)

    def test_round(self):
        """测试四舍五入"""
        self.assertEqual(MathUtils.round(1.2), 1)
        self.assertEqual(MathUtils.round(1.8), 2)

    def test_trunc(self):
        """测试截断"""
        self.assertEqual(MathUtils.trunc(1.8), 1)
        self.assertEqual(MathUtils.trunc(-1.8), -1)

    def test_sign(self):
        """测试符号"""
        self.assertEqual(MathUtils.sign(1), 1)
        self.assertEqual(MathUtils.sign(-1), -1)
        self.assertEqual(MathUtils.sign(0), 0)

    def test_max(self):
        """测试最大值"""
        self.assertEqual(MathUtils.max(1, 2, 3), 3)

    def test_min(self):
        """测试最小值"""
        self.assertEqual(MathUtils.min(1, 2, 3), 1)

    def test_sum(self):
        """测试求和"""
        self.assertEqual(MathUtils.sum(1, 2, 3), 6)

    def test_average(self):
        """测试平均值"""
        self.assertAlmostEqual(MathUtils.average(1, 2, 3), 2.0)

    def test_median(self):
        """测试中位数"""
        self.assertEqual(MathUtils.median(1, 2, 3), 2)
        self.assertEqual(MathUtils.median(1, 2, 3, 4), 2.5)

    def test_gcd(self):
        """测试最大公约数"""
        self.assertEqual(MathUtils.gcd(4, 6), 2)

    def test_lcm(self):
        """测试最小公倍数"""
        self.assertEqual(MathUtils.lcm(4, 6), 12)

    def test_is_integer(self):
        """测试是否为整数"""
        self.assertTrue(MathUtils.is_integer(1))
        self.assertFalse(MathUtils.is_integer(1.2))

    def test_is_even(self):
        """测试是否为偶数"""
        self.assertTrue(MathUtils.is_even(2))
        self.assertFalse(MathUtils.is_even(1))

    def test_is_odd(self):
        """测试是否为奇数"""
        self.assertTrue(MathUtils.is_odd(1))
        self.assertFalse(MathUtils.is_odd(2))

    def test_is_prime(self):
        """测试是否为质数"""
        self.assertTrue(MathUtils.is_prime(2))
        self.assertTrue(MathUtils.is_prime(3))
        self.assertFalse(MathUtils.is_prime(4))

    def test_generate_random_integer(self):
        """测试生成随机整数"""
        result = MathUtils.generate_random_integer(1, 10)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 10)

    def test_generate_random_float(self):
        """测试生成随机浮点数"""
        result = MathUtils.generate_random_float(1, 10)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 10)

    def test_generate_random_choice(self):
        """测试随机选择"""
        choices = [1, 2, 3, 4, 5]
        result = MathUtils.generate_random_choice(choices)
        self.assertIn(result, choices)

    def test_generate_random_sample(self):
        """测试随机采样"""
        population = [1, 2, 3, 4, 5]
        result = MathUtils.generate_random_sample(population, 3)
        self.assertEqual(len(result), 3)
        for item in result:
            self.assertIn(item, population)

    def test_shuffle(self):
        """测试洗牌"""
        arr = [1, 2, 3, 4, 5]
        original = arr.copy()
        MathUtils.shuffle(arr)
        self.assertNotEqual(arr, original)
        self.assertEqual(set(arr), set(original))

    def test_set_random_seed(self):
        """测试设置随机种子"""
        MathUtils.set_random_seed(42)
        result1 = MathUtils.generate_random_integer(1, 10)
        MathUtils.set_random_seed(42)
        result2 = MathUtils.generate_random_integer(1, 10)
        self.assertEqual(result1, result2)

    def test_distance(self):
        """测试距离"""
        self.assertAlmostEqual(MathUtils.distance(0, 0, 3, 4), 5.0)

    def test_clamp(self):
        """测试钳制"""
        self.assertEqual(MathUtils.clamp(5, 1, 10), 5)
        self.assertEqual(MathUtils.clamp(0, 1, 10), 1)
        self.assertEqual(MathUtils.clamp(15, 1, 10), 10)

    def test_lerp(self):
        """测试线性插值"""
        self.assertEqual(MathUtils.lerp(0, 10, 0.5), 5)

    def test_factorial(self):
        """测试阶乘"""
        self.assertEqual(MathUtils.factorial(5), 120)

    def test_combinations(self):
        """测试组合数"""
        self.assertEqual(MathUtils.combinations(5, 2), 10)

    def test_permutations(self):
        """测试排列数"""
        self.assertEqual(MathUtils.permutations(5, 2), 20)


if __name__ == "__main__":
    unittest.main()