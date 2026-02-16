# ImageUtils 使用指南

`ImageUtils` 是一个图像处理工具类，提供了丰富的图像处理方法，包括图像读取、保存、调整大小、裁剪、旋转、滤镜等功能。

## 功能特性

- 图像读取和保存
- 图像调整大小
- 图像裁剪
- 图像旋转
- 图像滤镜（灰度、模糊、锐化等）
- 图像水印
- 图像格式转换

## 基本用法

### 导入

```python
from btools import ImageUtils
```

### 示例

#### 图像读取和保存

```python
# 读取图像
image = ImageUtils.read_image("input.jpg")
print("Image read successfully!")

# 保存图像
ImageUtils.save_image(image, "output.jpg")
print("Image saved successfully!")
```

#### 图像调整大小

```python
# 调整图像大小（指定宽度和高度）
resized = ImageUtils.resize_image(image, width=800, height=600)
ImageUtils.save_image(resized, "resized.jpg")
print("Image resized successfully!")

# 调整图像大小（指定宽度，保持比例）
resized_width = ImageUtils.resize_image(image, width=800)
ImageUtils.save_image(resized_width, "resized_width.jpg")
print("Image resized by width successfully!")

# 调整图像大小（指定高度，保持比例）
resized_height = ImageUtils.resize_image(image, height=600)
ImageUtils.save_image(resized_height, "resized_height.jpg")
print("Image resized by height successfully!")
```

#### 图像裁剪

```python
# 裁剪图像（指定左上角和右下角坐标）
cropped = ImageUtils.crop_image(image, x1=100, y1=100, x2=500, y2=400)
ImageUtils.save_image(cropped, "cropped.jpg")
print("Image cropped successfully!")

# 裁剪图像（指定中心和宽高）
cropped_center = ImageUtils.crop_image_center(image, width=400, height=300)
ImageUtils.save_image(cropped_center, "cropped_center.jpg")
print("Image cropped from center successfully!")
```

#### 图像旋转

```python
# 旋转图像（指定角度）
rotated = ImageUtils.rotate_image(image, angle=45)
ImageUtils.save_image(rotated, "rotated.jpg")
print("Image rotated successfully!")

# 旋转图像（指定角度和背景色）
rotated_bg = ImageUtils.rotate_image(image, angle=45, background_color=(255, 255, 255))
ImageUtils.save_image(rotated_bg, "rotated_bg.jpg")
print("Image rotated with background color successfully!")
```

#### 图像滤镜

```python
# 灰度滤镜
grayscale = ImageUtils.apply_grayscale(image)
ImageUtils.save_image(grayscale, "grayscale.jpg")
print("Grayscale filter applied successfully!")

# 模糊滤镜
blurred = ImageUtils.apply_blur(image, radius=5)
ImageUtils.save_image(blurred, "blurred.jpg")
print("Blur filter applied successfully!")

# 锐化滤镜
sharpened = ImageUtils.apply_sharpen(image)
ImageUtils.save_image(sharpened, "sharpened.jpg")
print("Sharpen filter applied successfully!")
```

## 高级用法

### 图像水印

```python
# 添加文本水印
watermarked_text = ImageUtils.add_text_watermark(image, text="Watermark", position=(10, 10))
ImageUtils.save_image(watermarked_text, "watermarked_text.jpg")
print("Text watermark added successfully!")

# 添加图像水印
watermark_image = ImageUtils.read_image("watermark.png")
watermarked_image = ImageUtils.add_image_watermark(image, watermark_image, position=(10, 10))
ImageUtils.save_image(watermarked_image, "watermarked_image.jpg")
print("Image watermark added successfully!")
```

### 图像格式转换

```python
# 转换图像格式（JPG to PNG）
ImageUtils.convert_image_format("input.jpg", "output.png")
print("Image format converted from JPG to PNG successfully!")

# 转换图像格式（PNG to JPG）
ImageUtils.convert_image_format("input.png", "output.jpg")
print("Image format converted from PNG to JPG successfully!")
```

### 批量处理

```python
# 批量调整图像大小
input_files = ["image1.jpg", "image2.jpg", "image3.jpg"]
output_files = ["resized1.jpg", "resized2.jpg", "resized3.jpg"]

for i, input_file in enumerate(input_files):
    image = ImageUtils.read_image(input_file)
    resized = ImageUtils.resize_image(image, width=800)
    ImageUtils.save_image(resized, output_files[i])

print("Batch resize completed successfully!")
```

## 注意事项

1. 图像处理可能会占用较多的系统资源，对于大型图像，可能需要较长时间。
2. 某些滤镜效果可能会降低图像质量，请根据实际需求选择合适的滤镜。
3. 保存图像时，文件格式会根据文件扩展名自动确定。

## 总结

`ImageUtils` 提供了全面的图像处理功能，简化了图像处理的复杂度，使代码更加简洁易读。无论是基本的图像操作还是高级的图像处理，`ImageUtils` 都能满足你的需求。