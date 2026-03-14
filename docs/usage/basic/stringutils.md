# StringUtils 使用指南

`StringUtils` 是一个字符串处理工具类，提供了丰富的字符串操作、格式化、验证等功能，帮助开发者更方便地处理字符串。

## 导入

```python
from btools import StringUtils
```

## 方法详解

### 1. is_empty

**功能**：判断字符串是否为空。

**方法签名**：
```python
@staticmethod
def is_empty(s: Any) -> bool
```

**参数**：
- `s` (Any): 要判断的值

**返回值**：
- `bool`: 如果为空则返回 True，否则返回 False

**使用场景**：
- 验证用户输入是否为空
- 检查配置项是否设置
- 处理可能为 None 的字符串

**使用示例**：
```python
# 检查空字符串
print(StringUtils.is_empty(""))  # 输出: True

# 检查空白字符串
print(StringUtils.is_empty("   "))  # 输出: True

# 检查 None
print(StringUtils.is_empty(None))  # 输出: True

# 检查非空字符串
print(StringUtils.is_empty("hello"))  # 输出: False
```

### 2. is_not_empty

**功能**：判断字符串是否不为空。

**方法签名**：
```python
@staticmethod
def is_not_empty(s: Any) -> bool
```

**参数**：
- `s` (Any): 要判断的值

**返回值**：
- `bool`: 如果不为空则返回 True，否则返回 False

**使用场景**：
- 验证用户输入是否有效
- 检查配置项是否存在
- 作为条件判断

**使用示例**：
```python
# 检查非空字符串
print(StringUtils.is_not_empty("hello"))  # 输出: True

# 检查空字符串
print(StringUtils.is_not_empty(""))  # 输出: False
```

### 3. trim

**功能**：去除字符串两端的空白字符。

**方法签名**：
```python
@staticmethod
def trim(s: str) -> str
```

**参数**：
- `s` (str): 要处理的字符串

**返回值**：
- `str`: 去除空白字符后的字符串

**使用场景**：
- 处理用户输入的表单数据
- 清理从文件或网络获取的字符串
- 比较字符串前的预处理

**使用示例**：
```python
text = "  Hello World  "
trimmed = StringUtils.trim(text)
print(trimmed)  # 输出: "Hello World"
```

### 4. trim_start

**功能**：去除字符串开头的空白字符。

**方法签名**：
```python
@staticmethod
def trim_start(s: str) -> str
```

**参数**：
- `s` (str): 要处理的字符串

**返回值**：
- `str`: 去除开头空白字符后的字符串

**使用场景**：
- 处理左对齐的文本
- 保留右侧空白的场景

**使用示例**：
```python
text = "  Hello World  "
trimmed = StringUtils.trim_start(text)
print(trimmed)  # 输出: "Hello World  "
```

### 5. trim_end

**功能**：去除字符串结尾的空白字符。

**方法签名**：
```python
@staticmethod
def trim_end(s: str) -> str
```

**参数**：
- `s` (str): 要处理的字符串

**返回值**：
- `str`: 去除结尾空白字符后的字符串

**使用场景**：
- 处理右对齐的文本
- 保留左侧空白的场景

**使用示例**：
```python
text = "  Hello World  "
trimmed = StringUtils.trim_end(text)
print(trimmed)  # 输出: "  Hello World"
```

### 6. split

**功能**：分割字符串。

**方法签名**：
```python
@staticmethod
def split(s: str, separator: Optional[str] = ",", maxsplit: int = -1) -> List[str]
```

**参数**：
- `s` (str): 要分割的字符串
- `separator` (Optional[str]): 分隔符，默认为逗号
- `maxsplit` (int): 最大分割次数

**返回值**：
- `List[str]`: 分割后的字符串列表

**使用场景**：
- 解析 CSV 格式的数据
- 处理逗号分隔的配置项
- 分割 URL 路径

