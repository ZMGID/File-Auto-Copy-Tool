@echo off
echo ================================================================
echo                Windows EXE 自动打包脚本
echo ================================================================
echo.
echo 此脚本将自动安装PyInstaller并打包Python程序为EXE文件
echo.
pause

echo 正在检查Python环境...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误：未找到Python，请先安装Python
    echo 下载地址：https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python环境检查通过
echo.

echo 正在安装PyInstaller...
pip install pyinstaller
if %errorlevel% neq 0 (
    echo 错误：PyInstaller安装失败
    pause
    exit /b 1
)

echo.
echo 正在打包程序...
pyinstaller --onefile --console --name "文件自动复制工具" auto_copy_stl.py

if %errorlevel% neq 0 (
    echo 错误：打包失败
    pause
    exit /b 1
)

echo.
echo ================================================================
echo                        打包完成！
echo ================================================================
echo.
echo 生成的EXE文件位置：dist\文件自动复制工具.exe
echo.
echo 正在清理临时文件...
rmdir /s /q build 2>nul
del *.spec 2>nul

echo.
echo 打包完成！请查看dist文件夹中的EXE文件
echo.
pause