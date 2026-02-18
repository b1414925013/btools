import platform
from typing import Optional, Union, Any


class ClipboardUtils:
    """
    剪贴板工具类，提供剪贴板操作功能
    """

    @staticmethod
    def copy_text(text: str) -> bool:
        """
        复制文本到剪贴板
        
        Args:
            text: 要复制的文本
            
        Returns:
            bool: 操作是否成功
        """
        try:
            system = platform.system()
            
            if system == 'Windows':
                return ClipboardUtils._copy_text_windows(text)
            elif system == 'Darwin':
                return ClipboardUtils._copy_text_macos(text)
            elif system == 'Linux':
                return ClipboardUtils._copy_text_linux(text)
            else:
                return False
        except Exception:
            return False

    @staticmethod
    def get_text() -> Optional[str]:
        """
        从剪贴板获取文本
        
        Returns:
            Optional[str]: 剪贴板中的文本，如果获取失败则返回None
        """
        try:
            system = platform.system()
            
            if system == 'Windows':
                return ClipboardUtils._get_text_windows()
            elif system == 'Darwin':
                return ClipboardUtils._get_text_macos()
            elif system == 'Linux':
                return ClipboardUtils._get_text_linux()
            else:
                return None
        except Exception:
            return None

    @staticmethod
    def copy_image(image: Any) -> bool:
        """
        复制图片到剪贴板
        
        Args:
            image: 要复制的图片对象
            
        Returns:
            bool: 操作是否成功
        """
        try:
            system = platform.system()
            
            if system == 'Windows':
                return ClipboardUtils._copy_image_windows(image)
            elif system == 'Darwin':
                return ClipboardUtils._copy_image_macos(image)
            elif system == 'Linux':
                return ClipboardUtils._copy_image_linux(image)
            else:
                return False
        except Exception:
            return False

    @staticmethod
    def get_image() -> Optional[Any]:
        """
        从剪贴板获取图片
        
        Returns:
            Optional[Any]: 剪贴板中的图片对象，如果获取失败则返回None
        """
        try:
            system = platform.system()
            
            if system == 'Windows':
                return ClipboardUtils._get_image_windows()
            elif system == 'Darwin':
                return ClipboardUtils._get_image_macos()
            elif system == 'Linux':
                return ClipboardUtils._get_image_linux()
            else:
                return None
        except Exception:
            return None

    @staticmethod
    def clear() -> bool:
        """
        清空剪贴板
        
        Returns:
            bool: 操作是否成功
        """
        try:
            system = platform.system()
            
            if system == 'Windows':
                return ClipboardUtils._clear_windows()
            elif system == 'Darwin':
                return ClipboardUtils._clear_macos()
            elif system == 'Linux':
                return ClipboardUtils._clear_linux()
            else:
                return False
        except Exception:
            return False

    # Windows 实现
    @staticmethod
    def _copy_text_windows(text: str) -> bool:
        """
        Windows平台复制文本到剪贴板
        """
        try:
            import win32clipboard
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
            win32clipboard.CloseClipboard()
            return True
        except ImportError:
            # 如果没有安装pywin32，尝试使用ctypes
            try:
                import ctypes
                user32 = ctypes.windll.user32
                kernel32 = ctypes.windll.kernel32
                
                # 打开剪贴板
                if not user32.OpenClipboard(None):
                    return False
                
                # 清空剪贴板
                user32.EmptyClipboard()
                
                # 分配内存并复制文本
                text_bytes = text.encode('utf-16-le') + b'\x00\x00'
                hglobal = kernel32.GlobalAlloc(0x42, len(text_bytes))
                if hglobal == 0:
                    user32.CloseClipboard()
                    return False
                
                locked_memory = kernel32.GlobalLock(hglobal)
                if locked_memory is None:
                    kernel32.GlobalFree(hglobal)
                    user32.CloseClipboard()
                    return False
                
                ctypes.memmove(locked_memory, text_bytes, len(text_bytes))
                kernel32.GlobalUnlock(hglobal)
                
                # 设置剪贴板数据
                user32.SetClipboardData(13, hglobal)  # CF_UNICODETEXT
                user32.CloseClipboard()
                return True
            except Exception:
                return False

    @staticmethod
    def _get_text_windows() -> Optional[str]:
        """
        Windows平台从剪贴板获取文本
        """
        try:
            import win32clipboard
            win32clipboard.OpenClipboard()
            text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
            win32clipboard.CloseClipboard()
            return text
        except ImportError:
            # 如果没有安装pywin32，尝试使用ctypes
            try:
                import ctypes
                user32 = ctypes.windll.user32
                kernel32 = ctypes.windll.kernel32
                
                # 打开剪贴板
                if not user32.OpenClipboard(None):
                    return None
                
                # 获取剪贴板数据
                hglobal = user32.GetClipboardData(13)  # CF_UNICODETEXT
                if hglobal == 0:
                    user32.CloseClipboard()
                    return None
                
                # 锁定内存并读取文本
                locked_memory = kernel32.GlobalLock(hglobal)
                if locked_memory is None:
                    user32.CloseClipboard()
                    return None
                
                # 计算文本长度
                text_length = 0
                while ctypes.c_wchar_p(locked_memory)[text_length] != '\x00':
                    text_length += 1
                
                # 复制文本
                text = ctypes.wstring_at(locked_memory, text_length)
                kernel32.GlobalUnlock(hglobal)
                user32.CloseClipboard()
                return text
            except Exception:
                return None

    @staticmethod
    def _copy_image_windows(image: Any) -> bool:
        """
        Windows平台复制图片到剪贴板
        """
        try:
            import win32clipboard
            from PIL import Image
            import io
            
            # 确保图片是PIL Image对象
            if not isinstance(image, Image.Image):
                return False
            
            # 转换为BMP格式
            output = io.BytesIO()
            image.save(output, format='BMP')
            data = output.getvalue()[14:]  # 跳过BMP文件头
            output.close()
            
            # 复制到剪贴板
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
            win32clipboard.CloseClipboard()
            return True
        except Exception:
            return False

    @staticmethod
    def _get_image_windows() -> Optional[Any]:
        """
        Windows平台从剪贴板获取图片
        """
        try:
            import win32clipboard
            from PIL import Image
            import io
            
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
            win32clipboard.CloseClipboard()
            
            # 重建BMP文件
            bmp_header = b'BM' + (len(data) + 14).to_bytes(4, byteorder='little') + b'\x00\x00\x00\x00\x14\x00\x00\x00'
            bmp_data = bmp_header + data
            
            # 转换为PIL Image
            image = Image.open(io.BytesIO(bmp_data))
            return image
        except Exception:
            return None

    @staticmethod
    def _clear_windows() -> bool:
        """
        Windows平台清空剪贴板
        """
        try:
            import win32clipboard
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.CloseClipboard()
            return True
        except ImportError:
            # 如果没有安装pywin32，尝试使用ctypes
            try:
                import ctypes
                user32 = ctypes.windll.user32
                if not user32.OpenClipboard(None):
                    return False
                user32.EmptyClipboard()
                user32.CloseClipboard()
                return True
            except Exception:
                return False

    # macOS 实现
    @staticmethod
    def _copy_text_macos(text: str) -> bool:
        """
        macOS平台复制文本到剪贴板
        """
        try:
            import subprocess
            subprocess.run(['pbcopy'], input=text.encode('utf-8'), check=True)
            return True
        except Exception:
            return False

    @staticmethod
    def _get_text_macos() -> Optional[str]:
        """
        macOS平台从剪贴板获取文本
        """
        try:
            import subprocess
            result = subprocess.run(['pbpaste'], capture_output=True, text=True, check=True)
            return result.stdout
        except Exception:
            return None

    @staticmethod
    def _copy_image_macos(image: Any) -> bool:
        """
        macOS平台复制图片到剪贴板
        """
        try:
            from PIL import Image
            import io
            import subprocess
            
            # 确保图片是PIL Image对象
            if not isinstance(image, Image.Image):
                return False
            
            # 转换为PNG格式
            output = io.BytesIO()
            image.save(output, format='PNG')
            data = output.getvalue()
            output.close()
            
            # 复制到剪贴板
            process = subprocess.Popen(['pbcopy', '-Prefer', 'png'], stdin=subprocess.PIPE)
            process.communicate(input=data)
            return process.returncode == 0
        except Exception:
            return False

    @staticmethod
    def _get_image_macos() -> Optional[Any]:
        """
        macOS平台从剪贴板获取图片
        """
        try:
            from PIL import Image
            import io
            import subprocess
            
            # 从剪贴板获取图片
            result = subprocess.run(['pbpaste', '-Prefer', 'png'], capture_output=True, check=True)
            image = Image.open(io.BytesIO(result.stdout))
            return image
        except Exception:
            return None

    @staticmethod
    def _clear_macos() -> bool:
        """
        macOS平台清空剪贴板
        """
        try:
            import subprocess
            subprocess.run(['pbcopy'], input=b'', check=True)
            return True
        except Exception:
            return False

    # Linux 实现
    @staticmethod
    def _copy_text_linux(text: str) -> bool:
        """
        Linux平台复制文本到剪贴板
        """
        try:
            import subprocess
            # 尝试使用xclip
            try:
                process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
                process.communicate(input=text.encode('utf-8'))
                if process.returncode == 0:
                    return True
            except FileNotFoundError:
                pass
            
            # 尝试使用xsel
            try:
                process = subprocess.Popen(['xsel', '--input', '--clipboard'], stdin=subprocess.PIPE)
                process.communicate(input=text.encode('utf-8'))
                if process.returncode == 0:
                    return True
            except FileNotFoundError:
                pass
            
            return False
        except Exception:
            return False

    @staticmethod
    def _get_text_linux() -> Optional[str]:
        """
        Linux平台从剪贴板获取文本
        """
        try:
            import subprocess
            # 尝试使用xclip
            try:
                result = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True)
                if result.returncode == 0:
                    return result.stdout
            except FileNotFoundError:
                pass
            
            # 尝试使用xsel
            try:
                result = subprocess.run(['xsel', '--output', '--clipboard'], capture_output=True, text=True)
                if result.returncode == 0:
                    return result.stdout
            except FileNotFoundError:
                pass
            
            return None
        except Exception:
            return None

    @staticmethod
    def _copy_image_linux(image: Any) -> bool:
        """
        Linux平台复制图片到剪贴板
        """
        try:
            from PIL import Image
            import io
            import subprocess
            
            # 确保图片是PIL Image对象
            if not isinstance(image, Image.Image):
                return False
            
            # 转换为PNG格式
            output = io.BytesIO()
            image.save(output, format='PNG')
            data = output.getvalue()
            output.close()
            
            # 尝试使用xclip
            try:
                process = subprocess.Popen(['xclip', '-selection', 'clipboard', '-t', 'image/png'], stdin=subprocess.PIPE)
                process.communicate(input=data)
                if process.returncode == 0:
                    return True
            except FileNotFoundError:
                pass
            
            return False
        except Exception:
            return False

    @staticmethod
    def _get_image_linux() -> Optional[Any]:
        """
        Linux平台从剪贴板获取图片
        """
        try:
            from PIL import Image
            import io
            import subprocess
            
            # 尝试使用xclip
            try:
                result = subprocess.run(['xclip', '-selection', 'clipboard', '-o', '-t', 'image/png'], capture_output=True)
                if result.returncode == 0 and result.stdout:
                    image = Image.open(io.BytesIO(result.stdout))
                    return image
            except FileNotFoundError:
                pass
            
            return None
        except Exception:
            return None

    @staticmethod
    def _clear_linux() -> bool:
        """
        Linux平台清空剪贴板
        """
        try:
            import subprocess
            # 尝试使用xclip
            try:
                process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
                process.communicate(input=b'')
                if process.returncode == 0:
                    return True
            except FileNotFoundError:
                pass
            
            # 尝试使用xsel
            try:
                process = subprocess.Popen(['xsel', '--input', '--clipboard'], stdin=subprocess.PIPE)
                process.communicate(input=b'')
                if process.returncode == 0:
                    return True
            except FileNotFoundError:
                pass
            
            return False
        except Exception:
            return False
