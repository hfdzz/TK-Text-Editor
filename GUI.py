import tkinter as tk
from tkinter import filedialog

# TK ROOT
root = tk.Tk()

# ===== #
# App
# ===== #

# Head
root.title("Text Editor")

# Window Size
# root.geometry("800x800")

# Frames
frm_side_menu = tk.Frame(root,
    background="red"
    )
frm_editor= tk.Frame(root,
    background="blue"
    )

# ===== #
# Side Menu
# ===== #

# Buttons
btn_open = tk.Button(frm_side_menu,
    text="Open",
    height=1,
    width=10
    )
btn_open.pack()
btn_save = tk.Button(frm_side_menu,
    text="Save",
    height=1,
    width=10
    )
btn_save.pack()

# ===== #
# Main Editor
# ===== #

# Text
txt_main_editor = tk.Text(frm_editor,
    background="#3f3f3f",
    foreground="white",
    borderwidth=0
)
txt_main_editor.pack(fill=tk.BOTH, expand=True)

# Packs
frm_side_menu.pack(side=tk.LEFT, fill=tk.Y)
frm_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# ===== #
# Logics/Commands
# ===== #

# Global Var
f = None                # Current wokring file
file_opened = False     # File opened status

# Callback Function
def open_file():
    global f
    global file_opened
    if file_opened:
        f.close()
    fd = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")],
        title="Open Text File..."
    )
    if fd:
        f = open(fd, "r")
        txt_main_editor.delete("1.0", tk.END)
        txt_main_editor.insert("1.0", f.read())
        file_opened = True

def save_file():
    global f
    global file_opened
    if file_opened:
        fw = open(f.name, "w")
        fw.write(txt_main_editor.get("1.0", tk.END)[:-1])
        fw.close()
    else:
        fd = filedialog.asksaveasfile(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Save as...",
            defaultextension="*.*"
        )
        f = open(fd.name, "w")
        f.write(txt_main_editor.get("1.0", tk.END)[:-1])
        file_opened = True

# Buttons Command
btn_open["command"] = open_file
btn_save["command"] = save_file

# MAINLOOP
root.mainloop()