**使用示例**：
```python
# 基本分割
text = "Hello,World,Python"
parts = StringUtils.split(text, ",")
print(parts)  # 输出: ["Hello", "World", "Python"]

# 限制分割次数
text = "a,b,c,d,e"
parts = StringUtils.split(text, ",", 2)
print(parts)  # 输出: ["a", "b", "c,d,e"]
```

### 7. join

**功能**：连接字符串列表。

**方法签名**：
```python
@staticmethod
def join(strings: List[str], separator: str = "") -> str
```

**参数**：
- `strings` (List[str]): 字符串列表
- `separator` (str): 连接符

**返回值**：
- `str`: 连接后的字符串

**使用场景**：
- 构建 CSV 格式的数据
- 拼接 URL 路径
- 组合消息文本

**使用示例**：
```python
# 基本连接
words = ["Hello", "World", "Python"]
joined = StringUtils.join(words, " ")
print(joined)  # 输出: "Hello World Python"

# 使用逗号连接
numbers = ["1", "2", "3", "4"]
joined = StringUtils.join(numbers, ",")
print(joined)  # 输出: "1,2,3,4"
```

### 8. replace

**功能**：替换字符串。

**方法签名**：
```python
@staticmethod
def replace(s: str, old: str, new: str, count: int = -1) -> str
```

**参数**：
- `s` (str): 要处理的字符串
- `old` (str): 要替换的子串
- `new` (str): 替换后的子串
- `count` (int): 替换次数，-1 表示全部替换

**返回值**：
- `str`: 替换后的字符串

**使用场景**：
- 替换文本中的特定内容
- 清理字符串中的非法字符
- 格式化模板字符串

**使用示例**：
```python
# 替换单个匹配
text = "Hello World"
replaced = StringUtils.replace(text, "World", "Python")
print(replaced)  # 输出: "Hello Python"

# 替换所有匹配
text = "Hello Hello Hello"
replaced_all = StringUtils.replace(text, "Hello", "Hi")
print(replaced_all)  # 输出: "Hi Hi Hi"

# 限制替换次数
text = "Hello Hello Hello"
replaced_two = StringUtils.replace(text, "Hello", "Hi", 2)
print(replaced_two)  # 输出: "Hi Hi Hello"
```

### 9. substring

**功能**：截取字符串。

**方法签名**：
```python
@staticmethod
def substring(s: str, start: int, end: Optional[int] = None) -> str
```

**参数**：
- `s` (str): 要处理的字符串
- `start` (int): 起始位置
- `end` (Optional[int]): 结束位置

**返回值**：
- `str`: 截取后的字符串

**使用场景**：
- 提取字符串的一部分
- 处理固定格式的文本
- 截取文件路径或 URL

**使用示例**：
```python
text = "Hello World"

# 从索引 6 开始截取
sub = StringUtils.substring(text, 6)
print(sub)  # 输出: "World"

# 截取指定范围
sub = StringUtils.substring(text, 0, 5)
print(sub)  # 输出: "Hello"
```

### 10. starts_with

**功能**：判断字符串是否以指定前缀开头。

**方法签名**：
```python
@staticmethod
def starts_with(s: str, prefix: str, start: int = 0, end: Optional[int] = None) -> bool
```

**参数**：
- `s` (str): 要判断的字符串
- `prefix` (str): 前缀
- `start` (int): 起始位置
- `end` (Optional[int]): 结束位置

**返回值**：
- `bool`: 如果以指定前缀开头则返回 True，否则返回 False

**使用场景**：
- 验证文件扩展名
- 检查 URL 协议
- 识别特定格式的字符串

**使用示例**：
```python
text = "Hello World"

# 检查是否以 "Hello" 开头
print(StringUtils.starts_with(text, "Hello"))  # 输出: True

# 检查是否以 "World" 开头
print(StringUtils.starts_with(text, "World"))  # 输出: False
```

### 11. ends_with

**功能**：判断字符串是否以指定后缀结尾。

