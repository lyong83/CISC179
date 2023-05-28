from tkinter import messagebox
from cisc179.module2 import Module2Class

def test_module2():
    # Create an instance of Module2Class
    module = Module2Class()

    # Execute the module
    result = module.execute()

    # Display the result in a messagebox
    messagebox.showinfo("Module2Class Result", result)

    # File Input / Output Test
    output_file = "output.txt"

    # Write the result to a file
    with open(output_file, "w") as file:
        file.write(result)

    # Read the file and display the content
    with open(output_file, "r") as file:
        content = file.read()
        messagebox.showinfo("File Content", content)

# Call the test_module2 function
test_module2()
