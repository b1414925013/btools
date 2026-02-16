# -*- coding: utf-8 -*-
"""
API工具模块
"""
from .fastapiutils import FastAPIUtils, create_app, create_router, add_cors, add_middleware, add_exception_handler

__all__ = [
    "FastAPIUtils",
    "create_app",
    "create_router",
    "add_cors",
    "add_middleware",
    "add_exception_handler"
]