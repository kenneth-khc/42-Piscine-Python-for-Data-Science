import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Prints the shape of a 2D array and slices it according
    to the start and end indexes passed into the function.
    """

    try:
        validate_list(family, start)
        array = np.array(family)

    except (TypeError, ValueError, IndexError) as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)
        return None

    print(f"My shape is : {array.shape}")
    truncated_array = array[start:end]
    print(f"My new shape is : {truncated_array.shape}")
    truncated_list = truncated_array.tolist()
    return truncated_list


def validate_list(family, start: int):
    """Validate the list to be sliced."""

    if not isinstance(family, list):
        raise TypeError("Family is not a list!")

    if not family:
        raise ValueError("List is empty!")

    for i in family:
        if not isinstance(i, list):
            raise TypeError("Not a list of lists!")

    if start >= len(family):
        raise ValueError("Starting index to slice is bigger than the list!")
