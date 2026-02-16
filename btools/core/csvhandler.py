import os
import csv
from typing import Dict, List, Any, Optional, Union, Tuple

class CSVHandler:
    """
    CSV文件处理类，支持CSV文件的读写操作
    
    Attributes:
        None
    """
    
    @staticmethod
    def read_csv(file_path: str, delimiter: str = ',', encoding: str = 'utf-8', 
                skip_header: bool = False) -> List[List[Any]]:
        """
        读取CSV文件
        
        Args:
            file_path (str): CSV文件路径
            delimiter (str): 分隔符，默认为','
            encoding (str): 文件编码，默认为'utf-8'
            skip_header (bool): 是否跳过表头，默认为False
            
        Returns:
            List[List[Any]]: 二维列表，每行数据作为一个子列表
            
        Raises:
            FileNotFoundError: 文件不存在
            Exception: 读取文件失败
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")
        
        data = []
        try:
            with open(file_path, 'r', encoding=encoding, newline='') as f:
                reader = csv.reader(f, delimiter=delimiter)
                if skip_header:
                    next(reader, None)
                for row in reader:
                    data.append(row)
            return data
        except Exception as e:
            raise Exception(f"读取CSV文件失败: {str(e)}")
    
    @staticmethod
    def write_csv(file_path: str, data: List[List[Any]], delimiter: str = ',', 
                 encoding: str = 'utf-8', header: Optional[List[str]] = None) -> bool:
        """
        写入CSV文件
        
        Args:
            file_path (str): CSV文件路径
            data (List[List[Any]]): 要写入的数据，二维列表
            delimiter (str): 分隔符，默认为','
            encoding (str): 文件编码，默认为'utf-8'
            header (List[str]): 表头，可选
            
        Returns:
            bool: 写入是否成功
            
        Raises:
            Exception: 写入文件失败
        """
        try:
            # 确保目录存在
            os.makedirs(os.path.dirname(file_path) if os.path.dirname(file_path) else '.', exist_ok=True)
            
            with open(file_path, 'w', encoding=encoding, newline='') as f:
                writer = csv.writer(f, delimiter=delimiter)
                if header:
                    writer.writerow(header)
                for row in data:
                    writer.writerow(row)
            return True
        except Exception as e:
            raise Exception(f"写入CSV文件失败: {str(e)}")
    
    @staticmethod
    def read_csv_dict(file_path: str, delimiter: str = ',', encoding: str = 'utf-8') -> List[Dict[str, Any]]:
        """
        以字典形式读取CSV文件（使用表头作为键）
        
        Args:
            file_path (str): CSV文件路径
            delimiter (str): 分隔符，默认为','
            encoding (str): 文件编码，默认为'utf-8'
            
        Returns:
            List[Dict[str, Any]]: 字典列表，每个字典表示一行数据
            
        Raises:
            FileNotFoundError: 文件不存在
            Exception: 读取文件失败
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")
        
        data = []
        try:
            with open(file_path, 'r', encoding=encoding, newline='') as f:
                reader = csv.DictReader(f, delimiter=delimiter)
                for row in reader:
                    data.append(row)
            return data
        except Exception as e:
            raise Exception(f"读取CSV文件失败: {str(e)}")
    
    @staticmethod
    def write_csv_dict(file_path: str, data: List[Dict[str, Any]], delimiter: str = ',', 
                      encoding: str = 'utf-8') -> bool:
        """
        以字典形式写入CSV文件
        
        Args:
            file_path (str): CSV文件路径
            data (List[Dict[str, Any]]): 要写入的数据，字典列表
            delimiter (str): 分隔符，默认为','
            encoding (str): 文件编码，默认为'utf-8'
            
        Returns:
            bool: 写入是否成功
            
        Raises:
            Exception: 写入文件失败
        """
        if not data:
            return True
        
        try:
            # 确保目录存在
            os.makedirs(os.path.dirname(file_path) if os.path.dirname(file_path) else '.', exist_ok=True)
            
            # 获取所有键作为表头
            fieldnames = list(data[0].keys())
            
            with open(file_path, 'w', encoding=encoding, newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=delimiter)
                writer.writeheader()
                writer.writerows(data)
            return True
        except Exception as e:
            raise Exception(f"写入CSV文件失败: {str(e)}")
