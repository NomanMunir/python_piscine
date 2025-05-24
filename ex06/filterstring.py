from sys import argv

from ft_filter import ft_filter


def main():
    """filterstring(string, int) --> print the words longer than int

Prints the words in the string that are longer than the given int.
"""
    assert len(argv) == 3, "the arguments are bad"
    try:
        input_string = argv[1]
        num = int(argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    words = input_string.split()
    result = ft_filter(lambda x: len(x) > num, words)
    print(list(result))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
