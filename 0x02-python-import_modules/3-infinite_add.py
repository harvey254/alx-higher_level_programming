#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """
    Prints the result addition of all arguments

    """
    av = sys.argv
    len_av = len(av)
    sum = 0

    if len_av > 1:
        for i in range(1, len_av):
            sum += int(av[i])

    print(sum)
