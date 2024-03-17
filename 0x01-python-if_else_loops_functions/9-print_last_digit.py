#!/urs/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print("The last digit of", number, "is", last_digit)
    return last_digit
