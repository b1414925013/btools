# I18nUtils 使用指南

`I18nUtils` 是一个国际化工具类，提供了丰富的国际化操作方法，包括加载翻译、获取翻译、切换语言等功能。

## 功能特性

- 加载翻译
- 获取翻译
- 切换语言
- 翻译文本

## 基本用法

### 导入

```python
from btools import I18nUtils
```

### 示例

#### 加载翻译

```python
# 加载翻译
translations = {
    "en": {
        "hello": "Hello",
        "welcome": "Welcome to our website!",
        "user": {
            "name": "Name",
            "email": "Email"
        }
    },
    "zh": {
        "hello": "你好",
        "welcome": "欢迎来到我们的网站！",
        "user": {
            "name": "姓名",
            "email": "邮箱"
        }
    }
}

I18nUtils.load_translations(translations)
```

#### 获取翻译

```python
# 获取翻译（默认语言）
print(I18nUtils.get("hello"))  # 输出: Hello
print(I18nUtils.get("welcome"))  # 输出: Welcome to our website!

# 获取嵌套翻译
print(I18nUtils.get("user.name"))  # 输出: Name
print(I18nUtils.get("user.email"))  # 输出: Email

# 切换语言
I18nUtils.set_locale("zh")

# 获取翻译（中文）
print(I18nUtils.get("hello"))  # 输出: 你好
print(I18nUtils.get("welcome"))  # 输出: 欢迎来到我们的网站！
print(I18nUtils.get("user.name"))  # 输出: 姓名
print(I18nUtils.get("user.email"))  # 输出: 邮箱
```

#### 翻译文本

```python
# 翻译文本
print(I18nUtils.translate("hello", locale="en"))  # 输出: Hello
print(I18nUtils.translate("hello", locale="zh"))  # 输出: 你好

# 翻译嵌套文本
print(I18nUtils.translate("user.name", locale="en"))  # 输出: Name
print(I18nUtils.translate("user.name", locale="zh"))  # 输出: 姓名
```

## 高级用法

### 动态加载翻译

```python
# 动态加载翻译
def load_translations():
    return {
        "en": {
            "hello": "Hello",
            "bye": "Goodbye"
        },
        "fr": {
            "hello": "Bonjour",
            "bye": "Au revoir"
        }
    }

# 加载翻译
I18nUtils.load_translations(load_translations())

# 获取翻译
print(I18nUtils.get("hello"))  # 输出: Hello

# 切换到法语
I18nUtils.set_locale("fr")
print(I18nUtils.get("hello"))  # 输出: Bonjour
```

### 处理缺失的翻译

```python
# 处理缺失的翻译
I18nUtils.set_locale("zh")

# 获取存在的翻译
print(I18nUtils.get("hello"))  # 输出: 你好

# 获取不存在的翻译（返回键名）
print(I18nUtils.get("nonexistent"))  # 输出: nonexistent
```

### 批量翻译

```python
# 批量翻译
keys = ["hello", "welcome", "user.name", "user.email"]

# 英语翻译
I18nUtils.set_locale("en")
en_translations = {key: I18nUtils.get(key) for key in keys}
print(en_translations)
# 输出: {'hello': 'Hello', 'welcome': 'Welcome to our website!', 'user.name': 'Name', 'user.email': 'Email'}

# 中文翻译
I18nUtils.set_locale("zh")
zh_translations = {key: I18nUtils.get(key) for key in keys}
print(zh_translations)
# 输出: {'hello': '你好', 'welcome': '欢迎来到我们的网站！', 'user.name': '姓名', 'user.email': '邮箱'}
```

## 注意事项

1. 翻译文件的格式应该是嵌套的字典结构，其中顶级键是语言代码，值是该语言的翻译字典。
2. 如果尝试获取不存在的翻译键，会返回键名本身。
3. 默认语言是英语（"en"）。

## 总结

`I18nUtils` 提供了基本的国际化操作功能，简化了国际化处理的复杂度，使代码更加简洁易读。无论是基本的翻译操作还是高级的国际化处理，`I18nUtils` 都能满足你的需求。