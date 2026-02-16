"""二维码工具类"""
import qrcode
from pyzbar import pyzbar
from PIL import Image
import io
import base64
from typing import Optional, Dict, Any


class QrCodeUtils:
    """二维码工具类"""

    @staticmethod
    def generate_qr_code(
        data: str,
        version: Optional[int] = None,
        error_correction: int = qrcode.constants.ERROR_CORRECT_M,
        box_size: int = 10,
        border: int = 4,
        fill_color: str = 'black',
        back_color: str = 'white'
    ) -> Image.Image:
        """
        生成二维码
        
        Args:
            data: 要编码的数据
            version: 二维码版本（1-40），None表示自动选择
            error_correction: 错误校正级别
            box_size: 每个方块的大小
            border: 边框大小
            fill_color: 填充颜色
            back_color: 背景颜色
            
        Returns:
            Image.Image: 二维码图片对象
        """
        qr = qrcode.QRCode(
            version=version,
            error_correction=error_correction,
            box_size=box_size,
            border=border
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        return img

    @staticmethod
    def save_qr_code(
        data: str,
        save_path: str,
        version: Optional[int] = None,
        error_correction: int = qrcode.constants.ERROR_CORRECT_M,
        box_size: int = 10,
        border: int = 4,
        fill_color: str = 'black',
        back_color: str = 'white',
        format: Optional[str] = None
    ) -> bool:
        """
        生成并保存二维码
        
        Args:
            data: 要编码的数据
            save_path: 保存路径
            version: 二维码版本（1-40），None表示自动选择
            error_correction: 错误校正级别
            box_size: 每个方块的大小
            border: 边框大小
            fill_color: 填充颜色
            back_color: 背景颜色
            format: 图片格式
            
        Returns:
            bool: 如果保存成功则返回True，否则返回False
        """
        try:
            img = QrCodeUtils.generate_qr_code(
                data=data,
                version=version,
                error_correction=error_correction,
                box_size=box_size,
                border=border,
                fill_color=fill_color,
                back_color=back_color
            )
            img.save(save_path, format=format)
            return True
        except Exception:
            return False

    @staticmethod
    def qr_code_to_bytes(
        data: str,
        version: Optional[int] = None,
        error_correction: int = qrcode.constants.ERROR_CORRECT_M,
        box_size: int = 10,
        border: int = 4,
        fill_color: str = 'black',
        back_color: str = 'white',
        format: str = 'PNG'
    ) -> bytes:
        """
        生成二维码并转换为字节
        
        Args:
            data: 要编码的数据
            version: 二维码版本（1-40），None表示自动选择
            error_correction: 错误校正级别
            box_size: 每个方块的大小
            border: 边框大小
            fill_color: 填充颜色
            back_color: 背景颜色
            format: 图片格式
            
        Returns:
            bytes: 二维码图片字节
        """
        img = QrCodeUtils.generate_qr_code(
            data=data,
            version=version,
            error_correction=error_correction,
            box_size=box_size,
            border=border,
            fill_color=fill_color,
            back_color=back_color
        )
        buffer = io.BytesIO()
        img.save(buffer, format=format)
        return buffer.getvalue()

    @staticmethod
    def qr_code_to_base64(
        data: str,
        version: Optional[int] = None,
        error_correction: int = qrcode.constants.ERROR_CORRECT_M,
        box_size: int = 10,
        border: int = 4,
        fill_color: str = 'black',
        back_color: str = 'white',
        format: str = 'PNG'
    ) -> str:
        """
        生成二维码并转换为base64
        
        Args:
            data: 要编码的数据
            version: 二维码版本（1-40），None表示自动选择
            error_correction: 错误校正级别
            box_size: 每个方块的大小
            border: 边框大小
            fill_color: 填充颜色
            back_color: 背景颜色
            format: 图片格式
            
        Returns:
            str: 二维码图片base64字符串
        """
        img_bytes = QrCodeUtils.qr_code_to_bytes(
            data=data,
            version=version,
            error_correction=error_correction,
            box_size=box_size,
            border=border,
            fill_color=fill_color,
            back_color=back_color,
            format=format
        )
        return base64.b64encode(img_bytes).decode('utf-8')

    @staticmethod
    def decode_qr_code(image: Image.Image) -> Optional[str]:
        """
        解析二维码
        
        Args:
            image: 二维码图片对象
            
        Returns:
            Optional[str]: 解析出的数据，如果解析失败则返回None
        """
        try:
            decoded_objects = pyzbar.decode(image)
            if decoded_objects:
                return decoded_objects[0].data.decode('utf-8')
            return None
        except Exception:
            return None

    @staticmethod
    def decode_qr_code_from_file(image_path: str) -> Optional[str]:
        """
        从文件解析二维码
        
        Args:
            image_path: 二维码图片路径
            
        Returns:
            Optional[str]: 解析出的数据，如果解析失败则返回None
        """
        try:
            image = Image.open(image_path)
            return QrCodeUtils.decode_qr_code(image)
        except Exception:
            return None

    @staticmethod
    def decode_qr_code_from_bytes(image_bytes: bytes) -> Optional[str]:
        """
        从字节解析二维码
        
        Args:
            image_bytes: 二维码图片字节
            
        Returns:
            Optional[str]: 解析出的数据，如果解析失败则返回None
        """
        try:
            image = Image.open(io.BytesIO(image_bytes))
            return QrCodeUtils.decode_qr_code(image)
        except Exception:
            return None

    @staticmethod
    def decode_qr_code_from_base64(base64_str: str) -> Optional[str]:
        """
        从base64解析二维码
        
        Args:
            base64_str: 二维码图片base64字符串
            
        Returns:
            Optional[str]: 解析出的数据，如果解析失败则返回None
        """
        try:
            image_bytes = base64.b64decode(base64_str)
            return QrCodeUtils.decode_qr_code_from_bytes(image_bytes)
        except Exception:
            return None

    @staticmethod
    def generate_qr_code_with_logo(
        data: str,
        logo_path: str,
        logo_size: float = 0.2,
        version: Optional[int] = None,
        error_correction: int = qrcode.constants.ERROR_CORRECT_H,
        box_size: int = 10,
        border: int = 4,
        fill_color: str = 'black',
        back_color: str = 'white'
    ) -> Image.Image:
        """
        生成带Logo的二维码
        
        Args:
            data: 要编码的数据
            logo_path: Logo图片路径
            logo_size: Logo大小占比（0-1）
            version: 二维码版本（1-40），None表示自动选择
            error_correction: 错误校正级别
            box_size: 每个方块的大小
            border: 边框大小
            fill_color: 填充颜色
            back_color: 背景颜色
            
        Returns:
            Image.Image: 带Logo的二维码图片对象
        """
        # 生成二维码
        qr_img = QrCodeUtils.generate_qr_code(
            data=data,
            version=version,
            error_correction=error_correction,
            box_size=box_size,
            border=border,
            fill_color=fill_color,
            back_color=back_color
        )
        
        # 打开Logo图片
        logo = Image.open(logo_path)
        
        # 计算Logo大小
        qr_width, qr_height = qr_img.size
        logo_width = int(qr_width * logo_size)
        logo_height = int(qr_height * logo_size)
        logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
        
        # 计算Logo位置
        logo_x = (qr_width - logo_width) // 2
        logo_y = (qr_height - logo_height) // 2
        
        # 添加Logo到二维码
        qr_img.paste(logo, (logo_x, logo_y))
        
        return qr_img

    @staticmethod
    def save_qr_code_with_logo(
        data: str,
        logo_path: str,
        save_path: str,
        logo_size: float = 0.2,
        version: Optional[int] = None,
        error_correction: int = qrcode.constants.ERROR_CORRECT_H,
        box_size: int = 10,
        border: int = 4,
        fill_color: str = 'black',
        back_color: str = 'white',
        format: Optional[str] = None
    ) -> bool:
        """
        生成并保存带Logo的二维码
        
        Args:
            data: 要编码的数据
            logo_path: Logo图片路径
            save_path: 保存路径
            logo_size: Logo大小占比（0-1）
            version: 二维码版本（1-40），None表示自动选择
            error_correction: 错误校正级别
            box_size: 每个方块的大小
            border: 边框大小
            fill_color: 填充颜色
            back_color: 背景颜色
            format: 图片格式
            
        Returns:
            bool: 如果保存成功则返回True，否则返回False
        """
        try:
            img = QrCodeUtils.generate_qr_code_with_logo(
                data=data,
                logo_path=logo_path,
                logo_size=logo_size,
                version=version,
                error_correction=error_correction,
                box_size=box_size,
                border=border,
                fill_color=fill_color,
                back_color=back_color
            )
            img.save(save_path, format=format)
            return True
        except Exception:
            return False

    @staticmethod
    def get_error_correction_level(level: str) -> int:
        """
        获取错误校正级别
        
        Args:
            level: 错误校正级别字符串（L, M, Q, H）
            
        Returns:
            int: 错误校正级别常量
        """
        levels = {
            'L': qrcode.constants.ERROR_CORRECT_L,
            'M': qrcode.constants.ERROR_CORRECT_M,
            'Q': qrcode.constants.ERROR_CORRECT_Q,
            'H': qrcode.constants.ERROR_CORRECT_H
        }
        return levels.get(level.upper(), qrcode.constants.ERROR_CORRECT_M)

    @staticmethod
    def validate_qr_code_data(data: str) -> bool:
        """
        验证二维码数据
        
        Args:
            data: 要编码的数据
            
        Returns:
            bool: 如果数据有效则返回True，否则返回False
        """
        return bool(data and len(data) > 0)

    @staticmethod
    def generate_vcard_qr_code(
        name: str,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        company: Optional[str] = None,
        title: Optional[str] = None,
        url: Optional[str] = None,
        address: Optional[str] = None
    ) -> Image.Image:
        """
        生成VCARD二维码
        
        Args:
            name: 姓名
            phone: 电话号码
            email: 邮箱地址
            company: 公司名称
            title: 职位
            url: 个人网站
            address: 地址
            
        Returns:
            Image.Image: VCARD二维码图片对象
        """
        vcard_data = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\n"
        if phone:
            vcard_data += f"TEL:{phone}\n"
        if email:
            vcard_data += f"EMAIL:{email}\n"
        if company:
            vcard_data += f"ORG:{company}\n"
        if title:
            vcard_data += f"TITLE:{title}\n"
        if url:
            vcard_data += f"URL:{url}\n"
        if address:
            vcard_data += f"ADR:{address}\n"
        vcard_data += "END:VCARD"
        
        return QrCodeUtils.generate_qr_code(vcard_data)

    @staticmethod
    def generate_url_qr_code(url: str) -> Image.Image:
        """
        生成URL二维码
        
        Args:
            url: URL地址
            
        Returns:
            Image.Image: URL二维码图片对象
        """
        return QrCodeUtils.generate_qr_code(url)

    @staticmethod
    def generate_text_qr_code(text: str) -> Image.Image:
        """
        生成文本二维码
        
        Args:
            text: 文本内容
            
        Returns:
            Image.Image: 文本二维码图片对象
        """
        return QrCodeUtils.generate_qr_code(text)