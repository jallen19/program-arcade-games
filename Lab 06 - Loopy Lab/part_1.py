#!/usr/bin/env python3
# chap6.py
# James Allen
#11/13/2012

start = 10
for row in range(9):
    for column in range(row+1):
        print(start, end = " ")
        start += 1
    print()