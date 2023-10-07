import numpy as np
from numpy import array


def ft_invert(array) -> array:
    """Inverts the color of the image received."""

    try:
        inverted_array = 255 - array
        return inverted_array

    except TypeError as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)


def ft_red(array) -> array:
    """Extracts the red channel of the image received"""

    try:
        array[:, :, 1] = 0
        array[:, :, 2] = 0
        return array

    except TypeError as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)


def ft_green(array) -> array:
    """Extracts the green channel of the image received"""

    try:
        array[:, :, 0] = 0
        array[:, :, 2] = 0
        return array

    except TypeError as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)


def ft_blue(array) -> array:
    """Extracts the blue channel of the image received"""

    try:
        array[:, :, 0] = 0
        array[:, :, 1] = 0
        return array

    except TypeError as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)


def ft_grey(array) -> array:
    """Converts the image to greyscale by summing up RGB and dividing 3"""

    try:
        sum_rgb_channels = np.sum(array, axis=2)
        grey_array = (sum_rgb_channels / 3).astype(np.uint8)
        return grey_array

    except np.exceptions.AxisError as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)
