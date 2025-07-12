# 贡献指南 (Contributing Guide)

感谢您对文件自动复制工具的关注！我们欢迎任何形式的贡献。

## 🤝 如何贡献

### 报告问题 (Bug Reports)

如果您发现了错误，请通过 [GitHub Issues](https://github.com/yourusername/file-auto-copy/issues) 提交问题报告。

**好的问题报告应该包含:**
- 清晰的标题
- 详细的问题描述
- 重现步骤
- 期望的行为
- 实际发生的行为
- 运行环境信息（操作系统、Python版本等）
- 相关的错误信息或截图

### 功能请求 (Feature Requests)

我们欢迎新功能建议！请通过 GitHub Issues 提交功能请求。

**好的功能请求应该包含:**
- 功能的详细描述
- 使用场景和需求背景
- 可能的实现方案（可选）
- 相关的截图或示例（可选）

### 代码贡献 (Code Contributions)

#### 开发环境设置

1. **Fork 仓库**
   ```bash
   # 克隆您的 fork
   git clone https://github.com/yourusername/file-auto-copy.git
   cd file-auto-copy
   ```

2. **设置开发环境**
   ```bash
   # 创建虚拟环境（推荐）
   python -m venv venv
   
   # 激活虚拟环境
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   
   # 安装开发依赖
   pip install -r requirements-dev.txt
   ```

3. **创建功能分支**
   ```bash
   git checkout -b feature/amazing-feature
   ```

#### 代码规范

- **Python 代码风格**: 遵循 PEP 8 规范
- **注释**: 使用中文注释，保持代码可读性
- **函数文档**: 重要函数需要添加文档字符串
- **变量命名**: 使用有意义的变量名

#### 提交规范

- **提交信息格式**:
  ```
  类型(范围): 简短描述
  
  详细描述（可选）
  ```

- **提交类型**:
  - `feat`: 新功能
  - `fix`: 错误修复
  - `docs`: 文档更新
  - `style`: 代码格式调整
  - `refactor`: 代码重构
  - `test`: 测试相关
  - `chore`: 构建或工具变动

- **示例**:
  ```bash
  git commit -m "feat(core): 添加支持更多文件格式的功能"
  git commit -m "fix(windows): 修复中文路径处理问题"
  git commit -m "docs: 更新README安装说明"
  ```

#### 测试

在提交之前，请确保：

1. **手动测试**
   ```bash
   # 测试基本功能
   python 源码/auto_copy_stl.py
   
   # 测试不同文件类型
   # 测试中文路径
   # 测试边界情况
   ```

2. **跨平台测试**（如果可能）
   - Windows 批处理版本
   - macOS 可执行文件版本
   - Python 源码版本

#### Pull Request 流程

1. **确保您的代码是最新的**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **推送您的分支**
   ```bash
   git push origin feature/amazing-feature
   ```

3. **创建 Pull Request**
   - 清晰的标题和描述
   - 关联相关的 Issue
   - 详细说明您的更改
   - 包含测试结果

4. **响应审核意见**
   - 及时回复审核评论
   - 根据反馈进行必要的修改
   - 保持积极的沟通态度

## 📝 文档贡献

文档改进同样重要！您可以：

- 修复拼写错误和语法问题
- 改进现有文档的清晰度
- 添加缺失的文档
- 翻译文档到其他语言

## 🎨 设计贡献

我们欢迎设计相关的贡献：

- 图标设计
- 用户界面改进建议
- 用户体验优化方案

## 📞 联系方式

如果您有任何问题，可以通过以下方式联系我们：

- GitHub Issues: [提交问题](https://github.com/yourusername/file-auto-copy/issues)
- 邮箱: your.email@example.com

## 📄 许可协议

通过贡献代码，您同意您的贡献将在 [MIT License](../LICENSE) 下发布。

---

**感谢您的贡献！** 🎉