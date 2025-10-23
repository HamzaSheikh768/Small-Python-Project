#====================Build a Digital Clock====================#
# import tkinter as tk
# from time import strftime

# root = tk.Tk()
# root.title("Digital Clock")

# def time():
#     string = strftime('%H:%M:%S %p')
#     label.config(text=string) #
#     label.after(1000, time) # 

# label = tk.Label(root, font = ("caliber", 50, "bold"), background = "black", foreground = "dark green")
# label.pack(anchor='center')

# time()
# root.mainloop()


#  IS MEIN TIME FUNCTION KO UPDATE KIA GYA HAI DAY, MONTHS, YEARS

# Import required modules
import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Function to update time
def time():
    string = strftime("%H:%M:%S %p\n%d/%m/%Y")  # Format: HH:MM:SS AM/PM, Day/Month/Year
    label.config(text=string)  # Update the label with the current time
    label.after(1000, time)   # Call this function again after 1000ms (1 second)

# Create and configure the label
label = tk.Label(root, font=('calibri', 40, 'bold'), background='dark green', foreground='black')
label.pack(anchor="center")

# Start the clock
time()

# Run the application
root.mainloop()