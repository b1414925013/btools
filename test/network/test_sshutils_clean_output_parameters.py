import pytest
import inspect
from btools.core.network.sshutils import SSHClient


class TestSSHUtilsCleanOutputParameters:
    """测试SSHUtils的clean_output和remove_command参数"""

    def setup_method(self):
        """设置测试环境"""
        self.ssh_client = SSHClient()

    def test_execute_clean_output_parameter(self):
        """测试execute方法的clean_output参数存在性和默认值"""
        sig = inspect.signature(self.ssh_client.execute)
        params = sig.parameters
        assert 'clean_output' in params
        assert params['clean_output'].default == False

    def test_execute_as_root_clean_output_parameter(self):
        """测试execute_as_root方法的clean_output参数存在性和默认值"""
        sig = inspect.signature(self.ssh_client.execute_as_root)
        params = sig.parameters
        assert 'clean_output' in params
        assert params['clean_output'].default == False

    def test_su_to_root_clean_output_parameter(self):
        """测试su_to_root方法的clean_output参数存在性和默认值"""
        sig = inspect.signature(self.ssh_client.su_to_root)
        params = sig.parameters
        assert 'clean_output' in params
        assert params['clean_output'].default == True

    def test_start_root_shell_clean_output_parameter(self):
        """测试start_root_shell方法的clean_output参数存在性和默认值"""
        sig = inspect.signature(self.ssh_client.start_root_shell)
        params = sig.parameters
        assert 'clean_output' in params
        assert params['clean_output'].default == True

    def test_execute_in_root_shell_clean_output_parameter(self):
        """测试execute_in_root_shell方法的clean_output参数存在性和默认值"""
        sig = inspect.signature(self.ssh_client.execute_in_root_shell)
        params = sig.parameters
        assert 'clean_output' in params
        assert params['clean_output'].default == True

    def test_execute_in_root_shell_remove_command_parameter(self):
        """测试execute_in_root_shell方法的remove_command参数存在性和默认值"""
        sig = inspect.signature(self.ssh_client.execute_in_root_shell)
        params = sig.parameters
        assert 'remove_command' in params
        assert params['remove_command'].default == False

    def test_clean_output_default_values(self):
        """测试各方法clean_output参数的默认值"""
        # execute方法默认为False
        sig = inspect.signature(self.ssh_client.execute)
        assert sig.parameters['clean_output'].default == False

        # execute_as_root方法默认为False
        sig = inspect.signature(self.ssh_client.execute_as_root)
        assert sig.parameters['clean_output'].default == False

        # su_to_root方法默认为True
        sig = inspect.signature(self.ssh_client.su_to_root)
        assert sig.parameters['clean_output'].default == True

        # start_root_shell方法默认为True
        sig = inspect.signature(self.ssh_client.start_root_shell)
        assert sig.parameters['clean_output'].default == True

        # execute_in_root_shell方法默认为True
        sig = inspect.signature(self.ssh_client.execute_in_root_shell)
        assert sig.parameters['clean_output'].default == True

    def test_clean_output_functionality(self):
        """测试_clean_output方法的功能"""
        # 测试ANSI颜色代码清洗
        test_string = "\x1b[31mHello\x1b[0m World"
        result = self.ssh_client._clean_output(test_string)
        assert result == "Hello World"

        # 测试CSI序列清洗
        test_string = "\x1b[2J\x1b[HHello\x1b[5;10HWorld"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorld"

        # 测试OSC序列清洗
        test_string = "\x1b]0;Title\x07Hello"
        result = self.ssh_client._clean_output(test_string)
        assert result == "Hello"

        # 测试回车符处理
        test_string = "Hello\r\nWorld\rTest"
        result = self.ssh_client._clean_output(test_string)
        assert result == "Hello\nWorld\nTest"

        # 测试bytes类型输入
        test_bytes = b"\x1b[31mHello\x1b[0m World"
        result = self.ssh_client._clean_output(test_bytes)
        assert result == "Hello World"

    def test_parameter_signatures(self):
        """测试所有相关方法的参数签名"""
        # 测试execute方法
        sig = inspect.signature(self.ssh_client.execute)
        params = list(sig.parameters.keys())
        assert 'command' in params
        assert 'sudo' in params
        assert 'sudo_password' in params
        assert 'clean_output' in params

        # 测试execute_as_root方法
        sig = inspect.signature(self.ssh_client.execute_as_root)
        params = list(sig.parameters.keys())
        assert 'command' in params
        assert 'root_password' in params
        assert 'timeout' in params
        assert 'clean_output' in params

        # 测试su_to_root方法
        sig = inspect.signature(self.ssh_client.su_to_root)
        params = list(sig.parameters.keys())
        assert 'root_password' in params
        assert 'timeout' in params
        assert 'clean_output' in params

        # 测试start_root_shell方法
        sig = inspect.signature(self.ssh_client.start_root_shell)
        params = list(sig.parameters.keys())
        assert 'root_password' in params
        assert 'timeout' in params
        assert 'clean_output' in params

        # 测试execute_in_root_shell方法
        sig = inspect.signature(self.ssh_client.execute_in_root_shell)
        params = list(sig.parameters.keys())
        assert 'command' in params
        assert 'timeout' in params
        assert 'expected_prompt' in params
        assert 'clean_output' in params
        assert 'remove_command' in params


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
