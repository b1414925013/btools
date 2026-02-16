# -*- coding: utf-8 -*-
"""
FastAPI工具类模块
"""
from typing import Any, Dict, List, Optional, Union, Callable
from fastapi import FastAPI, APIRouter, HTTPException, Request, Response, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse
from fastapi.dependencies.utils import get_dependant
from pydantic import BaseModel, Field
import uvicorn


class FastAPIUtils:
    """
    FastAPI工具类
    提供FastAPI应用的创建、配置和管理功能
    """

    @staticmethod
    def create_app(
        title: str = "FastAPI Application",
        description: str = "",
        version: str = "1.0.0",
        docs_url: Optional[str] = "/docs",
        redoc_url: Optional[str] = "/redoc",
        openapi_url: Optional[str] = "/openapi.json",
        debug: bool = False
    ) -> FastAPI:
        """
        创建FastAPI应用实例

        Args:
            title: 应用标题
            description: 应用描述
            version: 应用版本
            docs_url: 文档URL
            redoc_url: ReDoc文档URL
            openapi_url: OpenAPI规范URL
            debug: 是否启用调试模式

        Returns:
            FastAPI应用实例
        """
        app = FastAPI(
            title=title,
            description=description,
            version=version,
            docs_url=docs_url,
            redoc_url=redoc_url,
            openapi_url=openapi_url,
            debug=debug
        )
        return app

    @staticmethod
    def create_router(
        prefix: Optional[str] = None,
        tags: Optional[List[str]] = None,
        dependencies: Optional[List[Any]] = None
    ) -> APIRouter:
        """
        创建API路由器

        Args:
            prefix: 路由前缀
            tags: 路由标签
            dependencies: 依赖项列表

        Returns:
            APIRouter实例
        """
        router = APIRouter(
            prefix=prefix,
            tags=tags,
            dependencies=dependencies
        )
        return router

    @staticmethod
    def add_cors(
        app: FastAPI,
        origins: List[str] = ["*"],
        methods: List[str] = ["*"],
        headers: List[str] = ["*"],
        allow_credentials: bool = True
    ) -> FastAPI:
        """
        添加CORS中间件

        Args:
            app: FastAPI应用实例
            origins: 允许的源
            methods: 允许的HTTP方法
            headers: 允许的HTTP头
            allow_credentials: 是否允许凭证

        Returns:
            FastAPI应用实例
        """
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=allow_credentials,
            allow_methods=methods,
            allow_headers=headers,
        )
        return app

    @staticmethod
    def add_middleware(
        app: FastAPI,
        middleware_class: Any,
        **options: Any
    ) -> FastAPI:
        """
        添加中间件

        Args:
            app: FastAPI应用实例
            middleware_class: 中间件类
            **options: 中间件选项

        Returns:
            FastAPI应用实例
        """
        app.add_middleware(middleware_class, **options)
        return app

    @staticmethod
    def add_exception_handler(
        app: FastAPI,
        exc_type: Any,
        handler: Callable[[Request, Any], Response]
    ) -> FastAPI:
        """
        添加异常处理器

        Args:
            app: FastAPI应用实例
            exc_type: 异常类型
            handler: 异常处理函数

        Returns:
            FastAPI应用实例
        """
        app.add_exception_handler(exc_type, handler)
        return app

    @staticmethod
    def setup_error_handlers(app: FastAPI) -> FastAPI:
        """
        设置默认错误处理器

        Args:
            app: FastAPI应用实例

        Returns:
            FastAPI应用实例
        """
        
        @app.exception_handler(HTTPException)
        async def http_exception_handler(request: Request, exc: HTTPException):
            return JSONResponse(
                status_code=exc.status_code,
                content={"detail": exc.detail}
            )

        @app.exception_handler(Exception)
        async def general_exception_handler(request: Request, exc: Exception):
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal Server Error"}
            )

        return app

    @staticmethod
    def run_app(
        app: FastAPI,
        host: str = "0.0.0.0",
        port: int = 8000,
        reload: bool = False,
        **kwargs: Any
    ) -> None:
        """
        运行FastAPI应用

        Args:
            app: FastAPI应用实例
            host: 主机地址
            port: 端口号
            reload: 是否启用热重载
            **kwargs: 其他uvicorn选项
        """
        uvicorn.run(app, host=host, port=port, reload=reload, **kwargs)

    @staticmethod
    def create_response(
        data: Any = None,
        message: str = "success",
        code: int = 200,
        headers: Optional[Dict[str, str]] = None
    ) -> JSONResponse:
        """
        创建统一格式的响应

        Args:
            data: 响应数据
            message: 响应消息
            code: 响应状态码
            headers: 响应头

        Returns:
            JSONResponse实例
        """
        response_data = {
            "code": code,
            "message": message,
            "data": data
        }
        return JSONResponse(
            content=response_data,
            status_code=code,
            headers=headers
        )

    @staticmethod
    def create_error_response(
        message: str = "error",
        code: int = 400,
        details: Optional[Any] = None
    ) -> JSONResponse:
        """
        创建错误响应

        Args:
            message: 错误消息
            code: 错误状态码
            details: 错误详情

        Returns:
            JSONResponse实例
        """
        response_data = {
            "code": code,
            "message": message,
            "details": details
        }
        return JSONResponse(
            content=response_data,
            status_code=code
        )


