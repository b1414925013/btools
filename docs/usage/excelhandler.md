# ExcelHandler 使用指南

`ExcelHandler` 类提供了Excel文件的读写和单元格更新操作功能。

## 依赖

使用 `ExcelHandler` 需要安装 `openpyxl` 库：

```bash
pip install openpyxl
```

## 基本使用

### 读取Excel文件

```python
from btools import ExcelHandler

# 基本读取
excel_data = ExcelHandler.read_excel("data.xlsx")
print("Excel数据:", excel_data)

# 读取指定工作表
excel_data_sheet = ExcelHandler.read_excel("data.xlsx", sheet_name="Sheet2")
print("指定工作表数据:", excel_data_sheet)

# 读取时跳过表头
excel_data_no_header = ExcelHandler.read_excel("data.xlsx", skip_header=True)
print("Excel数据（无表头）:", excel_data_no_header)

# 以字典形式读取（使用表头作为键）
excel_dict_data = ExcelHandler.read_excel_dict("data.xlsx")
print("Excel字典数据:", excel_dict_data)
```

### 写入Excel文件

```python
from btools import ExcelHandler

# 基本写入
data = [
    ["姓名", "年龄", "城市"],
    ["张三", 25, "北京"],
    ["李四", 30, "上海"],
    ["王五", 28, "广州"]
]
ExcelHandler.write_excel("output.xlsx", data)
print("Excel文件写入完成")

# 写入到指定工作表
data_no_header = [
    ["张三", 25, "北京"],
    ["李四", 30, "上海"],
    ["王五", 28, "广州"]
]
header = ["姓名", "年龄", "城市"]
ExcelHandler.write_excel("output_with_header.xlsx", data_no_header, 
                        sheet_name="员工信息", header=header)
print("带表头的Excel文件写入完成")

# 以字典形式写入
dict_data = [
    {"姓名": "张三", "年龄": 25, "城市": "北京"},
    {"姓名": "李四", "年龄": 30, "城市": "上海"},
    {"姓名": "王五", "年龄": 28, "城市": "广州"}
]
ExcelHandler.write_excel_dict("output_dict.xlsx", dict_data, sheet_name="员工数据")
print("字典形式Excel文件写入完成")
```

### 更新Excel单元格

```python
from btools import ExcelHandler

# 更新单个单元格
ExcelHandler.update_excel_cell("output.xlsx", cell="A1", value="员工姓名")
print("Excel单元格更新完成")

# 更新指定工作表的单元格
ExcelHandler.update_excel_cell("output.xlsx", sheet_name="Sheet1", 
                             cell="B1", value="员工年龄")
print("指定工作表的Excel单元格更新完成")
```

## 高级功能

### 多工作表操作

```python
# 写入多个工作表
worksheets = {
    "员工信息": [
        ["姓名", "年龄", "城市"],
        ["张三", 25, "北京"],
        ["李四", 30, "上海"]
    ],
    "部门信息": [
        ["部门名称", "人数", "负责人"],
        ["研发部", 20, "张三"],
        ["市场部", 10, "李四"]
    ]
}

# 写入多个工作表
for sheet_name, data in worksheets.items():
    ExcelHandler.write_excel("multi_sheet.xlsx", data, sheet_name=sheet_name)
print("多工作表写入完成")

# 读取多个工作表
all_sheets_data = {}
for sheet_name in ["员工信息", "部门信息"]:
    data = ExcelHandler.read_excel("multi_sheet.xlsx", sheet_name=sheet_name)
    all_sheets_data[sheet_name] = data
print("多工作表读取完成:", all_sheets_data)
```

### 单元格格式处理

```python
# 处理不同类型的单元格值
excel_data = ExcelHandler.read_excel("data.xlsx")
for row in excel_data:
    for cell in row:
        print(f"值: {cell}, 类型: {type(cell).__name__}")

# 写入不同类型的数据
type_data = [
    ["字符串", "数字", "日期", "布尔值"],
    ["测试", 123, "2023-12-25", True],
    ["示例", 456.78, "2024-01-01", False]
]
ExcelHandler.write_excel("types.xlsx", type_data)
print("不同类型数据写入完成")
```

### 批量更新

```python
# 批量更新单元格
updates = [
    {"cell": "A1", "value": "姓名"},
    {"cell": "B1", "value": "年龄"},
    {"cell": "C1", "value": "城市"},
    {"cell": "A2", "value": "张三"},
    {"cell": "B2", "value": 25},
    {"cell": "C2", "value": "北京"}
]

for update in updates:
    ExcelHandler.update_excel_cell("output.xlsx", cell=update["cell"], value=update["value"])
print("批量更新完成")
```

### 与pandas集成

```python
import pandas as pd
from btools import ExcelHandler

# 使用ExcelHandler读取数据，然后转换为pandas DataFrame
excel_data = ExcelHandler.read_excel_dict("data.xlsx")
df = pd.DataFrame(excel_data)
print(df.head())

# 使用pandas处理数据，然后使用ExcelHandler写入
processed_data = df.to_dict('records')
ExcelHandler.write_excel_dict("processed_output.xlsx", processed_data)
print("与pandas集成处理完成")

# 直接使用pandas读取Excel文件（作为对比）
df_pandas = pd.read_excel("data.xlsx")
print("使用pandas读取:")
print(df_pandas.head())
```

### 大型Excel文件处理

```python
# 处理大型Excel文件
# 注意：对于非常大的Excel文件，建议使用pandas的分块读取功能

# 生成大型数据
large_data = [[f"行{i}", i, f"值{i}"] for i in range(1000)]
ExcelHandler.write_excel("large_output.xlsx", large_data)
print("大型Excel文件写入完成")

# 读取大型Excel文件
data = ExcelHandler.read_excel("large_output.xlsx")
print(f"大型Excel文件读取完成，共 {len(data)} 行")
```