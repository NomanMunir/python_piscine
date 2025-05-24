from sys import argv

NESTED_MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    " ": "/"
}


def main():
    """sos program - converts a string to Morse code
Converts the input string to Morse code and prints it.
"""
    assert len(argv) == 2, "the arguments are bad"
    input_string = argv[1].upper()
    morse_code = []
    for char in input_string:
        if char in NESTED_MORSE:
            morse_code.append(NESTED_MORSE[char])
        else:
            raise AssertionError("the arguments are bad")
    print(f"{str.join(' ', morse_code)}")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
