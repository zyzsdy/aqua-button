# 项目维护相关工具集

### 目录结构

| 文件名       | 用途                                                         |
| ------------ | ------------------------------------------------------------ |
| format.py    | 基于Pandas使用下述CSV文件生成voices.json的脚本               |
| category.csv | 存储分类的CSV                                                |
| voice.csv    | 存储声音文件的CSV 其中`category`字段务必与category中`name`字段所含项匹配 |
| README.md    | 本文档 简要记录部分使用工具，命令及规范                      |

### 规范

命名：默认voice的name字段对应`<name>.mp3`

文件格式：请使用mp3格式

填写：名称无需编号（例如：嘎 1，嘎 2）统一写嘎就可 脚本会自动添加编号

字段：归类请回避名称重复 统一驼峰式或全小写 翻译文本首字母大写

### 工具

- 脚本运行

  使用Python3.7开发 低版本应该也能跑(>=3.4) 请安装pandas依赖

  `pip3 install pandas`或`py -3 -m pip install pandas`(Windows)

- 批量转码

  可使用SHANAEncoder

- 批量去除前缀（使用正则匹配 in PowerShell）

  ```powershell
  ls | ren -NewName {$_.name -replace '^.*\[SHANA\]',''}
  ```

- 单独转码

  可使用ffmpeg

  ```shell
  ffmpeg -i <name>.wav -f mp3 <name>.mp3
  ```

