import sys
from ft_filter import ft_filter


def is_integer(string) -> bool:
    """
    Check if string is integer.
    """
    try:
        int(string)
        return True
    except ValueError:
        return False


def filter_string(string: str, length: int) -> list:
    """
    Splits the string into words and filters the words
    that are less in length.
    """
    split_words = string.split()
    filtered_strings = ft_filter(lambda word: len(word) > length, split_words)
    return filtered_strings


def main():
    """Handle bad arguments and calls filter_string to filter.

    Arguments:
    argv[1] (str): The string to be split and filtered
    argv[2] (int): The number to compare words against

    Returns:
    A list containing the filtered words
    """
    try:
        assert len(sys.argv) == 3, "text"
        assert is_integer(sys.argv[2])
    except AssertionError:
        print("AssertionError: the arguments are bad")
    else:
        filtered_string = filter_string(sys.argv[1], int(sys.argv[2]))
        print(filtered_string)


if __name__ == "__main__":
    main()
