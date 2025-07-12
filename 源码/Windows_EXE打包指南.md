# Windows EXE 打包详细步骤

## 环境要求
- Windows 10/11
- Python 3.8 或更高版本

## 步骤1：安装Python（如果没有）
1. 访问 https://www.python.org/downloads/
2. 下载并安装最新版Python
3. 安装时勾选 "Add Python to PATH"

## 步骤2：安装PyInstaller
打开命令提示符（cmd），运行：
```cmd
pip install pyinstaller
```

## 步骤3：准备文件
将以下文件复制到Windows机器的同一个文件夹中：
- auto_copy_stl.py
- (可选) STL文件夹用于测试

## 步骤4：打包命令
在包含auto_copy_stl.py的文件夹中，打开命令提示符，运行：

### 基本打包（推荐）
```cmd
pyinstaller --onefile --console --name "文件自动复制工具" auto_copy_stl.py
```

### 高级打包（带图标，可选）
如果你有图标文件icon.ico：
```cmd
pyinstaller --onefile --console --name "文件自动复制工具" --icon=icon.ico auto_copy_stl.py
```

### 无控制台版本（可选，但不推荐，因为用户看不到进度）
```cmd
pyinstaller --onefile --windowed --name "文件自动复制工具" auto_copy_stl.py
```

## 步骤5：获取exe文件
打包完成后，在 `dist` 文件夹中找到：
- `文件自动复制工具.exe`

## 步骤6：测试
1. 将exe文件复制到包含测试文件的文件夹
2. 双击运行exe文件
3. 测试各种功能

## 步骤7：清理
可以删除以下文件夹（保留exe文件）：
- `build` 文件夹
- `dist` 文件夹中除了exe外的其他文件
- `*.spec` 文件

## 最终发布包建议
```
文件自动复制工具_发布包/
├── Windows/
│   ├── 文件自动复制工具.exe (打包版本)
│   └── 文件自动复制工具_Windows版.bat (脚本版本)
├── Mac/
│   └── 文件自动复制工具 (Mac版本)
├── 源码/
│   └── auto_copy_stl.py
└── 使用说明.txt
```

## 常见问题
1. **提示缺少模块**：确保Python环境完整
2. **exe文件太大**：正常现象，大约6-8MB
3. **运行报错**：检查Python版本是否兼容
4. **中文显示问题**：确保系统支持UTF-8编码

## 注意事项
- exe文件只能在Windows上运行
- 首次运行可能被杀毒软件拦截，添加信任即可
- 建议同时提供.bat版本作为备选方案