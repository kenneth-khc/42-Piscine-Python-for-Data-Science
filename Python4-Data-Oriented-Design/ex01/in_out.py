def square(x: int | float) -> int | float:
    """Returns the square of a number."""

    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns a number to the power of itself."""

    return x ** x


def outer(x: int | float, function) -> object:
    """Returns an inner function that applies a function and tracks
    how many time it is run."""

    count = 0

    def inner() -> float:
        """Applies a function to a number count amount of times."""

        nonlocal count
        count += 1
        result = x
        for _ in range(count):
            result = function(result)
        return result

    return inner
