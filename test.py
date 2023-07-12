from typing import Generator


def my_generator() -> Generator[int, None, None]:
    yield 1
    yield 2
    yield 3


print(my_generator())
# Using the type-annotated generator
for item in my_generator():
    print(item)
