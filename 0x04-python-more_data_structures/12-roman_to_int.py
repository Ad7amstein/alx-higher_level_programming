#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    roman_conv = {'I': 1, 'X': 10, 'C': 100,
                  'M': 1000, 'V': 5, 'L': 50, 'D': 500}
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    pre = 0
    for c in reversed(roman_string):
        if c not in roman_conv:
            return 0
        if roman_conv[c] >= pre:
            num += roman_conv[c]
        else:
            num -= roman_conv[c]
        pre = roman_conv[c]
    return num
