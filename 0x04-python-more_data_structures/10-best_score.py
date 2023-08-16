#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_key = None
    highest_score = float('-inf')

    for key, value in a_dictionary.items():
        if value > highest_score:
            best_key = key
            highest_score = value
    return best_key
