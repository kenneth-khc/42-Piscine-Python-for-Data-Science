import sys


def is_integer(string: str) -> bool:
    try:
        int(string)
        return True
    except ValueError:
        return False


if len(sys.argv) > 1:
    try:
        assert len(sys.argv) == 2, (
            "AssertionError: more than one argument is provided"
        )
        assert is_integer(sys.argv[1]), (
            "AssertionError: argument is not an integer"
        )
        integer = int(sys.argv[1])
        if integer % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as error:
        print(error)
