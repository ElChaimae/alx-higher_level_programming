#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    my_map = map(lambda x: x * number, my_list)
    return list(my_map)
