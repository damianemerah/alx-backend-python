
from typing import Generator


def my_generator() -> Generator[int, None, None]:
    yield 1
    yield 2
    yield 3


print(my_generator())
# Using the type-annotated generator
for item in my_generator():
    print(item)


def check_arguments(arg1, arg2):
    assert isinstance(
        arg1, int) and arg1 > 0, "arg1 must be an integer greater than 0"
    assert isinstance(
        arg2, int) and arg2 > 0, "arg2 must be an integer greater than 0"

    # Rest of your code here...


# Test the function with valid arguments
check_arguments(10, 5)

# Test the function with invalid arguments (will raise AssertionError)
check_arguments(0, 7)
check_arguments(3.14, 8)
check_arguments("hello", 12)
