# -*- coding: utf-8 -*-
"""
颜色工具模块
提供颜色转换和处理功能
"""

from typing import Dict, List, Tuple, Union


class ColorUtils:
    """
    颜色工具类
    提供颜色转换和处理功能
    """

    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int) -> str:
        """
        RGB颜色转HEX颜色

        Args:
            r: 红色通道值 (0-255)
            g: 绿色通道值 (0-255)
            b: 蓝色通道值 (0-255)

        Returns:
            HEX颜色字符串，格式为"#RRGGBB"
        """
        # 确保值在0-255范围内
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        return f"#{r:02x}{g:02x}{b:02x}".upper()

    @staticmethod
    def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
        """
        HEX颜色转RGB颜色

        Args:
            hex_color: HEX颜色字符串，格式为"#RRGGBB"或"RRGGBB"

        Returns:
            RGB颜色元组 (r, g, b)，每个值范围为0-255
        """
        # 移除#前缀
        hex_color = hex_color.lstrip('#')
        # 处理缩写形式 (#RGB -> #RRGGBB)
        if len(hex_color) == 3:
            hex_color = ''.join([c * 2 for c in hex_color])
        # 转换为RGB
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return (r, g, b)

    @staticmethod
    def rgb_to_hsl(r: int, g: int, b: int) -> Tuple[float, float, float]:
        """
        RGB颜色转HSL颜色

        Args:
            r: 红色通道值 (0-255)
            g: 绿色通道值 (0-255)
            b: 蓝色通道值 (0-255)

        Returns:
            HSL颜色元组 (h, s, l)，其中：
            h: 色相 (0-360)
            s: 饱和度 (0-100)
            l: 亮度 (0-100)
        """
        # 转换为0-1范围
        r_norm = r / 255.0
        g_norm = g / 255.0
        b_norm = b / 255.0

        max_val = max(r_norm, g_norm, b_norm)
        min_val = min(r_norm, g_norm, b_norm)
        h, s, l = 0, 0, (max_val + min_val) / 2

        if max_val != min_val:
            delta = max_val - min_val
            # 计算饱和度
            s = delta / (1 - abs(2 * l - 1))
            # 计算色相
            if max_val == r_norm:
                h = ((g_norm - b_norm) / delta) % 6
            elif max_val == g_norm:
                h = (b_norm - r_norm) / delta + 2
            else:  # max_val == b_norm
                h = (r_norm - g_norm) / delta + 4
            h *= 60
            if h < 0:
                h += 360

        return (round(h, 2), round(s * 100, 2), round(l * 100, 2))

    @staticmethod
    def hsl_to_rgb(h: float, s: float, l: float) -> Tuple[int, int, int]:
        """
        HSL颜色转RGB颜色

        Args:
            h: 色相 (0-360)
            s: 饱和度 (0-100)
            l: 亮度 (0-100)

        Returns:
            RGB颜色元组 (r, g, b)，每个值范围为0-255
        """
        # 转换为标准范围
        h = h % 360
        s = max(0, min(100, s)) / 100.0
        l = max(0, min(100, l)) / 100.0

        def hue_to_rgb(p, q, t):
            if t < 0:
                t += 1
            if t > 1:
                t -= 1
            if t < 1/6:
                return p + (q - p) * 6 * t
            if t < 1/2:
                return q
            if t < 2/3:
                return p + (q - p) * (2/3 - t) * 6
            return p

        if s == 0:
            # 灰色
            r = g = b = l
        else:
            if l < 0.5:
                q = l * (1 + s)
            else:
                q = l + s - l * s
            p = 2 * l - q
            r = hue_to_rgb(p, q, h/360 + 1/3)
            g = hue_to_rgb(p, q, h/360)
            b = hue_to_rgb(p, q, h/360 - 1/3)

        return (
            round(r * 255),
            round(g * 255),
            round(b * 255)
        )

    @staticmethod
    def rgb_to_hsv(r: int, g: int, b: int) -> Tuple[float, float, float]:
        """
        RGB颜色转HSV颜色

        Args:
            r: 红色通道值 (0-255)
            g: 绿色通道值 (0-255)
            b: 蓝色通道值 (0-255)

        Returns:
            HSV颜色元组 (h, s, v)，其中：
            h: 色相 (0-360)
            s: 饱和度 (0-100)
            v: 明度 (0-100)
        """
        # 转换为0-1范围
        r_norm = r / 255.0
        g_norm = g / 255.0
        b_norm = b / 255.0

        max_val = max(r_norm, g_norm, b_norm)
        min_val = min(r_norm, g_norm, b_norm)
        h, s, v = 0, 0, max_val

        delta = max_val - min_val
        if delta > 0:
            # 计算饱和度
            s = delta / max_val
            # 计算色相
            if max_val == r_norm:
                h = ((g_norm - b_norm) / delta) % 6
            elif max_val == g_norm:
                h = (b_norm - r_norm) / delta + 2
            else:  # max_val == b_norm
                h = (r_norm - g_norm) / delta + 4
            h *= 60
            if h < 0:
                h += 360

        return (round(h, 2), round(s * 100, 2), round(v * 100, 2))

    @staticmethod
    def hsv_to_rgb(h: float, s: float, v: float) -> Tuple[int, int, int]:
        """
        HSV颜色转RGB颜色

        Args:
            h: 色相 (0-360)
            s: 饱和度 (0-100)
            v: 明度 (0-100)

        Returns:
            RGB颜色元组 (r, g, b)，每个值范围为0-255
        """
        # 转换为标准范围
        h = h % 360
        s = max(0, min(100, s)) / 100.0
        v = max(0, min(100, v)) / 100.0

        c = v * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = v - c

        if 0 <= h < 60:
            r, g, b = c, x, 0
        elif 60 <= h < 120:
            r, g, b = x, c, 0
        elif 120 <= h < 180:
            r, g, b = 0, c, x
        elif 180 <= h < 240:
            r, g, b = 0, x, c
        elif 240 <= h < 300:
            r, g, b = x, 0, c
        else:  # 300 <= h < 360
            r, g, b = c, 0, x

        return (
            round((r + m) * 255),
            round((g + m) * 255),
            round((b + m) * 255)
        )

    @staticmethod
    def is_hex_color(hex_color: str) -> bool:
        """
        检查是否为有效的HEX颜色字符串

        Args:
            hex_color: 待检查的字符串

        Returns:
            是否为有效的HEX颜色字符串
        """
        hex_color = hex_color.lstrip('#')
        if len(hex_color) not in (3, 6):
            return False
        try:
            int(hex_color, 16)
            return True
        except ValueError:
            return False

    @staticmethod
    def lighten_color(hex_color: str, amount: float) -> str:
        """
        提亮颜色

        Args:
            hex_color: HEX颜色字符串
            amount: 提亮程度 (0-1)，0表示不变，1表示最亮（白色）

        Returns:
            提亮后的HEX颜色字符串
        """
        r, g, b = ColorUtils.hex_to_rgb(hex_color)
        # 计算提亮后的RGB值
        r = min(255, round(r + (255 - r) * amount))
        g = min(255, round(g + (255 - g) * amount))
        b = min(255, round(b + (255 - b) * amount))
        return ColorUtils.rgb_to_hex(r, g, b)

    @staticmethod
    def darken_color(hex_color: str, amount: float) -> str:
        """
        变暗颜色

        Args:
            hex_color: HEX颜色字符串
            amount: 变暗程度 (0-1)，0表示不变，1表示最暗（黑色）

        Returns:
            变暗后的HEX颜色字符串
        """
        r, g, b = ColorUtils.hex_to_rgb(hex_color)
        # 计算变暗后的RGB值
        r = max(0, round(r * (1 - amount)))
        g = max(0, round(g * (1 - amount)))
        b = max(0, round(b * (1 - amount)))
        return ColorUtils.rgb_to_hex(r, g, b)

    @staticmethod
    def get_complementary_color(hex_color: str) -> str:
        """
        获取互补色

        Args:
            hex_color: HEX颜色字符串

        Returns:
            互补色的HEX颜色字符串
        """
        r, g, b = ColorUtils.hex_to_rgb(hex_color)
        # 计算互补色（反转RGB值）
        r_comp = 255 - r
        g_comp = 255 - g
        b_comp = 255 - b
        return ColorUtils.rgb_to_hex(r_comp, g_comp, b_comp)

    @staticmethod
    def format_color_name(hex_color: str) -> str:
        """
        根据颜色值返回近似的颜色名称

        Args:
            hex_color: HEX颜色字符串

        Returns:
            近似的颜色名称
        """
        color_names = {
            "#FF0000": "红色",
            "#00FF00": "绿色",
            "#0000FF": "蓝色",
            "#FFFF00": "黄色",
            "#FF00FF": "洋红",
            "#00FFFF": "青色",
            "#000000": "黑色",
            "#FFFFFF": "白色",
            "#808080": "灰色",
            "#FFA500": "橙色",
            "#800080": "紫色",
            "#008000": "深绿色",
            "#000080": "深蓝色",
            "#800000": "深红色",
            "#C0C0C0": "银色",
            "#FFC0CB": "粉色",
            "#A52A2A": "棕色",
            "#FF00FF": "洋红色",
            "#FFFF00": "黄色",
            "#00FFFF": "青色"
        }
        return color_names.get(hex_color.upper(), "未知颜色")


