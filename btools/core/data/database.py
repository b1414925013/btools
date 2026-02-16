"""数据库工具类"""
import sqlite3
from typing import Any, Dict, List, Optional, Tuple, Union


class DatabaseUtils:
    """数据库工具类"""

    class SQLiteDatabase:
        """SQLite数据库实现"""

        def __init__(self, db_path: str = ':memory:'):
            """
            初始化SQLite数据库连接
            
            Args:
                db_path: 数据库文件路径，默认使用内存数据库
            """
            self._db_path = db_path
            self._conn = None

        def connect(self) -> None:
            """
            连接到SQLite数据库
            """
            if self._conn is None:
                self._conn = sqlite3.connect(self._db_path)
                self._conn.row_factory = sqlite3.Row

        def disconnect(self) -> None:
            """
            断开SQLite数据库连接
            """
            if self._conn:
                self._conn.close()
                self._conn = None

        def execute(self, sql: str, params: Optional[Tuple[Any, ...]] = None) -> sqlite3.Cursor:
            """
            执行SQL语句
            
            Args:
                sql: SQL语句
                params: SQL参数
                
            Returns:
                sqlite3.Cursor: 游标对象
            """
            self.connect()
            return self._conn.execute(sql, params or ())

        def executemany(self, sql: str, params: List[Tuple[Any, ...]]) -> sqlite3.Cursor:
            """
            批量执行SQL语句
            
            Args:
                sql: SQL语句
                params: SQL参数列表
                
            Returns:
                sqlite3.Cursor: 游标对象
            """
            self.connect()
            return self._conn.executemany(sql, params)

        def commit(self) -> None:
            """
            提交事务
            """
            if self._conn:
                self._conn.commit()

        def rollback(self) -> None:
            """
            回滚事务
            """
            if self._conn:
                self._conn.rollback()

        def fetch_one(self, sql: str, params: Optional[Tuple[Any, ...]] = None) -> Optional[Dict[str, Any]]:
            """
            获取单条数据
            
            Args:
                sql: SQL语句
                params: SQL参数
                
            Returns:
                Dict[str, Any]: 数据字典，如果没有数据则返回None
            """
            cursor = self.execute(sql, params)
            row = cursor.fetchone()
            if row:
                return dict(row)
            return None

        def fetch_all(self, sql: str, params: Optional[Tuple[Any, ...]] = None) -> List[Dict[str, Any]]:
            """
            获取所有数据
            
            Args:
                sql: SQL语句
                params: SQL参数
                
            Returns:
                List[Dict[str, Any]]: 数据字典列表
            """
            cursor = self.execute(sql, params)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

        def insert(self, table: str, data: Dict[str, Any]) -> int:
            """
            插入数据
            
            Args:
                table: 表名
                data: 数据字典
                
            Returns:
                int: 插入的行ID
            """
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['?'] * len(data))
            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cursor = self.execute(sql, tuple(data.values()))
            self.commit()
            return cursor.lastrowid

        def update(self, table: str, data: Dict[str, Any], where: str, where_params: Optional[Tuple[Any, ...]] = None) -> int:
            """
            更新数据
            
            Args:
                table: 表名
                data: 数据字典
                where: WHERE子句
                where_params: WHERE参数
                
            Returns:
                int: 受影响的行数
            """
            set_clause = ', '.join([f"{col} = ?" for col in data.keys()])
            sql = f"UPDATE {table} SET {set_clause} WHERE {where}"
            params = tuple(data.values()) + (where_params or ())
            cursor = self.execute(sql, params)
            self.commit()
            return cursor.rowcount

        def delete(self, table: str, where: str, where_params: Optional[Tuple[Any, ...]] = None) -> int:
            """
            删除数据
            
            Args:
                table: 表名
                where: WHERE子句
                where_params: WHERE参数
                
            Returns:
                int: 受影响的行数
            """
            sql = f"DELETE FROM {table} WHERE {where}"
            cursor = self.execute(sql, where_params or ())
            self.commit()
            return cursor.rowcount

        def create_table(self, table: str, columns: Dict[str, str]) -> None:
            """
            创建表
            
            Args:
                table: 表名
                columns: 列定义字典，格式为 {列名: 列类型}
            """
            column_defs = ', '.join([f"{col} {type_}" for col, type_ in columns.items()])
            sql = f"CREATE TABLE IF NOT EXISTS {table} ({column_defs})"
            self.execute(sql)
            self.commit()

        def drop_table(self, table: str) -> None:
            """
            删除表
            
            Args:
                table: 表名
            """
            sql = f"DROP TABLE IF EXISTS {table}"
            self.execute(sql)
            self.commit()

        def table_exists(self, table: str) -> bool:
            """
            检查表是否存在
            
            Args:
                table: 表名
                
            Returns:
                bool: 如果表存在则返回True，否则返回False
            """
            sql = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"
            return self.fetch_one(sql, (table,)) is not None

    class MySQLDatabase:
        """MySQL数据库实现"""

        def __init__(self, host: str = 'localhost', port: int = 3306, user: str = 'root', password: str = '', database: str = '', charset: str = 'utf8mb4'):
            """
            初始化MySQL数据库连接
            
            Args:
                host: 主机地址
                port: 端口
                user: 用户名
                password: 密码
                database: 数据库名
                charset: 字符集
            """
            self._host = host
            self._port = port
            self._user = user
            self._password = password
            self._database = database
            self._charset = charset
            self._conn = None

        def connect(self) -> None:
            """
            连接到MySQL数据库
            """
            if self._conn is None:
                try:
                    import pymysql
                    self._conn = pymysql.connect(
                        host=self._host,
                        port=self._port,
                        user=self._user,
                        password=self._password,
                        database=self._database,
                        charset=self._charset,
                        cursorclass=pymysql.cursors.DictCursor
                    )
                except ImportError:
                    raise ImportError("Please install pymysql: pip install pymysql")

        def disconnect(self) -> None:
            """
            断开MySQL数据库连接
            """
            if self._conn:
                self._conn.close()
                self._conn = None

        def execute(self, sql: str, params: Optional[Tuple[Any, ...]] = None) -> Any:
            """
            执行SQL语句
            
            Args:
                sql: SQL语句
                params: SQL参数
                
            Returns:
                Any: 游标对象
            """
            self.connect()
            with self._conn.cursor() as cursor:
                cursor.execute(sql, params or ())
                return cursor

        def executemany(self, sql: str, params: List[Tuple[Any, ...]]) -> Any:
            """
            批量执行SQL语句
            
            Args:
                sql: SQL语句
                params: SQL参数列表
                
            Returns:
                Any: 游标对象
            """
            self.connect()
            with self._conn.cursor() as cursor:
                cursor.executemany(sql, params)
                return cursor

        def commit(self) -> None:
            """
            提交事务
            """
            if self._conn:
                self._conn.commit()

        def rollback(self) -> None:
            """
            回滚事务
            """
            if self._conn:
                self._conn.rollback()

        def fetch_one(self, sql: str, params: Optional[Tuple[Any, ...]] = None) -> Optional[Dict[str, Any]]:
            """
            获取单条数据
            
            Args:
                sql: SQL语句
                params: SQL参数
                
            Returns:
                Dict[str, Any]: 数据字典，如果没有数据则返回None
            """
            cursor = self.execute(sql, params)
            return cursor.fetchone()

        def fetch_all(self, sql: str, params: Optional[Tuple[Any, ...]] = None) -> List[Dict[str, Any]]:
            """
            获取所有数据
            
            Args:
                sql: SQL语句
                params: SQL参数
                
            Returns:
                List[Dict[str, Any]]: 数据字典列表
            """
            cursor = self.execute(sql, params)
            return cursor.fetchall()

        def insert(self, table: str, data: Dict[str, Any]) -> int:
            """
            插入数据
            
            Args:
                table: 表名
                data: 数据字典
                
            Returns:
                int: 插入的行ID
            """
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cursor = self.execute(sql, tuple(data.values()))
            self.commit()
            return cursor.lastrowid

        def update(self, table: str, data: Dict[str, Any], where: str, where_params: Optional[Tuple[Any, ...]] = None) -> int:
            """
            更新数据
            
            Args:
                table: 表名
                data: 数据字典
                where: WHERE子句
                where_params: WHERE参数
                
            Returns:
                int: 受影响的行数
            """
            set_clause = ', '.join([f"{col} = %s" for col in data.keys()])
            sql = f"UPDATE {table} SET {set_clause} WHERE {where}"
            params = tuple(data.values()) + (where_params or ())
            cursor = self.execute(sql, params)
            self.commit()
            return cursor.rowcount

        def delete(self, table: str, where: str, where_params: Optional[Tuple[Any, ...]] = None) -> int:
            """
            删除数据
            
            Args:
                table: 表名
                where: WHERE子句
                where_params: WHERE参数
                
            Returns:
                int: 受影响的行数
            """
            sql = f"DELETE FROM {table} WHERE {where}"
            cursor = self.execute(sql, where_params or ())
            self.commit()
            return cursor.rowcount

        def create_table(self, table: str, columns: Dict[str, str]) -> None:
            """
            创建表
            
            Args:
                table: 表名
                columns: 列定义字典，格式为 {列名: 列类型}
            """
            column_defs = ', '.join([f"{col} {type_}" for col, type_ in columns.items()])
            sql = f"CREATE TABLE IF NOT EXISTS {table} ({column_defs})"
            self.execute(sql)
            self.commit()

        def drop_table(self, table: str) -> None:
            """
            删除表
            
            Args:
                table: 表名
            """
            sql = f"DROP TABLE IF EXISTS {table}"
            self.execute(sql)
            self.commit()

        def table_exists(self, table: str) -> bool:
            """
            检查表是否存在
            
            Args:
                table: 表名
                
            Returns:
                bool: 如果表存在则返回True，否则返回False
            """
            sql = "SELECT table_name FROM information_schema.tables WHERE table_schema = %s AND table_name = %s"
            return self.fetch_one(sql, (self._database, table)) is not None

    class PostgreSQLDatabase:
        """PostgreSQL数据库实现"""

        def __init__(self, host: str = 'localhost', port: int = 5432, user: str = 'postgres', password: str = '', database: str = 'postgres'):
            """
            初始化PostgreSQL数据库连接
            
            Args:
                host: 主机地址
                port: 端口
                user: 用户名
                password: 密码
                database: 数据库名
            """
            self._host = host
            self._port = port
            self._user = user
            self._password = password
            self._database = database
            self._conn = None

        def connect(self) -> None:
            """
            连接到PostgreSQL数据库
            """
            if self._conn is None:
                try:
                    import psycopg2
                    from psycopg2.extras import RealDictCursor
                    self._conn = psycopg2.connect(
                        host=self._host,
                        port=self._port,
                        user=self._user,
                        password=self._password,
                        database=self._database
                    )
                    self._cursor_factory = RealDictCursor
                except ImportError:
                    raise ImportError("Please install psycopg2: pip install psycopg2-binary")

        def disconnect(self) -> None:
            """
            断开PostgreSQL数据库连接
            """
            if self._conn:
                self._conn.close()
                self._conn = None

        def execute(self, sql: str, params: Optional[Tuple[Any, ...]] = None) -> Any:
            """
            执行SQL语句
            
            Args:
                sql: SQL语句
                params: SQL参数
                
            Returns:
                Any: 游标对象
            """
            self.connect()
            cursor = self._conn.cursor(cursor_factory=self._cursor_factory)
            cursor.execute(sql, params or ())
            return cursor

        def executemany(self, sql: str, params: List[Tuple[Any, ...]]) -> Any:
            """
            批量执行SQL语句
            
            Args:
                sql: SQL语句
                params: SQL参数列表
                
            Returns:
                Any: 游标对象
            """
            self.connect()
            cursor = self._conn.cursor(cursor_factory=self._cursor_factory)
            cursor.executemany(sql, params)
            return cursor

        def commit(self) -> None:
            """
            提交事务
            """
            if self._conn:
                self._conn.commit()

        def rollback(self) -> None:
            """
            回滚事务
            """
            if self._conn:
                self._conn.rollback()

        def fetch_one(self, sql: str, params: Optional[Tuple[Any, ...]] = None) -> Optional[Dict[str, Any]]:
            """
            获取单条数据
            
            Args:
                sql: SQL语句
                params: SQL参数
                
            Returns:
                Dict[str, Any]: 数据字典，如果没有数据则返回None
            """
            cursor = self.execute(sql, params)
            result = cursor.fetchone()
            cursor.close()
            return result

        def fetch_all(self, sql: str, params: Optional[Tuple[Any, ...]] = None) -> List[Dict[str, Any]]:
            """
            获取所有数据
            
            Args:
                sql: SQL语句
                params: SQL参数
                
            Returns:
                List[Dict[str, Any]]: 数据字典列表
            """
            cursor = self.execute(sql, params)
            results = cursor.fetchall()
            cursor.close()
            return results

        def insert(self, table: str, data: Dict[str, Any]) -> int:
            """
            插入数据
            
            Args:
                table: 表名
                data: 数据字典
                
            Returns:
                int: 插入的行ID
            """
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders}) RETURNING id"
            cursor = self.execute(sql, tuple(data.values()))
            result = cursor.fetchone()
            cursor.close()
            self.commit()
            return result['id'] if result else 0

        def update(self, table: str, data: Dict[str, Any], where: str, where_params: Optional[Tuple[Any, ...]] = None) -> int:
            """
            更新数据
            
            Args:
                table: 表名
                data: 数据字典
                where: WHERE子句
                where_params: WHERE参数
                
            Returns:
                int: 受影响的行数
            """
            set_clause = ', '.join([f"{col} = %s" for col in data.keys()])
            sql = f"UPDATE {table} SET {set_clause} WHERE {where}"
            params = tuple(data.values()) + (where_params or ())
            cursor = self.execute(sql, params)
            rowcount = cursor.rowcount
            cursor.close()
            self.commit()
            return rowcount

        def delete(self, table: str, where: str, where_params: Optional[Tuple[Any, ...]] = None) -> int:
            """
            删除数据
            
            Args:
                table: 表名
                where: WHERE子句
                where_params: WHERE参数
                
            Returns:
                int: 受影响的行数
            """
            sql = f"DELETE FROM {table} WHERE {where}"
            cursor = self.execute(sql, where_params or ())
            rowcount = cursor.rowcount
            cursor.close()
            self.commit()
            return rowcount

        def create_table(self, table: str, columns: Dict[str, str]) -> None:
            """
            创建表
            
            Args:
                table: 表名
                columns: 列定义字典，格式为 {列名: 列类型}
            """
            column_defs = ', '.join([f"{col} {type_}" for col, type_ in columns.items()])
            sql = f"CREATE TABLE IF NOT EXISTS {table} ({column_defs})"
            cursor = self.execute(sql)
            cursor.close()
            self.commit()

        def drop_table(self, table: str) -> None:
            """
            删除表
            
            Args:
                table: 表名
            """
            sql = f"DROP TABLE IF EXISTS {table}"
            cursor = self.execute(sql)
            cursor.close()
            self.commit()

        def table_exists(self, table: str) -> bool:
            """
            检查表是否存在
            
            Args:
                table: 表名
                
            Returns:
                bool: 如果表存在则返回True，否则返回False
            """
            sql = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = %s"
            return self.fetch_one(sql, (table,)) is not None

    @staticmethod
    def create_sqlite_database(db_path: str = ':memory:') -> SQLiteDatabase:
        """
        创建SQLite数据库实例
        
        Args:
            db_path: 数据库文件路径
            
        Returns:
            SQLiteDatabase: SQLite数据库实例
        """
        return DatabaseUtils.SQLiteDatabase(db_path)

    @staticmethod
    def create_mysql_database(host: str = 'localhost', port: int = 3306, user: str = 'root', password: str = '', database: str = '', charset: str = 'utf8mb4') -> MySQLDatabase:
        """
        创建MySQL数据库实例
        
        Args:
            host: 主机地址
            port: 端口
            user: 用户名
            password: 密码
            database: 数据库名
            charset: 字符集
            
        Returns:
            MySQLDatabase: MySQL数据库实例
        """
        return DatabaseUtils.MySQLDatabase(host, port, user, password, database, charset)

    @staticmethod
    def create_postgresql_database(host: str = 'localhost', port: int = 5432, user: str = 'postgres', password: str = '', database: str = 'postgres') -> PostgreSQLDatabase:
        """
        创建PostgreSQL数据库实例
        
        Args:
            host: 主机地址
            port: 端口
            user: 用户名
            password: 密码
            database: 数据库名
            
        Returns:
            PostgreSQLDatabase: PostgreSQL数据库实例
        """
        return DatabaseUtils.PostgreSQLDatabase(host, port, user, password, database)
