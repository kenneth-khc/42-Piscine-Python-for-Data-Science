def ft_tqdm(lst: range) -> None:
    """
    Iterates through an object and prints a progress bar
    signifying the progress of the list to be iterated.
    """
    for i in lst:
        completion = int(i / len(lst) * 100) + 1
        max_bar_length = 130
        bar_length = int(i / len(lst) * (max_bar_length)) + 1
        spaces = max_bar_length - bar_length
        formatted_strings = []
        formatted_strings.append(f"{completion}" + "%|")
        formatted_strings.append("█" * bar_length)
        formatted_strings.append(" " * spaces)
        formatted_strings.append("| " + f"{i+1}/" + str(len(lst)))
        yield print("".join(formatted_strings), end="\r")
