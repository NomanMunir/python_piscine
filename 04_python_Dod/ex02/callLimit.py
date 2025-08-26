def callLimit(limit: int):
    """
    Decorator that limits the number of times a function can be called.

    Args:
        limit: Maximum number of times the function can be called

    Returns:
        Decorator function that wraps the original function
    """
    count = 0

    def callLimiter(function):
        """
        Inner decorator that wraps the actual function.

        Args:
            function: The function to be limited

        Returns:
            Wrapper function with call limit functionality
        """

        def limit_function(*args, **kwargs):
            """
            Wrapper function that enforces the call limit.

            Args:
                *args: Positional arguments for the wrapped function
                **kwargs: Keyword arguments for the wrapped function

            Returns:
                Result of the wrapped function or None if limit exceeded
            """
            nonlocal count

            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(
                    f"Error: <function {function.__name__} at {hex(id(function))}> call too many times"
                )
                return None

        return limit_function

    return callLimiter


def main():
    """Main function for testing."""
    # Test the decorator as shown in the example

    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