# 便捷函数

def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    RGB颜色转HEX颜色

    Args:
        r: 红色通道值 (0-255)
        g: 绿色通道值 (0-255)
        b: 蓝色通道值 (0-255)

    Returns:
        HEX颜色字符串，格式为"#RRGGBB"
    """
    return ColorUtils.rgb_to_hex(r, g, b)


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """
    HEX颜色转RGB颜色

    Args:
        hex_color: HEX颜色字符串，格式为"#RRGGBB"或"RRGGBB"

    Returns:
        RGB颜色元组 (r, g, b)，每个值范围为0-255
    """
    return ColorUtils.hex_to_rgb(hex_color)


def rgb_to_hsl(r: int, g: int, b: int) -> Tuple[float, float, float]:
    """
    RGB颜色转HSL颜色

    Args:
        r: 红色通道值 (0-255)
        g: 绿色通道值 (0-255)
        b: 蓝色通道值 (0-255)

    Returns:
        HSL颜色元组 (h, s, l)，其中：
        h: 色相 (0-360)
        s: 饱和度 (0-100)
        l: 亮度 (0-100)
    """
    return ColorUtils.rgb_to_hsl(r, g, b)


def hsl_to_rgb(h: float, s: float, l: float) -> Tuple[int, int, int]:
    """
    HSL颜色转RGB颜色

    Args:
        h: 色相 (0-360)
        s: 饱和度 (0-100)
        l: 亮度 (0-100)

    Returns:
        RGB颜色元组 (r, g, b)，每个值范围为0-255
    """
    return ColorUtils.hsl_to_rgb(h, s, l)


def rgb_to_hsv(r: int, g: int, b: int) -> Tuple[float, float, float]:
    """
    RGB颜色转HSV颜色

    Args:
        r: 红色通道值 (0-255)
        g: 绿色通道值 (0-255)
        b: 蓝色通道值 (0-255)

    Returns:
        HSV颜色元组 (h, s, v)，其中：
        h: 色相 (0-360)
        s: 饱和度 (0-100)
        v: 明度 (0-100)
    """
    return ColorUtils.rgb_to_hsv(r, g, b)


def hsv_to_rgb(h: float, s: float, v: float) -> Tuple[int, int, int]:
    """
    HSV颜色转RGB颜色

    Args:
        h: 色相 (0-360)
        s: 饱和度 (0-100)
        v: 明度 (0-100)

    Returns:
        RGB颜色元组 (r, g, b)，每个值范围为0-255
    """
    return ColorUtils.hsv_to_rgb(h, s, v)


def is_hex_color(hex_color: str) -> bool:
    """
    检查是否为有效的HEX颜色字符串

    Args:
        hex_color: 待检查的字符串

    Returns:
        是否为有效的HEX颜色字符串
    """
    return ColorUtils.is_hex_color(hex_color)


def lighten_color(hex_color: str, amount: float) -> str:
    """
    提亮颜色

    Args:
        hex_color: HEX颜色字符串
        amount: 提亮程度 (0-1)，0表示不变，1表示最亮（白色）

    Returns:
        提亮后的HEX颜色字符串
    """
    return ColorUtils.lighten_color(hex_color, amount)


def darken_color(hex_color: str, amount: float) -> str:
    """
    变暗颜色

    Args:
        hex_color: HEX颜色字符串
        amount: 变暗程度 (0-1)，0表示不变，1表示最暗（黑色）

    Returns:
        变暗后的HEX颜色字符串
    """
    return ColorUtils.darken_color(hex_color, amount)


def get_complementary_color(hex_color: str) -> str:
    """
    获取互补色

    Args:
        hex_color: HEX颜色字符串

    Returns:
        互补色的HEX颜色字符串
    """
    return ColorUtils.get_complementary_color(hex_color)


def format_color_name(hex_color: str) -> str:
    """
    根据颜色值返回近似的颜色名称

    Args:
        hex_color: HEX颜色字符串

    Returns:
        近似的颜色名称
    """
    return ColorUtils.format_color_name(hex_color)