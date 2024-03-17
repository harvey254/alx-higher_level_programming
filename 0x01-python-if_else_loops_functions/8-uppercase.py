#!/urs/bin/python3
def uppercase(s):
    for char in s:
        print(chr(ord(char) - 32), end='')
    print()
uppercase("hello world")

