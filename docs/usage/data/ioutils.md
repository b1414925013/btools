# IOUtils 使用指南

`IOUtils` 是一个IO工具类，提供了丰富的IO流操作功能，包括流的读写、复制、转换等，支持字节流和文本流操作，帮助开发者更方便地处理各种IO场景。

## 导入

```python
from btools import IOUtils
# 或
from btools.core import IOUtils
# 或
from btools.core.data import IOUtils
```

## 核心功能

### 1. 流的读写

#### 读取字节流

```python
# 从文件路径读取
bytes_data = IOUtils.read_bytes('example.bin')
print(f"读取的字节数: {len(bytes_data)}")

# 从BytesIO对象读取
import io
buffer = io.BytesIO(b'Hello, World!')
bytes_data = IOUtils.read_bytes(buffer)
print(f"读取的字节数据: {bytes_data}")

# 直接传递字节数据
bytes_data = IOUtils.read_bytes(b'Hello, World!')
print(f"读取的字节数据: {bytes_data}")
```

#### 读取文本流

```python
# 从文件路径读取
text = IOUtils.read_text('example.txt')
print(f"读取的文本内容: {text}")

# 从StringIO对象读取
import io
buffer = io.StringIO('Hello, World!')
text = IOUtils.read_text(buffer)
print(f"读取的文本内容: {text}")

# 从字节数据读取
text = IOUtils.read_text(b'Hello, World!', encoding='utf-8')
print(f"读取的文本内容: {text}")

# 直接传递字符串
text = IOUtils.read_text('Hello, World!')
print(f"读取的文本内容: {text}")
```

#### 写入字节流

```python
# 写入到文件路径
IOUtils.write_bytes('output.bin', b'Hello, World!')
print("字节数据已写入文件")

# 写入到BytesIO对象
import io
buffer = io.BytesIO()
IOUtils.write_bytes(buffer, b'Hello, World!')
buffer.seek(0)
print(f"写入的字节数据: {buffer.read()}")
```

#### 写入文本流

```python
# 写入到文件路径
IOUtils.write_text('output.txt', 'Hello, World!')
print("文本内容已写入文件")

# 写入到StringIO对象
import io
buffer = io.StringIO()
IOUtils.write_text(buffer, 'Hello, World!')
buffer.seek(0)
print(f"写入的文本内容: {buffer.read()}")
```

### 2. 流的复制

```python
# 在文件之间复制
bytes_copied = IOUtils.copy('source.txt', 'destination.txt')
print(f"复制的字节数: {bytes_copied}")

# 在IO对象之间复制
import io
source = io.BytesIO(b'Hello, World!')
destination = io.BytesIO()
bytes_copied = IOUtils.copy(source, destination)
destination.seek(0)
print(f"复制的字节数: {bytes_copied}")
print(f"复制的内容: {destination.read()}")

# 混合复制（文件到IO对象）
source = 'source.txt'
destination = io.BytesIO()
bytes_copied = IOUtils.copy(source, destination)
destination.seek(0)
print(f"复制的字节数: {bytes_copied}")
print(f"复制的内容: {destination.read()}")
```

### 3. 流的转换

#### 转换为BytesIO对象

```python
# 从字符串转换
bytes_io = IOUtils.to_bytes_io('Hello, World!')
print(f"BytesIO内容: {bytes_io.getvalue()}")

# 从字节转换
bytes_io = IOUtils.to_bytes_io(b'Hello, World!')
print(f"BytesIO内容: {bytes_io.getvalue()}")
```

#### 转换为StringIO对象

```python
# 从字符串转换
string_io = IOUtils.to_string_io('Hello, World!')
print(f"StringIO内容: {string_io.getvalue()}")

# 从字节转换
string_io = IOUtils.to_string_io(b'Hello, World!', encoding='utf-8')
print(f"StringIO内容: {string_io.getvalue()}")
```

### 4. 流的其他操作

#### 关闭IO对象

```python
import io
buffer = io.BytesIO(b'Hello, World!')
# 使用buffer...
IOUtils.close(buffer)
print(f"Buffer是否已关闭: {IOUtils.is_closed(buffer)}")
```

#### 获取可用字节数

```python
import io
buffer = io.BytesIO(b'Hello, World!')
available = IOUtils.get_available_bytes(buffer)
print(f"可用字节数: {available}")
```

#### 跳过指定字节数

```python
import io
buffer = io.BytesIO(b'Hello, World!')
# 跳过5个字节
skipped = IOUtils.skip(buffer, 5)
print(f"实际跳过的字节数: {skipped}")
print(f"剩余内容: {buffer.read()}")
```

#### 读取所有行

```python
# 从文件读取
lines = IOUtils.read_lines('example.txt')
print(f"读取的行数: {len(lines)}")
for i, line in enumerate(lines):
    print(f"第{i+1}行: {line.rstrip()}")

# 从StringIO对象读取
import io
buffer = io.StringIO('Line 1\nLine 2\nLine 3')
lines = IOUtils.read_lines(buffer)
print(f"读取的行数: {len(lines)}")
for i, line in enumerate(lines):
    print(f"第{i+1}行: {line.rstrip()}")
```

