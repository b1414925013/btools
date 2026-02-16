"""图片工具类"""
from PIL import Image, ImageFilter, ImageOps
import io
import base64
from typing import Any, Optional, Union, Tuple, List


class ImageUtils:
    """图片工具类"""

    @staticmethod
    def open(image_path: str) -> Image.Image:
        """
        打开图片
        
        Args:
            image_path: 图片路径
            
        Returns:
            Image.Image: 图片对象
        """
        return Image.open(image_path)

    @staticmethod
    def save(image: Image.Image, save_path: str, format: Optional[str] = None) -> None:
        """
        保存图片
        
        Args:
            image: 图片对象
            save_path: 保存路径
            format: 图片格式
        """
        image.save(save_path, format=format)

    @staticmethod
    def resize(image: Image.Image, width: int, height: int, resample: int = Image.BICUBIC) -> Image.Image:
        """
        调整图片大小
        
        Args:
            image: 图片对象
            width: 新宽度
            height: 新高度
            resample: 重采样方法
            
        Returns:
            Image.Image: 调整大小后的图片
        """
        return image.resize((width, height), resample=resample)

    @staticmethod
    def resize_by_ratio(image: Image.Image, ratio: float, resample: int = Image.BICUBIC) -> Image.Image:
        """
        按比例调整图片大小
        
        Args:
            image: 图片对象
            ratio: 缩放比例
            resample: 重采样方法
            
        Returns:
            Image.Image: 调整大小后的图片
        """
        width, height = image.size
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        return image.resize((new_width, new_height), resample=resample)

    @staticmethod
    def crop(image: Image.Image, left: int, top: int, right: int, bottom: int) -> Image.Image:
        """
        裁剪图片
        
        Args:
            image: 图片对象
            left: 左边界
            top: 上边界
            right: 右边界
            bottom: 下边界
            
        Returns:
            Image.Image: 裁剪后的图片
        """
        return image.crop((left, top, right, bottom))

    @staticmethod
    def crop_center(image: Image.Image, width: int, height: int) -> Image.Image:
        """
        居中裁剪图片
        
        Args:
            image: 图片对象
            width: 裁剪宽度
            height: 裁剪高度
            
        Returns:
            Image.Image: 裁剪后的图片
        """
        img_width, img_height = image.size
        left = (img_width - width) // 2
        top = (img_height - height) // 2
        right = left + width
        bottom = top + height
        return image.crop((left, top, right, bottom))

    @staticmethod
    def rotate(image: Image.Image, angle: float, expand: bool = False, fillcolor: Optional[str] = None) -> Image.Image:
        """
        旋转图片
        
        Args:
            image: 图片对象
            angle: 旋转角度
            expand: 是否扩展画布
            fillcolor: 填充颜色
            
        Returns:
            Image.Image: 旋转后的图片
        """
        return image.rotate(angle, expand=expand, fillcolor=fillcolor)

    @staticmethod
    def flip_horizontal(image: Image.Image) -> Image.Image:
        """
        水平翻转图片
        
        Args:
            image: 图片对象
            
        Returns:
            Image.Image: 水平翻转后的图片
        """
        return image.transpose(Image.FLIP_LEFT_RIGHT)

    @staticmethod
    def flip_vertical(image: Image.Image) -> Image.Image:
        """
        垂直翻转图片
        
        Args:
            image: 图片对象
            
        Returns:
            Image.Image: 垂直翻转后的图片
        """
        return image.transpose(Image.FLIP_TOP_BOTTOM)

    @staticmethod
    def convert_to_grayscale(image: Image.Image) -> Image.Image:
        """
        转换为灰度图
        
        Args:
            image: 图片对象
            
        Returns:
            Image.Image: 灰度图
        """
        return image.convert('L')

    @staticmethod
    def convert_to_rgb(image: Image.Image) -> Image.Image:
        """
        转换为RGB图
        
        Args:
            image: 图片对象
            
        Returns:
            Image.Image: RGB图
        """
        return image.convert('RGB')

    @staticmethod
    def convert_to_rgba(image: Image.Image) -> Image.Image:
        """
        转换为RGBA图
        
        Args:
            image: 图片对象
            
        Returns:
            Image.Image: RGBA图
        """
        return image.convert('RGBA')

    @staticmethod
    def blur(image: Image.Image, radius: int = 2) -> Image.Image:
        """
        模糊图片
        
        Args:
            image: 图片对象
            radius: 模糊半径
            
        Returns:
            Image.Image: 模糊后的图片
        """
        return image.filter(ImageFilter.GaussianBlur(radius=radius))

    @staticmethod
    def sharpen(image: Image.Image) -> Image.Image:
        """
        锐化图片
        
        Args:
            image: 图片对象
            
        Returns:
            Image.Image: 锐化后的图片
        """
        return image.filter(ImageFilter.SHARPEN)

    @staticmethod
    def edge_enhance(image: Image.Image) -> Image.Image:
        """
        边缘增强
        
        Args:
            image: 图片对象
            
        Returns:
            Image.Image: 边缘增强后的图片
        """
        return image.filter(ImageFilter.EDGE_ENHANCE)

    @staticmethod
    def emboss(image: Image.Image) -> Image.Image:
        """
        浮雕效果
        
        Args:
            image: 图片对象
            
        Returns:
            Image.Image: 浮雕效果后的图片
        """
        return image.filter(ImageFilter.EMBOSS)

    @staticmethod
    def contour(image: Image.Image) -> Image.Image:
        """
        轮廓效果
        
        Args:
            image: 图片对象
            
        Returns:
            Image.Image: 轮廓效果后的图片
        """
        return image.filter(ImageFilter.CONTOUR)

    @staticmethod
    def invert(image: Image.Image) -> Image.Image:
        """
        反转颜色
        
        Args:
            image: 图片对象
            
        Returns:
            Image.Image: 颜色反转后的图片
        """
        return ImageOps.invert(image)

    @staticmethod
    def adjust_brightness(image: Image.Image, factor: float) -> Image.Image:
        """
        调整亮度
        
        Args:
            image: 图片对象
            factor: 亮度因子 (0.0 到 1.0 变暗，>1.0 变亮)
            
        Returns:
            Image.Image: 调整亮度后的图片
        """
        return ImageOps.autocontrast(image)

    @staticmethod
    def adjust_contrast(image: Image.Image, factor: float) -> Image.Image:
        """
        调整对比度
        
        Args:
            image: 图片对象
            factor: 对比度因子 (0.0 到 1.0 降低对比度，>1.0 增加对比度)
            
        Returns:
            Image.Image: 调整对比度后的图片
        """
        return ImageOps.autocontrast(image, cutoff=factor)

    @staticmethod
    def get_image_size(image: Image.Image) -> Tuple[int, int]:
        """
        获取图片尺寸
        
        Args:
            image: 图片对象
            
        Returns:
            Tuple[int, int]: (宽度, 高度)
        """
        return image.size

    @staticmethod
    def get_image_format(image: Image.Image) -> str:
        """
        获取图片格式
        
        Args:
            image: 图片对象
            
        Returns:
            str: 图片格式
        """
        return image.format

    @staticmethod
    def get_image_mode(image: Image.Image) -> str:
        """
        获取图片模式
        
        Args:
            image: 图片对象
            
        Returns:
            str: 图片模式
        """
        return image.mode

    @staticmethod
    def image_to_bytes(image: Image.Image, format: str = 'PNG') -> bytes:
        """
        将图片转换为字节
        
        Args:
            image: 图片对象
            format: 图片格式
            
        Returns:
            bytes: 图片字节
        """
        buffer = io.BytesIO()
        image.save(buffer, format=format)
        return buffer.getvalue()

    @staticmethod
    def bytes_to_image(image_bytes: bytes) -> Image.Image:
        """
        将字节转换为图片
        
        Args:
            image_bytes: 图片字节
            
        Returns:
            Image.Image: 图片对象
        """
        buffer = io.BytesIO(image_bytes)
        return Image.open(buffer)

    @staticmethod
    def image_to_base64(image: Image.Image, format: str = 'PNG') -> str:
        """
        将图片转换为base64
        
        Args:
            image: 图片对象
            format: 图片格式
            
        Returns:
            str: base64字符串
        """
        image_bytes = ImageUtils.image_to_bytes(image, format=format)
        return base64.b64encode(image_bytes).decode('utf-8')

    @staticmethod
    def base64_to_image(base64_str: str) -> Image.Image:
        """
        将base64转换为图片
        
        Args:
            base64_str: base64字符串
            
        Returns:
            Image.Image: 图片对象
        """
        image_bytes = base64.b64decode(base64_str)
        return ImageUtils.bytes_to_image(image_bytes)

    @staticmethod
    def thumbnail(image: Image.Image, size: Tuple[int, int], resample: int = Image.LANCZOS) -> Image.Image:
        """
        创建缩略图
        
        Args:
            image: 图片对象
            size: 缩略图大小
            resample: 重采样方法
            
        Returns:
            Image.Image: 缩略图
        """
        thumb = image.copy()
        thumb.thumbnail(size, resample=resample)
        return thumb

    @staticmethod
    def paste(image: Image.Image, paste_image: Image.Image, box: Optional[Tuple[int, int]] = None) -> Image.Image:
        """
        粘贴图片
        
        Args:
            image: 目标图片
            paste_image: 要粘贴的图片
            box: 粘贴位置
            
        Returns:
            Image.Image: 粘贴后的图片
        """
        result = image.copy()
        result.paste(paste_image, box=box)
        return result

    @staticmethod
    def split_channels(image: Image.Image) -> List[Image.Image]:
        """
        分离通道
        
        Args:
            image: 图片对象
            
        Returns:
            List[Image.Image]: 通道列表
        """
        return list(image.split())

    @staticmethod
    def merge_channels(channels: List[Image.Image]) -> Image.Image:
        """
        合并通道
        
        Args:
            channels: 通道列表
            
        Returns:
            Image.Image: 合并后的图片
        """
        return Image.merge('RGB', channels)

    @staticmethod
    def equalize(image: Image.Image) -> Image.Image:
        """
        直方图均衡化
        
        Args:
            image: 图片对象
            
        Returns:
            Image.Image: 均衡化后的图片
        """
        return ImageOps.equalize(image)

    @staticmethod
    def posterize(image: Image.Image, bits: int) -> Image.Image:
        """
        色调分离
        
        Args:
            image: 图片对象
            bits: 位数
            
        Returns:
            Image.Image: 色调分离后的图片
        """
        return ImageOps.posterize(image, bits)

    @staticmethod
    def solarize(image: Image.Image, threshold: int = 128) -> Image.Image:
        """
        曝光效果
        
        Args:
            image: 图片对象
            threshold: 阈值
            
        Returns:
            Image.Image: 曝光效果后的图片
        """
        return ImageOps.solarize(image, threshold=threshold)