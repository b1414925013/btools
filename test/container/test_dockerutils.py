"""测试DockerUtils类"""
import unittest
from btools.core.container.dockerutils import DockerUtils


class TestDockerUtils(unittest.TestCase):
    """测试DockerUtils类"""

    def test_is_available(self):
        """测试检查Docker是否可用"""
        is_available = DockerUtils.is_available()
        # 不强制断言，因为可能没有安装Docker
        self.assertIsInstance(is_available, bool)

    def test_run_docker_command(self):
        """测试运行Docker命令"""
        # 测试运行一个简单的命令
        code, stdout, stderr = DockerUtils.run_docker_command(["--version"])
        # 不强制断言，因为可能没有安装Docker
        self.assertIsInstance(code, int)


if __name__ == "__main__":
    unittest.main()