#### 写入多行

```python
# 写入到文件
lines = ['Line 1', 'Line 2', 'Line 3']
IOUtils.write_lines('output.txt', lines)
print("多行文本已写入文件")

# 写入到StringIO对象
import io
buffer = io.StringIO()
IOUtils.write_lines(buffer, lines)
buffer.seek(0)
print(f"写入的内容: {buffer.read()}")
```

#### 检查IO对象是否已关闭

```python
import io
buffer = io.BytesIO(b'Hello, World!')
print(f"Buffer是否已关闭: {IOUtils.is_closed(buffer)}")
buffer.close()
print(f"Buffer是否已关闭: {IOUtils.is_closed(buffer)}")
```

## 便捷函数

`IOUtils` 还提供了一系列便捷函数，与类方法功能相同，方便直接调用：

```python
from btools.core.data.ioutils import (
    read_bytes, read_text, write_bytes, write_text,
    copy, to_bytes_io, to_string_io, close,
    get_available_bytes, skip, read_lines, write_lines, is_closed
)

# 使用便捷函数
text = read_text('example.txt')
print(f"读取的文本内容: {text}")

# 其他函数使用方式与类方法相同
```

## 高级用法

### 1. 大文件处理

对于大文件，可以使用 `copy` 方法的 `buffer_size` 参数来控制缓冲区大小，提高处理效率：

```python
# 处理大文件，使用更大的缓冲区
bytes_copied = IOUtils.copy('large_file.bin', 'output.bin', buffer_size=65536)  # 64KB缓冲区
print(f"复制的字节数: {bytes_copied}")
```

### 2. 流的链式操作

```python
import io

# 读取文件内容，转换为大写，然后写回文件
text = IOUtils.read_text('input.txt')
upper_text = text.upper()
IOUtils.write_text('output.txt', upper_text)
print("文件内容已转换为大写并写回")

# 或者使用更简洁的方式
IOUtils.write_text('output.txt', IOUtils.read_text('input.txt').upper())
```

### 3. 内存流处理

```python
import io

# 在内存中处理数据
input_data = b'Hello, World!'

# 转换为大写
bytes_io = IOUtils.to_bytes_io(input_data)
data = bytes_io.read()
upper_data = data.upper()

# 写回到新的内存流
output_buffer = io.BytesIO()
IOUtils.write_bytes(output_buffer, upper_data)
output_buffer.seek(0)

print(f"处理后的数据: {output_buffer.read()}")
```

## 实际应用场景

### 1. 文件格式转换

```python
def convert_txt_to_bin(txt_file, bin_file):
    """将文本文件转换为二进制文件"""
    # 读取文本内容
    text = IOUtils.read_text(txt_file)
    # 转换为字节并写入
    IOUtils.write_bytes(bin_file, text.encode('utf-8'))
    print(f"已将 {txt_file} 转换为 {bin_file}")

# 使用示例
# convert_txt_to_bin('input.txt', 'output.bin')
```

### 2. 数据加密处理

```python
def encrypt_file(input_file, output_file, key):
    """加密文件内容"""
    from btools import CryptoUtils
    
    # 读取文件内容
    data = IOUtils.read_bytes(input_file)
    
    # 加密数据
    encrypted_data = CryptoUtils.encrypt_aes(data, key)
    
    # 写入加密后的数据
    IOUtils.write_bytes(output_file, encrypted_data)
    print(f"文件已加密并保存到 {output_file}")

# 使用示例
# encrypt_file('plain.txt', 'encrypted.bin', 'my_secret_key')
```

### 3. 网络数据处理

```python
def process_network_data(response):
    """处理网络响应数据"""
    # 假设response是一个包含字节数据的对象
    data = IOUtils.read_bytes(response)
    
    # 转换为文本
    text = data.decode('utf-8')
    print(f"网络数据长度: {len(data)}")
    print(f"网络数据内容: {text[:100]}...")  # 只打印前100个字符

# 使用示例
# response = requests.get('https://example.com')
# process_network_data(response.content)
```

## 注意事项

1. **编码处理**：在处理文本流时，确保指定正确的编码方式，默认使用UTF-8编码。

2. **资源管理**：对于打开的文件流，建议使用 `with` 语句或手动调用 `close` 方法关闭，以避免资源泄漏。

3. **大文件处理**：处理大文件时，建议使用 `copy` 方法并适当调整缓冲区大小，以提高处理效率。

4. **流位置**：在使用 `read_bytes` 和 `read_text` 方法时，它们会保存并恢复流的位置，不会影响原始流的状态。

5. **错误处理**：IO操作可能会抛出异常，建议在实际使用中添加适当的错误处理。

## 总结

`IOUtils` 提供了全面的IO流操作功能，简化了各种IO场景的处理复杂度，使代码更加简洁易读。无论是基本的文件读写、内存流操作，还是复杂的流转换和复制，`IOUtils` 都能满足你的需求。通过合理使用这些功能，你可以更高效地处理各种IO任务，提高代码的可维护性和可读性。