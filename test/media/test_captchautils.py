"""测试CaptchaUtils类"""
import unittest
from btools.core.media.captchautils import CaptchaUtils


class TestCaptchaUtils(unittest.TestCase):
    """测试CaptchaUtils类"""

    def test_generate_captcha(self):
        """测试生成验证码"""
        # 生成验证码
        captcha_text, image_bytes = CaptchaUtils.generate_captcha()
        
        # 验证结果
        self.assertEqual(len(captcha_text), 4)
        self.assertTrue(isinstance(image_bytes, bytes))
        self.assertTrue(len(image_bytes) > 0)

    def test_generate_captcha_with_custom_length(self):
        """测试生成指定长度的验证码"""
        # 生成6位验证码
        captcha_text, image_bytes = CaptchaUtils.generate_captcha(length=6)
        
        # 验证结果
        self.assertEqual(len(captcha_text), 6)
        self.assertTrue(isinstance(image_bytes, bytes))

    def test_generate_captcha_numeric(self):
        """测试生成纯数字验证码"""
        # 生成纯数字验证码
        captcha_text, image_bytes = CaptchaUtils.generate_captcha(captcha_type=CaptchaUtils.TYPE_NUMERIC)
        
        # 验证结果
        self.assertTrue(captcha_text.isdigit())
        self.assertTrue(isinstance(image_bytes, bytes))

    def test_generate_captcha_alpha(self):
        """测试生成纯字母验证码"""
        # 生成纯字母验证码
        captcha_text, image_bytes = CaptchaUtils.generate_captcha(captcha_type=CaptchaUtils.TYPE_ALPHA)
        
        # 验证结果
        self.assertTrue(captcha_text.isalpha())
        self.assertTrue(isinstance(image_bytes, bytes))

    def test_generate_captcha_alphanumeric(self):
        """测试生成字母数字混合验证码"""
        # 生成字母数字混合验证码
        captcha_text, image_bytes = CaptchaUtils.generate_captcha(captcha_type=CaptchaUtils.TYPE_ALPHANUMERIC)
        
        # 验证结果
        self.assertTrue(any(c.isalpha() for c in captcha_text) or any(c.isdigit() for c in captcha_text))
        self.assertTrue(isinstance(image_bytes, bytes))

    def test_generate_captcha_base64(self):
        """测试生成Base64格式的验证码"""
        # 生成Base64格式的验证码
        captcha_text, base64_str = CaptchaUtils.generate_captcha_base64()
        
        # 验证结果
        self.assertEqual(len(captcha_text), 4)
        self.assertTrue(isinstance(base64_str, str))
        self.assertTrue(len(base64_str) > 0)

    def test_generate_math_captcha(self):
        """测试生成数学计算验证码"""
        # 生成数学计算验证码
        expression, answer, image_bytes = CaptchaUtils.generate_math_captcha()
        
        # 验证结果
        self.assertTrue('=' in expression)
        self.assertTrue('?' in expression)
        self.assertTrue(answer.isdigit())
        self.assertTrue(isinstance(image_bytes, bytes))

    def test_validate_captcha(self):
        """测试验证验证码"""
        # 生成验证码
        captcha_text, _ = CaptchaUtils.generate_captcha()
        
        # 验证正确的验证码
        self.assertTrue(CaptchaUtils.validate_captcha(captcha_text, captcha_text))
        
        # 验证错误的验证码
        self.assertFalse(CaptchaUtils.validate_captcha('wrong', captcha_text))

    def test_validate_captcha_case_insensitive(self):
        """测试不区分大小写的验证码验证"""
        # 生成验证码
        captcha_text, _ = CaptchaUtils.generate_captcha(captcha_type=CaptchaUtils.TYPE_ALPHA)
        
        # 验证大小写不同但内容相同的验证码
        self.assertTrue(CaptchaUtils.validate_captcha(captcha_text.lower(), captcha_text, case_sensitive=False))
        self.assertTrue(CaptchaUtils.validate_captcha(captcha_text.upper(), captcha_text, case_sensitive=False))

    def test_validate_captcha_case_sensitive(self):
        """测试区分大小写的验证码验证"""
        # 生成验证码
        captcha_text, _ = CaptchaUtils.generate_captcha(captcha_type=CaptchaUtils.TYPE_ALPHA)
        
        # 验证大小写不同的验证码（区分大小写）
        if captcha_text.lower() != captcha_text:
            self.assertFalse(CaptchaUtils.validate_captcha(captcha_text.lower(), captcha_text, case_sensitive=True))
        if captcha_text.upper() != captcha_text:
            self.assertFalse(CaptchaUtils.validate_captcha(captcha_text.upper(), captcha_text, case_sensitive=True))

    def test_generate_simple_captcha(self):
        """测试生成简单验证码"""
        # 生成简单验证码
        captcha_text, image_bytes = CaptchaUtils.generate_simple_captcha()
        
        # 验证结果
        self.assertEqual(len(captcha_text), 4)
        self.assertTrue(isinstance(image_bytes, bytes))

    def test_generate_complex_captcha(self):
        """测试生成复杂验证码"""
        # 生成复杂验证码
        captcha_text, image_bytes = CaptchaUtils.generate_complex_captcha()
        
        # 验证结果
        self.assertEqual(len(captcha_text), 6)
        self.assertTrue(isinstance(image_bytes, bytes))


if __name__ == "__main__":
    unittest.main()