# Text Editor Project 2nd code.

import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        text_area.insert(1.0, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename()
    with open(file_path, 'w') as file:
        file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Success", "File saved successfully!")

root = tk.Tk()
root.title("Text Editor")

text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=1)

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