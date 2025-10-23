# Text Editor Project.

import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    global text
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt", filetypes=[("Text File", ".txt")]
    )
    if file_path:
        global text
    with open(file_path, 'r') as file:
        text.insert(1.0, file.read())
        text.delete(1.0, tk.END)

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text File", ".txt")]
    )
    if file_path:
        global text
    with open(file_path, 'w') as file:
        file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Success", "File saved successfully!")

root = tk.Tk()
root.title("Text Editor")
root.geometry("600x400")

text = tk.Text(root, warp=tk.WORD, font=("Helvetica", 12), fg="blue")
text.pack(fill=tk.BOTH, expand=1)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()

