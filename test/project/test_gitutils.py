"""测试GitUtils类"""
import unittest
import os
from btools.core.project.gitutils import GitUtils


class TestGitUtils(unittest.TestCase):
    """测试GitUtils类"""

    def test_get_current_branch(self):
        """测试获取当前分支"""
        branch = GitUtils.get_current_branch(".")
        self.assertIsNotNone(branch)

    def test_get_branches(self):
        """测试获取所有分支"""
        branches = GitUtils.get_branches(".")
        self.assertIsInstance(branches, list)

    def test_validate_commit_message(self):
        """测试验证提交信息"""
        self.assertTrue(GitUtils.validate_commit_message("feat: 添加新功能"))
        self.assertTrue(GitUtils.validate_commit_message("fix: 修复bug"))
        self.assertTrue(GitUtils.validate_commit_message("docs: 更新文档"))
        self.assertFalse(GitUtils.validate_commit_message("invalid message"))

    def test_run_git_command(self):
        """测试运行Git命令"""
        code, stdout, stderr = GitUtils.run_git_command(["status"], ".")
        self.assertIn(code, [0, 1])


if __name__ == "__main__":
    unittest.main()
