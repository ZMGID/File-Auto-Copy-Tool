# Windows用户打包说明

## 方法1：使用批处理文件（推荐，无需Python）
- 直接双击运行 `文件自动复制工具_Windows版.bat`
- 无需安装Python或任何其他软件
- 支持拖拽文件夹

## 方法2：打包Python可执行文件
如果需要单个exe文件，请在Windows机器上执行以下步骤：

### 1. 安装Python和PyInstaller
```cmd
pip install pyinstaller
```

### 2. 下载源码文件
将 `auto_copy_stl.py` 复制到Windows机器

### 3. 打包命令
```cmd
pyinstaller --onefile --console --name "文件自动复制工具.exe" auto_copy_stl.py
```

### 4. 生成的文件
在 `dist` 目录下会生成 `文件自动复制工具.exe`

## 发布包建议
```
文件自动复制工具_Windows版/
├── 文件自动复制工具_Windows版.bat (推荐使用)
├── 文件自动复制工具.exe (可选，需要打包)
├── auto_copy_stl.py (Python源码)
└── 使用说明.txt
```

## 用户使用
Windows用户只需双击 `.bat` 文件即可使用，无需任何额外安装。