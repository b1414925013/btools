"""国际化工具类"""
import os
import json
import yaml
from typing import Any, Dict, Optional, List


try:
    import gettext
    HAS_GETTEXT = True
except ImportError:
    HAS_GETTEXT = False


class I18nUtils:
    """国际化工具类"""

    _translations: Dict[str, Dict[str, str]] = {}
    _current_locale: str = 'en'

    @staticmethod
    def load_translations(translations_or_directory: Any) -> bool:
        """
        加载翻译
        
        支持两种调用方式：
        1. load_translations(directory) - 从目录加载翻译文件
        2. load_translations(translations_dict) - 从字典加载翻译
        
        Args:
            translations_or_directory: 翻译字典或翻译文件目录
            
        Returns:
            bool: 如果加载成功则返回True，否则返回False
        """
        try:
            # 从字典加载翻译
            if isinstance(translations_or_directory, dict):
                I18nUtils._translations.update(translations_or_directory)
                return True
            # 从目录加载翻译文件
            elif isinstance(translations_or_directory, str):
                directory = translations_or_directory
                for filename in os.listdir(directory):
                    if filename.endswith('.json'):
                        locale = filename[:-5]  # 去掉.json后缀
                        file_path = os.path.join(directory, filename)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            translations = json.load(f)
                            I18nUtils._translations[locale] = translations
                    elif filename.endswith('.yaml') or filename.endswith('.yml'):
                        locale = filename[:-5] if filename.endswith('.yaml') else filename[:-4]  # 去掉后缀
                        file_path = os.path.join(directory, filename)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            translations = yaml.safe_load(f)
                            I18nUtils._translations[locale] = translations
                return True
            return False
        except Exception:
            return False

    @staticmethod
    def set_locale(locale: str) -> None:
        """
        设置当前语言
        
        Args:
            locale: 语言代码，如 'zh_CN', 'en_US'
        """
        I18nUtils._current_locale = locale

    @staticmethod
    def get_locale() -> str:
        """
        获取当前语言
        
        Returns:
            str: 当前语言代码
        """
        return I18nUtils._current_locale

    @staticmethod
    def get(key: str, locale: Optional[str] = None, default: str = '') -> str:
        """
        获取翻译
        
        Args:
            key: 翻译键
            locale: 语言代码，默认为None（使用当前语言）
            default: 默认值
            
        Returns:
            str: 翻译后的文本
        """
        if locale is None:
            locale = I18nUtils._current_locale
        
        # 尝试使用完全匹配的语言
        translations = I18nUtils._translations.get(locale)
        if not translations:
            # 尝试使用语言的前缀（例如，当找不到'zh_CN'时，尝试使用'zh'）
            if '_' in locale:
                lang_prefix = locale.split('_')[0]
                translations = I18nUtils._translations.get(lang_prefix)
        
        if translations:
            # 支持嵌套键，如 'user.name'
            keys = key.split('.')
            value = translations
            for k in keys:
                if isinstance(value, dict) and k in value:
                    value = value[k]
                else:
                    return default
            return str(value)
        return default

    @staticmethod
    def translate(key: str, **kwargs) -> str:
        """
        翻译并格式化文本
        
        Args:
            key: 翻译键
            **kwargs: 格式化参数
            
        Returns:
            str: 翻译并格式化后的文本
        """
        text = I18nUtils.get(key)
        if kwargs:
            try:
                return text.format(**kwargs)
            except Exception:
                return text
        return text

    @staticmethod
    def add_translation(locale: str, key: str, value: str) -> None:
        """
        添加翻译
        
        Args:
            locale: 语言代码
            key: 翻译键
            value: 翻译值
        """
        if locale not in I18nUtils._translations:
            I18nUtils._translations[locale] = {}
        
        # 支持嵌套键，如 'user.name'
        keys = key.split('.')
        translations = I18nUtils._translations[locale]
        
        for k in keys[:-1]:
            if k not in translations:
                translations[k] = {}
            translations = translations[k]
        
        translations[keys[-1]] = value

    @staticmethod
    def remove_translation(locale: str, key: str) -> None:
        """
        删除翻译
        
        Args:
            locale: 语言代码
            key: 翻译键
        """
        if locale in I18nUtils._translations:
            # 支持嵌套键，如 'user.name'
            keys = key.split('.')
            translations = I18nUtils._translations[locale]
            
            for k in keys[:-1]:
                if k not in translations:
                    return
                translations = translations[k]
            
            if keys[-1] in translations:
                del translations[keys[-1]]

    @staticmethod
    def get_supported_locales() -> List[str]:
        """
        获取支持的语言列表
        
        Returns:
            List[str]: 支持的语言代码列表
        """
        return list(I18nUtils._translations.keys())

    @staticmethod
    def is_locale_supported(locale: str) -> bool:
        """
        检查语言是否支持
        
        Args:
            locale: 语言代码
            
        Returns:
            bool: 如果语言支持则返回True，否则返回False
        """
        return locale in I18nUtils._translations

    @staticmethod
    def save_translations(directory: str) -> bool:
        """
        保存翻译到文件
        
        Args:
            directory: 保存目录
            
        Returns:
            bool: 如果保存成功则返回True，否则返回False
        """
        try:
            os.makedirs(directory, exist_ok=True)
            
            for locale, translations in I18nUtils._translations.items():
                file_path = os.path.join(directory, f'{locale}.json')
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(translations, f, ensure_ascii=False, indent=2)
            return True
        except Exception:
            return False

    @staticmethod
    def load_gettext_translations(domain: str, localedir: str) -> bool:
        """
        加载gettext翻译
        
        Args:
            domain: 翻译域
            localedir: 翻译文件目录
            
        Returns:
            bool: 如果加载成功则返回True，否则返回False
        """
        if not HAS_GETTEXT:
            return False
        
        try:
            import gettext
            gettext.bindtextdomain(domain, localedir)
            gettext.textdomain(domain)
            return True
        except Exception:
            return False

    @staticmethod
    def gettext(key: str) -> str:
        """
        使用gettext获取翻译
        
        Args:
            key: 翻译键
            
        Returns:
            str: 翻译后的文本
        """
        if HAS_GETTEXT:
            import gettext
            return gettext.gettext(key)
        return key

    @staticmethod
    def ngettext(singular: str, plural: str, n: int) -> str:
        """
        使用gettext获取复数翻译
        
        Args:
            singular: 单数形式
            plural: 复数形式
            n: 数量
            
        Returns:
            str: 翻译后的文本
        """
        if HAS_GETTEXT:
            import gettext
            return gettext.ngettext(singular, plural, n)
        return plural if n != 1 else singular

    @staticmethod
    def format_number(number: int, locale: Optional[str] = None) -> str:
        """
        格式化数字
        
        Args:
            number: 数字
            locale: 语言代码，默认为None（使用当前语言）
            
        Returns:
            str: 格式化后的数字
        """
        # 简单实现，实际应该根据语言使用不同的格式化规则
        return f"{number:,}"

    @staticmethod
    def format_currency(amount: float, currency: str = 'CNY', locale: Optional[str] = None) -> str:
        """
        格式化货币
        
        Args:
            amount: 金额
            currency: 货币代码
            locale: 语言代码，默认为None（使用当前语言）
            
        Returns:
            str: 格式化后的货币
        """
        # 简单实现，实际应该根据语言和货币使用不同的格式化规则
        if currency == 'CNY':
            return f"¥{amount:.2f}"
        elif currency == 'USD':
            return f"${amount:.2f}"
        elif currency == 'EUR':
            return f"€{amount:.2f}"
        return f"{currency} {amount:.2f}"

    @staticmethod
    def format_percent(value: float, locale: Optional[str] = None) -> str:
        """
        格式化百分比
        
        Args:
            value: 百分比值（0-100）
            locale: 语言代码，默认为None（使用当前语言）
            
        Returns:
            str: 格式化后的百分比
        """
        # 简单实现，实际应该根据语言使用不同的格式化规则
        return f"{value:.2f}%"

    @staticmethod
    def get_language_name(locale: str, target_locale: Optional[str] = None) -> str:
        """
        获取语言名称
        
        Args:
            locale: 语言代码
            target_locale: 目标语言代码，默认为None（使用当前语言）
            
        Returns:
            str: 语言名称
        """
        language_names = {
            'zh_CN': {'zh_CN': '中文（简体）', 'en_US': 'Chinese (Simplified)'},
            'zh_TW': {'zh_CN': '中文（繁体）', 'en_US': 'Chinese (Traditional)'},
            'en_US': {'zh_CN': '英语（美国）', 'en_US': 'English (US)'},
            'en_GB': {'zh_CN': '英语（英国）', 'en_US': 'English (UK)'},
            'ja_JP': {'zh_CN': '日语', 'en_US': 'Japanese'},
            'ko_KR': {'zh_CN': '韩语', 'en_US': 'Korean'},
            'fr_FR': {'zh_CN': '法语', 'en_US': 'French'},
            'de_DE': {'zh_CN': '德语', 'en_US': 'German'},
            'es_ES': {'zh_CN': '西班牙语', 'en_US': 'Spanish'},
            'ru_RU': {'zh_CN': '俄语', 'en_US': 'Russian'}
        }
        
        if target_locale is None:
            target_locale = I18nUtils._current_locale
        
        if locale in language_names:
            return language_names[locale].get(target_locale, locale)
        return locale

    @staticmethod
    def clear_translations() -> None:
        """
        清空翻译
        """
        I18nUtils._translations.clear()

    @staticmethod
    def get_translations(locale: Optional[str] = None) -> Dict[str, str]:
        """
        获取指定语言的所有翻译
        
        Args:
            locale: 语言代码，默认为None（使用当前语言）
            
        Returns:
            Dict[str, str]: 翻译字典
        """
        if locale is None:
            locale = I18nUtils._current_locale
        return I18nUtils._translations.get(locale, {})

    @staticmethod
    def has_translation(key: str, locale: Optional[str] = None) -> bool:
        """
        检查是否有翻译
        
        Args:
            key: 翻译键
            locale: 语言代码，默认为None（使用当前语言）
            
        Returns:
            bool: 如果有翻译则返回True，否则返回False
        """
        return I18nUtils.get(key, locale=locale, default=None) is not None