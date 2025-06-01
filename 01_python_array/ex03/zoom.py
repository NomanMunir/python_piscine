import load_image
import numpy as np
import matplotlib.pyplot as plt


def zoom_image(image: np.ndarray, zoom_size: int = 40) -> np.ndarray:
    """
    Extracts a centered square of given size from the image.
    Returns only the red channel (grayscale-like) for display.
    """

    try:
        if image.ndim != 3 or image.shape[2] < 3:
            raise ValueError("Input image must be a 3-channel RGB image.")

        height, width, _ = image.shape

        if zoom_size > min(height, width):
            raise ValueError("Zoom size too large for the image dimensions.")

        center_y, center_x = height // 2, width // 2
        start_y, end_y = center_y - zoom_size // 2, center_y + zoom_size // 2
        start_x, end_x = center_x - zoom_size // 2, center_x + zoom_size // 2

        zoomed_image = image[start_y:end_y, start_x:end_x, 0]
        print(f"New shape after slicing: {zoomed_image.shape}")
        print(zoomed_image)
        return zoomed_image
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def display_image(image: np.ndarray):
    """
    Displays a 2D image using matplotlib, if image is not None.
    """

    if image is None:
        print("No image to display.")
        return
    try:
        plt.imshow(image, cmap='gray')
        plt.title("Zoomed Image")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.axis('on')
        plt.show()
    except Exception as e:
        print(f"An error occurred while displaying the image: {e}")


def main():
    """
    Main function to load an image, zoom it, and display the result.
    """

    try:
        image = load_image.ft_load('./landscape.jpeg')
        if image is None:
            print("Failed to load the image.")
            return

        zoomed = zoom_image(image, 3600)
        if zoomed is not None:
            display_image(zoomed)
    except Exception as e:
        print(f"An error occurred in the main function: {e}")
        return
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
