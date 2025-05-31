import numpy as np
import matplotlib.pyplot as plt
import load_image

def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image.
    Each RGB value becomes 255 - value.
    Allowed operators: =, +, -, *
    """
    inverted = np.empty_like(array)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            for c in range(3):
                inverted[i, j, c] = 255 - array[i, j, c]

    plt.imshow(inverted)
    plt.title("Inverted Image")
    plt.savefig("./images/filter_invert.png")
    print("Inverted image saved as 'filter_invert.png'")
    return inverted
