def ft_statistics(*args: any, **kwargs: any) -> None:
    """"""

    for value in kwargs.values():
        if value == "mean":
            find_mean(args)

        if value == "median":
            find_median(list(args))

        if value == "quartile":
            find_quartiles(list(args))

def find_mean(numbers: list) -> None:
    """"""

    mean = sum(numbers) / len(numbers)
    print(f"mean : {mean}")


def find_median(numbers: list) -> None:
    """"""

    numbers.sort()
    list_len = len(numbers)

    if list_len % 2 != 0:
        median = numbers[list_len // 2]
    else:
        median = (numbers[list_len // 2 - 1] + numbers[list_len // 2]) / 2

    print (f"median: {median}")

def find_quartiles(numbers: list) -> None:
    """"""

    numbers.sort()

    lower_half = numbers[:len(numbers) // 2]
    upper_half = numbers[len(numbers) // 2:]

    q1 = lower_half[len(lower_half) // 2]
    q2 = upper_half[len(upper_half) // 2]

    print(f"quartiles : {[float(q1), float(q2)]}")

ft_statistics(6, 5, 4, 3, 2, 1, a="mean", b="median", c="quartile")