def square(x: int | float) -> int | float:
    """
    Return the square of the argument.
    
    Args:
        x: Number to square
        
    Returns:
        The square of x (x * x)
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Return x raised to the power of itself.
    
    Args:
        x: Number to raise to its own power
        
    Returns:
        x raised to the power of x (x ** x)
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Create a closure that applies a function to x repeatedly.
    
    Args:
        x: Initial value
        function: Function to apply (square or pow)
        
    Returns:
        Inner function that applies the function and updates x
    """
    count = 0
    
    def inner() -> float:
        """
        Inner function that applies the outer function to x.
        
        Returns:
            Result of applying function to current x value
        """
        nonlocal x, count
        count += 1
        x = function(x)
        return x
    
    return inner


def main():
    """Main function for testing."""
    # Test from the example
    my_counter = outer(3, square)
    print(my_counter())  # 9 (3²)
    print(my_counter())  # 81 (9²)
    print(my_counter())  # 6561 (81²)
    print("-----")
    
    another_counter = outer(1.5, pow)
    print(another_counter())  # 1.837... (1.5^1.5)
    print(another_counter())  # Result^Result
    print(another_counter())  # Result^Result


if __name__ == "__main__":
    main()
