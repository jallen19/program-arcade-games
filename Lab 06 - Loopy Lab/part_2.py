#!/usr/bin/env python3
# chap6.py
# James Allen
#11/13/2017
height = int(input("E.g. n = "))
print('o'*(height*2))
for i in range(height - 2):
    print('o' + ' '*(height*2-2) + 'o')
print('o'*(height*2))