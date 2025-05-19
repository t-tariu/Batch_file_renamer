import os
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files():
    folder = folder_path.get()
    prefix = name_prefix.get()
    ext = extension.get().strip().lower()

    if not folder or not prefix or not ext:
        messagebox.showerror("오류", "모든 항목을 입력해주세요.")
        return

    # 파일 목록 가져오기
    files = sorted([
        f for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(ext)
    ])

    if not files:
        messagebox.showwarning("알림", f"확장자 '{ext}'를 가진 파일이 없습니다.")
        return

    # 리네이밍
    for i, filename in enumerate(files, 1):
        _, file_ext = os.path.splitext(filename)
        new_name = f"{prefix}_{i:02d}{file_ext}"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

    messagebox.showinfo("완료", f"{len(files)}개의 파일 이름이 변경되었습니다.")

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

# GUI 구성
root = tk.Tk()
root.title("파일 이름 일괄 변경기")
root.geometry("400x250")
root.resizable(False, False)

folder_path = tk.StringVar()
name_prefix = tk.StringVar()
extension = tk.StringVar()

tk.Label(root, text="1. 폴더 선택:").pack(anchor='w', padx=10, pady=(10, 0))
tk.Entry(root, textvariable=folder_path, width=40).pack(padx=10, pady=5)
tk.Button(root, text="폴더 찾기", command=select_folder).pack()

tk.Label(root, text="2. 원하는 이름름 입력 (예: asyLove):").pack(anchor='w', padx=10, pady=(10, 0))
tk.Entry(root, textvariable=name_prefix, width=30).pack(padx=10, pady=5)

tk.Label(root, text="3. 확장자 입력 (예: .mp4, .jpg, .png):").pack(anchor='w', padx=10, pady=(10, 0))
tk.Entry(root, textvariable=extension, width=20).pack(padx=10, pady=5)

tk.Button(root, text="파일 이름 바꾸기", command=rename_files, bg="#4CAF50", fg="white").pack(pady=15)

root.mainloop()





