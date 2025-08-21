class calculator:
    """Calculator class for vector operations using static methods."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate dot product of two vectors."""
        result = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise."""
        result = [float(v1 + v2) for v1, v2 in zip(V1, V2)]
        print(f"Add Vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract second vector from first vector element-wise."""
        result = [float(v1 - v2) for v1, v2 in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
