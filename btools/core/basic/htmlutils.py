#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML工具类

提供HTML处理功能，包括HTML转义、反转义、标签处理、属性处理等
"""
import re
from typing import Any, Dict, List, Optional, Union


class HtmlUtil:
    """
    HTML工具类
    """

    # HTML转义映射
    _ESCAPE_MAP = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#x27;',
        '/': '&#x2F;'
    }

    # HTML反转义映射
    _UNESCAPE_MAP = {
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
        '&quot;': '"',
        '&#x27;': "'",
        '&#x2F;': '/'
    }

    @staticmethod
    def escape(html: str) -> str:
        """
        HTML转义

        Args:
            html: 原始HTML字符串

        Returns:
            str: 转义后的HTML字符串
        """
        if not html:
            return html
        
        result = html
        for char, escaped in HtmlUtil._ESCAPE_MAP.items():
            result = result.replace(char, escaped)
        return result

    @staticmethod
    def unescape(html: str) -> str:
        """
        HTML反转义

        Args:
            html: 转义后的HTML字符串

        Returns:
            str: 反转义后的HTML字符串
        """
        if not html:
            return html
        
        result = html
        for escaped, char in HtmlUtil._UNESCAPE_MAP.items():
            result = result.replace(escaped, char)
        return result

    @staticmethod
    def removeHtmlTags(html: str) -> str:
        """
        移除HTML标签

        Args:
            html: HTML字符串

        Returns:
            str: 移除标签后的纯文本
        """
        if not html:
            return html
        
        # 移除HTML标签
        clean = re.compile('<.*?>')
        return re.sub(clean, '', html)

    @staticmethod
    def extractText(html: str) -> str:
        """
        提取HTML文本内容

        Args:
            html: HTML字符串

        Returns:
            str: 提取的文本内容
        """
        # 首先移除标签
        text = HtmlUtil.removeHtmlTags(html)
        # 然后反转义HTML实体
        return HtmlUtil.unescape(text)

    @staticmethod
    def getAttribute(html: str, tag: str, attr: str) -> Optional[str]:
        """
        获取HTML标签的属性值

        Args:
            html: HTML字符串
            tag: 标签名
            attr: 属性名

        Returns:
            Optional[str]: 属性值，不存在返回None
        """
        if not html:
            return None
        
        pattern = rf'<{tag}[^>]*?{attr}\s*=\s*["\']([^"\']*)["\']'
        match = re.search(pattern, html)
        if match:
            return match.group(1)
        return None

    @staticmethod
    def setAttribute(html: str, tag: str, attr: str, value: str) -> str:
        """
        设置HTML标签的属性值

        Args:
            html: HTML字符串
            tag: 标签名
            attr: 属性名
            value: 属性值

        Returns:
            str: 设置属性后的HTML字符串
        """
        if not html:
            return html
        
        # 检查是否已存在该属性
        pattern = rf'<({tag}[^>]*?)({attr}\s*=\s*["\'])([^"\']*)(["\'])([^>]*?>)'
        
        if re.search(pattern, html):
            # 替换已存在的属性值
            return re.sub(pattern, rf'<\1\2{value}\4\5>', html)
        else:
            # 添加新属性
            pattern = rf'<({tag})([^>]*?)(>)'
            return re.sub(pattern, rf'<\1 \2 {attr}="{value}"\3>', html)

    @staticmethod
    def removeAttribute(html: str, tag: str, attr: str) -> str:
        """
        移除HTML标签的属性

        Args:
            html: HTML字符串
            tag: 标签名
            attr: 属性名

        Returns:
            str: 移除属性后的HTML字符串
        """
        if not html:
            return html
        
        pattern = rf'<({tag}[^>]*?)(\s+{attr}\s*=\s*["\'][^"\']*["\'])([^>]*?>)'
        return re.sub(pattern, r'<\1\3>', html)

    @staticmethod
    def formatHtml(html: str, indent: int = 2) -> str:
        """
        格式化HTML字符串

        Args:
            html: 原始HTML字符串
            indent: 缩进空格数

        Returns:
            str: 格式化后的HTML字符串
        """
        if not html:
            return html
        
        # 移除多余的空白字符
        html = re.sub(r'\s+', ' ', html)
        html = re.sub(r'>\s+<', '><', html)
        
        # 格式化
        indent_level = 0
        result = []
        i = 0
        
        while i < len(html):
            if html[i] == '<':
                if i + 1 < len(html) and html[i + 1] == '/':
                    # 结束标签
                    indent_level -= 1
                    i += 2
                    tag_end = html.find('>', i)
                    if tag_end != -1:
                        result.append(' ' * (indent_level * indent) + '</' + html[i:tag_end] + '>')
                        i = tag_end + 1
                else:
                    # 开始标签
                    tag_end = html.find('>', i)
                    if tag_end != -1:
                        tag_content = html[i:tag_end + 1]
                        result.append(' ' * (indent_level * indent) + tag_content)
                        indent_level += 1
                        i = tag_end + 1
            else:
                # 文本内容
                text_end = html.find('<', i)
                if text_end != -1:
                    text = html[i:text_end].strip()
                    if text:
                        result.append(' ' * (indent_level * indent) + text)
                    i = text_end
                else:
                    text = html[i:].strip()
                    if text:
                        result.append(' ' * (indent_level * indent) + text)
                    break
        
        return '\n'.join(result)

    @staticmethod
    def minifyHtml(html: str) -> str:
        """
        压缩HTML字符串

        Args:
            html: 原始HTML字符串

        Returns:
            str: 压缩后的HTML字符串
        """
        if not html:
            return html
        
        # 移除注释
        html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
        # 移除多余的空白字符
        html = re.sub(r'\s+', ' ', html)
        # 移除标签间的空白
        html = re.sub(r'>\s+<', '><', html)
        # 移除首尾空白
        return html.strip()

    @staticmethod
    def isHtml(html: str) -> bool:
        """
        检查字符串是否为HTML

        Args:
            html: 字符串

        Returns:
            bool: 是否为HTML
        """
        if not html:
            return False
        
        # 检查是否包含HTML标签
        return bool(re.search(r'<[^>]+>', html))

    @staticmethod
    def wrapHtml(body: str, title: str = "", charset: str = "UTF-8") -> str:
        """
        包装HTML文档

        Args:
            body: 正文内容
            title: 页面标题
            charset: 字符集

        Returns:
            str: 完整的HTML文档
        """
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="{charset}">
    <title>{HtmlUtil.escape(title)}</title>
</head>
<body>
    {body}
</body>
</html>
        """
        return html.strip()

    @staticmethod
    def createTag(tag: str, attributes: Dict[str, str] = None, content: str = "") -> str:
        """
        创建HTML标签

        Args:
            tag: 标签名
            attributes: 属性字典
            content: 标签内容

        Returns:
            str: 创建的HTML标签
        """
        # 构建属性字符串
        attr_str = ""
        if attributes:
            for key, value in attributes.items():
                attr_str += f" {key}=\"{HtmlUtil.escape(str(value))}\""
        
        # 构建标签
        if content:
            return f"<{tag}{attr_str}>{HtmlUtil.escape(content)}</{tag}>"
        else:
            return f"<{tag}{attr_str} />"

    @staticmethod
    def getTags(html: str, tag: str) -> List[str]:
        """
        获取HTML中指定标签的所有实例

        Args:
            html: HTML字符串
            tag: 标签名

        Returns:
            List[str]: 标签列表
        """
        if not html:
            return []
        
        pattern = rf'<{tag}[^>]*?>[\s\S]*?</{tag}>'
        return re.findall(pattern, html)

    @staticmethod
    def replaceTag(html: str, old_tag: str, new_tag: str) -> str:
        """
        替换HTML标签名

        Args:
            html: HTML字符串
            old_tag: 旧标签名
            new_tag: 新标签名

        Returns:
            str: 替换后的HTML字符串
        """
        if not html:
            return html
        
        # 替换开始标签
        html = re.sub(rf'<({old_tag})([^>]*?)>', rf'<{new_tag}\2>', html)
        # 替换结束标签
        html = re.sub(rf'</{old_tag}>', rf'</{new_tag}>', html)
        return html

    @staticmethod
    def addClass(html: str, tag: str, class_name: str) -> str:
        """
        为HTML标签添加类

        Args:
            html: HTML字符串
            tag: 标签名
            class_name: 类名

        Returns:
            str: 添加类后的HTML字符串
        """
        if not html:
            return html
        
        # 检查是否已存在class属性
        pattern = rf'<({tag}[^>]*?)(class\s*=\s*["\'])([^"\']*)(["\'])([^>]*?>)'
        
        if re.search(pattern, html):
            # 已存在class属性，添加类名
            def replace_func(match):
                existing_classes = match.group(3)
                if class_name not in existing_classes.split():
                    new_classes = f"{existing_classes} {class_name}"
                    return f"<{match.group(1)}class=\"{new_classes}\"{match.group(5)}>"
                return match.group(0)
            
            return re.sub(pattern, replace_func, html)
        else:
            # 不存在class属性，添加
            pattern = rf'<({tag})([^>]*?)(>)'
            return re.sub(pattern, rf'<\1\2 class="{class_name}"\3>', html)

    @staticmethod
    def removeClass(html: str, tag: str, class_name: str) -> str:
        """
        从HTML标签移除类

        Args:
            html: HTML字符串
            tag: 标签名
            class_name: 类名

        Returns:
            str: 移除类后的HTML字符串
        """
        if not html:
            return html
        
        pattern = rf'<({tag}[^>]*?)(class\s*=\s*["\'])([^"\']*)(["\'])([^>]*?>)'
        
        def replace_func(match):
            existing_classes = match.group(3)
            new_classes = ' '.join(cls for cls in existing_classes.split() if cls != class_name)
            if new_classes:
                return f"<{match.group(1)}class=\"{new_classes}\"{match.group(5)}>"
            else:
                # 如果没有类了，移除class属性
                return f"<{match.group(1)}{match.group(5)}>"
        
        return re.sub(pattern, replace_func, html)

    @staticmethod
    def getInnerHtml(html: str, tag: str) -> Optional[str]:
        """
        获取HTML标签的内部内容

        Args:
            html: HTML字符串
            tag: 标签名

        Returns:
            Optional[str]: 内部内容，不存在返回None
        """
        if not html:
            return None
        
        pattern = rf'<{tag}[^>]*?>([\s\S]*?)</{tag}>'
        match = re.search(pattern, html)
        if match:
            return match.group(1)
        return None

    @staticmethod
    def setInnerHtml(html: str, tag: str, content: str) -> str:
        """
        设置HTML标签的内部内容

        Args:
            html: HTML字符串
            tag: 标签名
            content: 内部内容

        Returns:
            str: 设置内部内容后的HTML字符串
        """
        if not html:
            return html
        
        pattern = rf'<({tag}[^>]*?)>([\s\S]*?)</{tag}>'
        return re.sub(pattern, rf'<\1>{HtmlUtil.escape(content)}</{tag}>', html)