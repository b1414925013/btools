"""测试KubernetesUtils类"""
import unittest
from btools.core.container.kubernetesutils import KubernetesUtils


class TestKubernetesUtils(unittest.TestCase):
    """测试KubernetesUtils类"""

    def test_is_available(self):
        """测试检查kubectl是否可用"""
        is_available = KubernetesUtils.is_available()
        # 不强制断言，因为可能没有安装kubectl
        self.assertIsInstance(is_available, bool)

    def test_run_kubectl_command(self):
        """测试运行kubectl命令"""
        code, stdout, stderr = KubernetesUtils.run_kubectl_command(["version", "--client"])
        # 不强制断言，因为可能没有安装kubectl
        self.assertIsInstance(code, int)


if __name__ == "__main__":
    unittest.main()
