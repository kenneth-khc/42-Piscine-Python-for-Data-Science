from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
from load_image import ft_load


def main():
    """Loads an image, crops it, transposes it, and prints its contents."""

    try:
        pixel_data = ft_load("animal.jpeg")
        if pixel_data is None:
            raise TypeError("Failed to load image.")

    except TypeError as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)

    else:
        zoomed_array = zoom_and_greyscale(pixel_data)
        transposed_array = transpose_matrix(zoomed_array)

        print(f"New shape after Transpose: {transposed_array.shape}")
        print(transposed_array)

        transposed_image = Image.fromarray(transposed_array)
        plt.imshow(transposed_image, cmap="grey")
        plt.show()


def zoom_and_greyscale(pixel_data: array) -> array:
    """Zooms into an image, converts it to greyscale and prints its contents"""

    sliced_array = pixel_data[100:500, 450:850]

    zoomed_in_image = Image.fromarray(sliced_array)
    greyscaled_image = zoomed_in_image.convert("L")

    greyscaled_pixel_data = np.array(greyscaled_image)
    if len(greyscaled_pixel_data.shape) == 2:
        greyscaled_2d = greyscaled_pixel_data
        greyscaled_3d = np.expand_dims(greyscaled_pixel_data, axis=2)

    print(f"The shape of the image is: \
{greyscaled_3d.shape} or {greyscaled_2d.shape}")
    print(greyscaled_3d)

    return greyscaled_2d


def transpose_matrix(matrix: array) -> array:
    """Transposes a matrix.

    Get the number of rows and columns.
    Initialize an empty matrix to store the transposed result.
    Copy the original matrix into the transposed one in the correct order.
    Returns the array of transposed matrix.
    """

    rows = len(matrix)
    columns = len(matrix[0])

    outer = []
    for x in range(columns):
        inner = []
        for y in range(rows):
            inner.append(0)
        outer.append(inner)

    for i in range(columns):
        for j in range(rows):
            outer[j][i] = matrix[i][j]

    result = np.array(outer)
    return result


if __name__ == "__main__":
    main()
