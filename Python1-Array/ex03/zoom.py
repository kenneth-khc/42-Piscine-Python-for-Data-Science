from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from load_image import ft_load


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
        modified_array = zoom_and_greyscale(pixel_data)
        if len(modified_array.shape) == 2:
            grey_2d_array = modified_array
            grey_3d_array = np.expand_dims(modified_array, axis=2)

        print(f"New shape after slicing: \
{grey_3d_array.shape} or {grey_2d_array.shape}")
        print(grey_3d_array)

        plt.imshow(grey_3d_array, cmap="grey")
        plt.show()


def zoom_and_greyscale(data: array) -> array:
    """Zoom into the image and convert it to greyscale."""

    sliced_data = data[100:500, 450:850]

    zoomed_in_image = Image.fromarray(sliced_data)
    greyscaled_image = zoomed_in_image.convert("L")

    greyscaled_pixel_data = np.array(greyscaled_image)
    return greyscaled_pixel_data


if __name__ == "__main__":
    main()