**方法签名**：
```python
@staticmethod
def ends_with(s: str, suffix: str, start: int = 0, end: Optional[int] = None) -> bool
```

**参数**：
- `s` (str): 要判断的字符串
- `suffix` (str): 后缀
- `start` (int): 起始位置
- `end` (Optional[int]): 结束位置

**返回值**：
- `bool`: 如果以指定后缀结尾则返回 True，否则返回 False

**使用场景**：
- 验证文件扩展名
- 检查邮箱域名
- 识别特定格式的字符串

**使用示例**：
```python
text = "Hello World"

# 检查是否以 "World" 结尾
print(StringUtils.ends_with(text, "World"))  # 输出: True

# 检查是否以 "Hello" 结尾
print(StringUtils.ends_with(text, "Hello"))  # 输出: False
```

### 12. contains

**功能**：判断字符串是否包含指定子串。

**方法签名**：
```python
@staticmethod
def contains(s: str, substr: str, start: int = 0, end: Optional[int] = None) -> bool
```

**参数**：
- `s` (str): 要判断的字符串
- `substr` (str): 子串
- `start` (int): 起始位置
- `end` (Optional[int]): 结束位置

**返回值**：
- `bool`: 如果包含指定子串则返回 True，否则返回 False

**使用场景**：
- 搜索关键词
- 验证字符串内容
- 过滤特定文本

**使用示例**：
```python
text = "Hello World"

# 检查是否包含 "World"
print(StringUtils.contains(text, "World"))  # 输出: True

# 检查是否包含 "Python"
print(StringUtils.contains(text, "Python"))  # 输出: False
```

### 13. index_of

**功能**：查找子串在字符串中第一次出现的位置。

**方法签名**：
```python
@staticmethod
def index_of(s: str, substr: str, start: int = 0, end: Optional[int] = None) -> int
```

**参数**：
- `s` (str): 要查找的字符串
- `substr` (str): 子串
- `start` (int): 起始位置
- `end` (Optional[int]): 结束位置

**返回值**：
- `int`: 子串在字符串中第一次出现的位置，如果没有找到则返回 -1

**使用场景**：
- 查找分隔符位置
- 提取子串前的内容
- 验证字符串格式

**使用示例**：
```python
text = "Hello World"

# 查找 "World" 的位置
print(StringUtils.index_of(text, "World"))  # 输出: 6

# 查找 "Python" 的位置
print(StringUtils.index_of(text, "Python"))  # 输出: -1
```

### 14. last_index_of

**功能**：查找子串在字符串中最后一次出现的位置。

**方法签名**：
```python
@staticmethod
def last_index_of(s: str, substr: str, start: int = 0, end: Optional[int] = None) -> int
```

**参数**：
- `s` (str): 要查找的字符串
- `substr` (str): 子串
- `start` (int): 起始位置
- `end` (Optional[int]): 结束位置

**返回值**：
- `int`: 子串在字符串中最后一次出现的位置，如果没有找到则返回 -1

**使用场景**：
- 查找文件路径中的最后一个分隔符
- 提取文件扩展名
- 处理包含多个相同子串的情况

**使用示例**：
```python
text = "Hello World Hello"

# 查找最后一个 "Hello" 的位置
print(StringUtils.last_index_of(text, "Hello"))  # 输出: 12
```

### 15. length

**功能**：获取字符串长度。

**方法签名**：
```python
@staticmethod
def length(s: str) -> int
```

**参数**：
- `s` (str): 要处理的字符串

**返回值**：
- `int`: 字符串长度

**使用场景**：
- 验证字符串长度
- 分配缓冲区大小
- 计算字符串占用空间

**使用示例**：
```python
text = "Hello World"
print(StringUtils.length(text))  # 输出: 11

# 处理 None
print(StringUtils.length(None))  # 输出: 0
```

### 16. to_upper

**功能**：将字符串转换为大写。

**方法签名**：
```python
@staticmethod
def to_upper(s: str) -> str
```

**参数**：
- `s` (str): 要处理的字符串

