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


if __name__ == "__main__":
    pass
