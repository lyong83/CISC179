from tkinter import *
from tkinter import messagebox


class Module6Class:
    def __init__(self):
        window = Tk()
        window.title("Art Competition Program")
        window.geometry("800x250")

        left_frame = Frame(window)
        left_frame.pack(side=LEFT, padx=10, pady=10, fill=Y)

        first_name_label = Label(left_frame, text="First Name:")
        first_name_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        first_name_entry = Entry(left_frame)
        first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        family_name_label = Label(left_frame, text="Family Name:")
        family_name_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        family_name_entry = Entry(left_frame)
        family_name_entry.grid(row=1, column=1, padx=5, pady=5)

        birth_date_label = Label(left_frame, text="Date of Birth:")
        birth_date_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        dob_frame = Frame(left_frame)
        dob_frame.grid(row=2, column=1, padx=5, pady=5)
        birth_date_spinbox = Spinbox(dob_frame, from_=1, to=31, width=3)
        birth_date_spinbox.pack(side=LEFT)
        Label(dob_frame, text="/").pack(side=LEFT)
        birth_month_spinbox = Spinbox(dob_frame, from_=1, to=12, width=3)
        birth_month_spinbox.pack(side=LEFT)
        Label(dob_frame, text="/").pack(side=LEFT)
        birth_year_spinbox = Spinbox(dob_frame, from_=1900, to=2023, width=5)
        birth_year_spinbox.pack(side=LEFT)

        male_label = Label(left_frame, text="Male")
        male_label.grid(row=3, column=0, sticky=W,)
        female_label = Label(left_frame, text="Female")
        female_label.grid(row=3, column=1, sticky=W,)
        unspecified_label = Label(left_frame, text="Unspecified")
        unspecified_label.grid(row=3, column=2, sticky=W,)

        male_radio = Radiobutton(left_frame, value="Male")
        male_radio.grid(row=4, column=0, sticky=W, )
        female_radio = Radiobutton(left_frame, value="Female")
        female_radio.grid(row=4, column=1, sticky=W,)
        unspecified_radio = Radiobutton(left_frame, value="Unspecified")
        unspecified_radio.grid(row=4, column=2, sticky=W,)

        student_var = BooleanVar()
        student_cb = Checkbutton(left_frame, text="Student", variable=student_var)
        student_cb.grid(row=5, column=0, sticky=W)

        worker_var = BooleanVar()
        worker_cb = Checkbutton(left_frame, text="Worker Bee", variable=worker_var)
        worker_cb.grid(row=5, column=1, sticky=W)

        influencer_var = BooleanVar()
        influencer_cb = Checkbutton(left_frame, text="Influencer", variable=influencer_var)
        influencer_cb.grid(row=5, column=2, sticky=W)

        permission_var = BooleanVar()
        permission_cb = Checkbutton(left_frame, text="Personal data to be collected", variable=permission_var)
        permission_cb.grid(row=6, columnspan=3)
        self.permission_var = permission_var

        submit_button = Button(left_frame, text="Submit", command=self.submit)
        submit_button.grid(row=7, columnspan=3, padx=5, pady=5)

        self.canvas = Canvas(window, width=400, height=400, bg="white")
        self.canvas.pack(side=RIGHT, padx=10, pady=10)
        self.canvas.bind("<B1-Motion>", self.draw_with_brush)

        window.mainloop()

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


