from sys import argv
from string import punctuation


def main():
    """Counts chars in a given string: upper, lower, digits, spaces,
        and punctuation."""
    if len(argv) == 1:
        try:
            text = input("What is the text to count?\n")
        except BaseException:
            return
    else:
        assert len(argv) == 2, "more than one argument is provided"
        text = argv[1]

    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())
    punct = sum(1 for c in text if c in punctuation)
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
