import sys


def parse_args() -> str:
    """
    Parse the argument passed into the program.
    If no argument is passed, read the stdin for one.
    AssertionError when more than one argument is passed.
    """
    try:
        if len(sys.argv) == 1:
            print("What is the text to count?")
            argument = sys.stdin.readline()
        else:
            assert len(sys.argv) == 2, "AssertionError: Too many arguments"
            argument = sys.argv[1]
        return argument
    except AssertionError as error:
        print(error)


def count_characters(string: str) -> dict:
    """
    Count the number of characters, uppercases, lowercases,
    punctuations, spaces and digits.
    Store the numbers in character_counts.
    """
    character_counts = {"characters": 0, "uppercases": 0, "lowercases": 0,
                        "punctuations": 0, "spaces": 0, "digits": 0}
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    character_counts["characters"] = len(string)
    for char in string:
        if char.isupper():
            character_counts["uppercases"] += 1
        elif char.islower():
            character_counts["lowercases"] += 1
        elif char.isspace():
            character_counts["spaces"] += 1
        elif char.isdigit():
            character_counts["digits"] += 1
        elif char in punctuations:
            character_counts["punctuations"] += 1
    return character_counts


def print_results(character_counts: dict):
    """
    Print the results using the numbers stored
    in the character_counts.
    """
    print("The text contains " + str(character_counts["characters"]) +
          " characters:")
    print(str(character_counts["uppercases"]) + " upper letters")
    print(str(character_counts["lowercases"]) + " lower letters")
    print(str(character_counts["punctuations"]) + " punctuation marks")
    print(str(character_counts["spaces"]) + " spaces")
    print(str(character_counts["digits"]) + " digits")


def main():
    """
    Parse args and error handle
    """
    arg = parse_args()
    count = count_characters(arg)
    print_results(count)


if __name__ == "__main__":
    main()
