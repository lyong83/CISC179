import tkinter as tk
from flask import Flask, render_template, request
from cisc179.base import Cisc179

app = Flask(__name__)
cisc179 = Cisc179()

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Module Execution")

        self.modules = [
            "module1",
            "module2",
            "module3",
            "module4",
            "module5",
            "module6",
        ]

        self.create_widgets()

    def create_widgets(self):
        for index, module_name in enumerate(self.modules):
            label = tk.Label(self.master, text=f"Module {index + 1}: {module_name}")
            label.pack()

            button = tk.Button(self.master, text=f"Execute Module {index + 1}",
                               command=lambda module_name=module_name: self.execute_module(module_name))
            button.pack()

    def execute_module(self, module_name):
        module_class = cisc179.get_module_by_name(module_name)
        module_instance = module_class()
        result = module_instance.execute()
        print(result)

@app.route('/')
def index():
    module_names = cisc179.module_names.values()
    return render_template('index.html', module_names=module_names)

@app.route('/execute', methods=['POST'])
def execute():
    module_name = request.form['module_name']
    module_class = cisc179.get_module_by_name(module_name)
    module_instance = module_class()
    result = module_instance.execute()
    return render_template('result.html', result=result)


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
