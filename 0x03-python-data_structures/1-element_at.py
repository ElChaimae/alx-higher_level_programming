def element_at(my_list, idx):
    if idx < 0:
        return None

    max = len(my_list) - 1

    elif idx > max:
        return None

    else:
        return my_list[idx]
