#!/usr/bin/python3
def element_at(my_list, idx):
    if idx not in range(0, len(my_list)):
        return None
    else:
        return my_list[idx]
