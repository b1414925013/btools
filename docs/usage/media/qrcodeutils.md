# QrCodeUtils 使用指南

`QrCodeUtils` 是一个二维码工具类，提供了丰富的二维码操作方法，包括二维码生成、解析等功能。

## 功能特性

- 二维码生成
- 二维码解析
- 自定义二维码样式
- 二维码添加Logo

## 基本用法

### 导入

```python
from btools import QrCodeUtils
```

### 示例

#### 二维码生成

```python
# 生成二维码（默认设置）
QrCodeUtils.generate_qr_code("https://www.example.com", "qrcode.png")
print("QR code generated successfully!")

# 生成二维码（自定义大小）
QrCodeUtils.generate_qr_code("https://www.example.com", "qrcode_large.png", size=500)
print("Large QR code generated successfully!")

# 生成二维码（自定义颜色）
QrCodeUtils.generate_qr_code(
    "https://www.example.com", 
    "qrcode_custom.png", 
    fill_color="#000000", 
    back_color="#ffffff"
)
print("Custom color QR code generated successfully!")
```

#### 二维码解析

```python
# 解析二维码
result = QrCodeUtils.parse_qr_code("qrcode.png")
print(f"QR code parsed successfully! Content: {result}")
```

## 高级用法

### 二维码添加Logo

```python
# 生成带Logo的二维码
QrCodeUtils.generate_qr_code_with_logo(
    "https://www.example.com", 
    "qrcode_with_logo.png", 
    logo_path="logo.png"
)
print("QR code with logo generated successfully!")

# 生成带Logo的二维码（自定义Logo大小）
QrCodeUtils.generate_qr_code_with_logo(
    "https://www.example.com", 
    "qrcode_with_logo_custom.png", 
    logo_path="logo.png", 
    logo_size=100
)
print("QR code with custom logo size generated successfully!")
```

### 自定义二维码样式

```python
# 生成圆形二维码
QrCodeUtils.generate_qr_code(
    "https://www.example.com", 
    "qrcode_circular.png", 
    box_size=10, 
    border=4
)
print("Circular QR code generated successfully!")

# 生成二维码（使用不同的纠错级别）
# 纠错级别：L (7%), M (15%), Q (25%), H (30%)
QrCodeUtils.generate_qr_code(
    "https://www.example.com", 
    "qrcode_high_error_correction.png", 
    error_correction="H"
)
print("QR code with high error correction generated successfully!")
```

### 批量生成二维码

```python
# 批量生成二维码
data_list = [
    "https://www.example.com/page1",
    "https://www.example.com/page2",
    "https://www.example.com/page3"
]

for i, data in enumerate(data_list):
    output_file = f"qrcode_{i+1}.png"
    QrCodeUtils.generate_qr_code(data, output_file)
    print(f"QR code {i+1} generated successfully!")

print("Batch QR code generation completed!")
```

## 注意事项

1. 生成二维码时，数据内容不宜过长，否则会导致二维码过于复杂，难以扫描。
2. 添加Logo时，Logo大小不宜过大，否则会影响二维码的扫描成功率。
3. 解析二维码时，需要确保图像清晰，否则可能会解析失败。

## 总结

`QrCodeUtils` 提供了全面的二维码操作功能，简化了二维码生成和解析的复杂度，使代码更加简洁易读。无论是基本的二维码生成还是高级的二维码定制，`QrCodeUtils` 都能满足你的需求。