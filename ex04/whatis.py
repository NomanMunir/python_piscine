from sys import argv


def main():
    if len(argv) == 1:
        return

    assert len(argv) == 2, "more than one argument is provided"
    try:
        num = int(argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
