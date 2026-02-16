"""AI工具模块"""
from typing import Any, Dict, Optional, List
import json
import requests


class AIUtils:
    """AI工具类"""

    class AIClient:
        """AI客户端基类"""

        def __init__(self, api_key: str, base_url: Optional[str] = None):
            """
            初始化AI客户端
            
            Args:
                api_key: API密钥
                base_url: 基础URL
            """
            self.api_key = api_key
            self.base_url = base_url

        def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
            """
            聊天完成
            
            Args:
                messages: 消息列表
                **kwargs: 其他参数
                
            Returns:
                str: 聊天响应
            """
            raise NotImplementedError

        def generate(self, prompt: str, **kwargs) -> str:
            """
            文本生成
            
            Args:
                prompt: 提示词
                **kwargs: 其他参数
                
            Returns:
                str: 生成的文本
            """
            raise NotImplementedError

    class OpenAIClient(AIClient):
        """OpenAI客户端"""

        def __init__(self, api_key: str, base_url: str = "https://api.openai.com/v1"):
            """
            初始化OpenAI客户端
            
            Args:
                api_key: API密钥
                base_url: 基础URL
            """
            super().__init__(api_key, base_url)

        def chat(self, messages: List[Dict[str, str]], model: str = "gpt-3.5-turbo", **kwargs) -> str:
            """
            聊天完成
            
            Args:
                messages: 消息列表
                model: 模型名称
                **kwargs: 其他参数
                
            Returns:
                str: 聊天响应
            """
            url = f"{self.base_url}/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": model,
                "messages": messages,
                **kwargs
            }
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]

        def generate(self, prompt: str, model: str = "gpt-3.5-turbo", **kwargs) -> str:
            """
            文本生成
            
            Args:
                prompt: 提示词
                model: 模型名称
                **kwargs: 其他参数
                
            Returns:
                str: 生成的文本
            """
            messages = [{"role": "user", "content": prompt}]
            return self.chat(messages, model, **kwargs)

    class DeepSeekClient(AIClient):
        """DeepSeek客户端"""

        def __init__(self, api_key: str, base_url: str = "https://api.deepseek.com/v1"):
            """
            初始化DeepSeek客户端
            
            Args:
                api_key: API密钥
                base_url: 基础URL
            """
            super().__init__(api_key, base_url)

        def chat(self, messages: List[Dict[str, str]], model: str = "deepseek-chat", **kwargs) -> str:
            """
            聊天完成
            
            Args:
                messages: 消息列表
                model: 模型名称
                **kwargs: 其他参数
                
            Returns:
                str: 聊天响应
            """
            url = f"{self.base_url}/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": model,
                "messages": messages,
                **kwargs
            }
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]

        def generate(self, prompt: str, model: str = "deepseek-chat", **kwargs) -> str:
            """
            文本生成
            
            Args:
                prompt: 提示词
                model: 模型名称
                **kwargs: 其他参数
                
            Returns:
                str: 生成的文本
            """
            messages = [{"role": "user", "content": prompt}]
            return self.chat(messages, model, **kwargs)

    class DoubaoClient(AIClient):
        """豆包客户端"""

        def __init__(self, api_key: str, base_url: str = "https://ark.cn-beijing.volces.com/api/v3"):
            """
            初始化豆包客户端
            
            Args:
                api_key: API密钥
                base_url: 基础URL
            """
            super().__init__(api_key, base_url)

        def chat(self, messages: List[Dict[str, str]], model: str = "ep-20240216172343-6l96v", **kwargs) -> str:
            """
            聊天完成
            
            Args:
                messages: 消息列表
                model: 模型名称
                **kwargs: 其他参数
                
            Returns:
                str: 聊天响应
            """
            url = f"{self.base_url}/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": model,
                "messages": messages,
                **kwargs
            }
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]

        def generate(self, prompt: str, model: str = "ep-20240216172343-6l96v", **kwargs) -> str:
            """
            文本生成
            
            Args:
                prompt: 提示词
                model: 模型名称
                **kwargs: 其他参数
                
            Returns:
                str: 生成的文本
            """
            messages = [{"role": "user", "content": prompt}]
            return self.chat(messages, model, **kwargs)

    @staticmethod
    def create_openai_client(api_key: str, base_url: Optional[str] = None) -> OpenAIClient:
        """
        创建OpenAI客户端
        
        Args:
            api_key: API密钥
            base_url: 基础URL
            
        Returns:
            OpenAIClient: OpenAI客户端实例
        """
        return AIUtils.OpenAIClient(api_key, base_url)

    @staticmethod
    def create_deepseek_client(api_key: str, base_url: Optional[str] = None) -> DeepSeekClient:
        """
        创建DeepSeek客户端
        
        Args:
            api_key: API密钥
            base_url: 基础URL
            
        Returns:
            DeepSeekClient: DeepSeek客户端实例
        """
        return AIUtils.DeepSeekClient(api_key, base_url)

    @staticmethod
    def create_doubao_client(api_key: str, base_url: Optional[str] = None) -> DoubaoClient:
        """
        创建豆包客户端
        
        Args:
            api_key: API密钥
            base_url: 基础URL
            
        Returns:
            DoubaoClient: 豆包客户端实例
        """
        return AIUtils.DoubaoClient(api_key, base_url)

    @staticmethod
    def chat(api_key: str, model: str, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        一行代码调用聊天
        
        Args:
            api_key: API密钥
            model: 模型名称
            messages: 消息列表
            **kwargs: 其他参数
            
        Returns:
            str: 聊天响应
        """
        if model.startswith("gpt"):
            client = AIUtils.create_openai_client(api_key)
        elif model.startswith("deepseek"):
            client = AIUtils.create_deepseek_client(api_key)
        elif model.startswith("doubao") or model.startswith("ep-"):
            client = AIUtils.create_doubao_client(api_key)
        else:
            raise ValueError(f"Unsupported model: {model}")
        return client.chat(messages, model, **kwargs)

    @staticmethod
    def generate(api_key: str, model: str, prompt: str, **kwargs) -> str:
        """
        一行代码调用文本生成
        
        Args:
            api_key: API密钥
            model: 模型名称
            prompt: 提示词
            **kwargs: 其他参数
            
        Returns:
            str: 生成的文本
        """
        if model.startswith("gpt"):
            client = AIUtils.create_openai_client(api_key)
        elif model.startswith("deepseek"):
            client = AIUtils.create_deepseek_client(api_key)
        elif model.startswith("doubao") or model.startswith("ep-"):
            client = AIUtils.create_doubao_client(api_key)
        else:
            raise ValueError(f"Unsupported model: {model}")
        return client.generate(prompt, model, **kwargs)
