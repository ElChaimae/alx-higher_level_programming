#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            if not isinstance(dividend, (int, float)) or \
               not isinstance(divisor, (int, float)):
                raise TypeError
            if divisor == 0:
                raise ZeroDivisionError
            division = dividend / divisor
        except IndexError:
            print("out of range")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        finally:
            result.append(division)
    return result
