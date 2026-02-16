"""验证码生成工具类"""
import random
import string
from PIL import Image, ImageDraw, ImageFont
import io
import base64
from typing import Optional, Tuple, Union


class CaptchaUtils:
    """
    验证码生成工具类，提供图片验证码的生成功能
    """

    # 验证码类型
    TYPE_NUMERIC = 1  # 纯数字
    TYPE_ALPHA = 2  # 纯字母
    TYPE_ALPHANUMERIC = 3  # 字母数字混合

    @staticmethod
    def generate_captcha(length: int = 4, captcha_type: int = TYPE_ALPHANUMERIC, 
                       width: int = 120, height: int = 40, font_size: int = 24, 
                       noise_level: int = 2) -> Tuple[str, bytes]:
        """
        生成验证码
        
        Args:
            length: 验证码长度
            captcha_type: 验证码类型，支持 TYPE_NUMERIC, TYPE_ALPHA, TYPE_ALPHANUMERIC
            width: 图片宽度
            height: 图片高度
            font_size: 字体大小
            noise_level: 噪点级别，1-5，值越大噪点越多
            
        Returns:
            验证码文本和图片字节
        """
        # 生成验证码文本
        captcha_text = CaptchaUtils._generate_text(length, captcha_type)
        
        # 创建图片
        image = Image.new('RGB', (width, height), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)
        
        # 尝试加载字体
        try:
            # 尝试使用系统字体
            font = ImageFont.truetype('arial.ttf', font_size)
        except:
            # 如果没有arial字体，使用默认字体
            font = ImageFont.load_default()
        
        # 绘制验证码文本
        text_width = draw.textlength(captcha_text, font=font)
        text_x = (width - text_width) // 2
        text_y = (height - font_size) // 2
        
        # 为每个字符使用不同的颜色
        for i, char in enumerate(captcha_text):
            char_color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
            char_x = text_x + i * (text_width // length)
            char_y = text_y + random.randint(-5, 5)
            draw.text((char_x, char_y), char, fill=char_color, font=font)
        
        # 添加噪点
        CaptchaUtils._add_noise(draw, width, height, noise_level)
        
        # 添加干扰线
        CaptchaUtils._add_interference_lines(draw, width, height, noise_level)
        
        # 转换为字节
        buffer = io.BytesIO()
        image.save(buffer, format='PNG')
        image_bytes = buffer.getvalue()
        
        return captcha_text, image_bytes

    @staticmethod
    def generate_captcha_base64(length: int = 4, captcha_type: int = TYPE_ALPHANUMERIC, 
                              width: int = 120, height: int = 40, font_size: int = 24, 
                              noise_level: int = 2) -> Tuple[str, str]:
        """
        生成Base64格式的验证码
        
        Args:
            length: 验证码长度
            captcha_type: 验证码类型
            width: 图片宽度
            height: 图片高度
            font_size: 字体大小
            noise_level: 噪点级别
            
        Returns:
            验证码文本和Base64编码的图片
        """
        captcha_text, image_bytes = CaptchaUtils.generate_captcha(
            length, captcha_type, width, height, font_size, noise_level
        )
        
        # 转换为Base64
        base64_str = base64.b64encode(image_bytes).decode('utf-8')
        return captcha_text, base64_str

    @staticmethod
    def generate_math_captcha(width: int = 120, height: int = 40, font_size: int = 24, 
                            noise_level: int = 2) -> Tuple[str, str, bytes]:
        """
        生成数学计算验证码
        
        Args:
            width: 图片宽度
            height: 图片高度
            font_size: 字体大小
            noise_level: 噪点级别
            
        Returns:
            验证码表达式、答案和图片字节
        """
        # 生成随机数学表达式
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        
        # 计算答案
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            # 确保结果为正数
            if num1 < num2:
                num1, num2 = num2, num1
            answer = num1 - num2
        else:  # *
            # 确保结果不太大
            num1 = random.randint(1, 5)
            num2 = random.randint(1, 5)
            answer = num1 * num2
        
        # 生成表达式字符串
        expression = f"{num1} {operator} {num2} = ?"
        captcha_text = str(answer)
        
        # 创建图片
        image = Image.new('RGB', (width, height), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)
        
        # 尝试加载字体
        try:
            font = ImageFont.truetype('arial.ttf', font_size)
        except:
            font = ImageFont.load_default()
        
        # 绘制表达式
        text_width = draw.textlength(expression, font=font)
        text_x = (width - text_width) // 2
        text_y = (height - font_size) // 2
        
        text_color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
        draw.text((text_x, text_y), expression, fill=text_color, font=font)
        
        # 添加噪点
        CaptchaUtils._add_noise(draw, width, height, noise_level)
        
        # 添加干扰线
        CaptchaUtils._add_interference_lines(draw, width, height, noise_level)
        
        # 转换为字节
        buffer = io.BytesIO()
        image.save(buffer, format='PNG')
        image_bytes = buffer.getvalue()
        
        return expression, captcha_text, image_bytes

    @staticmethod
    def _generate_text(length: int, captcha_type: int) -> str:
        """
        生成验证码文本
        
        Args:
            length: 验证码长度
            captcha_type: 验证码类型
            
        Returns:
            验证码文本
        """
        if captcha_type == CaptchaUtils.TYPE_NUMERIC:
            chars = string.digits
        elif captcha_type == CaptchaUtils.TYPE_ALPHA:
            chars = string.ascii_letters
        else:  # TYPE_ALPHANUMERIC
            chars = string.ascii_letters + string.digits
        
        return ''.join(random.choice(chars) for _ in range(length))

    @staticmethod
    def _add_noise(draw: ImageDraw.ImageDraw, width: int, height: int, noise_level: int):
        """
        添加噪点
        
        Args:
            draw: ImageDraw对象
            width: 图片宽度
            height: 图片高度
            noise_level: 噪点级别
        """
        # 根据噪点级别计算噪点数量
        noise_count = width * height // 50 * noise_level
        
        for _ in range(noise_count):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            color = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))
            draw.point((x, y), fill=color)

    @staticmethod
    def _add_interference_lines(draw: ImageDraw.ImageDraw, width: int, height: int, noise_level: int):
        """
        添加干扰线
        
        Args:
            draw: ImageDraw对象
            width: 图片宽度
            height: 图片高度
            noise_level: 噪点级别
        """
        # 根据噪点级别计算干扰线数量
        line_count = noise_level
        
        for _ in range(line_count):
            start_x = random.randint(0, width // 3)
            start_y = random.randint(0, height)
            end_x = random.randint(width * 2 // 3, width)
            end_y = random.randint(0, height)
            color = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))
            draw.line([(start_x, start_y), (end_x, end_y)], fill=color, width=1)

    @staticmethod
    def validate_captcha(user_input: str, correct_captcha: str, case_sensitive: bool = False) -> bool:
        """
        验证验证码
        
        Args:
            user_input: 用户输入的验证码
            correct_captcha: 正确的验证码
            case_sensitive: 是否区分大小写
            
        Returns:
            是否验证通过
        """
        if not case_sensitive:
            user_input = user_input.lower()
            correct_captcha = correct_captcha.lower()
        
        return user_input == correct_captcha

    @staticmethod
    def generate_simple_captcha() -> Tuple[str, bytes]:
        """
        生成简单验证码（默认参数）
        
        Returns:
            验证码文本和图片字节
        """
        return CaptchaUtils.generate_captcha()

    @staticmethod
    def generate_complex_captcha() -> Tuple[str, bytes]:
        """
        生成复杂验证码（更长、更多噪点）
        
        Returns:
            验证码文本和图片字节
        """
        return CaptchaUtils.generate_captcha(length=6, width=160, height=50, 
                                          noise_level=4)