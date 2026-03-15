# -*- coding: utf-8 -*-
"""
颜色工具测试
"""

import unittest

from btools.core.media.colorutils import (
    ColorUtils,
    rgb_to_hex,
    hex_to_rgb,
    rgb_to_hsl,
    hsl_to_rgb,
    rgb_to_hsv,
    hsv_to_rgb,
    is_hex_color,
    lighten_color,
    darken_color,
    get_complementary_color,
    format_color_name,
)


class TestColorUtils(unittest.TestCase):
    """
    颜色工具测试类
    """

    def test_rgb_to_hex(self):
        """
        测试RGB转HEX
        """
        # 测试标准颜色
        self.assertEqual(ColorUtils.rgb_to_hex(255, 0, 0), "#FF0000")
        self.assertEqual(ColorUtils.rgb_to_hex(0, 255, 0), "#00FF00")
        self.assertEqual(ColorUtils.rgb_to_hex(0, 0, 255), "#0000FF")
        # 测试边界值
        self.assertEqual(ColorUtils.rgb_to_hex(0, 0, 0), "#000000")
        self.assertEqual(ColorUtils.rgb_to_hex(255, 255, 255), "#FFFFFF")
        # 测试超出范围的值（应该被限制在0-255）
        self.assertEqual(ColorUtils.rgb_to_hex(-10, 300, 128), "#00FF80")

    def test_hex_to_rgb(self):
        """
        测试HEX转RGB
        """
        # 测试标准颜色
        self.assertEqual(ColorUtils.hex_to_rgb("#FF0000"), (255, 0, 0))
        self.assertEqual(ColorUtils.hex_to_rgb("#00FF00"), (0, 255, 0))
        self.assertEqual(ColorUtils.hex_to_rgb("#0000FF"), (0, 0, 255))
        # 测试不带#前缀的情况
        self.assertEqual(ColorUtils.hex_to_rgb("FF0000"), (255, 0, 0))
        # 测试缩写形式
        self.assertEqual(ColorUtils.hex_to_rgb("#FFF"), (255, 255, 255))
        self.assertEqual(ColorUtils.hex_to_rgb("#123"), (17, 34, 51))

    def test_rgb_to_hsl(self):
        """
        测试RGB转HSL
        """
        # 测试标准颜色
        # 红色
        h, s, l = ColorUtils.rgb_to_hsl(255, 0, 0)
        self.assertAlmostEqual(h, 0, delta=0.1)
        self.assertAlmostEqual(s, 100, delta=0.1)
        self.assertAlmostEqual(l, 50, delta=0.1)
        # 绿色
        h, s, l = ColorUtils.rgb_to_hsl(0, 255, 0)
        self.assertAlmostEqual(h, 120, delta=0.1)
        self.assertAlmostEqual(s, 100, delta=0.1)
        self.assertAlmostEqual(l, 50, delta=0.1)
        # 蓝色
        h, s, l = ColorUtils.rgb_to_hsl(0, 0, 255)
        self.assertAlmostEqual(h, 240, delta=0.1)
        self.assertAlmostEqual(s, 100, delta=0.1)
        self.assertAlmostEqual(l, 50, delta=0.1)

    def test_hsl_to_rgb(self):
        """
        测试HSL转RGB
        """
        # 测试标准颜色
        # 红色
        r, g, b = ColorUtils.hsl_to_rgb(0, 100, 50)
        self.assertEqual(r, 255)
        self.assertEqual(g, 0)
        self.assertEqual(b, 0)
        # 绿色
        r, g, b = ColorUtils.hsl_to_rgb(120, 100, 50)
        self.assertEqual(r, 0)
        self.assertEqual(g, 255)
        self.assertEqual(b, 0)
        # 蓝色
        r, g, b = ColorUtils.hsl_to_rgb(240, 100, 50)
        self.assertEqual(r, 0)
        self.assertEqual(g, 0)
        self.assertEqual(b, 255)

    def test_rgb_to_hsv(self):
        """
        测试RGB转HSV
        """
        # 测试标准颜色
        # 红色
        h, s, v = ColorUtils.rgb_to_hsv(255, 0, 0)
        self.assertAlmostEqual(h, 0, delta=0.1)
        self.assertAlmostEqual(s, 100, delta=0.1)
        self.assertAlmostEqual(v, 100, delta=0.1)
        # 绿色
        h, s, v = ColorUtils.rgb_to_hsv(0, 255, 0)
        self.assertAlmostEqual(h, 120, delta=0.1)
        self.assertAlmostEqual(s, 100, delta=0.1)
        self.assertAlmostEqual(v, 100, delta=0.1)
        # 蓝色
        h, s, v = ColorUtils.rgb_to_hsv(0, 0, 255)
        self.assertAlmostEqual(h, 240, delta=0.1)
        self.assertAlmostEqual(s, 100, delta=0.1)
        self.assertAlmostEqual(v, 100, delta=0.1)

    def test_hsv_to_rgb(self):
        """
        测试HSV转RGB
        """
        # 测试标准颜色
        # 红色
        r, g, b = ColorUtils.hsv_to_rgb(0, 100, 100)
        self.assertEqual(r, 255)
        self.assertEqual(g, 0)
        self.assertEqual(b, 0)
        # 绿色
        r, g, b = ColorUtils.hsv_to_rgb(120, 100, 100)
        self.assertEqual(r, 0)
        self.assertEqual(g, 255)
        self.assertEqual(b, 0)
        # 蓝色
        r, g, b = ColorUtils.hsv_to_rgb(240, 100, 100)
        self.assertEqual(r, 0)
        self.assertEqual(g, 0)
        self.assertEqual(b, 255)

    def test_is_hex_color(self):
        """
        测试是否为有效的HEX颜色
        """
        # 测试有效颜色
        self.assertTrue(ColorUtils.is_hex_color("#FF0000"))
        self.assertTrue(ColorUtils.is_hex_color("FF0000"))
        self.assertTrue(ColorUtils.is_hex_color("#F00"))
        self.assertTrue(ColorUtils.is_hex_color("F00"))
        # 测试无效颜色
        self.assertFalse(ColorUtils.is_hex_color("#FFFF"))
        self.assertFalse(ColorUtils.is_hex_color("FF00000"))
        self.assertFalse(ColorUtils.is_hex_color("GG0000"))
        self.assertFalse(ColorUtils.is_hex_color(""))

    def test_lighten_color(self):
        """
        测试提亮颜色
        """
        # 测试提亮红色
        light_red = ColorUtils.lighten_color("#FF0000", 0.5)
        self.assertEqual(light_red, "#FF8080")
        # 测试提亮到白色
        white = ColorUtils.lighten_color("#FF0000", 1.0)
        self.assertEqual(white, "#FFFFFF")
        # 测试不变
        same_color = ColorUtils.lighten_color("#FF0000", 0.0)
        self.assertEqual(same_color, "#FF0000")

    def test_darken_color(self):
        """
        测试变暗颜色
        """
        # 测试变暗红色
        dark_red = ColorUtils.darken_color("#FF0000", 0.5)
        self.assertEqual(dark_red, "#800000")
        # 测试变暗到黑色
        black = ColorUtils.darken_color("#FF0000", 1.0)
        self.assertEqual(black, "#000000")
        # 测试不变
        same_color = ColorUtils.darken_color("#FF0000", 0.0)
        self.assertEqual(same_color, "#FF0000")

    def test_get_complementary_color(self):
        """
        测试获取互补色
        """
        # 测试红色的互补色（青色）
        complementary = ColorUtils.get_complementary_color("#FF0000")
        self.assertEqual(complementary, "#00FFFF")
        # 测试绿色的互补色（洋红）
        complementary = ColorUtils.get_complementary_color("#00FF00")
        self.assertEqual(complementary, "#FF00FF")
        # 测试蓝色的互补色（黄色）
        complementary = ColorUtils.get_complementary_color("#0000FF")
        self.assertEqual(complementary, "#FFFF00")

    def test_format_color_name(self):
        """
        测试颜色名称
        """
        # 测试已知颜色
        self.assertEqual(ColorUtils.format_color_name("#FF0000"), "红色")
        self.assertEqual(ColorUtils.format_color_name("#00FF00"), "绿色")
        self.assertEqual(ColorUtils.format_color_name("#0000FF"), "蓝色")
        # 测试未知颜色
        self.assertEqual(ColorUtils.format_color_name("#123456"), "未知颜色")

    def test_convenience_functions(self):
        """
        测试便捷函数
        """
        # 测试rgb_to_hex
        self.assertEqual(rgb_to_hex(255, 0, 0), "#FF0000")
        # 测试hex_to_rgb
        self.assertEqual(hex_to_rgb("#FF0000"), (255, 0, 0))
        # 测试rgb_to_hsl
        h, s, l = rgb_to_hsl(255, 0, 0)
        self.assertAlmostEqual(h, 0, delta=0.1)
        # 测试hsl_to_rgb
        r, g, b = hsl_to_rgb(0, 100, 50)
        self.assertEqual(r, 255)
        # 测试rgb_to_hsv
        h, s, v = rgb_to_hsv(255, 0, 0)
        self.assertAlmostEqual(h, 0, delta=0.1)
        # 测试hsv_to_rgb
        r, g, b = hsv_to_rgb(0, 100, 100)
        self.assertEqual(r, 255)
        # 测试is_hex_color
        self.assertTrue(is_hex_color("#FF0000"))
        # 测试lighten_color
        self.assertEqual(lighten_color("#FF0000", 0.5), "#FF8080")
        # 测试darken_color
        self.assertEqual(darken_color("#FF0000", 0.5), "#800000")
        # 测试get_complementary_color
        self.assertEqual(get_complementary_color("#FF0000"), "#00FFFF")
        # 测试format_color_name
        self.assertEqual(format_color_name("#FF0000"), "红色")


if __name__ == "__main__":
    unittest.main()