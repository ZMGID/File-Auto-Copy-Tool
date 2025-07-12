#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import re
import sys
from pathlib import Path

try:
    import tkinter as tk
    from tkinter import filedialog, messagebox
    HAS_TKINTER = True
except ImportError:
    HAS_TKINTER = False

def select_folder():
    """
    使用图形界面选择文件夹，如果不可用则使用命令行输入
    """
    if HAS_TKINTER:
        try:
            root = tk.Tk()
            root.withdraw()  # 隐藏主窗口
            
            folder_path = filedialog.askdirectory(
                title="请选择包含STL文件的文件夹",
                initialdir=os.getcwd()
            )
            
            root.destroy()
            return folder_path
        except Exception as e:
            print(f"图形界面出错: {e}")
            return select_folder_console()
    else:
        return select_folder_console()

def select_folder_console():
    """
    命令行方式选择文件夹
    """
    print("请选择文件夹:")
    print("1. 输入文件夹完整路径")
    print("2. 直接回车使用程序所在目录")
    print("3. 输入 'drag' 然后拖拽文件夹到终端窗口")
    
    folder_path = input("请输入选择: ").strip()
    
    if not folder_path or folder_path.lower() == '2':
        # 获取可执行文件所在目录
        if getattr(sys, 'frozen', False):
            # 如果是打包的可执行文件
            program_dir = os.path.dirname(sys.executable)
        else:
            # 如果是Python脚本
            program_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 检查是否有STL子文件夹
        stl_dir = os.path.join(program_dir, 'STL')
        if os.path.exists(stl_dir) and os.path.isdir(stl_dir):
            folder_path = stl_dir
            print(f"找到STL文件夹: {folder_path}")
        else:
            folder_path = program_dir
            print(f"使用程序所在目录: {folder_path}")
            
    elif folder_path.lower() == 'drag':
        print("请拖拽文件夹到此窗口，然后按回车:")
        folder_path = input().strip()
        # 移除可能的引号和处理转义字符
        folder_path = folder_path.strip('"\'')
        # 处理bash转义字符
        folder_path = folder_path.replace('\\ ', ' ')
        print(f"处理后的路径: {folder_path}")
    
    return folder_path

def auto_copy_stl_files(stl_folder=None):
    """
    自动复制文件夹中带有xN字样的文件（支持所有文件类型）
    """
    if stl_folder is None:
        print("请选择包含文件的文件夹...")
        stl_folder = select_folder()
        
        if not stl_folder:
            print("未选择文件夹，程序退出。")
            return
    
    stl_path = Path(stl_folder)
    
    if not stl_path.exists():
        print(f"错误：找不到文件夹 {stl_folder}")
        return
    
    # 匹配模式：确保_x数字在文件名末尾位置（任何文件类型）
    pattern = re.compile(r'.*_x(\d+)_?\.(\w+)$', re.IGNORECASE)
    
    copied_files = []
    
    print(f"扫描文件夹: {stl_path}")
    # 扫描所有文件，不只是STL
    all_files = [f for f in stl_path.iterdir() if f.is_file()]
    
    if not all_files:
        print("该文件夹中没有找到文件。")
        return
    
    for file_path in all_files:
        match = pattern.search(file_path.name)
        
        if match:
            copies_needed = int(match.group(1))
            file_extension = match.group(2)
            base_name = file_path.stem
            extension = file_path.suffix
            
            print(f"发现需要复制的文件: {file_path.name} (需要 {copies_needed} 份)")
            
            # 复制文件 (总共需要copies_needed份，所以要复制copies_needed-1份)
            for i in range(1, copies_needed):
                new_name = f"{base_name}_copy{i}{extension}"
                new_path = stl_path / new_name
                
                # 检查文件是否已存在
                if new_path.exists():
                    print(f"  跳过已存在的文件: {new_name}")
                    continue
                
                try:
                    shutil.copy2(file_path, new_path)
                    copied_files.append(new_name)
                    print(f"  已复制: {new_name}")
                except Exception as e:
                    print(f"  复制失败 {new_name}: {e}")
    
    if copied_files:
        print(f"\n总共复制了 {len(copied_files)} 个文件:")
        for file in copied_files:
            print(f"  - {file}")
    else:
        print("没有找到需要复制的文件。")

def main():
    print("=" * 60)
    print("                文件自动复制工具")
    print("=" * 60)
    print("说明：自动识别文件名中的x2、x4等标记，复制相应数量的文件")
    print("支持：所有文件类型（不仅限于STL文件）")
    print("使用方法：选择包含文件的文件夹")
    print("=" * 60)
    print()
    
    try:
        auto_copy_stl_files()
    except KeyboardInterrupt:
        print("\n程序被用户中断。")
    except Exception as e:
        print(f"程序运行出错: {e}")
    
    print()
    print("=" * 60)
    
    # 更好的退出方式
    try:
        input("按回车键退出...")
    except (EOFError, KeyboardInterrupt):
        pass

if __name__ == "__main__":
    main()