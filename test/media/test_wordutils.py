"""测试WordUtils类"""
import unittest
import os
import tempfile
from btools.core.media.wordutils import WordUtils


class TestWordUtils(unittest.TestCase):
    """测试WordUtils类"""

    def setUp(self):
        """设置测试环境"""
        # 创建临时目录
        self.temp_dir = tempfile.mkdtemp()
        # 创建测试文档路径
        self.test_file = os.path.join(self.temp_dir, "test.docx")

    def tearDown(self):
        """清理测试环境"""
        # 删除临时文件
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        # 删除临时目录
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)

    def test_create_document(self):
        """测试创建新的Word文档"""
        doc = WordUtils.create_document()
        self.assertIsNotNone(doc)

    def test_save_and_open_document(self):
        """测试保存和打开Word文档"""
        # 创建文档
        doc = WordUtils.create_document()
        WordUtils.add_heading(doc, "测试文档", level=0)
        WordUtils.add_paragraph(doc, "这是一个测试文档")
        
        # 保存文档
        WordUtils.save_document(doc, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))
        
        # 打开文档
        opened_doc = WordUtils.open_document(self.test_file)
        self.assertIsNotNone(opened_doc)

    def test_add_heading(self):
        """测试添加标题"""
        doc = WordUtils.create_document()
        heading = WordUtils.add_heading(doc, "测试标题", level=1)
        self.assertIsNotNone(heading)

    def test_add_paragraph(self):
        """测试添加段落"""
        doc = WordUtils.create_document()
        paragraph = WordUtils.add_paragraph(doc, "测试段落")
        self.assertIsNotNone(paragraph)

    def test_add_table(self):
        """测试添加表格"""
        doc = WordUtils.create_document()
        table = WordUtils.add_table(doc, 2, 3)
        self.assertIsNotNone(table)

    def test_add_page_break(self):
        """测试添加分页符"""
        doc = WordUtils.create_document()
        WordUtils.add_paragraph(doc, "第一页")
        WordUtils.add_page_break(doc)
        WordUtils.add_paragraph(doc, "第二页")
        # 保存并验证文档存在
        WordUtils.save_document(doc, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_set_paragraph_alignment(self):
        """测试设置段落对齐方式"""
        doc = WordUtils.create_document()
        paragraph = WordUtils.add_paragraph(doc, "测试段落")
        WordUtils.set_paragraph_alignment(paragraph, "center")
        self.assertIsNotNone(paragraph)

    def test_create_table_from_data(self):
        """测试从数据创建表格"""
        doc = WordUtils.create_document()
        data = [
            ["1", "John", "30"],
            ["2", "Jane", "25"],
            ["3", "Bob", "35"]
        ]
        headers = ["ID", "Name", "Age"]
        table = WordUtils.create_table_from_data(doc, data, headers)
        self.assertIsNotNone(table)

    def test_read_document(self):
        """测试读取Word文档内容"""
        # 创建测试文档
        doc = WordUtils.create_document()
        WordUtils.add_heading(doc, "测试标题", level=1)
        WordUtils.add_paragraph(doc, "测试段落")
        data = [["1", "John"], ["2", "Jane"]]
        headers = ["ID", "Name"]
        WordUtils.create_table_from_data(doc, data, headers)
        WordUtils.save_document(doc, self.test_file)
        
        # 读取文档内容
        content = WordUtils.read_document(self.test_file)
        self.assertIsInstance(content, dict)
        self.assertIn('headings', content)
        self.assertIn('paragraphs', content)
        self.assertIn('tables', content)

    def test_set_page_orientation(self):
        """测试设置页面方向"""
        doc = WordUtils.create_document()
        WordUtils.set_page_orientation(doc, 'landscape')
        # 保存并验证文档存在
        WordUtils.save_document(doc, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_set_page_margins(self):
        """测试设置页面边距"""
        doc = WordUtils.create_document()
        WordUtils.set_page_margins(doc, top=1.5, bottom=1.5, left=1.5, right=1.5)
        # 保存并验证文档存在
        WordUtils.save_document(doc, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_create_simple_report(self):
        """测试创建简单的Word报告"""
        # 准备报告内容
        content = {
            'sections': [
                {
                    'title': '报告概述',
                    'content': '这是一份测试报告，用于测试WordUtils的功能。'
                },
                {
                    'title': '测试结果',
                    'content': '所有测试都已通过。'
                }
            ],
            'tables': [
                {
                    'title': '测试数据',
                    'headers': ['测试项', '状态'],
                    'data': [
                        ['功能1', '通过'],
                        ['功能2', '通过'],
                        ['功能3', '通过']
                    ]
                }
            ]
        }
        
        # 创建报告
        report_file = os.path.join(self.temp_dir, "report.docx")
        WordUtils.create_simple_report(report_file, "测试报告", content)
        
        # 验证报告存在
        self.assertTrue(os.path.exists(report_file))


if __name__ == "__main__":
    unittest.main()