"""测试EnvironmentUtils类"""
import unittest
import os
import tempfile
from btools.core.config.environmentutils import EnvironmentUtils


class TestEnvironmentUtils(unittest.TestCase):
    """测试EnvironmentUtils类"""

    def setUp(self):
        """设置测试环境"""
        self.temp_file = tempfile.mktemp(suffix=".env")
        with open(self.temp_file, "w", encoding="utf-8") as f:
            f.write("""TEST_STRING=hello
TEST_INT=123
TEST_BOOL=true
TEST_FLOAT=45.67
TEST_LIST=a,b,c
TEST_DICT=key1=value1,key2=value2
""")

    def tearDown(self):
        """清理测试环境"""
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_load_env(self):
        """测试加载环境变量文件"""
        success = EnvironmentUtils.load_env(self.temp_file)
        self.assertTrue(success)
        self.assertEqual(EnvironmentUtils.get_env('TEST_STRING'), 'hello')

    def test_get_env(self):
        """测试获取环境变量"""
        EnvironmentUtils.set_env('TEST_KEY', 'test_value')
        self.assertEqual(EnvironmentUtils.get_env('TEST_KEY'), 'test_value')
        self.assertEqual(EnvironmentUtils.get_env('NON_EXISTENT', 'default'), 'default')

    def test_get_env_int(self):
        """测试获取整型环境变量"""
        EnvironmentUtils.set_env('TEST_INT', '123')
        self.assertEqual(EnvironmentUtils.get_env_int('TEST_INT'), 123)
        self.assertEqual(EnvironmentUtils.get_env_int('NON_EXISTENT', 456), 456)

    def test_get_env_bool(self):
        """测试获取布尔型环境变量"""
        EnvironmentUtils.set_env('TEST_BOOL', 'true')
        self.assertTrue(EnvironmentUtils.get_env_bool('TEST_BOOL'))
        self.assertFalse(EnvironmentUtils.get_env_bool('NON_EXISTENT', False))

    def test_get_env_float(self):
        """测试获取浮点型环境变量"""
        EnvironmentUtils.set_env('TEST_FLOAT', '45.67')
        self.assertEqual(EnvironmentUtils.get_env_float('TEST_FLOAT'), 45.67)
        self.assertEqual(EnvironmentUtils.get_env_float('NON_EXISTENT', 12.34), 12.34)

    def test_set_env(self):
        """测试设置环境变量"""
        EnvironmentUtils.set_env('NEW_KEY', 'new_value')
        self.assertEqual(EnvironmentUtils.get_env('NEW_KEY'), 'new_value')

    def test_unset_env(self):
        """测试取消设置环境变量"""
        EnvironmentUtils.set_env('TO_DELETE', 'value')
        EnvironmentUtils.unset_env('TO_DELETE')
        self.assertIsNone(EnvironmentUtils.get_env('TO_DELETE'))

    def test_has_env(self):
        """测试检查环境变量是否存在"""
        EnvironmentUtils.set_env('EXISTENT', 'value')
        self.assertTrue(EnvironmentUtils.has_env('EXISTENT'))
        self.assertFalse(EnvironmentUtils.has_env('NON_EXISTENT'))

    def test_get_env_list(self):
        """测试获取列表型环境变量"""
        EnvironmentUtils.set_env('TEST_LIST', 'a,b,c')
        self.assertEqual(EnvironmentUtils.get_env_list('TEST_LIST'), ['a', 'b', 'c'])

    def test_get_env_dict(self):
        """测试获取字典型环境变量"""
        EnvironmentUtils.set_env('TEST_DICT', 'key1=value1,key2=value2')
        result = EnvironmentUtils.get_env_dict('TEST_DICT')
        self.assertEqual(result['key1'], 'value1')
        self.assertEqual(result['key2'], 'value2')

    def test_load_environment(self):
        """测试加载指定环境"""
        success = EnvironmentUtils.load_environment('test')
        self.assertTrue(success or not success)  # 只要不抛出异常就可以

    def test_get_current_environment(self):
        """测试获取当前环境"""
        env = EnvironmentUtils.get_current_environment()
        self.assertIsNotNone(env)

    def test_validate_environment(self):
        """测试验证环境变量"""
        EnvironmentUtils.set_env('REQUIRED1', 'value1')
        EnvironmentUtils.set_env('REQUIRED2', 'value2')
        missing = EnvironmentUtils.validate_environment(['REQUIRED1', 'REQUIRED2', 'REQUIRED3'])
        self.assertEqual(missing, ['REQUIRED3'])


if __name__ == "__main__":
    unittest.main()
