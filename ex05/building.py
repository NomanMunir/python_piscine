from sys import argv
from string import punctuation


def main():
    """Counts chars in a given string: upper, lower, digits, spaces,
        and punctuation."""
    if len(argv) == 1:
        try:
            text = input("What is the text to count?\n")
        except EOFError:
            return
    else:
        assert len(argv) == 2, "more than one argument is provided"
    text = argv[1]

    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())
    punct = sum(1 for c in text if c in punctuation)
    print(f"Uppercase letters: {upper}")
    print(f"Lowercase letters: {lower}")
    print(f"Digits: {digits}")
    print(f"Spaces: {spaces}")
    print(f"Punctuation: {punct}")


if __name__ == "__main__":
    main()
