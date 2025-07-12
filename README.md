# 文件自动复制工具 (File Auto-Copy Tool)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue.svg)](https://github.com/ZMGID/File-Auto-Copy-Tool)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://www.python.org/)

一个智能的文件复制工具，可以根据文件名中的数字标记（如 `_x2_`, `_x4_`）自动复制指定数量的文件。支持所有文件格式，完美适用于3D打印、文档管理等场景。

## ✨ 主要功能

- 🎯 **智能识别**: 自动识别文件名中的 `_x2_`, `_x4_` 等复制标记
- 📁 **全格式支持**: 支持所有文件类型（STL、PDF、JPG、TXT、DOC等）
- 🔄 **防重复**: 自动跳过已存在的复制文件，支持多次运行
- 🖱️ **拖拽支持**: 支持拖拽文件夹操作
- 🌍 **中文支持**: 完美支持中文路径和文件名
- 💻 **跨平台**: Windows、macOS、Linux 全平台支持
- 🚀 **零依赖**: 无需安装Python环境（提供独立可执行文件）

## 📋 使用示例

| 原文件名 | 复制结果 | 说明 |
|---------|---------|------|
| `零件_x2_.stl` | `零件_x2_.stl` + `零件_x2__copy1.stl` | 总共2份 |
| `文档_x3_.pdf` | 原文件 + 2个副本 | 总共3份 |
| `图片_x5_.jpg` | 原文件 + 4个副本 | 总共5份 |

## 🚀 快速开始

### 下载预编译版本（推荐）

#### Windows 用户
1. 进入 `Windows/` 文件夹
2. 双击运行 `文件自动复制工具_Windows版.bat`
3. 按提示选择文件夹

#### macOS 用户  
1. 进入 `Mac/` 文件夹
2. 双击运行 `文件自动复制工具`
3. 按提示选择文件夹

### 从源码运行

```bash
# 克隆仓库
git clone https://github.com/ZMGID/File-Auto-Copy-Tool.git
cd File-Auto-Copy-Tool

# 运行程序
python 源码/auto_copy_stl.py
```

## 📁 项目结构

```
File-Auto-Copy-Tool/
├── Mac/                              # macOS 版本
│   ├── 文件自动复制工具               # macOS 可执行文件
│   └── 使用说明.txt                   # macOS 使用说明
├── Windows/                          # Windows 版本
│   ├── 文件自动复制工具_Windows版.bat  # Windows 批处理版本
│   ├── 自动打包EXE.bat               # 自动打包 EXE 脚本
│   └── 使用说明.txt                   # Windows 使用说明
├── 源码/                             # 源代码
│   ├── auto_copy_stl.py              # 主程序源码
│   ├── Windows_EXE打包指南.md         # EXE 打包指南
│   └── README.md                     # 源码技术文档
├── docs/                             # 文档
│   ├── CHANGELOG.md                  # 更新日志
│   └── CONTRIBUTING.md               # 贡献指南
├── README.md                         # 项目说明（本文件）
├── LICENSE                           # 开源协议
└── .gitignore                        # Git 忽略文件
```

## 🛠️ 自定义打包

### Windows EXE 打包
```cmd
# 安装依赖
pip install pyinstaller

# 自动打包（推荐）
cd Windows/
双击运行 自动打包EXE.bat

# 或手动打包
pyinstaller --onefile --console --name "文件自动复制工具" 源码/auto_copy_stl.py
```

### macOS 打包
```bash
# 安装依赖
pip install pyinstaller

# 打包
pyinstaller --onefile --console --name "文件自动复制工具" 源码/auto_copy_stl.py
```

## 💡 使用场景

- **3D 打印**: 自动复制需要多个副本的 STL 文件
- **文档管理**: 批量复制需要多份的文档
- **设计工作**: 复制需要多个版本的设计文件
- **备份管理**: 根据需求自动生成文件副本

## 📖 详细文档

- [更新日志](docs/CHANGELOG.md)
- [贡献指南](docs/CONTRIBUTING.md)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📄 开源协议

本项目采用 MIT 协议开源 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🌟 Star History

如果这个项目对您有帮助，请给个 ⭐️ Star 支持一下！

## 📞 联系方式

- 提交 Issue: [GitHub Issues](https://github.com/ZMGID/File-Auto-Copy-Tool/issues)

---

**Made with ❤️ by [ZMGID](https://github.com/ZMGID)**
