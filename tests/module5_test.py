import matplotlib.pyplot as plt
import os
from cisc179.module5 import Module5Class


def test_execute():
    # Create an instance of Module5Class
    module5 = Module5Class()

    # Call the execute method to generate the plot
    module5.execute()

    # Check if the plot image file exists
    image_file = 'module5_plot.png'
    assert os.path.exists(image_file), f"execute test failed. Plot image file '{image_file}' not found."


if __name__ == "__main__":
    # Call the test_execute function
    test_execute()
    print("All tests passed!")
