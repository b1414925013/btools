import re
import pytest
from btools.core.network.sshutils import SSHClient

class TestSSHUtilsCleanOutput:
    """测试SSHUtils的_clean_output方法"""

    def setup_method(self):
        """设置测试环境"""
        self.ssh_client = SSHClient()

    def test_clean_ansi_color_codes(self):
        """测试清洗ANSI颜色代码"""
        test_string = "\x1b[31mHello\x1b[0m World"
        result = self.ssh_client._clean_output(test_string)
        assert result == "Hello World"

    def test_clean_csi_sequences(self):
        """测试清洗CSI序列"""
        # 光标移动序列
        test_string = "\x1b[2J\x1b[HHello\x1b[5;10HWorld"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorld"

        # 清除屏幕和行的序列
        test_string = "\x1b[2J\x1b[KHello\x1b[1KWorld"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorld"

        # 控制光标显示的序列
        test_string = "\x1b[?25lHello\x1b[?25hWorld"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorld"

    def test_clean_osc_sequences(self):
        """测试清洗OSC序列（设置窗口标题等）"""
        # 带BEL结束的OSC序列
        test_string = "\x1b]0;Title\x07Hello"
        result = self.ssh_client._clean_output(test_string)
        assert result == "Hello"

        # 带ST结束的OSC序列
        test_string = "\x1b]0;Title\x1b\\Hello"
        result = self.ssh_client._clean_output(test_string)
        assert result == "Hello"

    def test_clean_charset_switching(self):
        """测试清洗字符集切换序列"""
        test_string = "\x1b(AHello\x1b)BWorld"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorld"

    def test_clean_private_sequences(self):
        """测试清洗私有序列"""
        test_string = "\x1b<Hello\x1b>World"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorld"

    def test_clean_control_characters(self):
        """测试清洗控制字符"""
        test_string = "Hello\x00\x01\x02World\x7f"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorld"

    def test_clean_carriage_returns(self):
        """测试清洗回车符"""
        test_string = "Hello\r\nWorld\rTest"
        result = self.ssh_client._clean_output(test_string)
        assert result == "Hello\nWorld\nTest"

    def test_clean_bytes_input(self):
        """测试处理bytes类型输入"""
        test_bytes = b"\x1b[31mHello\x1b[0m World"
        result = self.ssh_client._clean_output(test_bytes)
        assert result == "Hello World"

    def test_clean_complex_mixed_sequences(self):
        """测试清洗复杂的混合序列"""
        test_string = "\x1b]0;Title\x07\x1b[31mHello\x1b[0m\x1b[2J\x1b[HWorld\r\nTest"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorld\nTest"

    def test_clean_empty_string(self):
        """测试清洗空字符串"""
        result = self.ssh_client._clean_output("")
        assert result == ""

    def test_clean_non_string_input(self):
        """测试清洗非字符串输入"""
        result = self.ssh_client._clean_output(123)
        assert result == "123"

        result = self.ssh_client._clean_output(None)
        assert result == "None"

    def test_clean_nested_sequences(self):
        """测试清洗嵌套序列"""
        test_string = "\x1b[31mHello\x1b[0m\x1b]0;Title\x07World"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorld"

    def test_clean_partial_overlapping_sequences(self):
        """测试清洗部分重叠的序列"""
        # 这里模拟一个部分重叠的情况
        test_string = "\x1b[31mHello\x1b[0mWorld"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorld"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])