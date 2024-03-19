#!/usr/bin/python3
def uppercase(str):
    str1 = ""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            str1 += chr(ord(str[i]) - 32)
            continue
        str1 += str[i]

    print('{0}'.format(str1))
