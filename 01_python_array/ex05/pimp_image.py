import numpy as np
import matplotlib.pyplot as plt


def show_image(image: np.ndarray, title: str):
    """Display Image on the screen."""
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image.

    Each RGB value becomes 255 - value.
    """
    try:
        image = (255 - array).astype(np.uint8)
        show_image(image, "Invert")
        return image
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red channel.

    Allowed operators: =, *
    """

    try:
        red_channel = array[:, :, 0]
        image = np.stack(
            [
                red_channel,
                np.zeros_like(red_channel),
                np.zeros_like(red_channel),
            ],
            axis=2,
        )

        show_image(image, "Red")
        return image
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps only the green channel.

    Allowed operators: =, -
    """

    try:
        image = array.copy()
        image[:, :, 0] = 0
        image[:, :, 2] = 0
        show_image(image, "Green")
        return image
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps only the blue channel.

    Allowed operators: =
    """

    try:
        blue_channel = array[:, :, 2]
        image = np.zeros_like(array)
        image[:, :, 2] = blue_channel
        show_image(image, "Blue")
        return image
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts RGB to grayscale using only = and / operators."""
    try:
        grey = (array[:, :, 0] / 3) + (array[:, :, 1] / 3)
        +(array[:, :, 2] / 3)
        grey = grey.astype(np.uint8)

        plt.imshow(grey, cmap="gray")
        plt.title("Grey")
        plt.axis("off")
        plt.show()
        return grey
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


# def ft_grey(array) -> np.ndarray:
#     """
#     Converts RGB to grayscale using only = and / operators.
#     """
#     try:
#         grey = np.mean(array, axis=2, keepdims=True)
#         np_grey = np.squeeze(grey, axis=2)
#         plt.imshow(np_grey, cmap='gray')
#         plt.axis('off')
#         plt.show()
#         return np_grey
#     except Exception as e:
#         print("Exception:", e)
#     except KeyboardInterrupt:
#         pass
