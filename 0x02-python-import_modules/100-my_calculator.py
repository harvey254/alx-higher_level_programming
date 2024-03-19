#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    """
    Handles basic operations :
    addition
    aubtraction
    multiplication
    division
    Between two numbers
    """
    len_av = len(argv) - 1

    if len_av == 3:
        op = argv[2]
        var_a = int(argv[1])
        var_b = int(argv[3])
        if op == '+':
            res = add(var_a, var_b)
            print('{:d} + {:d} = {:d}'.format(var_a, var_b, res))
            exit(0)
        elif op == '-':
            res = sub(var_a, var_b)
            print('{:d} - {:d} = {:d}'.format(var_a, var_b, res))
            exit(0)
        elif op == '*':
            res = mul(var_a, var_b)
            print('{:d} * {:d} = {:d}'.format(var_a, var_b, res))
            exit(0)
        elif op == '/':
            res = div(var_a, var_b)
            print('{:d} / {:d} = {:d}'.format(var_a, var_b, res))
            exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