**返回值**：
- `str`: 转换后的大写字符串

**使用场景**：
- 统一字符串大小写
- 不区分大小写的比较
- 格式化输出

**使用示例**：
```python
text = "Hello World"
upper = StringUtils.to_upper(text)
print(upper)  # 输出: "HELLO WORLD"
```

### 17. to_lower

**功能**：将字符串转换为小写。

**方法签名**：
```python
@staticmethod
def to_lower(s: str) -> str
```

**参数**：
- `s` (str): 要处理的字符串

**返回值**：
- `str`: 转换后的小写字符串

**使用场景**：
- 统一字符串大小写
- 不区分大小写的比较
- 格式化输入

**使用示例**：
```python
text = "Hello World"
lower = StringUtils.to_lower(text)
print(lower)  # 输出: "hello world"
```

### 18. capitalize

**功能**：将字符串首字母大写。

**方法签名**：
```python
@staticmethod
def capitalize(s: str) -> str
```

**参数**：
- `s` (str): 要处理的字符串

**返回值**：
- `str`: 首字母大写后的字符串

**使用场景**：
- 格式化姓名
- 句子开头大写
- 标题处理

**使用示例**：
```python
text = "hello world"
capitalized = StringUtils.capitalize(text)
print(capitalized)  # 输出: "Hello world"
```

### 19. title

**功能**：将字符串每个单词的首字母大写。

**方法签名**：
```python
@staticmethod
def title(s: str) -> str
```

**参数**：
- `s` (str): 要处理的字符串

**返回值**：
- `str`: 每个单词首字母大写后的字符串

**使用场景**：
- 格式化标题
- 处理人名和地名
- 生成规范化的文本

**使用示例**：
```python
text = "hello world"
titled = StringUtils.title(text)
print(titled)  # 输出: "Hello World"
```

### 20. pad_left

**功能**：在字符串左侧填充指定字符。

**方法签名**：
```python
@staticmethod
def pad_left(s: str, width: int, fillchar: str = " ") -> str
```

**参数**：
- `s` (str): 要处理的字符串
- `width` (int): 填充后的宽度
- `fillchar` (str): 填充字符

**返回值**：
- `str`: 左侧填充后的字符串

**使用场景**：
- 格式化数字（补前导零）
- 对齐文本
- 生成固定长度的字符串

**使用示例**：
```python
text = "123"

# 左侧填充零
padded = StringUtils.pad_left(text, 5, "0")
print(padded)  # 输出: "00123"

# 左侧填充空格
padded = StringUtils.pad_left(text, 10)
print(f"'{padded}'")  # 输出: "       123"
```

### 21. pad_right

**功能**：在字符串右侧填充指定字符。

**方法签名**：
```python
@staticmethod
def pad_right(s: str, width: int, fillchar: str = " ") -> str
```

**参数**：
- `s` (str): 要处理的字符串
- `width` (int): 填充后的宽度
- `fillchar` (str): 填充字符

**返回值**：
- `str`: 右侧填充后的字符串

**使用场景**：
- 对齐文本
- 生成固定长度的字符串
- 格式化表格输出

**使用示例**：
```python
text = "123"

# 右侧填充零
padded = StringUtils.pad_right(text, 5, "0")
print(padded)  # 输出: "12300"

# 右侧填充空格
padded = StringUtils.pad_right(text, 10)
print(f"'{padded}'")  # 输出: "123       "
```

### 22. pad_center

**功能**：在字符串两侧填充指定字符。

**方法签名**：
```python
@staticmethod
def pad_center(s: str, width: int, fillchar: str = " ") -> str
```

**参数**：
- `s` (str): 要处理的字符串
- `width` (int): 填充后的宽度
- `fillchar` (str): 填充字符

**返回值**：
- `str`: 两侧填充后的字符串

**使用场景**：
- 居中对齐文本
- 生成装饰性文本
- 格式化标题

