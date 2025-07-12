# 文件自动复制工具 - 源码说明

## 文件说明
- `auto_copy_stl.py` - 主程序源码（Python）
- `Windows_EXE打包指南.md` - Windows EXE打包详细步骤
- `Windows打包说明.md` - Windows版本开发说明

## 源码特性
- 跨平台兼容（Mac/Windows/Linux）
- 支持图形界面和命令行两种文件选择方式
- 智能路径处理（转义字符、拖拽支持）
- 正则表达式匹配文件名模式
- 防重复复制机制

## 开发环境
- Python 3.8+
- 标准库：os, shutil, re, sys, pathlib
- 可选库：tkinter（图形界面）

## 打包说明

### Mac平台
```bash
pyinstaller --onefile --console --name "文件自动复制工具" auto_copy_stl.py
```

### Windows平台
```cmd
pyinstaller --onefile --console --name "文件自动复制工具" auto_copy_stl.py
```

### Linux平台
```bash
pyinstaller --onefile --console --name "文件自动复制工具" auto_copy_stl.py
```

## 功能扩展
- 可以修改正则表达式支持更多文件名格式
- 可以添加GUI界面
- 可以添加配置文件支持
- 可以添加日志记录功能

## 许可协议
此源码可自由使用、修改和分发。