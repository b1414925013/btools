import requests
import os
from typing import Dict, Optional, Any, Union, Tuple, List

class HTTPClient:
    """
    HTTP客户端类，基于requests库实现
    
    Attributes:
        base_url (str): 基础URL
        headers (dict): 默认请求头
        timeout (int): 请求超时时间（秒）
        session (requests.Session): 请求会话
    """
    
    def __init__(self, base_url: str = "", headers: Optional[Dict[str, str]] = None, timeout: int = 30,
                 use_cache: bool = False, cache_name: str = "http_cache", cache_backend: str = "memory",
                 retry_enabled: bool = False, retry_total: int = 3, retry_backoff_factor: float = 0.1):
        """
        初始化HTTPClient实例
        
        Args:
            base_url (str): 基础URL
            headers (dict): 默认请求头
            timeout (int): 请求超时时间（秒）
            use_cache (bool): 是否使用缓存
            cache_name (str): 缓存名称
            cache_backend (str): 缓存后端，可选值：memory, sqlite, redis, mongodb等
            retry_enabled (bool): 是否启用重试
            retry_total (int): 最大重试次数
            retry_backoff_factor (float): 重试退避因子
        """
        self.base_url = base_url
        self.headers = headers or {}
        self.timeout = timeout
        
        # 初始化会话
        if use_cache:
            from requests_cache import CachedSession
            self.session = CachedSession(
                cache_name=cache_name,
                backend=cache_backend
            )
        else:
            self.session = requests.Session()
        
        self.session.headers.update(self.headers)
        
        # 配置重试机制
        if retry_enabled:
            from urllib3.util.retry import Retry
            from requests.adapters import HTTPAdapter
            
            retry = Retry(
                total=retry_total,
                backoff_factor=retry_backoff_factor,
                status_forcelist=[429, 500, 502, 503, 504],
                allowed_methods=["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE", "POST", "PATCH"]
            )
            adapter = HTTPAdapter(max_retries=retry)
            self.session.mount("http://", adapter)
            self.session.mount("https://", adapter)
    
    def add_headers(self, headers: Dict[str, str]) -> 'HTTPClient':
        """
        添加请求头（保留原有的请求头）
        
        Args:
            headers (dict): 要添加的请求头
            
        Returns:
            HTTPClient: 返回自身，支持链式调用
        """
        self.headers.update(headers)
        self.session.headers.update(headers)
        return self
    
    def set_headers(self, headers: Dict[str, str]) -> 'HTTPClient':
        """
        设置请求头（替换原有的所有请求头）
        
        Args:
            headers (dict): 要设置的请求头
            
        Returns:
            HTTPClient: 返回自身，支持链式调用
        """
        self.headers = headers.copy()
        self.session.headers.clear()
        self.session.headers.update(self.headers)
        return self
    
    def clear_headers(self) -> 'HTTPClient':
        """
        清空所有请求头
        
        Returns:
            HTTPClient: 返回自身，支持链式调用
        """
        self.headers = {}
        self.session.headers.clear()
        return self
    
    def get(self, url: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, **kwargs) -> requests.Response:
        """
        发送GET请求
        
        Args:
            url (str): 请求URL
            params (dict): URL参数
            headers (dict): 请求头
            **kwargs: 其他requests参数
            
        Returns:
            requests.Response: 响应对象
        """
        full_url = self._build_url(url, params)
        headers = self._merge_headers(headers)
        return self.session.get(full_url, headers=headers, timeout=self.timeout, **kwargs)
    
    def post(self, url: str, data: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None, 
             params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, **kwargs) -> requests.Response:
        """
        发送POST请求
        
        Args:
            url (str): 请求URL
            data (dict): 表单数据
            json (dict): JSON数据
            params (dict): URL参数
            headers (dict): 请求头
            **kwargs: 其他requests参数
            
        Returns:
            requests.Response: 响应对象
        """
        full_url = self._build_url(url, params)
        headers = self._merge_headers(headers)
        return self.session.post(full_url, data=data, json=json, headers=headers, timeout=self.timeout, **kwargs)
    
    def put(self, url: str, data: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, **kwargs) -> requests.Response:
        """
        发送PUT请求
        
        Args:
            url (str): 请求URL
            data (dict): 表单数据
            json (dict): JSON数据
            params (dict): URL参数
            headers (dict): 请求头
            **kwargs: 其他requests参数
            
        Returns:
            requests.Response: 响应对象
        """
        full_url = self._build_url(url, params)
        headers = self._merge_headers(headers)
        return self.session.put(full_url, data=data, json=json, headers=headers, timeout=self.timeout, **kwargs)
    
    def patch(self, url: str, data: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None,
              params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, **kwargs) -> requests.Response:
        """
        发送PATCH请求
        
        Args:
            url (str): 请求URL
            data (dict): 表单数据
            json (dict): JSON数据
            params (dict): URL参数
            headers (dict): 请求头
            **kwargs: 其他requests参数
            
        Returns:
            requests.Response: 响应对象
        """
        full_url = self._build_url(url, params)
        headers = self._merge_headers(headers)
        return self.session.patch(full_url, data=data, json=json, headers=headers, timeout=self.timeout, **kwargs)
    
    def delete(self, url: str, params: Optional[Dict[str, Any]] = None, 
               headers: Optional[Dict[str, str]] = None, **kwargs) -> requests.Response:
        """
        发送DELETE请求
        
        Args:
            url (str): 请求URL
            params (dict): URL参数
            headers (dict): 请求头
            **kwargs: 其他requests参数
            
        Returns:
            requests.Response: 响应对象
        """
        full_url = self._build_url(url, params)
        headers = self._merge_headers(headers)
        return self.session.delete(full_url, headers=headers, timeout=self.timeout, **kwargs)
    
    def upload_file(self, url: str, file_path: str, field_name: str = 'file', 
                    params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None,
                    form_data: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        """
        上传文件（使用requests-toolbelt库）
        
        Args:
            url (str): 请求URL
            file_path (str): 本地文件路径
            field_name (str): 表单字段名，默认为'file'
            params (dict): URL参数
            headers (dict): 请求头
            form_data (dict): 其他表单数据
            **kwargs: 其他requests参数
            
        Returns:
            requests.Response: 响应对象
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")
        
        from requests_toolbelt.multipart.encoder import MultipartEncoder
        
        # 构建表单数据
        data = form_data.copy() if form_data else {}
        # 添加文件到表单数据
        file_name = os.path.basename(file_path)
        data[field_name] = (file_name, open(file_path, 'rb'), 'application/octet-stream')
        
        # 创建MultipartEncoder
        encoder = MultipartEncoder(fields=data)
        
        try:
            full_url = self._build_url(url, params)
            # 合并请求头，添加Content-Type
            merged_headers = self._merge_headers(headers)
            merged_headers['Content-Type'] = encoder.content_type
            
            return self.session.post(
                full_url, 
                data=encoder, 
                headers=merged_headers, 
                timeout=self.timeout, 
                **kwargs
            )
        finally:
            # 关闭文件
            for key, value in data.items():
                if isinstance(value, tuple) and len(value) == 3:
                    try:
                        value[1].close()
                    except:
                        pass
    
    def download_file(self, url: str, save_path: str, params: Optional[Dict[str, Any]] = None,
                      headers: Optional[Dict[str, str]] = None, chunk_size: int = 8192, **kwargs) -> str:
        """
        下载文件
        
        Args:
            url (str): 请求URL
            save_path (str): 保存文件的路径
            params (dict): URL参数
            headers (dict): 请求头
            chunk_size (int): 下载块大小，默认为8192字节
            **kwargs: 其他requests参数
            
        Returns:
            str: 保存的文件路径
        """
        full_url = self._build_url(url, params)
        headers = self._merge_headers(headers)
        
        response = self.session.get(full_url, headers=headers, timeout=self.timeout, stream=True, **kwargs)
        response.raise_for_status()
        
        os.makedirs(os.path.dirname(save_path) if os.path.dirname(save_path) else '.', exist_ok=True)
        
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
        
        return save_path
    
    def _build_url(self, url: str, params: Optional[Dict[str, Any]] = None) -> str:
        """
        构建完整的URL，支持路径参数替换
        
        Args:
            url (str): 相对或绝对URL，可包含路径参数如 /users/{user_id}
            params (dict): URL参数或路径参数
            
        Returns:
            str: 完整的URL
        """
        if url.startswith(('http://', 'https://')):
            full_url = url
        else:
            full_url = f"{self.base_url.rstrip('/')}/{url.lstrip('/')}"
        
        if params:
            path_params = {}
            query_params = {}
            
            for key, value in params.items():
                if '{' + key + '}' in full_url:
                    path_params[key] = value
                else:
                    query_params[key] = value
            
            for key, value in path_params.items():
                full_url = full_url.replace(f'{{{key}}}', str(value))
            
            if query_params:
                from urllib.parse import urlencode
                separator = '&' if '?' in full_url else '?'
                full_url = f"{full_url}{separator}{urlencode(query_params)}"
        
        return full_url
    
    def _merge_headers(self, headers: Optional[Dict[str, str]]) -> Dict[str, str]:
        """
        合并请求头
        
        Args:
            headers (dict): 请求头
            
        Returns:
            dict: 合并后的请求头
        """
        if not headers:
            return self.headers
        merged_headers = self.headers.copy()
        merged_headers.update(headers)
        return merged_headers
    
    def close(self):
        """
        关闭会话
        """
        self.session.close()
    
    def __enter__(self):
        """
        支持上下文管理器
        """
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        退出上下文管理器时关闭会话
        """
        self.close()
