import load_image
import numpy as np
import matplotlib.pyplot as plt


def zoom(image, x_start=450, x_end=850, y_start=100, y_end=500) -> np.ndarray:
    """
    Extracts a centered square of given size from the image.
    Returns only the red channel (grayscale-like) for display.
    """

    try:
        if image.ndim != 3 or image.shape[2] < 3:
            raise ValueError("Input image must be a 3-channel RGB image.")

        height, width, _ = image.shape

        zoomed_img = image[y_start:y_end, x_start:x_end, 0:1]
        return zoomed_img

    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    except KeyboardInterrupt:
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
        image = load_image.ft_load('./animal.jpeg')
        if image is None:
            print("Failed to load the image.")
            return

        zoomed = zoom(image)
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        if zoomed is not None:
            display_image(zoomed)
    except Exception as e:
        print(f"An error occurred in the main function: {e}")
        return
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
