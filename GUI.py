import tkinter as tk
from tkinter import filedialog

# TK ROOT
root = tk.Tk()

# ===== #
# App
# ===== #

# Head
CONST_app_name = "Text Editor"
root.title(CONST_app_name)

# Root Window Size
root.geometry("900x800")
root.minsize(0,800) # Tinggi minimal window 800px (sesuai spesifikasi tugas)

# Root Grid Configuration
root.rowconfigure(0, weight=1,minsize=100)
root.columnconfigure(0, weight=0, minsize=100)
root.columnconfigure(1, weight=1, minsize=100)

# Root Frames
frm_side_menu = tk.Frame(root,
    background="#4f4f4f"
    )
frm_side_menu.grid(row=0, column=0, sticky="ns")
frm_editor= tk.Frame(root,
    background="#3f3f3f"
    )
frm_editor.grid(row=0,column=1, sticky="nswe")

# ===== #
# Side Menu
# ===== #

# Buttons
btn_open = tk.Button(frm_side_menu,
    text="Open",
    height=1,
    width=10
    )
btn_open.grid(row=0, column=0, padx=10,pady=(10,5))
btn_save = tk.Button(frm_side_menu,
    text="Save",
    height=1,
    width=10
    )
btn_save.grid(row=1, column=0, padx=10,pady=5)

# ===== #
# Main Editor
# ===== #

# Textbox
txt_main_editor = tk.Text(frm_editor,
    background="#3f3f3f",
    # background="red", # For debugging purpose
    foreground="white",
    borderwidth=0,
    insertbackground="white"
)
txt_main_editor.grid(column=0, row=0, padx=10, pady=10, sticky="nswe")
# Frame Editor Grid Config
frm_editor.rowconfigure(0, weight=1)
frm_editor.columnconfigure(0, weight=1, minsize=800,)

# ===== #
# Logics/Commands
# ===== #

# Global Var
f_opened = False    # File open status
f_name = None       # Opened file name

# Callback Function
def open_file():
    global f_opened
    global f_name

    fd = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files","*.*")],
        title="Open Text File..."
    )
    if fd:
        # If a file is selected
        with open(fd, "r") as f:
            txt_main_editor.delete("1.0", tk.END)
            txt_main_editor.insert("1.0", f.read())
            root.title(f"{CONST_app_name} - {f.name}")
            f_name = f.name
            f_opened = True

def save_file() -> int: 
    global f_opened
    global f_name

    if f_opened:
        # Save opened file
        with open(f_name, "w") as fw:
            fw.write(txt_main_editor.get("1.0", tk.END)[:-1])
    else:
        # If no file is opened, do save as..
        fd = filedialog.asksaveasfile(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Save as...",
            defaultextension="*.*"
        )
        if fd:
            with open(fd.name, "w") as fw:
                fw.write(txt_main_editor.get("1.0", tk.END)[:-1]) # [:-1] avoid 'newline' from tk.END
                root.title(f"{CONST_app_name} - {fw.name}")
                f_opened = True
                f_name = fw.name

# Buttons Command
btn_open["command"] = open_file
btn_save["command"] = save_file

# MAINLOOP
root.mainloop()