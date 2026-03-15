# ColorUtils 使用指南

`ColorUtils` 类提供了丰富的颜色转换和处理功能，支持多种颜色空间之间的转换，以及颜色的调整和处理。

## 基本使用

### 颜色空间转换

#### RGB 转 HEX

```python
from btools import ColorUtils

# RGB转HEX
hex_color = ColorUtils.rgb_to_hex(255, 0, 0)  # "#FF0000"
print(f"RGB(255, 0, 0) 转 HEX: {hex_color}")
```

#### HEX 转 RGB

```python
from btools import ColorUtils

# HEX转RGB
rgb = ColorUtils.hex_to_rgb("#FF0000")  # (255, 0, 0)
print(f"HEX #FF0000 转 RGB: {rgb}")

# 支持不带#前缀的HEX
rgb = ColorUtils.hex_to_rgb("00FF00")  # (0, 255, 0)
print(f"HEX 00FF00 转 RGB: {rgb}")

# 支持缩写形式 (#RGB)
rgb = ColorUtils.hex_to_rgb("#F00")  # (255, 0, 0)
print(f"HEX #F00 转 RGB: {rgb}")
```

#### RGB 转 HSL

```python
from btools import ColorUtils

# RGB转HSL
hsl = ColorUtils.rgb_to_hsl(255, 0, 0)  # (0.0, 100.0, 50.0)
print(f"RGB(255, 0, 0) 转 HSL: {hsl}")
```

#### HSL 转 RGB

```python
from btools import ColorUtils

# HSL转RGB
rgb = ColorUtils.hsl_to_rgb(0, 100, 50)  # (255, 0, 0)
print(f"HSL(0, 100, 50) 转 RGB: {rgb}")
```

#### RGB 转 HSV

```python
from btools import ColorUtils

# RGB转HSV
hsv = ColorUtils.rgb_to_hsv(255, 0, 0)  # (0.0, 100.0, 100.0)
print(f"RGB(255, 0, 0) 转 HSV: {hsv}")
```

#### HSV 转 RGB

```python
from btools import ColorUtils

# HSV转RGB
rgb = ColorUtils.hsv_to_rgb(0, 100, 100)  # (255, 0, 0)
print(f"HSV(0, 100, 100) 转 RGB: {rgb}")
```

### 颜色处理

#### 检查 HEX 颜色有效性

```python
from btools import ColorUtils

# 检查HEX颜色有效性
print(f"#FF0000 是有效的HEX颜色: {ColorUtils.is_hex_color('#FF0000')}")  # True
print(f"#GG0000 是有效的HEX颜色: {ColorUtils.is_hex_color('#GG0000')}")  # False
print(f"FFF 是有效的HEX颜色: {ColorUtils.is_hex_color('FFF')}")  # True
```

#### 提亮颜色

```python
from btools import ColorUtils

# 提亮颜色
light_red = ColorUtils.lighten_color("#FF0000", 0.5)  # "#FF8080"
print(f"提亮红色 50%: {light_red}")

# 完全提亮到白色
white = ColorUtils.lighten_color("#FF0000", 1.0)  # "#FFFFFF"
print(f"完全提亮红色: {white}")
```

#### 变暗颜色

```python
from btools import ColorUtils

# 变暗颜色
dark_red = ColorUtils.darken_color("#FF0000", 0.5)  # "#800000"
print(f"变暗红色 50%: {dark_red}")

# 完全变暗到黑色
black = ColorUtils.darken_color("#FF0000", 1.0)  # "#000000"
print(f"完全变暗红色: {black}")
```

#### 获取互补色

```python
from btools import ColorUtils

# 获取互补色
complementary = ColorUtils.get_complementary_color("#FF0000")  # "#00FFFF"
print(f"红色的互补色: {complementary}")

complementary = ColorUtils.get_complementary_color("#00FF00")  # "#FF00FF"
print(f"绿色的互补色: {complementary}")

complementary = ColorUtils.get_complementary_color("#0000FF")  # "#FFFF00"
print(f"蓝色的互补色: {complementary}")
```

#### 获取颜色名称

```python
from btools import ColorUtils

# 获取颜色名称
print(f"#FF0000 的颜色名称: {ColorUtils.format_color_name('#FF0000')}")  # "红色"
print(f"#00FF00 的颜色名称: {ColorUtils.format_color_name('#00FF00')}")  # "绿色"
print(f"#0000FF 的颜色名称: {ColorUtils.format_color_name('#0000FF')}")  # "蓝色"
print(f"#123456 的颜色名称: {ColorUtils.format_color_name('#123456')}")  # "未知颜色"
```

