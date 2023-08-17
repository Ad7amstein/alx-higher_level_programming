#!/usr/bin/python3
def weight_average(my_list=[]):
    _mul = 0
    _sum = 0
    if my_list is None or len(my_list) == 0:
        return 0
    for t in my_list:
        _sum += t[1]
        _mul += t[0] * t[1]
    return _mul / _sum
