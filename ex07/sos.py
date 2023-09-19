import sys


def valid_argument(text_to_encode: str) -> bool:
    valid = " ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for char in text_to_encode:
        if char not in valid:
            return False
    return True


def convert_to_morse(text_to_encode):
    MORSE_CODE = {" ": "/", "A": ".-", "B": "-...", "C": "-.-.",
                  "D": "-..", "E": ".", "F": "..-.", "G": "--.",
                  "H": "....", "I": "..", "J": ".---", "K": "-.-",
                  "L": ".-..", "M": "--", "N": "-.", "O": "---",
                  "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
                  "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
                  "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
                  "2": "..---", "3": "...--", "4": "....-", "5": ".....",
                  "6": "-....", "7": "--...", "8": "---..", "9": "----."}
    morse_coded = [MORSE_CODE[i] for i in text_to_encode if i in MORSE_CODE]
    print(" ".join(morse_coded))


def main():
    try:
        assert len(sys.argv) == 2
        assert valid_argument(sys.argv[1])
    except AssertionError:
        print("AssertionError: the arguments are bad")
    else:
        convert_to_morse(sys.argv[1].upper())


if __name__ == "__main__":
    main()
