"""模板工具类"""
import os
import re
from typing import Dict, Any, Optional, Callable


try:
    import jinja2
    HAS_JINJA2 = True
except ImportError:
    HAS_JINJA2 = False


class TemplateUtils:
    """模板工具类"""

    @staticmethod
    def render_template(template: str, variables: Dict[str, Any]) -> str:
        """
        渲染简单模板
        
        Args:
            template: 模板字符串
            variables: 变量字典
            
        Returns:
            str: 渲染后的字符串
        """
        result = template
        for key, value in variables.items():
            # 处理带空格的模板变量格式，如 {{ name }}
            result = re.sub(r'\{\{\s*' + re.escape(key) + r'\s*\}\}', str(value), result)
        return result

    @staticmethod
    def render_template_from_file(file_path: str, variables: Dict[str, Any]) -> Optional[str]:
        """
        从文件渲染模板
        
        Args:
            file_path: 模板文件路径
            variables: 变量字典
            
        Returns:
            Optional[str]: 渲染后的字符串，如果文件不存在则返回None
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                template = f.read()
            return TemplateUtils.render_template(template, variables)
        except Exception:
            return None

    @staticmethod
    def render_jinja2_template(template: str, variables: Dict[str, Any]) -> Optional[str]:
        """
        使用Jinja2渲染模板
        
        Args:
            template: 模板字符串
            variables: 变量字典
            
        Returns:
            Optional[str]: 渲染后的字符串，如果Jinja2不可用则返回None
        """
        if not HAS_JINJA2:
            return None
        try:
            from jinja2 import Template
            jinja_template = Template(template)
            return jinja_template.render(**variables)
        except Exception:
            return None

    @staticmethod
    def render_jinja2_template_from_file(file_path: str, variables: Dict[str, Any]) -> Optional[str]:
        """
        使用Jinja2从文件渲染模板
        
        Args:
            file_path: 模板文件路径
            variables: 变量字典
            
        Returns:
            Optional[str]: 渲染后的字符串，如果文件不存在或Jinja2不可用则返回None
        """
        if not HAS_JINJA2:
            return None
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                template = f.read()
            return TemplateUtils.render_jinja2_template(template, variables)
        except Exception:
            return None

    @staticmethod
    def create_template_loader(search_path: str) -> Optional[Any]:
        """
        创建Jinja2模板加载器
        
        Args:
            search_path: 模板搜索路径
            
        Returns:
            Optional[Any]: Jinja2模板加载器，如果Jinja2不可用则返回None
        """
        if not HAS_JINJA2:
            return None
        try:
            from jinja2 import FileSystemLoader, Environment
            loader = FileSystemLoader(search_path)
            return Environment(loader=loader)
        except Exception:
            return None

    @staticmethod
    def get_template_variables(template: str) -> list:
        """
        提取模板中的变量
        
        Args:
            template: 模板字符串
            
        Returns:
            list: 变量名列表
        """
        # 提取{{variable}}格式的变量
        pattern = r'\{\{([^}]+)\}\}'
        matches = re.findall(pattern, template)
        variables = []
        for match in matches:
            var_name = match.strip()
            if var_name and var_name not in variables:
                variables.append(var_name)
        return variables

    @staticmethod
    def get_template_variables_from_file(file_path: str) -> list:
        """
        从文件提取模板中的变量
        
        Args:
            file_path: 模板文件路径
            
        Returns:
            list: 变量名列表
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                template = f.read()
            return TemplateUtils.get_template_variables(template)
        except Exception:
            return []

    @staticmethod
    def validate_template(template: str, required_variables: list) -> bool:
        """
        验证模板是否包含所有必需的变量
        
        Args:
            template: 模板字符串
            required_variables: 必需的变量列表
            
        Returns:
            bool: 如果模板包含所有必需的变量则返回True，否则返回False
        """
        template_variables = TemplateUtils.get_template_variables(template)
        for var in required_variables:
            if var not in template_variables:
                return False
        return True

    @staticmethod
    def validate_template_from_file(file_path: str, required_variables: list) -> bool:
        """
        从文件验证模板是否包含所有必需的变量
        
        Args:
            file_path: 模板文件路径
            required_variables: 必需的变量列表
            
        Returns:
            bool: 如果模板包含所有必需的变量则返回True，否则返回False
        """
        template_variables = TemplateUtils.get_template_variables_from_file(file_path)
        for var in required_variables:
            if var not in template_variables:
                return False
        return True

    @staticmethod
    def escape_html(text: str) -> str:
        """
        转义HTML特殊字符
        
        Args:
            text: 要转义的文本
            
        Returns:
            str: 转义后的文本
        """
        html_escape_table = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#39;'
        }
        return ''.join(html_escape_table.get(c, c) for c in text)

    @staticmethod
    def unescape_html(text: str) -> str:
        """
        反转义HTML特殊字符
        
        Args:
            text: 要反转义的文本
            
        Returns:
            str: 反转义后的文本
        """
        html_unescape_table = {
            '&amp;': '&',
            '&lt;': '<',
            '&gt;': '>',
            '&quot;': '"',
            '&#39;': "'"
        }
        for escape_seq, char in html_unescape_table.items():
            text = text.replace(escape_seq, char)
        return text

    @staticmethod
    def render_template_with_filters(
        template: str, 
        variables: Dict[str, Any], 
        filters: Dict[str, Callable]
    ) -> str:
        """
        使用自定义过滤器渲染模板
        
        Args:
            template: 模板字符串
            variables: 变量字典
            filters: 过滤器字典
            
        Returns:
            str: 渲染后的字符串
        """
        result = template
        
        # 提取带过滤器的变量，如 {{var|filter}}
        pattern = r'\{\{([^}]+)\}\}'
        matches = re.findall(pattern, template)
        
        for match in matches:
            expr = match.strip()
            if '|' in expr:
                var_part, filter_part = expr.split('|', 1)
                var_name = var_part.strip()
                filter_name = filter_part.strip()
                
                if var_name in variables and filter_name in filters:
                    value = variables[var_name]
                    filtered_value = filters[filter_name](value)
                    result = result.replace(f'{{{{{expr}}}}}', str(filtered_value))
            else:
                var_name = expr
                if var_name in variables:
                    result = result.replace(f'{{{{{expr}}}}}', str(variables[var_name]))
        
        return result

    @staticmethod
    def render_template_with_conditions(
        template: str, 
        variables: Dict[str, Any]
    ) -> str:
        """
        渲染带条件的模板
        
        Args:
            template: 模板字符串
            variables: 变量字典
            
        Returns:
            str: 渲染后的字符串
        """
        result = template
        
        # 处理 {% if condition %}...{% endif %} 条件
        pattern = r'\{%\s*if\s+([^%]+)\s*%\}([\s\S]*?)\{%\s*endif\s*%\}'
        
        def replace_condition(match):
            condition = match.group(1).strip()
            content = match.group(2)
            
            # 简单条件处理，支持变量存在性检查
            if condition in variables:
                if variables[condition]:
                    return content
                else:
                    return ''
            return ''
        
        result = re.sub(pattern, replace_condition, result)
        
        # 处理变量替换
        for key, value in variables.items():
            result = result.replace(f'{{{{{key}}}}}', str(value))
        
        return result

    @staticmethod
    def render_template_with_loops(
        template: str, 
        variables: Dict[str, Any]
    ) -> str:
        """
        渲染带循环的模板
        
        Args:
            template: 模板字符串
            variables: 变量字典
            
        Returns:
            str: 渲染后的字符串
        """
        result = template
        
        # 处理 {% for item in list %}...{% endfor %} 循环
        pattern = r'\{%\s*for\s+([^\s]+)\s+in\s+([^%]+)\s*%\}([\s\S]*?)\{%\s*endfor\s*%\}'
        
        def replace_loop(match):
            item_var = match.group(1).strip()
            list_var = match.group(2).strip()
            content = match.group(3)
            
            if list_var in variables:
                items = variables[list_var]
                if isinstance(items, (list, tuple)):
                    loop_content = ''
                    for item in items:
                        item_content = content
                        item_content = item_content.replace(f'{{{{{item_var}}}}}', str(item))
                        loop_content += item_content
                    return loop_content
            return ''
        
        result = re.sub(pattern, replace_loop, result)
        
        # 处理变量替换
        for key, value in variables.items():
            result = result.replace(f'{{{{{key}}}}}', str(value))
        
        return result

    @staticmethod
    def save_rendered_template(template: str, variables: Dict[str, Any], output_path: str) -> bool:
        """
        渲染模板并保存到文件
        
        Args:
            template: 模板字符串
            variables: 变量字典
            output_path: 输出文件路径
            
        Returns:
            bool: 如果保存成功则返回True，否则返回False
        """
        try:
            rendered = TemplateUtils.render_template(template, variables)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(rendered)
            return True
        except Exception:
            return False

    @staticmethod
    def save_rendered_template_from_file(
        file_path: str, 
        variables: Dict[str, Any], 
        output_path: str
    ) -> bool:
        """
        从文件渲染模板并保存到文件
        
        Args:
            file_path: 模板文件路径
            variables: 变量字典
            output_path: 输出文件路径
            
        Returns:
            bool: 如果保存成功则返回True，否则返回False
        """
        try:
            rendered = TemplateUtils.render_template_from_file(file_path, variables)
            if rendered:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(rendered)
                return True
            return False
        except Exception:
            return False

    @staticmethod
    def has_jinja2() -> bool:
        """
        检查是否安装了Jinja2
        
        Returns:
            bool: 如果安装了Jinja2则返回True，否则返回False
        """
        return HAS_JINJA2

    @staticmethod
    def get_template_engine() -> str:
        """
        获取可用的模板引擎
        
        Returns:
            str: 模板引擎名称
        """
        if HAS_JINJA2:
            return 'jinja2'
        return 'simple'

    @staticmethod
    def create_simple_template_engine() -> Callable:
        """
        创建简单模板引擎
        
        Returns:
            Callable: 模板渲染函数
        """
        def render(template, **kwargs):
            return TemplateUtils.render_template(template, kwargs)
        return render