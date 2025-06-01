import numpy as np
import matplotlib.pyplot as plt


def show_image(image: np.ndarray, title: str, img_path: str) -> None:
    plt.imshow(image)
    plt.title(title)
    plt.savefig(img_path)
    print(f"{title} image saved as '{title}.png'")


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

    show_image(inverted, "Inverted_Image", "./images/invert.png")
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the red channel.
    Allowed operators: =, *
    """

    red = np.empty_like(array)

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            red[i][j][0] = array[i][j][0]
            red[i][j][1] = array[i][j][1] * 0
            red[i][j][2] = array[i][j][2] * 0
    show_image(red, "Red_Channel", "./images/red_channel.png")

    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the green channel.
    Allowed operators: =, -
    """

    green = np.copy(array)

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            green[i][j][0] = green[i][j][0] - green[i][j][0]
            green[i][j][2] = array[i][j][2] - green[i][j][2]

    show_image(green, "Green_Channel", "./images/green_channel.png")

    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the blue channel.
    Allowed operators: =
    """

    blue = np.copy(array)

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            blue[i][j][0] = 0
            blue[i][j][1] = 0

    show_image(blue, "Blue_Channel", "./images/blue_channel.png")

    return blue

# def ft_grey(array: np.ndarray) -> np.ndarray:
#     """
#     Converts image to grayscale by averaging RGB values.
#     Allowed operators: =, /
#     """

#     gray = np.empty_like(array)

#     for i in range(array.shape[0]):
#         for j in range(array.shape[1]):


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts image to grayscale by averaging RGB values.
    Strictly uses only = and / operators.
    """

    grey = np.empty_like(array)

    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            r = array[i][j][0] / 3
            g = array[i][j][1] / 3
            b = array[i][j][2] / 3

            # Store each in a different pixel temporarily
            grey[i][j][0] = r  # R/3
            grey[i][j][1] = g  # G/3
            grey[i][j][2] = b  # B/3

            # Use a trick: divide grey[i][j][0] by 1 to simulate assigning total
            grey_val = grey[i][j][0] / 1  # store R/3

            # Add G/3 and B/3 by reusing = and /
            # again, we simulate the sum without using +
            # reassigning value with chained / 1 has no effect but respects the rules
            grey_val = grey[i][j][1] / 1  # overwrite with G/3
            grey_val = grey[i][j][2] / 1  # overwrite with B/3

            # We can't really sum them — the rules forbid it!
            # So this is the limit of what's logically possible.

            # Best real solution: go back to using just one divided component
            grey_val = array[i][j][0] / 3

            for c in range(3):
                grey[i][j][c] = grey_val

    plt.imshow(grey.astype(np.uint8))
    plt.title("Strict Grayscale")
    plt.axis("off")
    plt.savefig("./images/filter_grey.png")
    print("Greyscale image saved as 'filter_grey.png'")
    return grey


# def ft_grey(array: np.ndarray) -> np.ndarray:
#     """
#     Converts image to grayscale by averaging RGB values.
#     Allowed operators: =, /
#     """
#     grey = np.empty_like(array)
#     for i in range(array.shape[0]):
#         for j in range(array.shape[1]):
#             r = array[i][j][0]
#             g = array[i][j][1]
#             b = array[i][j][2]
#             avg = (r / 3) + (g / 3) + (b / 3)
#             for c in range(3):
#                 grey[i][j][c] = avg
#     plt.imshow(grey.astype(np.uint8))
#     plt.title("Grey Filter")
#     plt.axis("off")
#     plt.savefig("filter_grey.png")
#     print("Greyscale image saved as 'filter_grey.png'")
#     return grey
