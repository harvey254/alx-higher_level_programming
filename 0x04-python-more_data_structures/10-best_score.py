#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    else:
        best_score = (max(a_dictionary, key=a_dictionary.get))
        if best_score == 0:
            return None
        else:
            return best_score
