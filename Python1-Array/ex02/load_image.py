from PIL import Image
from numpy import array
import numpy as np


def ft_load(path: str) -> array:
    """
    Loads an image, converts it to RGB and prints its pixel contents.
    """

    try:
        img = Image.open(path)
        if img.mode != "RGB":
            img = img.convert("RGB")
        pixel_array = np.array(img)

    except (FileNotFoundError, Exception) as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)
        return None

    print(f"The shape of image is: {pixel_array.shape}")
    print(pixel_array)
    return pixel_array
