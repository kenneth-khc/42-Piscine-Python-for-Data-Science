def ft_statistics(*args: any, **kwargs: any) -> None:
    """Takes in a quantity of numbers and does statistical operations."""

    try:
        if len(args) == 0:
            raise AssertionError
        if not valid_args(args):
            raise TypeError("Not a list of numbers!")
    except AssertionError:
        print_errors(kwargs)
    except TypeError as e:
        print(f"Error: {e}")

    else:
        mean = sum(args) / len(args)
        median = find_median(list(args))
        quartiles = find_quartiles(list(args))
        variance = find_variance(list(args), mean)
        std_dev = variance ** 0.5

        for value in kwargs.values():
            if value == "mean":
                print(f"mean: {mean}")
            if value == "median":
                print(f"median: {median}")
            if value == "quartile":
                print(f"quartiles: {quartiles}")
            if value == "std":
                print(f"std : {std_dev}")
            if value == "var":
                print(f"var : {variance}")


def valid_args(args: list[int | float]):
    """Validate the arguments passed in to the program to be int or floats."""

    for i in args:
        if not isinstance(i, (int, float)):
            return False

    return True


def find_median(numbers: list) -> float:
    """Find the median of a list of numbers."""

    numbers.sort()
    list_len = len(numbers)
    if list_len % 2 != 0:
        median = numbers[list_len // 2]
    else:
        median = (numbers[list_len // 2 - 1] + numbers[list_len // 2]) / 2

    return median


def find_quartiles(numbers: list) -> list[float]:
    """Find the 25% and 75% quartiles in a list of numbers."""

    numbers.sort()
    list_len = len(numbers)
    lower_half = numbers[:list_len // 2]
    upper_half = numbers[list_len // 2:]

    q1 = lower_half[len(lower_half) // 2]
    q2 = upper_half[len(upper_half) // 2]

    return [float(q1), float(q2)]


def find_variance(numbers: list, mean: float) -> float:
    """Calculate the variance of a list of numbers.

        Variance is the measure of how spread out data is from the mean.
        The variance is calculated by taking the average of
        the difference of each value with the mean, squared.
    """

    squared_differences = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_differences) / len(numbers)

    return variance


def print_errors(kwargs: any):
    """Cheeky way to print error messages because I want to be funny."""

    valid_operations = ["mean", "median", "quartile", "std", "var"]
    num_of_errors = 0

    for kwarg in kwargs.values():
        if kwarg in valid_operations:
            num_of_errors += 1

    print("ERROR\n" * num_of_errors, end="")
