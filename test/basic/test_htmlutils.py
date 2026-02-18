#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HtmlUtil 测试文件
"""
import unittest
from btools.core.basic import HtmlUtil


class TestHtmlUtil(unittest.TestCase):
    """
    HtmlUtil 测试类
    """

    def test_escape(self):
        """
        测试HTML转义
        """
        # 测试空字符串
        self.assertEqual(HtmlUtil.escape(""), "")
        
        # 测试普通字符串
        self.assertEqual(HtmlUtil.escape("hello"), "hello")
        
        # 测试需要转义的字符串
        html = "<div>hello & world</div>"
        escaped = HtmlUtil.escape(html)
        self.assertEqual(escaped, "&lt;div&gt;hello &amp; world&lt;/div&gt;")

    def test_unescape(self):
        """
        测试HTML反转义
        """
        # 测试空字符串
        self.assertEqual(HtmlUtil.unescape(""), "")
        
        # 测试普通字符串
        self.assertEqual(HtmlUtil.unescape("hello"), "hello")
        
        # 测试需要反转义的字符串
        escaped = "&lt;div&gt;hello &amp; world&lt;/div&gt;"
        unescaped = HtmlUtil.unescape(escaped)
        self.assertEqual(unescaped, "<div>hello & world</div>")

    def test_removeHtmlTags(self):
        """
        测试移除HTML标签
        """
        # 测试空字符串
        self.assertEqual(HtmlUtil.removeHtmlTags(""), "")
        
        # 测试无标签字符串
        self.assertEqual(HtmlUtil.removeHtmlTags("hello"), "hello")
        
        # 测试有标签字符串
        html = "<div>hello <b>world</b></div>"
        text = HtmlUtil.removeHtmlTags(html)
        self.assertEqual(text, "hello world")

    def test_extractText(self):
        """
        测试提取HTML文本内容
        """
        # 测试空字符串
        self.assertEqual(HtmlUtil.extractText(""), "")
        
        # 测试有标签和转义字符的字符串
        html = "<div>hello &lt;b&gt;world&lt;/b&gt;</div>"
        text = HtmlUtil.extractText(html)
        self.assertEqual(text, "hello <b>world</b>")

    def test_getAttribute(self):
        """
        测试获取HTML标签的属性值
        """
        # 测试空字符串
        self.assertIsNone(HtmlUtil.getAttribute("", "div", "class"))
        
        # 测试有属性的标签
        html = '<div class="test" id="test-id">content</div>'
        class_attr = HtmlUtil.getAttribute(html, "div", "class")
        self.assertEqual(class_attr, "test")
        
        # 测试不存在的属性
        self.assertIsNone(HtmlUtil.getAttribute(html, "div", "style"))

    def test_setAttribute(self):
        """
        测试设置HTML标签的属性值
        """
        # 测试空字符串
        self.assertEqual(HtmlUtil.setAttribute("", "div", "class", "test"), "")
        
        # 测试设置不存在的属性
        html = '<div>content</div>'
        updated = HtmlUtil.setAttribute(html, "div", "class", "test")
        self.assertIn('class="test"', updated)
        
        # 测试更新已存在的属性
        html = '<div class="old">content</div>'
        updated = HtmlUtil.setAttribute(html, "div", "class", "new")
        self.assertIn('class="new"', updated)

    def test_removeAttribute(self):
        """
        测试移除HTML标签的属性
        """
        # 测试空字符串
        self.assertEqual(HtmlUtil.removeAttribute("", "div", "class"), "")
        
        # 测试移除存在的属性
        html = '<div class="test" id="test-id">content</div>'
        updated = HtmlUtil.removeAttribute(html, "div", "class")
        self.assertNotIn('class="test"', updated)
        self.assertIn('id="test-id"', updated)

    def test_formatHtml(self):
        """
        测试格式化HTML字符串
        """
        # 测试空字符串
        self.assertEqual(HtmlUtil.formatHtml(""), "")
        
        # 测试格式化HTML
        html = '<div><p>hello</p></div>'
        formatted = HtmlUtil.formatHtml(html)
        self.assertIn('\n', formatted)
        self.assertIn('  <p>hello</p>', formatted)

    def test_minifyHtml(self):
        """
        测试压缩HTML字符串
        """
        # 测试空字符串
        self.assertEqual(HtmlUtil.minifyHtml(""), "")
        
        # 测试压缩HTML
        html = '''
        <div>
            <p>hello</p>
        </div>
        '''
        minified = HtmlUtil.minifyHtml(html)
        self.assertEqual(minified, '<div><p>hello</p></div>')

    def test_isHtml(self):
        """
        测试检查字符串是否为HTML
        """
        # 测试空字符串
        self.assertFalse(HtmlUtil.isHtml(""))
        
        # 测试普通字符串
        self.assertFalse(HtmlUtil.isHtml("hello"))
        
        # 测试HTML字符串
        self.assertTrue(HtmlUtil.isHtml("<div>hello</div>"))

    def test_wrapHtml(self):
        """
        测试包装HTML文档
        """
        # 测试空内容
        html = HtmlUtil.wrapHtml("")
        self.assertIn('<!DOCTYPE html>', html)
        self.assertIn('<body></body>', html)
        
        # 测试有内容
        html = HtmlUtil.wrapHtml("<p>hello</p>", "Test Page")
        self.assertIn('<!DOCTYPE html>', html)
        self.assertIn('<title>Test Page</title>', html)
        self.assertIn('<body>', html)
        self.assertIn('<p>hello</p>', html)

    def test_createTag(self):
        """
        测试创建HTML标签
        """
        # 测试创建无属性无内容的标签
        tag = HtmlUtil.createTag("div")
        self.assertEqual(tag, '<div />')
        
        # 测试创建有属性无内容的标签
        tag = HtmlUtil.createTag("img", {"src": "test.jpg", "alt": "test"})
        self.assertIn('src="test.jpg"', tag)
        self.assertIn('alt="test"', tag)
        
        # 测试创建有属性有内容的标签
        tag = HtmlUtil.createTag("div", {"class": "test"}, "hello")
        self.assertIn('class="test"', tag)
        self.assertIn('hello', tag)

    def test_getTags(self):
        """
        测试获取HTML中指定标签的所有实例
        """
        # 测试空字符串
        self.assertEqual(HtmlUtil.getTags("", "div"), [])
        
        # 测试获取标签
        html = '<div>first</div><div>second</div>'
        tags = HtmlUtil.getTags(html, "div")
        self.assertEqual(len(tags), 2)
        self.assertIn('first', tags[0])
        self.assertIn('second', tags[1])

    def test_replaceTag(self):
        """
        测试替换HTML标签名
        """
        # 测试空字符串
        self.assertEqual(HtmlUtil.replaceTag("", "div", "span"), "")
        
        # 测试替换标签
        html = '<div>hello</div>'
        updated = HtmlUtil.replaceTag(html, "div", "span")
        self.assertEqual(updated, '<span>hello</span>')

    def test_addClass(self):
        """
        测试为HTML标签添加类
        """
        # 测试空字符串
        self.assertEqual(HtmlUtil.addClass("", "div", "test"), "")
        
        # 测试为无class属性的标签添加类
        html = '<div>hello</div>'
        updated = HtmlUtil.addClass(html, "div", "test")
        self.assertIn('class="test"', updated)
        
        # 测试为有class属性的标签添加类
        html = '<div class="old">hello</div>'
        updated = HtmlUtil.addClass(html, "div", "new")
        self.assertIn('class="old new"', updated)

    def test_removeClass(self):
        """
        测试从HTML标签移除类
        """
        # 测试空字符串
        self.assertEqual(HtmlUtil.removeClass("", "div", "test"), "")
        
        # 测试移除类
        html = '<div class="old new">hello</div>'
        updated = HtmlUtil.removeClass(html, "div", "old")
        self.assertIn('class="new"', updated)
        self.assertNotIn('old', updated)

    def test_getInnerHtml(self):
        """
        测试获取HTML标签的内部内容
        """
        # 测试空字符串
        self.assertIsNone(HtmlUtil.getInnerHtml("", "div"))
        
        # 测试获取内部内容
        html = '<div>hello <b>world</b></div>'
        inner = HtmlUtil.getInnerHtml(html, "div")
        self.assertEqual(inner, 'hello <b>world</b>')

    def test_setInnerHtml(self):
        """
        测试设置HTML标签的内部内容
        """
        # 测试空字符串
        self.assertEqual(HtmlUtil.setInnerHtml("", "div", "hello"), "")
        
        # 测试设置内部内容
        html = '<div>old content</div>'
        updated = HtmlUtil.setInnerHtml(html, "div", "new content")
        self.assertIn('new content', updated)
        self.assertNotIn('old content', updated)


if __name__ == '__main__':
    unittest.main()