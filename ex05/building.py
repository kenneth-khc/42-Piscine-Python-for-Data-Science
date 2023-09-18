import sys


def main():
    arg = parse_args()
    count = count_characters(arg)
    print_results(count)


def parse_args() -> str:
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
    dictionary = {"characters": 0, "uppercases": 0, "lowercases": 0,
                  "punctuations": 0, "spaces": 0, "digits": 0}
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    dictionary["characters"] = len(string)
    for char in string:
        if char.isupper():
            dictionary["uppercases"] += 1
        elif char.islower():
            dictionary["lowercases"] += 1
        elif char.isspace():
            dictionary["spaces"] += 1
        elif char.isdigit():
            dictionary["digits"] += 1
        elif char in punctuations:
            dictionary["punctuations"] += 1
    return dictionary


def print_results(dictionary: dict):
    print("The text contains " + str(dictionary["characters"]) +
          " characters:")
    print(str(dictionary["uppercases"]) + " upper letters")
    print(str(dictionary["lowercases"]) + " lower letters")
    print(str(dictionary["punctuations"]) + " punctuation marks")
    print(str(dictionary["spaces"]) + " spaces")
    print(str(dictionary["digits"]) + " digits")


if __name__ == "__main__":
    main()
