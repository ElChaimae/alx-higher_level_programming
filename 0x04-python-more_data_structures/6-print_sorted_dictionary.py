#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_d = sorted(a_dictionary.keys())
    for key in sorted_d:
        print(key + ": " + str(a_dictionary[key]))
