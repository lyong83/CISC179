import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Module3Class:
    def execute(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main Tkinter window

        v = self.read_int(root, "Enter a number from -10 to 10: ", -10, 10)
        messagebox.showinfo("Number", f"The number is: {v}")

        root.destroy()  # Close the Tkinter window

    def read_int(self, root, prompt, min_val, max_val):
        value = simpledialog.askinteger("Input", prompt, minvalue=min_val, maxvalue=max_val, parent=root)

        if value is None:
            exit()  # Exit the program if the user cancels the input

        return value
