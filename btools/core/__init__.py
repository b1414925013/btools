# Core module
# 基础工具类
from .basic.stringutils import StringUtils
from .basic.collectionutils import CollectionUtils
from .basic.arrayutils import ArrayUtils
from .basic.mathutils import MathUtils
from .basic.reflectutils import ReflectUtils
from .basic.exceptionutils import ExceptionUtils
from .basic.convertutils import Converter
from .basic.validatorutils import Validator
from .basic.beanutils import BeanUtils
from .basic.assertutils import AssertUtil

# 系统工具类
from .system.systemutils import SystemUtils
from .system.threadutils import ThreadUtils
from .scheduler.scheduleutils import ScheduleUtils

# 网络工具类
from .network.httputils import HTTPClient
from .network.sshutils import SSHClient
from .network.netutils import NetUtils
from .network.mailutils import MailUtils

# 数据处理类
from .data.fileutils import FileUtils
from .data.datetimeutils import DateTimeUtils
from .data.cryptoutils import CryptoUtils
from .data.databaseutils import DatabaseUtils
from .data.csvutils import CSVHandler
from .data.excelutils import ExcelHandler
from .data.encodeutils import EncodeUtils
from .data.regexutils import RegexUtils
from .data.xmlutils import XmlUtils
from .data.jsonutils import JSONUtils
from .data.jsonpathutils import JSONPathUtils
from .data.ioutils import IOUtils

# 媒体工具类
from .media.imageutils import ImageUtils
from .media.qrcodeutils import QrCodeUtils
from .media.compressutils import CompressUtils
from .media.captchautils import CaptchaUtils
# 可选导入WordUtils，因为它依赖python-docx
WordUtils = None
try:
    from .media.wordutils import WordUtils
except ImportError:
    pass

# 模板和国际化
from .template.templateutils import TemplateUtils
from .template.i18nutils import I18nUtils

# 缓存工具类
from .cache.cacheutils import CacheUtils

# 配置工具类
from .config.configutils import Config

# 日志工具类
from .log.logutils import Logger

# 自动化测试工具类
from .automation.seleniumutils import SeleniumUtils
from .automation.playwrightutils import PlaywrightUtils
from .automation.appiumutils import AppiumUtils
from .automation.fakerutils import FakerUtils

# AI工具类
from .ai.aiutils import AIUtils

# API工具类
from .api.fastapiutils import FastAPIUtils, APIResponse, APIErrorResponse

__all__ = [
    # 基础工具类
    'StringUtils',
    'CollectionUtils',
    'ArrayUtils',
    'MathUtils',
    'ReflectUtils',
    'ExceptionUtils',
    'Converter',
    'Validator',
    'BeanUtils',
    'AssertUtil',
    
    # 系统工具类
    'SystemUtils',
    'ThreadUtils',
    'ScheduleUtils',
    
    # 网络工具类
    'HTTPClient',
    'SSHClient',
    'NetUtils',
    'MailUtils',
    
    # 数据处理类
    'FileUtils',
    'DateTimeUtils',
    'CryptoUtils',
    'DatabaseUtils',
    'CSVHandler',
    'ExcelHandler',
    'EncodeUtils',
    'RegexUtils',
    'XmlUtils',
    'JSONUtils',
    'JSONPathUtils',
    'IOUtils',
    
    # 媒体工具类
    'ImageUtils',
    'QrCodeUtils',
    'CompressUtils',
    'CaptchaUtils',
    
    # 模板和国际化
    'TemplateUtils',
    'I18nUtils',
    
    # 缓存工具类
    'CacheUtils',
    
    # 配置工具类
    'Config',
    
    # 日志工具类
    'Logger',
    
    # 自动化测试工具类
    'SeleniumUtils',
    'PlaywrightUtils',
    'AppiumUtils',
    'FakerUtils',
    
    # AI工具类
    'AIUtils',
    
    # API工具类
    'FastAPIUtils',
    'APIResponse',
    'APIErrorResponse'
]
