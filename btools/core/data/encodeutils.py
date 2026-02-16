"""编码工具类"""
import base64
import urllib.parse
import html
import json
import binascii
from typing import Any, Optional, Union


class EncodeUtils:
    """编码工具类"""

    @staticmethod
    def base64_encode(data: Union[str, bytes]) -> str:
        """
        Base64编码
        
        Args:
            data: 要编码的数据
            
        Returns:
            str: Base64编码后的字符串
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        return base64.b64encode(data).decode('utf-8')

    @staticmethod
    def base64_decode(encoded_str: str) -> str:
        """
        Base64解码
        
        Args:
            encoded_str: Base64编码的字符串
            
        Returns:
            str: 解码后的字符串
        """
        return base64.b64decode(encoded_str).decode('utf-8')

    @staticmethod
    def base64_url_encode(data: Union[str, bytes]) -> str:
        """
        URL安全的Base64编码
        
        Args:
            data: 要编码的数据
            
        Returns:
            str: URL安全的Base64编码后的字符串
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        return base64.urlsafe_b64encode(data).decode('utf-8').rstrip('=')

    @staticmethod
    def base64_url_decode(encoded_str: str) -> str:
        """
        URL安全的Base64解码
        
        Args:
            encoded_str: URL安全的Base64编码的字符串
            
        Returns:
            str: 解码后的字符串
        """
        # 补齐=号
        padding = '=' * ((4 - len(encoded_str) % 4) % 4)
        encoded_str += padding
        return base64.urlsafe_b64decode(encoded_str).decode('utf-8')

    @staticmethod
    def url_encode(data: Union[str, dict]) -> str:
        """
        URL编码
        
        Args:
            data: 要编码的数据，可以是字符串或字典
            
        Returns:
            str: URL编码后的字符串
        """
        if isinstance(data, dict):
            return urllib.parse.urlencode(data)
        return urllib.parse.quote(data)

    @staticmethod
    def url_decode(encoded_str: str) -> str:
        """
        URL解码
        
        Args:
            encoded_str: URL编码的字符串
            
        Returns:
            str: 解码后的字符串
        """
        return urllib.parse.unquote(encoded_str)

    @staticmethod
    def html_encode(text: str) -> str:
        """
        HTML编码
        
        Args:
            text: 要编码的文本
            
        Returns:
            str: HTML编码后的字符串
        """
        return html.escape(text)

    @staticmethod
    def html_decode(encoded_str: str) -> str:
        """
        HTML解码
        
        Args:
            encoded_str: HTML编码的字符串
            
        Returns:
            str: 解码后的字符串
        """
        return html.unescape(encoded_str)

    @staticmethod
    def json_encode(data: any, ensure_ascii: bool = False, indent: Optional[int] = None) -> str:
        """
        JSON编码
        
        Args:
            data: 要编码的数据
            ensure_ascii: 是否确保ASCII编码
            indent: 缩进空格数
            
        Returns:
            str: JSON编码后的字符串
        """
        return json.dumps(data, ensure_ascii=ensure_ascii, indent=indent)

    @staticmethod
    def json_decode(json_str: str) -> any:
        """
        JSON解码
        
        Args:
            json_str: JSON编码的字符串
            
        Returns:
            any: 解码后的数据
        """
        return json.loads(json_str)

    @staticmethod
    def hex_encode(data: Union[str, bytes]) -> str:
        """
        十六进制编码
        
        Args:
            data: 要编码的数据
            
        Returns:
            str: 十六进制编码后的字符串
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        return binascii.hexlify(data).decode('utf-8')

    @staticmethod
    def hex_decode(encoded_str: str) -> str:
        """
        十六进制解码
        
        Args:
            encoded_str: 十六进制编码的字符串
            
        Returns:
            str: 解码后的字符串
        """
        return binascii.unhexlify(encoded_str).decode('utf-8')

    @staticmethod
    def utf8_encode(text: str) -> bytes:
        """
        UTF-8编码
        
        Args:
            text: 要编码的文本
            
        Returns:
            bytes: UTF-8编码后的字节
        """
        return text.encode('utf-8')

    @staticmethod
    def utf8_decode(data: bytes) -> str:
        """
        UTF-8解码
        
        Args:
            data: UTF-8编码的字节
            
        Returns:
            str: 解码后的字符串
        """
        return data.decode('utf-8')

    @staticmethod
    def gbk_encode(text: str) -> bytes:
        """
        GBK编码
        
        Args:
            text: 要编码的文本
            
        Returns:
            bytes: GBK编码后的字节
        """
        return text.encode('gbk')

    @staticmethod
    def gbk_decode(data: bytes) -> str:
        """
        GBK解码
        
        Args:
            data: GBK编码的字节
            
        Returns:
            str: 解码后的字符串
        """
        return data.decode('gbk')

    @staticmethod
    def ascii_encode(text: str) -> bytes:
        """
        ASCII编码
        
        Args:
            text: 要编码的文本
            
        Returns:
            bytes: ASCII编码后的字节
        """
        return text.encode('ascii')

    @staticmethod
    def ascii_decode(data: bytes) -> str:
        """
        ASCII解码
        
        Args:
            data: ASCII编码的字节
            
        Returns:
            str: 解码后的字符串
        """
        return data.decode('ascii')

    @staticmethod
    def latin1_encode(text: str) -> bytes:
        """
        Latin-1编码
        
        Args:
            text: 要编码的文本
            
        Returns:
            bytes: Latin-1编码后的字节
        """
        return text.encode('latin-1')

    @staticmethod
    def latin1_decode(data: bytes) -> str:
        """
        Latin-1解码
        
        Args:
            data: Latin-1编码的字节
            
        Returns:
            str: 解码后的字符串
        """
        return data.decode('latin-1')

    @staticmethod
    def quoted_printable_encode(text: str, encoding: str = 'utf-8') -> str:
        """
        Quoted-Printable编码
        
        Args:
            text: 要编码的文本
            encoding: 编码格式
            
        Returns:
            str: Quoted-Printable编码后的字符串
        """
        import quopri
        return quopri.encodestring(text.encode(encoding)).decode('ascii')

    @staticmethod
    def quoted_printable_decode(encoded_str: str, encoding: str = 'utf-8') -> str:
        """
        Quoted-Printable解码
        
        Args:
            encoded_str: Quoted-Printable编码的字符串
            encoding: 编码格式
            
        Returns:
            str: 解码后的字符串
        """
        import quopri
        return quopri.decodestring(encoded_str).decode(encoding)

    @staticmethod
    def uu_encode(data: Union[str, bytes]) -> str:
        """
        UU编码
        
        Args:
            data: 要编码的数据
            
        Returns:
            str: UU编码后的字符串
        """
        import uu
        import io
        buffer = io.BytesIO()
        if isinstance(data, str):
            data = data.encode('utf-8')
        uu.encode(io.BytesIO(data), buffer)
        return buffer.getvalue().decode('ascii')

    @staticmethod
    def uu_decode(encoded_str: str) -> str:
        """
        UU解码
        
        Args:
            encoded_str: UU编码的字符串
            
        Returns:
            str: 解码后的字符串
        """
        import uu
        import io
        buffer = io.BytesIO(encoded_str.encode('ascii'))
        result = io.BytesIO()
        uu.decode(buffer, result)
        return result.getvalue().decode('utf-8')

    @staticmethod
    def rot13_encode(text: str) -> str:
        """
        ROT13编码
        
        Args:
            text: 要编码的文本
            
        Returns:
            str: ROT13编码后的字符串
        """
        import codecs
        return codecs.encode(text, 'rot_13')

    @staticmethod
    def rot13_decode(text: str) -> str:
        """
        ROT13解码
        
        Args:
            text: ROT13编码的文本
            
        Returns:
            str: ROT13解码后的字符串
        """
        import codecs
        return codecs.encode(text, 'rot_13')

    @staticmethod
    def morse_encode(text: str) -> str:
        """
        摩尔斯电码编码
        
        Args:
            text: 要编码的文本
            
        Returns:
            str: 摩尔斯电码编码后的字符串
        """
        morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
        }
        result = []
        for char in text.upper():
            if char in morse_code:
                result.append(morse_code[char])
        return ' '.join(result)

    @staticmethod
    def morse_decode(encoded_str: str) -> str:
        """
        摩尔斯电码解码
        
        Args:
            encoded_str: 摩尔斯电码编码的字符串
            
        Returns:
            str: 摩尔斯电码解码后的字符串
        """
        morse_code = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
            '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
            '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
            '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '/': ' '
        }
        result = []
        for code in encoded_str.split(' '):
            if code in morse_code:
                result.append(morse_code[code])
        return ''.join(result)