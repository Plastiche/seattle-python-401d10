def inplace_selection_sort(input_list):
    """Selection sort for an unordered list.
    """
    if len(input_list) < 2:
        return input_list

    for i in range(len(input_list)):
        idx_min = i

        for n in range(i + 1, len(input_list)):
            if input_list[idx_min] > input_list[n]:
                idx_min = n

        input_list[i], input_list[idx_min] = input_list[idx_min], input_list[i]

    return input_list


def selection_sort(input_list):
    """Selection sort for an unordered list.
    """
    if len(input_list) < 2:
        return input_list

    sorted_output = []

    for i in range(len(input_list)):
        idx_min = i

        for n in range(i + 1, len(input_list)):
            if input_list[idx_min] > input_list[n]:
                idx_min = n

        sorted_output.append(input_list[idx_min])

    return sorted_output
