from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def main():
    pixel_data = ft_load("animal.jpeg")
    zoomed_in = pixel_data[100:500, 450:850]
    img = Image.fromarray(zoomed_in)
    img = img.convert("L")
    greyscaled = np.array(img)
    two_dim = greyscaled
    if len(greyscaled.shape) == 2:
        greyscaled = np.expand_dims(greyscaled, axis=2)
    print(f"New shape after slicing: {greyscaled.shape} or {two_dim.shape}")
    print(greyscaled)
    plt.imshow(greyscaled, cmap="grey")
    plt.show()

if __name__ == "__main__":
    main()