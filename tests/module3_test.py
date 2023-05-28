from cisc179.module3 import Module3Class
from tkinter import simpledialog



def test_read_int():
    # Test valid input
    root = None  # Pass None as the root parameter to simulate the absence of Tkinter window
    prompt = "Enter a number from -10 to 10: "
    min_val = -10
    max_val = 10
    expected_result = 5  # Modify this to match your expected result

    # Simulate user input
    def mock_askinteger(title, prompt, **kwargs):
        return expected_result

    # Monkey patch the askinteger function with the mock function
    simpledialog.askinteger = mock_askinteger

    # Create an instance of Module3Class
    module3 = Module3Class()

    # Call the read_int method and get the actual result
    actual_result = module3.read_int(root, prompt, min_val, max_val)

    # Perform the assertion
    assert actual_result == expected_result, f"read_int test failed. Expected: {expected_result}, Actual: {actual_result}"


if __name__ == "__main__":
    # Call the test_read_int function
    test_read_int()
    print("All tests passed!")

