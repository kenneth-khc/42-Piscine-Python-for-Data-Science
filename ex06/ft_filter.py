def ft_filter(function, iterable):
    """
    Iterate through each element in iterable and apply function to it.
    Store the element into a new list if true.
    """
    filtered_list = [i for i in iterable if function(i)]
    return filtered_list
