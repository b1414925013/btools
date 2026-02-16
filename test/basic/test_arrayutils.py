"""测试ArrayUtils类"""
import unittest
import numpy as np
from btools.core.basic.arrayutils import ArrayUtils


class TestArrayUtils(unittest.TestCase):
    """测试ArrayUtils类"""

    def test_is_empty(self):
        """测试数组为空检查"""
        self.assertTrue(ArrayUtils.is_empty(None))
        self.assertTrue(ArrayUtils.is_empty([]))
        self.assertFalse(ArrayUtils.is_empty([1, 2, 3]))

    def test_size(self):
        """测试数组大小"""
        self.assertEqual(ArrayUtils.size([1, 2, 3]), 3)
        self.assertEqual(ArrayUtils.size(None), 0)

    def test_add(self):
        """测试添加元素"""
        arr = [1, 2, 3]
        ArrayUtils.add(arr, 4)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_add_all(self):
        """测试添加所有元素"""
        arr1 = [1, 2]
        arr2 = [3, 4]
        ArrayUtils.add_all(arr1, arr2)
        self.assertEqual(arr1, [1, 2, 3, 4])

    def test_remove(self):
        """测试移除元素"""
        arr = [1, 2, 3, 4]
        ArrayUtils.remove(arr, 2)
        self.assertEqual(arr, [1, 3, 4])

    def test_remove_at(self):
        """测试移除指定位置元素"""
        arr = [1, 2, 3, 4]
        ArrayUtils.remove_at(arr, 1)
        self.assertEqual(arr, [1, 3, 4])

    def test_get(self):
        """测试获取元素"""
        arr = [1, 2, 3, 4]
        self.assertEqual(ArrayUtils.get(arr, 1), 2)
        self.assertIsNone(ArrayUtils.get(arr, 10))

    def test_set(self):
        """测试设置元素"""
        arr = [1, 2, 3, 4]
        ArrayUtils.set(arr, 1, 5)
        self.assertEqual(arr, [1, 5, 3, 4])

    def test_index_of(self):
        """测试元素索引"""
        arr = [1, 2, 3, 4]
        self.assertEqual(ArrayUtils.index_of(arr, 2), 1)
        self.assertEqual(ArrayUtils.index_of(arr, 10), -1)

    def test_last_index_of(self):
        """测试元素最后索引"""
        arr = [1, 2, 3, 2, 4]
        self.assertEqual(ArrayUtils.last_index_of(arr, 2), 3)
        self.assertEqual(ArrayUtils.last_index_of(arr, 10), -1)

    def test_contains(self):
        """测试是否包含元素"""
        arr = [1, 2, 3, 4]
        self.assertTrue(ArrayUtils.contains(arr, 2))
        self.assertFalse(ArrayUtils.contains(arr, 10))

    def test_sort(self):
        """测试排序"""
        arr = [3, 1, 4, 2]
        ArrayUtils.sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4])

    def test_sorted(self):
        """测试返回排序后的数组"""
        arr = [3, 1, 4, 2]
        result = ArrayUtils.sorted(arr)
        self.assertEqual(result, [1, 2, 3, 4])
        self.assertEqual(arr, [3, 1, 4, 2])  # 原数组不变

    def test_reverse(self):
        """测试反转"""
        arr = [1, 2, 3, 4]
        ArrayUtils.reverse(arr)
        self.assertEqual(arr, [4, 3, 2, 1])

    def test_reversed(self):
        """测试返回反转后的数组"""
        arr = [1, 2, 3, 4]
        result = ArrayUtils.reversed(arr)
        self.assertEqual(result, [4, 3, 2, 1])
        self.assertEqual(arr, [1, 2, 3, 4])  # 原数组不变

    def test_copy(self):
        """测试复制"""
        arr = [1, 2, 3, 4]
        result = ArrayUtils.copy(arr)
        self.assertEqual(result, [1, 2, 3, 4])
        self.assertIsNot(result, arr)  # 不是同一个对象

    def test_sub_array(self):
        """测试子数组"""
        arr = [1, 2, 3, 4, 5]
        result = ArrayUtils.sub_array(arr, 1, 3)
        self.assertEqual(result, [2, 3])

    def test_concat(self):
        """测试连接"""
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        result = ArrayUtils.concat(arr1, arr2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_flatten(self):
        """测试扁平化"""
        arr = [[1, 2], [3, 4], [5, 6]]
        result = ArrayUtils.flatten(arr)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_distinct(self):
        """测试去重"""
        arr = [1, 2, 2, 3, 4, 4]
        result = ArrayUtils.distinct(arr)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_chunk(self):
        """测试分块"""
        arr = [1, 2, 3, 4, 5, 6]
        result = ArrayUtils.chunk(arr, 2)
        self.assertEqual(result, [[1, 2], [3, 4], [5, 6]])

    def test_fill(self):
        """测试填充"""
        arr = [1, 2, 3, 4]
        ArrayUtils.fill(arr, 0)
        self.assertEqual(arr, [0, 0, 0, 0])

    def test_to_list(self):
        """测试转换为列表"""
        arr = (1, 2, 3)
        result = ArrayUtils.to_list(arr)
        self.assertIsInstance(result, list)
        self.assertEqual(result, [1, 2, 3])

    def test_to_tuple(self):
        """测试转换为元组"""
        arr = [1, 2, 3]
        result = ArrayUtils.to_tuple(arr)
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (1, 2, 3))

    def test_to_numpy(self):
        """测试转换为numpy数组"""
        arr = [1, 2, 3, 4]
        result = ArrayUtils.to_numpy(arr)
        self.assertIsInstance(result, np.ndarray)
        np.testing.assert_array_equal(result, np.array([1, 2, 3, 4]))

    def test_max(self):
        """测试最大值"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayUtils.max(arr), 5)

    def test_min(self):
        """测试最小值"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayUtils.min(arr), 1)

    def test_sum(self):
        """测试求和"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayUtils.sum(arr), 15)

    def test_average(self):
        """测试平均值"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayUtils.average(arr), 3.0)

    def test_median(self):
        """测试中位数"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(ArrayUtils.median(arr), 3)
        arr = [1, 2, 3, 4]
        self.assertEqual(ArrayUtils.median(arr), 2.5)

    def test_frequency(self):
        """测试频率"""
        arr = [1, 2, 2, 3, 3, 3]
        self.assertEqual(ArrayUtils.frequency(arr, 2), 2)

    def test_filter(self):
        """测试过滤"""
        arr = [1, 2, 3, 4, 5]
        result = ArrayUtils.filter(arr, lambda x: x > 2)
        self.assertEqual(result, [3, 4, 5])

    def test_map(self):
        """测试映射"""
        arr = [1, 2, 3, 4, 5]
        result = ArrayUtils.map(arr, lambda x: x * 2)
        self.assertEqual(result, [2, 4, 6, 8, 10])

    def test_for_each(self):
        """测试遍历"""
        arr = [1, 2, 3, 4, 5]
        result = []
        ArrayUtils.for_each(arr, lambda x: result.append(x * 2))
        self.assertEqual(result, [2, 4, 6, 8, 10])

    def test_any_match(self):
        """测试任意匹配"""
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(ArrayUtils.any_match(arr, lambda x: x > 2))
        self.assertFalse(ArrayUtils.any_match(arr, lambda x: x > 10))

    def test_all_match(self):
        """测试所有匹配"""
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(ArrayUtils.all_match(arr, lambda x: x > 0))
        self.assertFalse(ArrayUtils.all_match(arr, lambda x: x > 2))

    def test_none_match(self):
        """测试无匹配"""
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(ArrayUtils.none_match(arr, lambda x: x > 10))
        self.assertFalse(ArrayUtils.none_match(arr, lambda x: x > 2))


if __name__ == "__main__":
    unittest.main()