**使用示例**：
```python
text = "123"

# 两侧填充连字符
padded = StringUtils.pad_center(text, 7, "-")
print(padded)  # 输出: "--123--"

# 两侧填充空格
padded = StringUtils.pad_center(text, 10)
print(f"'{padded}'")  # 输出: "   123    "
```

### 23. remove_whitespace

**功能**：移除字符串中的所有空白字符。

**方法签名**：
```python
@staticmethod
def remove_whitespace(s: str) -> str
```

**参数**：
- `s` (str): 要处理的字符串

**返回值**：
- `str`: 移除空白字符后的字符串

**使用场景**：
- 清理用户输入
- 生成紧凑的字符串
- 处理不含空格的标识符

**使用示例**：
```python
text = "  Hello   World  "
removed = StringUtils.remove_whitespace(text)
print(removed)  # 输出: "HelloWorld"
```

### 24. replace_whitespace

**功能**：替换字符串中的所有空白字符。

**方法签名**：
```python
@staticmethod
def replace_whitespace(s: str, replacement: str = " ") -> str
```

**参数**：
- `s` (str): 要处理的字符串
- `replacement` (str): 替换字符

**返回值**：
- `str`: 替换空白字符后的字符串

**使用场景**：
- 标准化空白字符
- 将多个空格替换为单个空格
- 生成格式化的文本

**使用示例**：
```python
text = "  Hello   World  "
replaced = StringUtils.replace_whitespace(text, " ")
print(replaced)  # 输出: " Hello World "

# 替换为下划线
replaced = StringUtils.replace_whitespace(text, "_")
print(replaced)  # 输出: "__Hello___World__"
```

### 25. is_alpha

**功能**：判断字符串是否只包含字母。

**方法签名**：
```python
@staticmethod
def is_alpha(s: str) -> bool
```

**参数**：
- `s` (str): 要判断的字符串

**返回值**：
- `bool`: 如果只包含字母则返回 True，否则返回 False

**使用场景**：
- 验证用户名
- 检查标识符
- 过滤非字母字符

**使用示例**：
```python
print(StringUtils.is_alpha("Hello"))  # 输出: True
print(StringUtils.is_alpha("Hello123"))  # 输出: False
print(StringUtils.is_alpha("Hello World"))  # 输出: False
```

### 26. is_digit

**功能**：判断字符串是否只包含数字。

**方法签名**：
```python
@staticmethod
def is_digit(s: str) -> bool
```

**参数**：
- `s` (str): 要判断的字符串

**返回值**：
- `bool`: 如果只包含数字则返回 True，否则返回 False

**使用场景**：
- 验证数字输入
- 检查身份证号
- 处理数值字符串

**使用示例**：
```python
print(StringUtils.is_digit("123"))  # 输出: True
print(StringUtils.is_digit("123abc"))  # 输出: False
print(StringUtils.is_digit("12.3"))  # 输出: False
```

### 27. is_alphanumeric

**功能**：判断字符串是否只包含字母和数字。

**方法签名**：
```python
@staticmethod
def is_alphanumeric(s: str) -> bool
```

**参数**：
- `s` (str): 要判断的字符串

**返回值**：
- `bool`: 如果只包含字母和数字则返回 True，否则返回 False

**使用场景**：
- 验证密码强度
- 检查标识符
- 过滤特殊字符

**使用示例**：
```python
print(StringUtils.is_alphanumeric("Hello123"))  # 输出: True
print(StringUtils.is_alphanumeric("Hello 123"))  # 输出: False
print(StringUtils.is_alphanumeric("Hello@123"))  # 输出: False
```

### 28. is_numeric

**功能**：判断字符串是否只包含数字字符。

**方法签名**：
```python
@staticmethod
def is_numeric(s: str) -> bool
```

**参数**：
- `s` (str): 要判断的字符串

**返回值**：
- `bool`: 如果只包含数字字符则返回 True，否则返回 False

**使用场景**：
- 验证数字输入
- 检查数值字符串
- 处理数字相关的输入

