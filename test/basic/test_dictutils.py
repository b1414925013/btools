"""字典工具类测试"""
import unittest
from btools.core.basic import DictUtil


class TestDictUtil(unittest.TestCase):
    """DictUtil 测试类"""

    def test_is_empty(self):
        """测试 is_empty 方法"""
        self.assertTrue(DictUtil.is_empty(None))
        self.assertTrue(DictUtil.is_empty({}))
        self.assertFalse(DictUtil.is_empty({'a': 1}))

    def test_is_not_empty(self):
        """测试 is_not_empty 方法"""
        self.assertFalse(DictUtil.is_not_empty(None))
        self.assertFalse(DictUtil.is_not_empty({}))
        self.assertTrue(DictUtil.is_not_empty({'a': 1}))

    def test_size(self):
        """测试 size 方法"""
        self.assertEqual(DictUtil.size(None), 0)
        self.assertEqual(DictUtil.size({}), 0)
        self.assertEqual(DictUtil.size({'a': 1, 'b': 2}), 2)

    def test_get(self):
        """测试 get 方法"""
        d = {'a': 1, 'b': 2}
        self.assertEqual(DictUtil.get(d, 'a'), 1)
        self.assertEqual(DictUtil.get(d, 'c', 0), 0)
        self.assertIsNone(DictUtil.get(None, 'a'))

    def test_get_int(self):
        """测试 get_int 方法"""
        d = {'a': 1, 'b': '2', 'c': 'invalid'}
        self.assertEqual(DictUtil.get_int(d, 'a'), 1)
        self.assertEqual(DictUtil.get_int(d, 'b'), 2)
        self.assertEqual(DictUtil.get_int(d, 'c', 0), 0)
        self.assertEqual(DictUtil.get_int(d, 'd', 10), 10)

    def test_get_float(self):
        """测试 get_float 方法"""
        d = {'a': 1.5, 'b': '2.5', 'c': 'invalid'}
        self.assertEqual(DictUtil.get_float(d, 'a'), 1.5)
        self.assertEqual(DictUtil.get_float(d, 'b'), 2.5)
        self.assertEqual(DictUtil.get_float(d, 'c', 0.0), 0.0)
        self.assertEqual(DictUtil.get_float(d, 'd', 10.5), 10.5)

    def test_get_bool(self):
        """测试 get_bool 方法"""
        d = {'a': True, 'b': 'true', 'c': 'false', 'd': 1, 'e': 0}
        self.assertTrue(DictUtil.get_bool(d, 'a'))
        self.assertTrue(DictUtil.get_bool(d, 'b'))
        self.assertFalse(DictUtil.get_bool(d, 'c'))
        self.assertTrue(DictUtil.get_bool(d, 'd'))
        self.assertFalse(DictUtil.get_bool(d, 'e'))
        self.assertFalse(DictUtil.get_bool(d, 'f'))

    def test_get_str(self):
        """测试 get_str 方法"""
        d = {'a': 'hello', 'b': 123}
        self.assertEqual(DictUtil.get_str(d, 'a'), 'hello')
        self.assertEqual(DictUtil.get_str(d, 'b'), '123')
        self.assertEqual(DictUtil.get_str(d, 'c'), '')
        self.assertEqual(DictUtil.get_str(d, 'c', 'default'), 'default')

    def test_get_list(self):
        """测试 get_list 方法"""
        d = {'a': [1, 2, 3], 'b': 'not a list'}
        self.assertEqual(DictUtil.get_list(d, 'a'), [1, 2, 3])
        self.assertIsNone(DictUtil.get_list(d, 'b'))
        self.assertEqual(DictUtil.get_list(d, 'c', []), [])

    def test_get_dict(self):
        """测试 get_dict 方法"""
        d = {'a': {'x': 1}, 'b': 'not a dict'}
        self.assertEqual(DictUtil.get_dict(d, 'a'), {'x': 1})
        self.assertIsNone(DictUtil.get_dict(d, 'b'))
        self.assertEqual(DictUtil.get_dict(d, 'c', {}), {})

    def test_put(self):
        """测试 put 方法"""
        d = {'a': 1}
        DictUtil.put(d, 'b', 2)
        self.assertEqual(d, {'a': 1, 'b': 2})
        d2 = DictUtil.put(None, 'a', 1)
        self.assertEqual(d2, {'a': 1})

    def test_put_all(self):
        """测试 put_all 方法"""
        d = {'a': 1}
        DictUtil.put_all(d, {'b': 2, 'c': 3})
        self.assertEqual(d, {'a': 1, 'b': 2, 'c': 3})

    def test_put_if_absent(self):
        """测试 put_if_absent 方法"""
        d = {'a': 1}
        DictUtil.put_if_absent(d, 'a', 2)
        DictUtil.put_if_absent(d, 'b', 2)
        self.assertEqual(d, {'a': 1, 'b': 2})

    def test_remove(self):
        """测试 remove 方法"""
        d = {'a': 1, 'b': 2}
        DictUtil.remove(d, 'a')
        self.assertEqual(d, {'b': 2})

    def test_remove_all(self):
        """测试 remove_all 方法"""
        d = {'a': 1, 'b': 2, 'c': 3}
        DictUtil.remove_all(d, ['a', 'b'])
        self.assertEqual(d, {'c': 3})

    def test_clear(self):
        """测试 clear 方法"""
        d = {'a': 1, 'b': 2}
        DictUtil.clear(d)
        self.assertEqual(d, {})

    def test_contains_key(self):
        """测试 contains_key 方法"""
        d = {'a': 1}
        self.assertTrue(DictUtil.contains_key(d, 'a'))
        self.assertFalse(DictUtil.contains_key(d, 'b'))
        self.assertFalse(DictUtil.contains_key(None, 'a'))

    def test_contains_value(self):
        """测试 contains_value 方法"""
        d = {'a': 1}
        self.assertTrue(DictUtil.contains_value(d, 1))
        self.assertFalse(DictUtil.contains_value(d, 2))
        self.assertFalse(DictUtil.contains_value(None, 1))

    def test_keys(self):
        """测试 keys 方法"""
        d = {'a': 1, 'b': 2}
        self.assertEqual(sorted(DictUtil.keys(d)), ['a', 'b'])
        self.assertEqual(DictUtil.keys(None), [])

    def test_values(self):
        """测试 values 方法"""
        d = {'a': 1, 'b': 2}
        self.assertEqual(sorted(DictUtil.values(d)), [1, 2])
        self.assertEqual(DictUtil.values(None), [])

    def test_items(self):
        """测试 items 方法"""
        d = {'a': 1, 'b': 2}
        self.assertEqual(sorted(DictUtil.items(d)), [('a', 1), ('b', 2)])
        self.assertEqual(DictUtil.items(None), [])

    def test_invert(self):
        """测试 invert 方法"""
        d = {'a': 1, 'b': 2}
        self.assertEqual(DictUtil.invert(d), {1: 'a', 2: 'b'})
        self.assertEqual(DictUtil.invert(None), {})

    def test_merge(self):
        """测试 merge 方法"""
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        merged = DictUtil.merge(d1, d2)
        self.assertEqual(merged, {'a': 1, 'b': 3, 'c': 4})
        merged_no_overwrite = DictUtil.merge(d1, d2, overwrite=False)
        self.assertEqual(merged_no_overwrite, {'a': 1, 'b': 2, 'c': 4})

    def test_filter(self):
        """测试 filter 方法"""
        d = {'a': 1, 'b': 2, 'c': 3}
        filtered = DictUtil.filter(d, lambda k, v: v > 1)
        self.assertEqual(filtered, {'b': 2, 'c': 3})

    def test_filter_keys(self):
        """测试 filter_keys 方法"""
        d = {'a': 1, 'b': 2, 'c': 3}
        filtered = DictUtil.filter_keys(d, lambda k: k != 'a')
        self.assertEqual(filtered, {'b': 2, 'c': 3})

    def test_filter_values(self):
        """测试 filter_values 方法"""
        d = {'a': 1, 'b': 2, 'c': 3}
        filtered = DictUtil.filter_values(d, lambda v: v < 3)
        self.assertEqual(filtered, {'a': 1, 'b': 2})

    def test_map_keys(self):
        """测试 map_keys 方法"""
        d = {'a': 1, 'b': 2}
        mapped = DictUtil.map_keys(d, lambda k: k.upper())
        self.assertEqual(mapped, {'A': 1, 'B': 2})

    def test_map_values(self):
        """测试 map_values 方法"""
        d = {'a': 1, 'b': 2}
        mapped = DictUtil.map_values(d, lambda v: v * 2)
        self.assertEqual(mapped, {'a': 2, 'b': 4})

    def test_map_items(self):
        """测试 map_items 方法"""
        d = {'a': 1, 'b': 2}
        mapped = DictUtil.map_items(d, lambda k, v: (k.upper(), v * 2))
        self.assertEqual(mapped, {'A': 2, 'B': 4})

    def test_sort_by_key(self):
        """测试 sort_by_key 方法"""
        d = {'b': 2, 'a': 1, 'c': 3}
        sorted_dict = DictUtil.sort_by_key(d)
        self.assertEqual(list(sorted_dict.keys()), ['a', 'b', 'c'])

    def test_sort_by_value(self):
        """测试 sort_by_value 方法"""
        d = {'b': 2, 'a': 1, 'c': 3}
        sorted_dict = DictUtil.sort_by_value(d)
        self.assertEqual(list(sorted_dict.values()), [1, 2, 3])

    def test_slice(self):
        """测试 slice 方法"""
        d = {'a': 1, 'b': 2, 'c': 3}
        sliced = DictUtil.slice(d, ['a', 'c'])
        self.assertEqual(sliced, {'a': 1, 'c': 3})

    def test_omit(self):
        """测试 omit 方法"""
        d = {'a': 1, 'b': 2, 'c': 3}
        omitted = DictUtil.omit(d, ['a', 'c'])
        self.assertEqual(omitted, {'b': 2})

    def test_to_list(self):
        """测试 to_list 方法"""
        d = {'a': 1, 'b': 2}
        lst = DictUtil.to_list(d)
        self.assertEqual(len(lst), 2)

    def test_from_list(self):
        """测试 from_list 方法"""
        lst = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}]
        d = DictUtil.from_list(lst)
        self.assertEqual(d, {'a': 1, 'b': 2})

    def test_deep_copy(self):
        """测试 deep_copy 方法"""
        d = {'a': 1, 'b': {'x': 1}}
        copied = DictUtil.deep_copy(d)
        self.assertEqual(copied, d)
        copied['b']['x'] = 2
        self.assertEqual(d['b']['x'], 1)

    def test_shallow_copy(self):
        """测试 shallow_copy 方法"""
        d = {'a': 1, 'b': {'x': 1}}
        copied = DictUtil.shallow_copy(d)
        self.assertEqual(copied, d)
        copied['b']['x'] = 2
        self.assertEqual(d['b']['x'], 2)

    def test_get_nested(self):
        """测试 get_nested 方法"""
        d = {'a': {'b': {'c': 1}}}
        self.assertEqual(DictUtil.get_nested(d, ['a', 'b', 'c']), 1)
        self.assertEqual(DictUtil.get_nested(d, ['a', 'x', 'c'], 'default'), 'default')

    def test_set_nested(self):
        """测试 set_nested 方法"""
        d = {}
        DictUtil.set_nested(d, ['a', 'b', 'c'], 1)
        self.assertEqual(d, {'a': {'b': {'c': 1}}})

    def test_has_nested(self):
        """测试 has_nested 方法"""
        d = {'a': {'b': {'c': 1}}}
        self.assertTrue(DictUtil.has_nested(d, ['a', 'b', 'c']))
        self.assertFalse(DictUtil.has_nested(d, ['a', 'x', 'c']))

    def test_group_by(self):
        """测试 group_by 方法"""
        lst = [{'name': 'a', 'type': 1}, {'name': 'b', 'type': 1}, {'name': 'c', 'type': 2}]
        grouped = DictUtil.group_by(lst, lambda x: x['type'])
        self.assertEqual(len(grouped[1]), 2)
        self.assertEqual(len(grouped[2]), 1)

    def test_count_by(self):
        """测试 count_by 方法"""
        lst = [{'name': 'a', 'type': 1}, {'name': 'b', 'type': 1}, {'name': 'c', 'type': 2}]
        counted = DictUtil.count_by(lst, lambda x: x['type'])
        self.assertEqual(counted[1], 2)
        self.assertEqual(counted[2], 1)


if __name__ == '__main__':
    unittest.main()
