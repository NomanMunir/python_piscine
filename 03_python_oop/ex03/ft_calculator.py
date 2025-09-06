class calculator:
    """Calculator class that performs vector operations with scalars."""

    def __init__(self, vector: list) -> None:
        """Initialize calculator with a vector (list of numbers)."""
        self.vector = vector

    def __add__(self, scalar) -> None:
        """Add scalar to each element of the vector and print result."""
        self.vector = [value + scalar for value in self.vector]
        print(self.vector)

    def __mul__(self, scalar) -> None:
        """Multiply each element of the vector by scalar and print result."""
        self.vector = [value * scalar for value in self.vector]
        print(self.vector)

    def __sub__(self, scalar) -> None:
        """Subtract scalar from each element of the vector and print result."""
        self.vector = [value - scalar for value in self.vector]
        print(self.vector)

    def __truediv__(self, scalar) -> None:
        """Divide each element of the vector by scalar and print result."""
        if scalar == 0:
            print("Error: Division by zero is not allowed")
            return
        self.vector = [value / scalar for value in self.vector]
        print(self.vector)
c = calculator([1, 2, 3])
c + 3
c * 3