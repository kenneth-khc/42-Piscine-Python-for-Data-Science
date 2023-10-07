def count_in_list(lst: list, arg) -> int:
    return sum(1 for i in lst if i == arg)
