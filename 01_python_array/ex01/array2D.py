import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slices a 2D list using NumPy and prints original and new shapes.

    Parameters:
    - family: a 2D list of equal-length rows
    - start: start index for slicing (inclusive)
    - end: end index for slicing (exclusive)

    Returns:
    - A sliced 2D list
    """
    try:

        if not isinstance(family, list) or not all(
            isinstance(row, list) for row in family
        ):
            raise ValueError("Input must be a 2D list array.")

        row_lengths = [len(row) for row in family]

        if len(set(row_lengths)) != 1:
            raise ValueError("All rows must have the same number of columns.")

        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Start and end indices must be integers.")

        np_array = np.array(family)
        print(f"My shape is : {np_array.shape}")

        sliced = np_array[start:end]
        print(f"My new shape is : {sliced.shape}")

        return sliced.tolist()
    except Exception as e:
        print(f"Error: {e}")
