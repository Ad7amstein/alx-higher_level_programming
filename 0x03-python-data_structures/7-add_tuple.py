#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    for i in range(2):
        if len(tuple_a) > i:
            if i == 0:
                a += tuple_a[i]
            elif i == 1:
                b += tuple_a[i]
        if len(tuple_b) > i:
            if i == 0:
                a += tuple_b[i]
            elif i == 1:
                b += tuple_b[i]
    result = (a, b)
    return result
