#!/urs/bin/python3
def islower(c):
    return 97 <= ord(c) <= 122
print(islower('a'))  # True
print(islower('A'))  # False
print(islower('z'))  # True
print(islower('Z'))  # False
print(islower('5'))  # False

