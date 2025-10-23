# Rent Calculator with GUI using Tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

# Function to calculate per person cost
def calculate():
    try:
        rent = float(rent_entry.get())
        food = float(food_entry.get())
        electricity = float(electricity_entry.get())
        charge_per_unit = float(charge_entry.get())
        no_of_person = int(person_entry.get())

        total_bill = electricity * charge_per_unit
        total = (rent + total_bill + food) / no_of_person

        result_label.config(text=f"Per Person Total: {total:.2f} Pkr")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# --- Main window ---
root = tk.Tk()
root.title("Expense Splitter")
root.geometry("400x420")
root.configure(bg="#f5f5f5")
root.resizable(False, False)

# --- Fonts ---
heading_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
label_font = tkfont.Font(family="Helvetica", size=10)

# --- Frame Container ---
container = tk.Frame(root, padx=20, pady=20, bg="#ffffff", relief="ridge", bd=2)
container.pack(pady=20)

# --- Heading ---
tk.Label(container, text="Monthly Expense Splitter", font=heading_font, bg="#ffffff", fg="#333").grid(row=0, column=0, columnspan=2, pady=(0, 20))

# --- Labels and Entry Fields ---
labels = ["Rent", "Food", "Electricity (Units)", "Charge per Unit", "Number of Persons"]
entries = []

for i, label in enumerate(labels):
    tk.Label(container, text=label, font=label_font, bg="#ffffff").grid(row=i+1, column=0, sticky="e", pady=5, padx=10)
    entry = tk.Entry(container, width=25)
    entry.grid(row=i+1, column=1, pady=5)
    entries.append(entry)

rent_entry, food_entry, electricity_entry, charge_entry, person_entry = entries

# --- Calculate Button ---
tk.Button(container, text="Calculate", command=calculate, bg="#4CAF50", fg="white", padx=10, pady=5, relief="flat").grid(row=7, column=0, columnspan=2, pady=20)

# --- Result Label ---
result_label = tk.Label(container, text="Per Person Total: ---", font=label_font, bg="#ffffff", fg="#000")
result_label.grid(row=8, column=0, columnspan=2, pady=10)

# --- Start GUI ---
root.mainloop()
