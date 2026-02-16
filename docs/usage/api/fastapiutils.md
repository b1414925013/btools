# FastAPIUtils 使用指南

`FastAPIUtils` 是一个FastAPI工具类，提供了丰富的API应用创建和配置方法，包括应用创建、路由器管理、CORS配置、异常处理、响应格式化等功能。

## 功能特性

- 创建FastAPI应用实例
- 创建API路由器
- 配置CORS中间件
- 配置自定义中间件
- 设置异常处理器
- 创建统一格式的响应
- 创建错误响应
- 运行FastAPI应用
- 提供统一的响应模型

## 基本用法

### 导入

```python
from btools.core.api import FastAPIUtils, create_app, create_router, add_cors, create_response, create_error_response
```

### 示例

#### 创建FastAPI应用

```python
# 创建基本应用
app = FastAPIUtils.create_app()

# 创建自定义配置的应用
app = FastAPIUtils.create_app(
    title="我的API",
    description="这是一个示例API应用",
    version="1.0.0",
    debug=True
)
```

#### 创建路由器

```python
# 创建基本路由器
router = FastAPIUtils.create_router()

# 创建带前缀和标签的路由器
router = FastAPIUtils.create_router(
    prefix="/api/v1",
    tags=["用户管理"]
)

# 添加路由
@router.get("/users")
def get_users():
    return {"users": []}

# 将路由器添加到应用
app.include_router(router)
```

#### 配置CORS

```python
# 配置默认CORS（允许所有来源）
app = FastAPIUtils.add_cors(app)

# 配置自定义CORS
app = FastAPIUtils.add_cors(
    app,
    origins=["https://example.com", "https://www.example.com"],
    methods=["GET", "POST", "PUT", "DELETE"],
    headers=["*"],
    allow_credentials=True
)
```

#### 设置异常处理器

```python
# 设置默认错误处理器
app = FastAPIUtils.setup_error_handlers(app)

# 自定义异常处理器
def custom_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "自定义错误"}
    )

app = FastAPIUtils.add_exception_handler(app, Exception, custom_exception_handler)
```

#### 创建统一响应

```python
# 创建基本响应
response = FastAPIUtils.create_response()

# 创建带数据的响应
data = {"name": "张三", "age": 25}
response = FastAPIUtils.create_response(
    data=data,
    message="获取成功",
    code=200
)

# 创建错误响应
error_response = FastAPIUtils.create_error_response(
    message="参数错误",
    code=400,
    details={"字段": "username", "原因": "用户名不能为空"}
)
```

#### 运行应用

```python
# 基本运行
FastAPIUtils.run_app(app)

# 自定义配置运行
FastAPIUtils.run_app(
    app,
    host="0.0.0.0",
    port=8000,
    reload=True
)
```

#### 使用便捷函数

```python
from btools.core.api import create_app, create_router, add_cors, create_response, create_error_response, run_app

# 创建应用
app = create_app(title="便捷函数示例")

# 创建路由器
router = create_router(prefix="/api")

# 添加CORS
app = add_cors(app)

# 定义路由
@router.get("/hello")
def hello():
    return create_response(data={"message": "Hello World"})

app.include_router(router)

# 运行应用
if __name__ == "__main__":
    run_app(app)
```

## 高级用法

### 完整的API应用示例

```python
from btools.core.api import (
    FastAPIUtils, create_app, create_router, add_cors,
    create_response, create_error_response, APIResponse
)
from pydantic import BaseModel

# 创建应用
app = create_app(
    title="用户管理API",
    description="一个完整的用户管理API示例",
    version="1.0.0"
)

# 配置CORS
app = add_cors(app)

# 设置错误处理器
app = FastAPIUtils.setup_error_handlers(app)

# 创建路由器
user_router = create_router(prefix="/api/users", tags=["用户管理"])

# 定义数据模型
class User(BaseModel):
    id: int
    name: str
    email: str

# 模拟数据库
users_db = {
    1: User(id=1, name="张三", email="zhangsan@example.com"),
    2: User(id=2, name="李四", email="lisi@example.com")
}

# 定义路由
@user_router.get("/", response_model=APIResponse)
def get_users():
    """获取所有用户"""
    users_list = list(users_db.values())
    return create_response(data=users_list)

@user_router.get("/{user_id}", response_model=APIResponse)
def get_user(user_id: int):
    """获取指定用户"""
    if user_id not in users_db:
        return create_error_response(message="用户不存在", code=404)
    return create_response(data=users_db[user_id])

@user_router.post("/", response_model=APIResponse)
def create_user(user: User):
    """创建用户"""
    if user.id in users_db:
        return create_error_response(message="用户ID已存在", code=400)
    users_db[user.id] = user
    return create_response(data=user, message="创建成功", code=201)

# 添加路由器到应用
app.include_router(user_router)

# 运行应用
if __name__ == "__main__":
    FastAPIUtils.run_app(app, host="0.0.0.0", port=8000, reload=True)
```

### 使用响应模型

```python
from btools.core.api import APIResponse, APIErrorResponse
from fastapi import FastAPI

app = FastAPI()

@app.get("/success", response_model=APIResponse)
def success_endpoint():
    """成功响应示例"""
    return APIResponse(
        code=200,
        message="操作成功",
        data={"result": "数据"}
    )

@app.get("/error", response_model=APIErrorResponse)
def error_endpoint():
    """错误响应示例"""
    return APIErrorResponse(
        code=400,
        message="操作失败",
        details={"字段": "必填项"}
    )
```

## 注意事项

1. **CORS配置**：在生产环境中，建议明确指定允许的来源，而不是使用通配符`*`。
2. **异常处理**：使用`setup_error_handlers()`可以设置统一的错误处理，但也可以根据需要添加自定义异常处理器。
3. **热重载**：`reload=True`只应在开发环境中使用，生产环境应设置为`False`。
4. **响应格式**：统一的响应格式可以让前端更容易处理响应数据，建议在所有API接口中使用。

## 总结

`FastAPIUtils` 提供了全面的FastAPI应用开发功能，简化了API开发的复杂度，使代码更加简洁易读。无论是基本的应用创建还是高级的配置和错误处理，`FastAPIUtils` 都能满足你的需求，帮助你快速构建高质量的API服务。