**使用示例**：
```python
print(StringUtils.is_numeric("123"))  # 输出: True
print(StringUtils.is_numeric("123abc"))  # 输出: False
print(StringUtils.is_numeric("12.3"))  # 输出: False
```

### 29. is_blank

**功能**：判断字符串是否为空白。

**方法签名**：
```python
@staticmethod
def is_blank(s: str) -> bool
```

**参数**：
- `s` (str): 要判断的字符串

**返回值**：
- `bool`: 如果为空白则返回 True，否则返回 False

**使用场景**：
- 验证用户输入
- 检查配置项
- 处理空字符串

**使用示例**：
```python
print(StringUtils.is_blank(""))  # 输出: True
print(StringUtils.is_blank("   "))  # 输出: True
print(StringUtils.is_blank("Hello"))  # 输出: False
```

### 30. is_not_blank

**功能**：判断字符串是否不为空白。

**方法签名**：
```python
@staticmethod
def is_not_blank(s: str) -> bool
```

**参数**：
- `s` (str): 要判断的字符串

**返回值**：
- `bool`: 如果不为空白则返回 True，否则返回 False

**使用场景**：
- 验证用户输入
- 检查配置项
- 作为条件判断

**使用示例**：
```python
print(StringUtils.is_not_blank("Hello"))  # 输出: True
print(StringUtils.is_not_blank(""))  # 输出: False
```

### 31. repeat

**功能**：重复字符串。

**方法签名**：
```python
@staticmethod
def repeat(s: str, times: int) -> str
```

**参数**：
- `s` (str): 要重复的字符串
- `times` (int): 重复次数

**返回值**：
- `str`: 重复后的字符串

**使用场景**：
- 生成装饰性文本
- 创建分隔线
- 填充固定长度的字符串

**使用示例**：
```python
text = "Hello"
repeated = StringUtils.repeat(text, 3)
print(repeated)  # 输出: "HelloHelloHello"

# 生成分隔线
divider = StringUtils.repeat("-", 20)
print(divider)  # 输出: "--------------------"
```

### 32. reverse

**功能**：反转字符串。

**方法签名**：
```python
@staticmethod
def reverse(s: str) -> str
```

**参数**：
- `s` (str): 要反转的字符串

**返回值**：
- `str`: 反转后的字符串

**使用场景**：
- 检查回文
- 生成镜像文本
- 处理特定格式的字符串

**使用示例**：
```python
text = "Hello World"
reversed = StringUtils.reverse(text)
print(reversed)  # 输出: "dlroW olleH"

# 检查回文
word = "level"
is_palindrome = word == StringUtils.reverse(word)
print(f"{word} 是回文: {is_palindrome}")  # 输出: "level 是回文: True"
```

### 33. format_template

**功能**：格式化模板字符串。

**方法签名**：
```python
@staticmethod
def format_template(template: str, data: Optional[Dict] = None, **kwargs) -> str
```

**参数**：
- `template` (str): 模板字符串
- `data` (Optional[Dict]): 模板参数字典
- `**kwargs`: 模板参数

**返回值**：
- `str`: 格式化后的字符串

**使用场景**：
- 生成动态文本
- 格式化邮件内容
- 构建消息模板

**使用示例**：
```python
# 使用字典参数
template = "Name: {name}, Age: {age}"
data = {"name": "John", "age": 30}
formatted = StringUtils.format_template(template, data)
print(formatted)  # 输出: "Name: John, Age: 30"

# 使用关键字参数
formatted = StringUtils.format_template(template, name="John", age=30)
print(formatted)  # 输出: "Name: John, Age: 30"
```

### 34. generate_random_string

**功能**：生成随机字符串。

**方法签名**：
```python
@staticmethod
def generate_random_string(length: int, chars: str = string.ascii_letters + string.digits) -> str
```

**参数**：
- `length` (int): 字符串长度
- `chars` (str): 字符集

**返回值**：
- `str`: 随机字符串

