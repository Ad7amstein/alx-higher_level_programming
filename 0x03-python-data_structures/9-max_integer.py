#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    mx = my_list[0]
    for element in my_list:
        if element > mx:
            mx = element
    return mx
