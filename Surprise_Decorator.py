from typing import Optional
import functools


def decorator(original_func: Optional[callable]) -> Optional[callable]:
    """
    A decorator that make a function print “surprise!” instead of its original functionality.
    The outer function that gets a function as parameter and inner function that uses the
    original function but wraps it.
    :param original_func: A function as parameter
    :return inner_function: Edited function
    """
    @functools.wraps(original_func)  # Using wraps to preserve the original function name and documentation.
    def wrapper_decorator(*args, **kwargs) -> None:
        """
        inner function that uses the original function but wraps it.
        Prints 'surprise!'.
        :param args: Multiple arguments.
        :param kwargs: Multiple keyword arguments
        """
        print("Surprise!")

    return wrapper_decorator


if __name__ == "__main__":
    pass
