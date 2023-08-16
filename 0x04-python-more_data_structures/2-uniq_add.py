#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    if my_list:
        new_list = list(set(my_list))
        for el in new_list:
            result += el
    return result
