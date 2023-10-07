from PIL import Image
from numpy import array
import numpy as np


def ft_load(path: str) -> array:
    """Loads image, converts it to RGB, returns array of the image's pixels"""

    try:
        img = Image.open(path)
        if img.mode != "RGB":
            img = img.convert("RGB")
        pixel_data = np.array(img)

    except (FileNotFoundError, Exception) as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)
        return None

    return pixel_data
