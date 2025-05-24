from sys import argv

from ft_filter import ft_filter


def main():
    ''' Main function to filter a string based on a condition.'''
    assert len(argv) == 3, "the arguments are bad"
    try:
        input_string = argv[1]
        num = int(argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    except Exception as e:
        raise AssertionError(f"unexpected error: {type(e).__name__}: {e}")
    words = input_string.split()
    result = ft_filter(lambda x: len(x) > num, words)
    print(list(result))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
