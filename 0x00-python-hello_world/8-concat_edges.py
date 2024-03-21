#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split()[5] + " " + str.split()[6] + " " +str.split()[-1][:-1] + " " + str.split()[-4][:-1] + " " + str.split()[-3][:-1]
print(str)
