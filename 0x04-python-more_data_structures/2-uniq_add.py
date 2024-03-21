#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_add = []
    for x in my_list:
        if x not in uniq_add:
            uniq_add.append(x)
    result = 0
    for x in uniq_add:
        result += x
    return result
