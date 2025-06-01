from load_image import ft_load

try:
    print(ft_load("./landscape.jpeg"))
except Exception as e:
    print(f"An error occurred: {e}")
