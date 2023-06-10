#!/usr/bin/python3
from sys import argv

res, i = 0, 1

if __name__ == '__main__':
    while i < len(argv):
        res += int(argv[i])
        i += 1
    print(res)
