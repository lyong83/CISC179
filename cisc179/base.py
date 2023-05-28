from cisc179 import module1, module2, module3, module4, module5, module6

NAME = "cisc179"
class Cisc179:
    def __init__(self):
        self.module_names = {
            1: "module1",
            2: "module2",
            3: "module3",
            4: "module4",
            5: "module5",
            6: "module6",
        }

        self.modules = {
            "module1": {
                "class": module1.Module1Class,
                "content": "Inheritance, Polymorphism, Type Casting",
            },
            "module2": {
                "class": module2.Module2Class,
                "content": "File Input / Output",
            },
            "module3": {
                "class": module3.Module3Class,
                "content": "Data Validation",
            },
            "module4": {
                "class": module4.Module4Class,
                "content": "Event and Procedural Programming",
            },
            "module5": {
                "class": module5.Module5Class,
                "content": "Graphics and Charts",
            },
            "module6": {
                "class": module6.Module6Class,
                "content": "GUI",
            },
        }


    def get_module_by_name(self, module_name):
        module_info = self.modules.get(module_name)
        if module_info:
            return module_info["class"]
        raise ImportError(f"Module '{module_name}' not found")
