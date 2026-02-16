# -*- coding: utf-8 -*-
"""
FastAPI工具测试
"""
import unittest
from btools.core.api.fastapiutils import (
    FastAPIUtils, create_app, create_router, add_cors, add_middleware,
    add_exception_handler, setup_error_handlers, create_response, create_error_response
)
from fastapi import FastAPI, APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse


class TestFastAPIUtils(unittest.TestCase):
    """
    FastAPI工具测试类
    """

    def test_create_app(self):
        """
        测试创建FastAPI应用实例
        """
        # 测试默认参数
        app = FastAPIUtils.create_app()
        self.assertIsInstance(app, FastAPI)
        self.assertEqual(app.title, "FastAPI Application")
        self.assertEqual(app.version, "1.0.0")

        # 测试自定义参数
        app = FastAPIUtils.create_app(
            title="Test App",
            description="Test Description",
            version="0.1.0",
            docs_url="/test-docs",
            redoc_url="/test-redoc",
            openapi_url="/test-openapi.json",
            debug=True
        )
        self.assertIsInstance(app, FastAPI)
        self.assertEqual(app.title, "Test App")
        self.assertEqual(app.description, "Test Description")
        self.assertEqual(app.version, "0.1.0")
        self.assertEqual(app.docs_url, "/test-docs")
        self.assertEqual(app.redoc_url, "/test-redoc")
        self.assertEqual(app.openapi_url, "/test-openapi.json")
        self.assertTrue(app.debug)

    def test_create_router(self):
        """
        测试创建API路由器
        """
        # 测试默认参数
        router = FastAPIUtils.create_router()
        self.assertIsInstance(router, APIRouter)

        # 测试自定义参数
        router = FastAPIUtils.create_router(
            prefix="/api",
            tags=["test"],
            dependencies=[]
        )
        self.assertIsInstance(router, APIRouter)
        self.assertEqual(router.prefix, "/api")
        self.assertEqual(router.tags, ["test"])

    def test_add_cors(self):
        """
        测试添加CORS中间件
        """
        app = FastAPIUtils.create_app()
        app = FastAPIUtils.add_cors(app)
        self.assertIsInstance(app, FastAPI)

    def test_setup_error_handlers(self):
        """
        测试设置默认错误处理器
        """
        app = FastAPIUtils.create_app()
        app = FastAPIUtils.setup_error_handlers(app)
        self.assertIsInstance(app, FastAPI)

    def test_create_response(self):
        """
        测试创建统一格式的响应
        """
        # 测试默认参数
        response = FastAPIUtils.create_response()
        self.assertIsInstance(response, JSONResponse)
        self.assertEqual(response.status_code, 200)

        # 测试自定义参数
        test_data = {"key": "value"}
        response = FastAPIUtils.create_response(
            data=test_data,
            message="Test Message",
            code=201,
            headers={"X-Test": "test"}
        )
        self.assertIsInstance(response, JSONResponse)
        self.assertEqual(response.status_code, 201)

    def test_create_error_response(self):
        """
        测试创建错误响应
        """
        # 测试默认参数
        response = FastAPIUtils.create_error_response()
        self.assertIsInstance(response, JSONResponse)
        self.assertEqual(response.status_code, 400)

        # 测试自定义参数
        test_details = {"error": "Test Error"}
        response = FastAPIUtils.create_error_response(
            message="Test Error Message",
            code=404,
            details=test_details
        )
        self.assertIsInstance(response, JSONResponse)
        self.assertEqual(response.status_code, 404)

    def test_convenience_functions(self):
        """
        测试便捷函数
        """
        # 测试create_app便捷函数
        app = create_app()
        self.assertIsInstance(app, FastAPI)

        # 测试create_router便捷函数
        router = create_router()
        self.assertIsInstance(router, APIRouter)

        # 测试add_cors便捷函数
        app = add_cors(app)
        self.assertIsInstance(app, FastAPI)

        # 测试setup_error_handlers便捷函数
        app = setup_error_handlers(app)
        self.assertIsInstance(app, FastAPI)

        # 测试create_response便捷函数
        response = create_response()
        self.assertIsInstance(response, JSONResponse)

        # 测试create_error_response便捷函数
        error_response = create_error_response()
        self.assertIsInstance(error_response, JSONResponse)


if __name__ == '__main__':
    unittest.main()