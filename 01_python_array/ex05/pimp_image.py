import numpy as np
import PIL.Image


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image.
    Each RGB value becomes 255 - value.
    """
    try:
        inverted = 255 - array
        PIL.Image.fromarray(inverted).show()
        return inverted
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the red channel.
    Allowed operators: =, *
    """

    try:
        red_array = array[:, :, 0]
        red_np = np.stack([red_array,
        np.zeros_like(red_array),
        np.zeros_like(red_array)], axis=2)
        PIL.Image.fromarray(red_np).show()
        return red_np
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the green channel.
    Allowed operators: =, -
    """

    try:
        image = array.copy()
        image[:, :, 0] = 0
        image[:, :, 2] = 0
        PIL.Image.fromarray(image).show()
        return image
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the blue channel.
    Allowed operators: =
    """

    try:
        blue_array = array[:, :, 2]
        image = np.zeros_like(array)
        image[:, :, 2] = blue_array
        PIL.Image.fromarray(image).show()
        return image
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts image to grayscale by averaging RGB values.
    Strictly uses only = and / operators.
    """
    try:
        grey_array = np.mean(array, axis=2, keepdims=True)
        image = np.squeeze(grey_array, axis=2)
        PIL.Image.fromarray(image).show()
        return image
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass
