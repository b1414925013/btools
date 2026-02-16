# CSVHandler 使用指南

`CSVHandler` 类提供了CSV文件的读写操作功能。

## 基本使用

### 读取CSV文件

```python
from btools import CSVHandler

# 基本读取
csv_data = CSVHandler.read_csv("data.csv")
print("CSV数据:", csv_data)

# 读取时跳过表头
csv_data_no_header = CSVHandler.read_csv("data.csv", skip_header=True)
print("CSV数据（无表头）:", csv_data_no_header)

# 自定义分隔符
csv_data_tab = CSVHandler.read_csv("data.tsv", delimiter="\t")
print("TSV数据:", csv_data_tab)

# 以字典形式读取（使用表头作为键）
csv_dict_data = CSVHandler.read_csv_dict("data.csv")
print("CSV字典数据:", csv_dict_data)
```

### 写入CSV文件

```python
from btools import CSVHandler

# 基本写入
data = [
    ["姓名", "年龄", "城市"],
    ["张三", 25, "北京"],
    ["李四", 30, "上海"],
    ["王五", 28, "广州"]
]
CSVHandler.write_csv("output.csv", data)
print("CSV文件写入完成")

# 写入时指定表头
data_no_header = [
    ["张三", 25, "北京"],
    ["李四", 30, "上海"],
    ["王五", 28, "广州"]
]
header = ["姓名", "年龄", "城市"]
CSVHandler.write_csv("output_with_header.csv", data_no_header, header=header)
print("带表头的CSV文件写入完成")

# 以字典形式写入
dict_data = [
    {"姓名": "张三", "年龄": 25, "城市": "北京"},
    {"姓名": "李四", "年龄": 30, "城市": "上海"},
    {"姓名": "王五", "年龄": 28, "城市": "广州"}
]
CSVHandler.write_csv_dict("output_dict.csv", dict_data)
print("字典形式CSV文件写入完成")
```

## 高级功能

### 自定义编码

```python
# 读取指定编码的CSV文件
csv_data = CSVHandler.read_csv("data.csv", encoding="utf-8")

# 写入指定编码的CSV文件
CSVHandler.write_csv("output.csv", data, encoding="utf-8")
```

### 处理引号和转义

```python
# 自定义引号字符
csv_data = CSVHandler.read_csv("data.csv", quotechar="'")

# 自定义转义字符
csv_data = CSVHandler.read_csv("data.csv", escapechar="\\")
```

### 批量处理

```python
# 批量读取多个CSV文件
files = ["data1.csv", "data2.csv", "data3.csv"]
all_data = []
for file in files:
    data = CSVHandler.read_csv(file, skip_header=True)
    all_data.extend(data)
print(f"共读取 {len(all_data)} 条记录")

# 批量写入数据到CSV文件
large_data = [[f"行{i}", i, f"值{i}"] for i in range(1000)]
CSVHandler.write_csv("large_output.csv", large_data)
print("批量写入完成")
```

### 与pandas集成

```python
import pandas as pd
from btools import CSVHandler

# 使用CSVHandler读取数据，然后转换为pandas DataFrame
csv_data = CSVHandler.read_csv_dict("data.csv")
df = pd.DataFrame(csv_data)
print(df.head())

# 使用pandas处理数据，然后使用CSVHandler写入
processed_data = df.to_dict('records')
CSVHandler.write_csv_dict("processed_output.csv", processed_data)
print("与pandas集成处理完成")
```