# 统一响应模型
class APIResponse(BaseModel):
    """
    API统一响应模型
    """
    code: int = Field(200, description="状态码")
    message: str = Field("success", description="响应消息")
    data: Optional[Any] = Field(None, description="响应数据")


class APIErrorResponse(BaseModel):
    """
    API错误响应模型
    """
    code: int = Field(400, description="状态码")
    message: str = Field("error", description="错误消息")
    details: Optional[Any] = Field(None, description="错误详情")


# 便捷函数

def create_app(
    title: str = "FastAPI Application",
    description: str = "",
    version: str = "1.0.0",
    docs_url: Optional[str] = "/docs",
    redoc_url: Optional[str] = "/redoc",
    openapi_url: Optional[str] = "/openapi.json",
    debug: bool = False
) -> FastAPI:
    """
    创建FastAPI应用实例

    Args:
        title: 应用标题
        description: 应用描述
        version: 应用版本
        docs_url: 文档URL
        redoc_url: ReDoc文档URL
        openapi_url: OpenAPI规范URL
        debug: 是否启用调试模式

    Returns:
        FastAPI应用实例
    """
    return FastAPIUtils.create_app(
        title=title,
        description=description,
        version=version,
        docs_url=docs_url,
        redoc_url=redoc_url,
        openapi_url=openapi_url,
        debug=debug
    )


def create_router(
    prefix: Optional[str] = None,
    tags: Optional[List[str]] = None,
    dependencies: Optional[List[Any]] = None
) -> APIRouter:
    """
    创建API路由器

    Args:
        prefix: 路由前缀
        tags: 路由标签
        dependencies: 依赖项列表

    Returns:
        APIRouter实例
    """
    return FastAPIUtils.create_router(
        prefix=prefix,
        tags=tags,
        dependencies=dependencies
    )


def add_cors(
    app: FastAPI,
    origins: List[str] = ["*"],
    methods: List[str] = ["*"],
    headers: List[str] = ["*"],
    allow_credentials: bool = True
) -> FastAPI:
    """
    添加CORS中间件

    Args:
        app: FastAPI应用实例
        origins: 允许的源
        methods: 允许的HTTP方法
        headers: 允许的HTTP头
        allow_credentials: 是否允许凭证

    Returns:
        FastAPI应用实例
    """
    return FastAPIUtils.add_cors(
        app=app,
        origins=origins,
        methods=methods,
        headers=headers,
        allow_credentials=allow_credentials
    )


def add_middleware(
    app: FastAPI,
    middleware_class: Any,
    **options: Any
) -> FastAPI:
    """
    添加中间件

    Args:
        app: FastAPI应用实例
        middleware_class: 中间件类
        **options: 中间件选项

    Returns:
        FastAPI应用实例
    """
    return FastAPIUtils.add_middleware(app=app, middleware_class=middleware_class, **options)


def add_exception_handler(
    app: FastAPI,
    exc_type: Any,
    handler: Callable[[Request, Any], Response]
) -> FastAPI:
    """
    添加异常处理器

    Args:
        app: FastAPI应用实例
        exc_type: 异常类型
        handler: 异常处理函数

    Returns:
        FastAPI应用实例
    """
    return FastAPIUtils.add_exception_handler(
        app=app,
        exc_type=exc_type,
        handler=handler
    )


def setup_error_handlers(app: FastAPI) -> FastAPI:
    """
    设置默认错误处理器

    Args:
        app: FastAPI应用实例

    Returns:
        FastAPI应用实例
    """
    return FastAPIUtils.setup_error_handlers(app=app)


def run_app(
    app: FastAPI,
    host: str = "0.0.0.0",
    port: int = 8000,
    reload: bool = False,
    **kwargs: Any
) -> None:
    """
    运行FastAPI应用

    Args:
        app: FastAPI应用实例
        host: 主机地址
        port: 端口号
        reload: 是否启用热重载
        **kwargs: 其他uvicorn选项
    """
    FastAPIUtils.run_app(
        app=app,
        host=host,
        port=port,
        reload=reload,
        **kwargs
    )


def create_response(
    data: Any = None,
    message: str = "success",
    code: int = 200,
    headers: Optional[Dict[str, str]] = None
) -> JSONResponse:
    """
    创建统一格式的响应

    Args:
        data: 响应数据
        message: 响应消息
        code: 响应状态码
        headers: 响应头

    Returns:
        JSONResponse实例
    """
    return FastAPIUtils.create_response(
        data=data,
        message=message,
        code=code,
        headers=headers
    )


def create_error_response(
    message: str = "error",
    code: int = 400,
    details: Optional[Any] = None
) -> JSONResponse:
    """
    创建错误响应

    Args:
        message: 错误消息
        code: 错误状态码
        details: 错误详情

    Returns:
        JSONResponse实例
    """
    return FastAPIUtils.create_error_response(
        message=message,
        code=code,
        details=details
    )