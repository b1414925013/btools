"""测试CollectionUtils类"""
import unittest
from btools.core.basic.collectionutils import CollectionUtils


class TestCollectionUtils(unittest.TestCase):
    """测试CollectionUtils类"""

    def test_is_empty(self):
        """测试集合为空检查"""
        self.assertTrue(CollectionUtils.is_empty(None))
        self.assertTrue(CollectionUtils.is_empty([]))
        self.assertFalse(CollectionUtils.is_empty([1, 2, 3]))

    def test_size(self):
        """测试集合大小"""
        self.assertEqual(CollectionUtils.size([1, 2, 3]), 3)
        self.assertEqual(CollectionUtils.size(None), 0)

    def test_add_all(self):
        """测试添加所有元素"""
        list1 = [1, 2]
        list2 = [3, 4]
        CollectionUtils.add_all(list1, list2)
        self.assertEqual(list1, [1, 2, 3, 4])

    def test_remove_all(self):
        """测试移除所有元素"""
        list1 = [1, 2, 3, 4]
        list2 = [2, 4]
        CollectionUtils.remove_all(list1, list2)
        self.assertEqual(list1, [1, 3])

    def test_retain_all(self):
        """测试保留所有元素"""
        list1 = [1, 2, 3, 4]
        list2 = [2, 4]
        CollectionUtils.retain_all(list1, list2)
        self.assertEqual(list1, [2, 4])

    def test_contains_all(self):
        """测试是否包含所有元素"""
        list1 = [1, 2, 3, 4]
        list2 = [2, 4]
        self.assertTrue(CollectionUtils.contains_all(list1, list2))
        list3 = [2, 5]
        self.assertFalse(CollectionUtils.contains_all(list1, list3))

    def test_find(self):
        """测试查找元素"""
        list1 = [1, 2, 3, 4]
        result = CollectionUtils.find(list1, lambda x: x > 2)
        self.assertEqual(result, 3)

    def test_filter(self):
        """测试过滤元素"""
        list1 = [1, 2, 3, 4]
        result = CollectionUtils.filter(list1, lambda x: x > 2)
        self.assertEqual(result, [3, 4])

    def test_map(self):
        """测试映射元素"""
        list1 = [1, 2, 3, 4]
        result = CollectionUtils.map(list1, lambda x: x * 2)
        self.assertEqual(result, [2, 4, 6, 8])

    def test_reduce(self):
        """测试归约元素"""
        list1 = [1, 2, 3, 4]
        result = CollectionUtils.reduce(list1, lambda x, y: x + y, 0)
        self.assertEqual(result, 10)

    def test_sort(self):
        """测试排序"""
        list1 = [3, 1, 4, 2]
        CollectionUtils.sort(list1)
        self.assertEqual(list1, [1, 2, 3, 4])

    def test_reverse(self):
        """测试反转"""
        list1 = [1, 2, 3, 4]
        CollectionUtils.reverse(list1)
        self.assertEqual(list1, [4, 3, 2, 1])

    def test_distinct(self):
        """测试去重"""
        list1 = [1, 2, 2, 3, 4, 4]
        result = CollectionUtils.distinct(list1)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_union(self):
        """测试并集"""
        list1 = [1, 2, 3]
        list2 = [3, 4, 5]
        result = CollectionUtils.union(list1, list2)
        self.assertEqual(set(result), {1, 2, 3, 4, 5})

    def test_intersection(self):
        """测试交集"""
        list1 = [1, 2, 3, 4]
        list2 = [3, 4, 5, 6]
        result = CollectionUtils.intersection(list1, list2)
        self.assertEqual(set(result), {3, 4})

    def test_difference(self):
        """测试差集"""
        list1 = [1, 2, 3, 4]
        list2 = [3, 4, 5, 6]
        result = CollectionUtils.difference(list1, list2)
        self.assertEqual(set(result), {1, 2})

    def test_to_list(self):
        """测试转换为列表"""
        s = {1, 2, 3}
        result = CollectionUtils.to_list(s)
        self.assertIsInstance(result, list)
        self.assertEqual(set(result), {1, 2, 3})

    def test_to_set(self):
        """测试转换为集合"""
        lst = [1, 2, 2, 3]
        result = CollectionUtils.to_set(lst)
        self.assertIsInstance(result, set)
        self.assertEqual(result, {1, 2, 3})

    def test_to_dict(self):
        """测试转换为字典"""
        lst = [("a", 1), ("b", 2)]
        result = CollectionUtils.to_dict(lst)
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {"a": 1, "b": 2})

    def test_zip(self):
        """测试压缩"""
        list1 = [1, 2, 3]
        list2 = ["a", "b", "c"]
        result = CollectionUtils.zip(list1, list2)
        self.assertEqual(result, [(1, "a"), (2, "b"), (3, "c")])

    def test_unzip(self):
        """测试解压"""
        lst = [(1, "a"), (2, "b"), (3, "c")]
        result1, result2 = CollectionUtils.unzip(lst)
        self.assertEqual(result1, [1, 2, 3])
        self.assertEqual(result2, ["a", "b", "c"])

    def test_chunk(self):
        """测试分块"""
        lst = [1, 2, 3, 4, 5, 6]
        result = CollectionUtils.chunk(lst, 2)
        self.assertEqual(result, [[1, 2], [3, 4], [5, 6]])

    def test_flatten(self):
        """测试扁平化"""
        lst = [[1, 2], [3, 4], [5, 6]]
        result = CollectionUtils.flatten(lst)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_frequency(self):
        """测试频率"""
        lst = [1, 2, 2, 3, 3, 3]
        result = CollectionUtils.frequency(lst, 2)
        self.assertEqual(result, 2)

    def test_max(self):
        """测试最大值"""
        lst = [1, 2, 3, 4, 5]
        result = CollectionUtils.max(lst)
        self.assertEqual(result, 5)

    def test_min(self):
        """测试最小值"""
        lst = [1, 2, 3, 4, 5]
        result = CollectionUtils.min(lst)
        self.assertEqual(result, 1)

    def test_sum(self):
        """测试求和"""
        lst = [1, 2, 3, 4, 5]
        result = CollectionUtils.sum(lst)
        self.assertEqual(result, 15)

    def test_average(self):
        """测试平均值"""
        lst = [1, 2, 3, 4, 5]
        result = CollectionUtils.average(lst)
        self.assertEqual(result, 3.0)


if __name__ == "__main__":
    unittest.main()