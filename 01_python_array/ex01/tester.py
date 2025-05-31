from array2D import slice_me

family = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2],
    ['hello', 1],
    [1, 3],
]

try:
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -1))
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
