import decorator
from typing import Optional


@decorator.decorator
def do_twice(func: Optional[callable], *args, **kwargs) -> tuple:
    """
    A decorator that executes the function it wraps twice
    :param func: The function
    :param args: The function arguments
    :param kwargs: The function optional arguments
    :return: A tuple with the parameters returned from the functions
    """
    return func(*args, **kwargs), func(*args, **kwargs)


@do_twice
def increase_by_one(num: int) -> int:
    """
    A function to demonstrate the decorator.
    The function gets an integer and increases its value by one.
    :param num: An integer number.
    :return: The integer parameter received increased by one.
    """
    return num + 1


if __name__ == "__main__":
    print(increase_by_on(5))

