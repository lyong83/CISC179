import random
from cisc179.module4 import Module4Class

def test_module4():
    # Create an instance of Module4Class
    module4 = Module4Class()

    # Define the expected result
    expected_result = None  # Modify this to match your expected result

    # Mock the Tkinter mainloop function
    def mock_mainloop():
        return expected_result

    # Mock the random.choice function
    def mock_random_choice(options):
        return random.choice(options)

    # Patch the mainloop and random.choice functions
    module4.mainloop = mock_mainloop
    module4.random_choice = mock_random_choice

    # Call the execute method
    actual_result = module4.execute()

    # Perform the assertion
    assert actual_result == expected_result, "Event and Procedural Programming test failed"

if __name__ == "__main__":
    # Call the test_module4 function
    test_module4()
    print("All tests passed!")
