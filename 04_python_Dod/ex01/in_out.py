def square(x: int | float) -> int | float:
    """Return the square of the argument.

    Args:
        x: Number to square

    Returns:
        The square of x (x * x)

    Raises:
        TypeError: If x is not a number
        OverflowError: If result is too large
    """
    try:
        if not isinstance(x, (int, float)):
            raise TypeError(f"Expected int or float, got {type(x).__name__}")

        result = x * x

        if result == float("inf") or result == float("-inf"):
            raise OverflowError("Square operation resulted in infinity")

        return result

    except (TypeError, OverflowError):
        raise  # Re-raise the specific errors
    except Exception as e:
        raise RuntimeError(f"Unexpected error in square function: {e}")


def pow(x: int | float) -> int | float:
    """Return x raised to the power of itself.

    Args:
        x: Number to raise to its own power

    Returns:
        x raised to the power of x (x ** x)

    Raises:
        TypeError: If x is not a number
        ValueError: If operation is invalid
            (e.g., negative base with non-integer exponent)
        OverflowError: If result is too large
    """
    try:
        if not isinstance(x, (int, float)):
            raise TypeError(f"Expected int or float, got {type(x).__name__}")

        if x == 0:
            return 1  # 0^0 = 1 by convention

        if x < 0 and not x.is_integer():
            raise ValueError("Negative base with non-integer exponent")

        result = x**x

        if result == float("inf") or result == float("-inf"):
            raise OverflowError("Power operation resulted in infinity")

        if result != result:
            raise ValueError("Power operation resulted in NaN")

        return result

    except (TypeError, ValueError, OverflowError):
        raise  # Re-raise the specific errors
    except Exception as e:
        raise RuntimeError(f"Unexpected error in pow function: {e}")


def outer(x: int | float, function) -> object:
    """Create a closure that applies a function to x repeatedly.

    Args:
        x: Initial value
        function: Function to apply (square or pow)

    Returns:
        Inner function that applies the function and updates x
    """
    try:
        if not isinstance(x, (int, float)):
            raise TypeError(f"x must be int or float, got {type(x).__name__}")

        if not callable(function):
            raise TypeError(
                f"function must be callable, got {type(function).__name__}"
            )

        count = 0

        def inner() -> float:
            """Inner function that applies the outer function to x.

            Returns:
                Result of applying function to current x value
            """
            nonlocal x, count
            try:
                count += 1
                x = function(x)

                if not isinstance(x, (int, float)):
                    raise TypeError(
                        f"Function returned invalid type: {type(x).__name__}"
                    )

                if x == float("inf") or x == float("-inf"):
                    raise OverflowError("Result is infinite")

                if x != x:
                    raise ValueError("Result is NaN (Not a Number)")

                return x

            except (
                TypeError,
                ValueError,
                OverflowError,
                ZeroDivisionError,
            ) as e:
                print(f"Error in inner function: {e}")
                return None
            except Exception as e:
                print(f"Unexpected error in inner function: {e}")
                return None

        return inner

    except (TypeError, ValueError) as e:
        print(f"Error in outer function: {e}")
        return lambda: None
    except Exception as e:
        print(f"Unexpected error in outer function: {e}")
        return lambda: None


def main():
    """Main function for testing."""
    try:
        print("=== Testing valid cases ===")
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
        print("-----")

        print("=== Testing error cases ===")

        # Test with invalid x type
        print("Testing with string as x:")
        bad_counter1 = outer("hello", square)
        print(bad_counter1())

        # Test with invalid function
        print("Testing with non-callable function:")
        bad_counter2 = outer(5, "not_a_function")
        print(bad_counter2())

        # Test function that causes overflow
        print("Testing with function that causes overflow:")

        def big_power(x):
            return x**1000

        overflow_counter = outer(2, big_power)
        print(overflow_counter())

        # Test function that returns invalid type
        print("Testing with function that returns string:")

        def bad_function(x):
            return str(x)

        string_counter = outer(5, bad_function)
        print(string_counter())

    except Exception as e:
        print(f"Error in main function: {e}")

    print("\n=== Testing complete ===")


if __name__ == "__main__":
    main()
