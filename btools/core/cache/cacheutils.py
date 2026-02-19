"""缓存工具类"""
import time
import json
import os
from typing import Any, Optional, Dict, Union


class CacheUtils:
    """缓存工具类"""

    class MemoryCache:
        """内存缓存实现"""

        def __init__(self, default_ttl: int = 3600):
            """
            初始化内存缓存
            
            Args:
                default_ttl: 默认过期时间（秒）
            """
            self._cache: Dict[str, Dict[str, Any]] = {}
            self._default_ttl = default_ttl

        def get(self, key: str) -> Optional[Any]:
            """
            获取缓存值
            
            Args:
                key: 缓存键
                
            Returns:
                Any: 缓存值，如果不存在或已过期则返回None
            """
            if key not in self._cache:
                return None
            
            item = self._cache[key]
            if time.time() > item['expire_time']:
                del self._cache[key]
                return None
            
            return item['value']

        def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
            """
            设置缓存值
            
            Args:
                key: 缓存键
                value: 缓存值
                ttl: 过期时间（秒），如果为None则使用默认值
            """
            expire_time = time.time() + (ttl or self._default_ttl)
            self._cache[key] = {
                'value': value,
                'expire_time': expire_time
            }

        def delete(self, key: str) -> None:
            """
            删除缓存值
            
            Args:
                key: 缓存键
            """
            if key in self._cache:
                del self._cache[key]

        def clear(self) -> None:
            """
            清空缓存
            """
            self._cache.clear()

        def exists(self, key: str) -> bool:
            """
            检查缓存键是否存在且未过期
            
            Args:
                key: 缓存键
                
            Returns:
                bool: 如果存在且未过期则返回True，否则返回False
            """
            return self.get(key) is not None

        def size(self) -> int:
            """
            获取缓存大小
            
            Returns:
                int: 缓存中的键值对数量
            """
            # 清理过期项
            self._clean_expired()
            return len(self._cache)

        def _clean_expired(self) -> None:
            """
            清理过期的缓存项
            """
            expired_keys = []
            current_time = time.time()
            
            for key, item in self._cache.items():
                if current_time > item['expire_time']:
                    expired_keys.append(key)
            
            for key in expired_keys:
                del self._cache[key]

    class FileCache:
        """文件缓存实现"""

        def __init__(self, cache_dir: str = './cache', default_ttl: int = 3600):
            """
            初始化文件缓存
            
            Args:
                cache_dir: 缓存目录
                default_ttl: 默认过期时间（秒）
            """
            self._cache_dir = cache_dir
            self._default_ttl = default_ttl
            
            # 创建缓存目录
            os.makedirs(self._cache_dir, exist_ok=True)

        def get(self, key: str) -> Optional[Any]:
            """
            获取缓存值
            
            Args:
                key: 缓存键
                
            Returns:
                Any: 缓存值，如果不存在或已过期则返回None
            """
            cache_file = os.path.join(self._cache_dir, f"{key}.json")
            
            if not os.path.exists(cache_file):
                return None
            
            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                if time.time() > data['expire_time']:
                    os.remove(cache_file)
                    return None
                
                return data['value']
            except Exception:
                return None

        def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
            """
            设置缓存值
            
            Args:
                key: 缓存键
                value: 缓存值
                ttl: 过期时间（秒），如果为None则使用默认值
            """
            cache_file = os.path.join(self._cache_dir, f"{key}.json")
            expire_time = time.time() + (ttl or self._default_ttl)
            
            data = {
                'value': value,
                'expire_time': expire_time
            }
            
            try:
                with open(cache_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
            except Exception:
                pass

        def delete(self, key: str) -> None:
            """
            删除缓存值
            
            Args:
                key: 缓存键
            """
            cache_file = os.path.join(self._cache_dir, f"{key}.json")
            if os.path.exists(cache_file):
                try:
                    os.remove(cache_file)
                except Exception:
                    pass

        def clear(self) -> None:
            """
            清空缓存
            """
            try:
                for file_name in os.listdir(self._cache_dir):
                    if file_name.endswith('.json'):
                        os.remove(os.path.join(self._cache_dir, file_name))
            except Exception:
                pass

        def exists(self, key: str) -> bool:
            """
            检查缓存键是否存在且未过期
            
            Args:
                key: 缓存键
                
            Returns:
                bool: 如果存在且未过期则返回True，否则返回False
            """
            return self.get(key) is not None

        def size(self) -> int:
            """
            获取缓存大小
            
            Returns:
                int: 缓存中的键值对数量
            """
            # 清理过期项
            self._clean_expired()
            
            count = 0
            try:
                for file_name in os.listdir(self._cache_dir):
                    if file_name.endswith('.json'):
                        count += 1
            except Exception:
                pass
            
            return count

        def _clean_expired(self) -> None:
            """
            清理过期的缓存项
            """
            try:
                for file_name in os.listdir(self._cache_dir):
                    if file_name.endswith('.json'):
                        cache_file = os.path.join(self._cache_dir, file_name)
                        try:
                            with open(cache_file, 'r', encoding='utf-8') as f:
                                data = json.load(f)
                            
                            if time.time() > data['expire_time']:
                                os.remove(cache_file)
                        except Exception:
                            pass
            except Exception:
                pass

    class RedisCache:
        """Redis缓存实现"""

        def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0, password: Optional[str] = None, default_ttl: int = 3600):
            """
            初始化Redis缓存
            
            Args:
                host: Redis主机
                port: Redis端口
                db: Redis数据库
                password: Redis密码
                default_ttl: 默认过期时间（秒）
            """
            try:
                import redis
                self._redis = redis.Redis(host=host, port=port, db=db, password=password, decode_responses=True)
                self._default_ttl = default_ttl
                self._available = True
            except ImportError:
                self._redis = None
                self._available = False

        def get(self, key: str) -> Optional[Any]:
            """
            获取缓存值
            
            Args:
                key: 缓存键
                
            Returns:
                Any: 缓存值，如果不存在或Redis不可用则返回None
            """
            if not self._available:
                return None
            
            try:
                value = self._redis.get(key)
                if value:
                    return json.loads(value)
                return None
            except Exception:
                return None

        def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
            """
            设置缓存值
            
            Args:
                key: 缓存键
                value: 缓存值
                ttl: 过期时间（秒），如果为None则使用默认值
            """
            if not self._available:
                return
            
            try:
                self._redis.setex(key, ttl or self._default_ttl, json.dumps(value, ensure_ascii=False))
            except Exception:
                pass

        def delete(self, key: str) -> None:
            """
            删除缓存值
            
            Args:
                key: 缓存键
            """
            if not self._available:
                return
            
            try:
                self._redis.delete(key)
            except Exception:
                pass

        def clear(self) -> None:
            """
            清空缓存
            """
            if not self._available:
                return
            
            try:
                self._redis.flushdb()
            except Exception:
                pass

        def exists(self, key: str) -> bool:
            """
            检查缓存键是否存在
            
            Args:
                key: 缓存键
                
            Returns:
                bool: 如果存在则返回True，否则返回False
            """
            if not self._available:
                return False
            
            try:
                return bool(self._redis.exists(key))
            except Exception:
                return False

        def size(self) -> int:
            """
            获取缓存大小
            
            Returns:
                int: 缓存中的键值对数量
            """
            if not self._available:
                return 0
            
            try:
                return self._redis.dbsize()
            except Exception:
                return 0

        def is_available(self) -> bool:
            """
            检查Redis是否可用
            
            Returns:
                bool: 如果Redis可用则返回True，否则返回False
            """
            if not self._available:
                return False
            
            try:
                self._redis.ping()
                return True
            except Exception:
                return False

    @staticmethod
    def create_memory_cache(default_ttl: int = 3600) -> MemoryCache:
        """
        创建内存缓存实例
        
        Args:
            default_ttl: 默认过期时间（秒）
            
        Returns:
            MemoryCache: 内存缓存实例
        """
        return CacheUtils.MemoryCache(default_ttl)

    @staticmethod
    def create_file_cache(cache_dir: str = './cache', default_ttl: int = 3600) -> FileCache:
        """
        创建文件缓存实例
        
        Args:
            cache_dir: 缓存目录
            default_ttl: 默认过期时间（秒）
            
        Returns:
            FileCache: 文件缓存实例
        """
        return CacheUtils.FileCache(cache_dir, default_ttl)

    @staticmethod
    def create_redis_cache(host: str = 'localhost', port: int = 6379, db: int = 0, password: Optional[str] = None, default_ttl: int = 3600) -> RedisCache:
        """
        创建Redis缓存实例
        
        Args:
            host: Redis主机
            port: Redis端口
            db: Redis数据库
            password: Redis密码
            default_ttl: 默认过期时间（秒）
            
        Returns:
            RedisCache: Redis缓存实例
        """
        return CacheUtils.RedisCache(host, port, db, password, default_ttl)
