from tkinter import messagebox

class Module2Class:
    def execute(self):
        # Add your execution logic here
        zoo = ["lion", "elephant", "monkey"]
        number = 15
        output = ""

        output += ' and '.join(zoo)
        output += '\n'
        # Add the number to the output as well
        output += str(number)

        return output

if __name__ == "__main__":
    module = Module2Class()
    result = module.execute()
    messagebox.showinfo("Module2Class Result", result)
