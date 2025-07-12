@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ============================================================
echo                 文件自动复制工具 (Windows版)
echo ============================================================
echo 说明：自动识别文件名中的x2、x4等标记，复制相应数量的文件
echo 支持：所有文件类型（不仅限于STL文件）
echo 使用方法：选择包含文件的文件夹
echo ============================================================
echo.

:: 获取批处理文件所在目录
set "SCRIPT_DIR=%~dp0"

echo 请选择文件夹:
echo 1. 输入文件夹完整路径
echo 2. 直接回车使用当前目录（程序所在目录）
echo 3. 拖拽文件夹到此窗口

set /p "choice=请输入选择: "

if "%choice%"=="" (
    set "folder_path=%SCRIPT_DIR%"
    :: 检查是否有STL子文件夹
    if exist "%SCRIPT_DIR%STL\" (
        set "folder_path=%SCRIPT_DIR%STL"
        echo 找到STL文件夹: !folder_path!
    ) else (
        echo 使用程序所在目录: !folder_path!
    )
) else if "%choice%"=="2" (
    set "folder_path=%SCRIPT_DIR%"
    :: 检查是否有STL子文件夹
    if exist "%SCRIPT_DIR%STL\" (
        set "folder_path=%SCRIPT_DIR%STL"
        echo 找到STL文件夹: !folder_path!
    ) else (
        echo 使用程序所在目录: !folder_path!
    )
) else (
    set "folder_path=%choice%"
    :: 移除可能的引号
    set "folder_path=!folder_path:"=!"
    echo 使用指定路径: !folder_path!
)

:: 检查目录是否存在
if not exist "!folder_path!" (
    echo 错误：目录不存在: !folder_path!
    pause
    exit /b 1
)

echo 扫描目录: !folder_path!
echo.

set copied_count=0

:: 查找所有文件并处理
for %%f in ("!folder_path!\*.*") do (
    set "filename=%%~nxf"
    set "basename=%%~nf"
    set "extension=%%~xf"
    
    :: 检查文件名是否包含_x数字_模式
    echo !filename! | findstr /r ".*_x[0-9][0-9]*_.*" >nul 2>&1
    if !errorlevel! equ 0 (
        :: 简化的数字提取（支持常见情况）
        set copies_needed=0
        
        for /l %%i in (2,1,20) do (
            echo !filename! | findstr /r "_x%%i_" >nul 2>&1
            if !errorlevel! equ 0 set copies_needed=%%i
        )
        
        if !copies_needed! gtr 1 (
            echo 发现需要复制的文件: !filename! ^(需要 !copies_needed! 份^)
            
            :: 复制文件
            for /l %%j in (1,1,!copies_needed!) do (
                if %%j lss !copies_needed! (
                    set "new_name=!basename!_copy%%j!extension!"
                    set "new_path=!folder_path!\!new_name!"
                    
                    if exist "!new_path!" (
                        echo   跳过已存在的文件: !new_name!
                    ) else (
                        copy "%%f" "!new_path!" >nul 2>&1
                        if !errorlevel! equ 0 (
                            echo   已复制: !new_name!
                            set /a copied_count+=1
                        ) else (
                            echo   复制失败: !new_name!
                        )
                    )
                )
            )
        )
    )
)

echo.
if !copied_count! gtr 0 (
    echo 总共复制了 !copied_count! 个文件
) else (
    echo 没有找到需要复制的文件
)

echo ============================================================
pause