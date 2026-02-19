import json
import yaml
import os

class Config:
    """
    配置管理类，支持JSON和YAML格式的配置文件读写
    
    Attributes:
        config_path (str): 配置文件路径
        config_data (dict): 配置数据
    """
    
    def __init__(self, config_path):
        """
        初始化Config实例
        
        Args:
            config_path (str): 配置文件路径
        """
        self.config_path = config_path
        self.config_data = {}
        
        # 如果配置文件存在，加载配置
        if os.path.exists(config_path):
            self.load()
    
    def load(self):
        """
        加载配置文件
        
        Raises:
            ValueError: 如果文件格式不支持
        """
        ext = os.path.splitext(self.config_path)[1].lower()
        
        with open(self.config_path, 'r', encoding='utf-8') as f:
            if ext == '.json':
                self.config_data = json.load(f)
            elif ext in ['.yaml', '.yml']:
                self.config_data = yaml.safe_load(f)
            else:
                raise ValueError(f"Unsupported config file format: {ext}")
    
    def save(self):
        """
        保存配置文件
        
        Raises:
            ValueError: 如果文件格式不支持
        """
        ext = os.path.splitext(self.config_path)[1].lower()
        
        # 确保目录存在
        os.makedirs(os.path.dirname(self.config_path) if os.path.dirname(self.config_path) else '.', exist_ok=True)
        
        with open(self.config_path, 'w', encoding='utf-8') as f:
            if ext == '.json':
                json.dump(self.config_data, f, indent=2, ensure_ascii=False)
            elif ext in ['.yaml', '.yml']:
                yaml.dump(self.config_data, f, default_flow_style=False, allow_unicode=True)
            else:
                raise ValueError(f"Unsupported config file format: {ext}")
    
    def get(self, key, default=None):
        """
        获取配置值
        
        Args:
            key (str): 配置键，支持点号分隔的嵌套键，如 "database.host"
            default: 默认值，如果键不存在则返回
            
        Returns:
            配置值或默认值
        """
        keys = key.split('.')
        value = self.config_data
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key, value):
        """
        设置配置值
        
        Args:
            key (str): 配置键，支持点号分隔的嵌套键，如 "database.host"
            value: 配置值
        """
        keys = key.split('.')
        config = self.config_data
        
        # 遍历键，创建嵌套字典（如果不存在）
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        # 设置最终值
        config[keys[-1]] = value
    
    def remove(self, key):
        """
        删除配置项
        
        Args:
            key (str): 配置键，支持点号分隔的嵌套键，如 "database.host"
        """
        keys = key.split('.')
        config = self.config_data
        
        # 遍历键，找到父字典
        for k in keys[:-1]:
            if isinstance(config, dict) and k in config:
                config = config[k]
            else:
                return
        
        # 删除键
        if isinstance(config, dict) and keys[-1] in config:
            del config[keys[-1]]
