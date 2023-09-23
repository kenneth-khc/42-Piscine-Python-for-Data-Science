from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def main():
    """Loads an image, zooms in on it, and prints its new details.

The image loaded converted to an array which is then sliced to zoom
into a portion of it. The array is then converted back to an image
to be converted into greyscale. Afterwards, expand another dimension
on the new array to print its greyscale channel as part of its shape.
    """
    try:
        pixel_data = ft_load("animal.jpeg")
        if pixel_data is None:
            raise TypeError("Failed to load image.")

    except TypeError as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)

    else:
        zoomed_in = pixel_data[100:500, 450:850]
        zoomed_in_image = Image.fromarray(zoomed_in)
        greyscaled_image = zoomed_in_image.convert("L")

        greyscaled_pixel_data = np.array(greyscaled_image)

        if len(greyscaled_pixel_data.shape) == 2:
            greyscaled_2d = greyscaled_pixel_data
            greyscaled_3d = np.expand_dims(greyscaled_pixel_data, axis=2)

        print(f"New shape after slicing: \
{greyscaled_3d.shape} or {greyscaled_2d.shape}")
        print(greyscaled_3d)
        plt.imshow(greyscaled_3d, cmap="grey")
        plt.show()


if __name__ == "__main__":
    main()
