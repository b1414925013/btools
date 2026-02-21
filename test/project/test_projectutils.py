"""测试ProjectUtils类"""
import unittest
import os
import tempfile
from btools.core.project.projectutils import ProjectUtils


class TestProjectUtils(unittest.TestCase):
    """测试ProjectUtils类"""

    def setUp(self):
        """设置测试环境"""
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """清理测试环境"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_get_project_structure(self):
        """测试获取项目结构"""
        structure = ProjectUtils.get_project_structure(".")
        self.assertIsInstance(structure, dict)
        self.assertIn('__files__', structure)

    def test_analyze_dependencies(self):
        """测试分析依赖"""
        deps = ProjectUtils.analyze_dependencies(".")
        self.assertIsInstance(deps, dict)
        self.assertIn('requirements', deps)
        self.assertIn('setup', deps)
        self.assertIn('pip', deps)

    def test_is_python_project(self):
        """测试检查是否为Python项目"""
        is_python = ProjectUtils.is_python_project(".")
        self.assertTrue(is_python)

    def test_has_git_repository(self):
        """测试检查是否有Git仓库"""
        has_git = ProjectUtils.has_git_repository(".")
        self.assertTrue(has_git)


if __name__ == "__main__":
    unittest.main()
