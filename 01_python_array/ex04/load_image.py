import numpy as np
import PIL.Image
import os

def ft_load(path: str) -> np.ndarray:
    """
    Loads an image file and returns its RGB pixel data as a NumPy array.
    Prints the shape and the content.
    """


    try:
        if not isinstance(path, str):
            raise AssertionError("Error: Path must be a string.")
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found: ", path)
        with PIL.Image.open(path) as img:
            img = img.convert("RGB")
            img_array = np.array(img)
            return img_array

    except KeyboardInterrupt:
        return None
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])
