import pytest
from btools.core.network.sshutils import SSHClient

class TestSSHUtilsComplexSequences:
    """测试SSHUtils的_clean_output方法处理复杂序列组合"""

    def setup_method(self):
        """设置测试环境"""
        self.ssh_client = SSHClient()

    def test_complex_sequence_combination(self):
        """测试复杂的序列组合"""
        # 包含多种类型的终端控制序列
        test_string = """
        \x1b]0;Test Window Title\x07
        \x1b[31m\x1b[1mHello\x1b[0m
        \x1b[2J\x1b[H
        \x1b[5;10H\x1b[32mWorld\x1b[0m
        \x1b[?25l
        \x1b(A\x1b[?25h\x1b)B
        \x1b<\x1b>\x1b[34mTest\x1b[0m
        \r\nLine 1\rLine 2\nLine 3
        """
        
        result = self.ssh_client._clean_output(test_string)
        expected = "Hello\nWorld\nTest\nLine 1\nLine 2\nLine 3"
        
        # 去除所有空白字符后比较，因为原始测试字符串有很多换行和空格
        import re
        result_clean = re.sub(r'\s+', '', result)
        expected_clean = re.sub(r'\s+', '', expected)
        
        assert result_clean == expected_clean

    def test_nested_sequences(self):
        """测试嵌套的序列"""
        # 嵌套的终端控制序列
        test_string = "\x1b[31mHello\x1b[32mWorld\x1b[0m"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorld"

    def test_overlapping_sequences(self):
        """测试部分重叠的序列"""
        # 模拟部分重叠的情况
        test_string = "\x1b[31mHello\x1b[0mWorld\x1b[32mTest\x1b[0m"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorldTest"

    def test_sequential_sequences(self):
        """测试连续的序列"""
        # 连续的终端控制序列
        test_string = "\x1b[31m\x1b[1m\x1b[4mHello\x1b[0m\x1b[32mWorld\x1b[0m"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorld"

    def test_mixed_with_control_characters(self):
        """测试混合控制字符的情况"""
        # 混合终端控制序列和其他控制字符
        test_string = "\x00\x1b[31mHello\x01\x1b[0m\x02World\x7f"
        result = self.ssh_client._clean_output(test_string)
        assert result == "HelloWorld"

    def test_real_world_scenario(self):
        """测试真实世界的场景"""
        # 模拟真实SSH会话中的输出
        test_string = """\x1b[0;32mroot@server:~#\x1b[0m \x1b[31mls -la\x1b[0m\r\n\x1b[0;34mdrwxr-xr-x  2 root root 4096 Mar 15 10:00\x1b[0m .\r\n\x1b[0;34mdrwxr-xr-x 20 root root 4096 Mar 15 09:00\x1b[0m ..\r\n\x1b[0;31m-rw-r--r--  1 root root  123 Mar 15 10:00\x1b[0m test.txt\r\n\x1b[0;32mroot@server:~#\x1b[0m"""
        result = self.ssh_client._clean_output(test_string)
        
        # 期望的结果应该包含命令和输出，但不包含颜色代码和提示符
        expected_lines = [
            "root@server:~# ls -la",
            "drwxr-xr-x  2 root root 4096 Mar 15 10:00 .",
            "drwxr-xr-x 20 root root 4096 Mar 15 09:00 ..",
            "-rw-r--r--  1 root root  123 Mar 15 10:00 test.txt",
            "root@server:~#"
        ]
        expected = "\n".join(expected_lines)
        
        assert result == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])