## 便捷函数

除了使用类方法外，ColorUtils 还提供了便捷函数，可以直接使用：

```python
from btools.core.media.colorutils import (
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
    format_color_name
)

# 使用便捷函数
print(rgb_to_hex(255, 0, 0))  # "#FF0000"
print(hex_to_rgb("#FF0000"))  # (255, 0, 0)
print(rgb_to_hsl(255, 0, 0))  # (0.0, 100.0, 50.0)
print(hsl_to_rgb(0, 100, 50))  # (255, 0, 0)
print(rgb_to_hsv(255, 0, 0))  # (0.0, 100.0, 100.0)
print(hsv_to_rgb(0, 100, 100))  # (255, 0, 0)
print(is_hex_color("#FF0000"))  # True
print(lighten_color("#FF0000", 0.5))  # "#FF8080"
print(darken_color("#FF0000", 0.5))  # "#800000"
print(get_complementary_color("#FF0000"))  # "#00FFFF"
print(format_color_name("#FF0000"))  # "红色"
```

## 实际应用场景

### 1. 生成颜色主题

```python
from btools import ColorUtils

# 生成基于主色的颜色主题
def generate_color_theme(primary_color):
    """生成颜色主题"""
    theme = {
        "primary": primary_color,
        "primary_light": ColorUtils.lighten_color(primary_color, 0.2),
        "primary_dark": ColorUtils.darken_color(primary_color, 0.2),
        "complementary": ColorUtils.get_complementary_color(primary_color),
        "text": "#333333",
        "background": "#FFFFFF"
    }
    return theme

# 生成蓝色主题
theme = generate_color_theme("#1976D2")
print("蓝色主题:")
for key, value in theme.items():
    print(f"{key}: {value}")
```

### 2. 颜色验证

```python
from btools import ColorUtils

def validate_color_input(color_str):
    """验证颜色输入"""
    if ColorUtils.is_hex_color(color_str):
        print(f"{color_str} 是有效的颜色")
        rgb = ColorUtils.hex_to_rgb(color_str)
        print(f"对应的RGB值: {rgb}")
        return True
    else:
        print(f"{color_str} 不是有效的颜色")
        return False

# 测试颜色验证
validate_color_input("#FF0000")  # 有效
validate_color_input("#GG0000")  # 无效
validate_color_input("123456")  # 有效
```

### 3. 动态调整颜色

```python
from btools import ColorUtils

def generate_color_gradient(start_color, end_color, steps=10):
    """生成颜色渐变"""
    start_r, start_g, start_b = ColorUtils.hex_to_rgb(start_color)
    end_r, end_g, end_b = ColorUtils.hex_to_rgb(end_color)
    
    gradient = []
    for i in range(steps):
        # 计算当前步骤的RGB值
        r = int(start_r + (end_r - start_r) * i / (steps - 1))
        g = int(start_g + (end_g - start_g) * i / (steps - 1))
        b = int(start_b + (end_b - start_b) * i / (steps - 1))
        # 转换为HEX
        hex_color = ColorUtils.rgb_to_hex(r, g, b)
        gradient.append(hex_color)
    
    return gradient

# 生成从红色到蓝色的渐变
gradient = generate_color_gradient("#FF0000", "#0000FF", 5)
print("红色到蓝色的渐变:")
for color in gradient:
    print(color)
```

## 注意事项

1. **颜色值范围**：
   - RGB值范围为0-255
   - HSL和HSV中的色相范围为0-360
   - HSL和HSV中的饱和度和亮度/明度范围为0-100

2. **HEX颜色格式**：
   - 支持带#前缀的格式："#RRGGBB"
   - 支持不带#前缀的格式："RRGGBB"
   - 支持缩写格式："#RGB"（会自动扩展为"#RRGGBB"）

3. **边界值处理**：
   - 对于超出范围的RGB值，会自动限制在0-255范围内
   - 对于超出范围的HSL/HSV值，会自动处理

4. **颜色名称**：
   - 目前只支持常见的16种颜色名称
   - 对于未识别的颜色，会返回"未知颜色"

## 总结

`ColorUtils` 提供了全面的颜色处理功能，包括：

- 多种颜色空间之间的转换（RGB、HEX、HSL、HSV）
- 颜色有效性检查
- 颜色调整（提亮、变暗）
- 互补色计算
- 颜色名称识别

这些功能可以帮助开发者在各种场景中处理颜色，如UI设计、数据可视化、图像处理等。通过使用 `ColorUtils`，开发者可以更方便地进行颜色相关的操作，提高开发效率。