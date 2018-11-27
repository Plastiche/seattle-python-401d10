def array_reverse(list_input):
    """
    """
    if type(list_input) is not list:
        raise TypeError('Must pass a list as argument')

    for idx in range(len(list_input) // 2):
        list_input[idx], list_input[-idx - 1] = list_input[-idx - 1], list_input[idx]

    return list_input
