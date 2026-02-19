# AIUtils 使用指南

`AIUtils` 是一个AI工具类，提供了丰富的AI操作方法，包括AI模型调用、文本处理等功能。

## 功能特性

- AI模型调用
- 文本处理

## 基本用法

### 导入

```python
from btools import AIUtils
```

### 示例

#### AI模型调用

```python
# 调用AI模型
prompt = "Hello, how are you?"
response = AIUtils.call_model(prompt)
print(response)  # 输出: AI模型的响应

# 调用指定模型
response = AIUtils.call_model(prompt, model="gpt-3.5-turbo")
print(response)  # 输出: 指定模型的响应
```

#### 文本处理

```python
# 文本摘要
text = "This is a long text that needs to be summarized. It contains multiple sentences and provides detailed information about a topic."
summary = AIUtils.summarize_text(text)
print(summary)  # 输出: 文本摘要

# 文本分类
text = "I love this product! It's amazing and works perfectly."
category = AIUtils.classify_text(text)
print(category)  # 输出: 文本分类结果

# 情感分析
sentiment = AIUtils.analyze_sentiment(text)
print(sentiment)  # 输出: 情感分析结果
```

## 高级用法

### 多轮对话

```python
# 多轮对话
messages = [
    {"role": "user", "content": "Hello, what's your name?"},
    {"role": "assistant", "content": "I'm an AI assistant."},
    {"role": "user", "content": "What can you do?"}
]
response = AIUtils.chat(messages)
print(response)  # 输出: AI助手的响应
```

### 文本翻译

```python
# 文本翻译
text = "Hello, how are you?"
translated = AIUtils.translate_text(text, target_language="zh")
print(translated)  # 输出: 你好，你怎么样？

# 多语言翻译
languages = ["fr", "es", "de"]
for lang in languages:
    translated = AIUtils.translate_text(text, target_language=lang)
    print(f"{lang}: {translated}")
```

## 注意事项

1. 使用AI模型需要确保已配置相关API密钥。
2. 不同AI模型的响应格式和质量可能会有所不同。
3. 对于大型文本处理，可能会受到API限制或产生较高的费用。

## 总结

`AIUtils` 提供了全面的AI操作功能，简化了AI模型调用和文本处理的复杂度，使代码更加简洁易读。无论是基本的AI模型调用还是高级的文本处理，`AIUtils` 都能满足你的需求。