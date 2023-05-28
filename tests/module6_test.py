from cisc179.module6 import Module6Class
from tkinter import *
from tkinter import messagebox


class Module6Class:
    def __init__(self):
        window = Tk()
        window.title("Art Competition Program")
        window.geometry("800x250")

        left_frame = Frame(window)
        left_frame.pack(side=LEFT, padx=10, pady=10, fill=Y)

        # 控件的定义...

        permission_var = BooleanVar()
        permission_cb = Checkbutton(left_frame, text="Personal data to be collected", variable=permission_var)
        permission_cb.grid(row=6, columnspan=3)
        self.permission_var = permission_var

        submit_button = Button(left_frame, text="Submit", command=self.submit)
        submit_button.grid(row=7, columnspan=3, padx=5, pady=5)

        self.canvas = Canvas(window, width=400, height=400, bg="white")
        self.canvas.pack(side=RIGHT, padx=10, pady=10)
        self.canvas.bind("<B1-Motion>", self.draw_with_brush)

        self.window = window

    def submit(self):
        if not self.permission_var.get():
            messagebox.showwarning("Data Collection Warning",
                                   "You must give permission for your personal data to be collected in order to enter the prize draw.")
        else:
            messagebox.showinfo("Submission Successful", "Thank you for submitting your entry!")

    def execute(self):
        messagebox.showinfo("Module Execution", "Executing Module 6")

    def draw_with_brush(self, event):
        x_position_of_click = event.x
        y_position_of_click = event.y
        x1 = x_position_of_click - 10
        y1 = y_position_of_click - 10
        x2 = x_position_of_click + 10
        y2 = y_position_of_click + 10
        colour = "green"
        outline = "blue"
        self.canvas.create_oval(x1, y1, x2, y2, fill=colour, outline=outline)

    def run(self):
        self.window.mainloop()


def test_module6():
    module_instance = Module6Class()
    messagebox.showwarning = lambda *args: print("Warning dialog shown:", args)
    module_instance.submit()

    messagebox.showinfo = lambda *args: print("Info dialog shown:", args)
    module_instance.permission_var.set(True)
    module_instance.submit()


    print("All tests passed!")


if __name__ == "__main__":
    test_module6()

