import numpy as np
import PIL.Image
import os


def ft_load(path: str) -> np.ndarray:
    """Loads an image file and returns its RGB pixel data as a NumPy array.

    Prints the shape and the content.
    """

    if not isinstance(path, str):
        print("Error: Path must be a string.")
        return None

    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found: ", path)
        with PIL.Image.open(path) as img:
            img = img.convert("RGB")
            img_array = np.array(img)
            print(f"The shape of image is: {img_array.shape}")
            print(img_array)
            return img_array

    except OSError:
        print(f"Error: '{path}' is not a valid image file.")
        return None
    except KeyboardInterrupt:
        return None
    except Exception as e:
        print(f"Error loading image: {e}")
        return np.array([])
