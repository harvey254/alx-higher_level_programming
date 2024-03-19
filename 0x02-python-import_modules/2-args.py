#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """Prints the argument list passed to the program

    The program takes all the arguments starting from the second
    and prints the number of arguments and their value

    """
    av = sys.argv
    len_av = len(av) - 1

    if len_av > 1:
        print(len_av, 'arguments:')
        for i in range(1, len_av + 1):
            print('{:d}: {}'.format(i, av[i]))
    elif len_av == 1:
        print(len_av, 'argument:')
        for i in range(1, len_av + 1):
            print('{:d}: {}'.format(i, av[i]))
    elif len_av == 0:
        print(len_av, 'arguments.')