**使用场景**：
- 生成验证码
- 创建临时密码
- 生成唯一标识符

**使用示例**：
```python
# 生成默认字符集的随机字符串
random_str = StringUtils.generate_random_string(10)
print(random_str)  # 输出: 例如 "aB3cDeFgHi"

# 生成只包含数字的随机字符串
import string
random_digits = StringUtils.generate_random_string(6, string.digits)
print(random_digits)  # 输出: 例如 "123456"

# 生成只包含字母的随机字符串
random_letters = StringUtils.generate_random_string(8, string.ascii_letters)
print(random_letters)  # 输出: 例如 "AbCdEfGh"
```

## 综合使用示例

### 1. 处理用户输入

```python
def process_user_input(input_str):
    """处理用户输入"""
    # 修剪空白字符
    input_str = StringUtils.trim(input_str)
    
    # 检查是否为空
    if StringUtils.is_empty(input_str):
        return "输入不能为空"
    
    # 转换为小写
    input_str = StringUtils.to_lower(input_str)
    
    return input_str

# 使用示例
user_input = "  Hello World  "
processed = process_user_input(user_input)
print(processed)  # 输出: "hello world"
```

### 2. 生成唯一标识符

```python
import time
def generate_unique_id(prefix="id"):
    """生成唯一标识符"""
    timestamp = str(int(time.time()))
    random_str = StringUtils.generate_random_string(8)
    return f"{prefix}_{timestamp}_{random_str}"

# 使用示例
unique_id = generate_unique_id()
print(unique_id)  # 输出: 例如 "id_1620000000_aB3cDeFg"
```

### 3. 格式化数据输出

```python
def format_user_info(user):
    """格式化用户信息"""
    template = """用户信息:
姓名: {name}
年龄: {age}
邮箱: {email}
地址: {address}"""
    
    return StringUtils.format_template(template, user)

# 使用示例
user = {
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com",
    "address": "123 Main St, New York"
}

formatted_info = format_user_info(user)
print(formatted_info)
# 输出:
# 用户信息:
# 姓名: John Doe
# 年龄: 30
# 邮箱: john@example.com
# 地址: 123 Main St, New York
```

### 4. 验证和处理表单数据

```python
def validate_form_data(data):
    """验证表单数据"""
    errors = []
    
    # 验证用户名
    username = data.get("username")
    if StringUtils.is_empty(username):
        errors.append("用户名不能为空")
    elif not StringUtils.is_alphanumeric(username):
        errors.append("用户名只能包含字母和数字")
    elif StringUtils.length(username) < 3:
        errors.append("用户名长度不能少于3个字符")
    
    # 验证邮箱
    email = data.get("email")
    if StringUtils.is_empty(email):
        errors.append("邮箱不能为空")
    elif "@" not in email:
        errors.append("邮箱格式不正确")
    
    return errors

# 使用示例
form_data = {
    "username": "john123",
    "email": "john@example.com"
}

errors = validate_form_data(form_data)
if errors:
    print("表单验证失败:")
    for error in errors:
        print(f"- {error}")
else:
    print("表单验证成功")
```

## 性能提示

- 对于频繁的字符串操作，建议使用 `join()` 而不是 `+` 来连接字符串，因为 `join()` 更高效
- 对于大字符串的替换操作，考虑使用正则表达式以获得更好的性能
- 对于需要重复使用的字符串模板，建议预编译模板以提高性能
- 对于大量的字符串处理，考虑使用生成器表达式和迭代器来减少内存使用

## 总结

`StringUtils` 提供了全面的字符串处理功能，从基本的修剪、大小写转换到高级的字符串模板和随机字符串生成，涵盖了日常开发中大部分字符串处理需求。通过合理使用这些功能，可以大大简化字符串处理代码，提高开发效率。

所有方法都提供了对 `None` 值的安全处理，确保在处理可能为 `None` 的字符串时不会抛出异常。这使得 `StringUtils` 成为处理字符串的可靠工具类。