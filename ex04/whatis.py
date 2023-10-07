import sys


def is_integer(string: str) -> bool:
    """Checks whether a string can be converted to an int."""

    try:
        int(string)
        return True
    except ValueError:
        return False


try:
    if len(sys.argv) == 1:
        exit(0)
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    if not is_integer(sys.argv[1]):
        raise AssertionError("argument is not an integer")

    integer = int(sys.argv[1])
    if integer % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(f"AssertionError: {e}")
