# ClipboardUtils 使用指南

`ClipboardUtils` 是一个剪贴板工具类，提供了跨平台的剪贴板操作功能，包括复制和粘贴文本、图片等。

## 功能特性

- **跨平台支持**：支持 Windows、macOS 和 Linux 平台
- **文本操作**：支持复制文本到剪贴板和从剪贴板获取文本
- **图片操作**：支持复制图片到剪贴板和从剪贴板获取图片
- **剪贴板清空**：支持清空剪贴板内容
- **优雅降级**：在不同平台上使用不同的实现方式，确保功能可用
- **异常处理**：所有操作都会捕获异常，确保不会因为剪贴板操作失败而导致程序崩溃

## 基本用法

### 导入

```python
from btools import ClipboardUtils
# 或
from btools.core import ClipboardUtils
# 或
from btools.core.basic import ClipboardUtils
```

### 示例

#### 1. 复制文本到剪贴板

```python
# 复制文本到剪贴板
test_text = "Hello, ClipboardUtils!"
result = ClipboardUtils.copy_text(test_text)
print(f"复制文本到剪贴板: {'成功' if result else '失败'}")
```

#### 2. 从剪贴板获取文本

```python
# 从剪贴板获取文本
text = ClipboardUtils.get_text()
if text:
    print(f"从剪贴板获取的文本: {text}")
else:
    print("剪贴板为空或获取失败")
```

#### 3. 清空剪贴板

```python
# 清空剪贴板
result = ClipboardUtils.clear()
print(f"清空剪贴板: {'成功' if result else '失败'}")
```

#### 4. 复制图片到剪贴板

```python
from PIL import Image

# 创建一个测试图片
image = Image.new('RGB', (100, 100), color='blue')

# 复制图片到剪贴板
result = ClipboardUtils.copy_image(image)
print(f"复制图片到剪贴板: {'成功' if result else '失败'}")
```

#### 5. 从剪贴板获取图片

```python
from PIL import Image

# 从剪贴板获取图片
image = ClipboardUtils.get_image()
if image:
    print(f"从剪贴板获取的图片: {type(image)}")
    print(f"图片尺寸: {image.size}")
    # 可以保存图片或进行其他操作
    # image.save('clipboard_image.png')
else:
    print("剪贴板中没有图片或获取失败")
```

## 高级用法

### 文本操作的完整流程

```python
def process_clipboard_text():
    """处理剪贴板文本的完整流程"""
    # 1. 获取当前剪贴板内容
    current_text = ClipboardUtils.get_text()
    print(f"当前剪贴板内容: {current_text}")
    
    # 2. 处理文本
    if current_text:
        processed_text = current_text.upper()  # 示例：转换为大写
        print(f"处理后的文本: {processed_text}")
        
        # 3. 将处理后的文本复制回剪贴板
        result = ClipboardUtils.copy_text(processed_text)
        print(f"复制处理后的文本到剪贴板: {'成功' if result else '失败'}")
    else:
        print("剪贴板为空，无法处理")

# 执行处理
process_clipboard_text()
```

### 图片操作的完整流程

```python
def process_clipboard_image():
    """处理剪贴板图片的完整流程"""
    from PIL import Image
    
    # 1. 从剪贴板获取图片
    image = ClipboardUtils.get_image()
    
    if image:
        print(f"获取到图片: {type(image)}")
        print(f"图片尺寸: {image.size}")
        
        # 2. 处理图片（示例：转换为灰度图）
        gray_image = image.convert('L')
        print("图片已转换为灰度图")
        
        # 3. 将处理后的图片复制回剪贴板
        result = ClipboardUtils.copy_image(gray_image)
        print(f"复制处理后的图片到剪贴板: {'成功' if result else '失败'}")
    else:
        print("剪贴板中没有图片")

# 执行处理
process_clipboard_image()
```

### 剪贴板操作的异常处理

```python
def safe_clipboard_operation():
    """安全的剪贴板操作"""
    try:
        # 复制文本
        copy_result = ClipboardUtils.copy_text("Safe clipboard operation")
        if not copy_result:
            print("警告：复制文本到剪贴板失败")
        
        # 获取文本
        text = ClipboardUtils.get_text()
        if text:
            print(f"获取到文本: {text}")
        else:
            print("警告：从剪贴板获取文本失败")
    except Exception as e:
        print(f"剪贴板操作异常: {e}")

# 执行安全操作
safe_clipboard_operation()
```

## 平台实现详情

### Windows 平台

- **文本操作**：优先使用 `pywin32` 库，如果未安装则使用 `ctypes`
- **图片操作**：使用 `pywin32` 库和 `PIL` 库
- **清空操作**：优先使用 `pywin32` 库，如果未安装则使用 `ctypes`

### macOS 平台

- **文本操作**：使用 `subprocess` 调用 `pbcopy` 和 `pbpaste` 命令
- **图片操作**：使用 `subprocess` 调用 `pbcopy` 和 `pbpaste` 命令，并使用 `PIL` 库处理图片
- **清空操作**：使用 `subprocess` 调用 `pbcopy` 命令

### Linux 平台

- **文本操作**：优先使用 `xclip` 命令，如果未安装则尝试使用 `xsel` 命令
- **图片操作**：使用 `xclip` 命令和 `PIL` 库
- **清空操作**：优先使用 `xclip` 命令，如果未安装则尝试使用 `xsel` 命令

## 注意事项

1. **依赖项**：
   - Windows 平台：建议安装 `pywin32` 库以获得更好的性能和稳定性
   - 所有平台：处理图片时需要安装 `PIL`（Pillow）库
   - Linux 平台：需要安装 `xclip` 或 `xsel` 命令行工具

2. **权限问题**：
   - 某些系统可能会限制剪贴板访问权限，特别是在无头环境或容器中
   - 在这种情况下，剪贴板操作可能会失败，但不会抛出异常

3. **环境影响**：
   - 剪贴板是系统级资源，可能会被其他应用程序修改
   - 因此，复制和获取操作之间可能会有时间窗口，导致获取到的内容不是之前复制的内容

4. **异常处理**：
   - 所有剪贴板操作都会捕获异常并返回布尔值或 None
   - 这样设计是为了确保程序不会因为剪贴板操作失败而崩溃

5. **性能考虑**：
   - 剪贴板操作涉及系统调用，可能会比较慢
   - 对于大量数据的操作，建议考虑性能影响

## 应用场景

`ClipboardUtils` 适用于以下场景：

- **文本处理工具**：需要与剪贴板交互的文本编辑器、格式化工具等
- **图片处理工具**：需要复制和粘贴图片的图像处理应用
- **自动化脚本**：需要在脚本执行过程中操作剪贴板的场景
- **用户界面应用**：需要提供剪贴板功能的桌面应用程序
- **数据迁移**：需要在不同应用程序之间传递数据的场景

这些功能使得 `ClipboardUtils` 成为处理剪贴板操作的强大工具，可以在各种应用场景中方便地使用。
