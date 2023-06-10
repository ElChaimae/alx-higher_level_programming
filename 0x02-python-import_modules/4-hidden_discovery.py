#!/usr/bin/python3
import hidden_4

i = 0

if __name__ == '__main__':
    l = dir(hidden_4)
    thelist = sorted(l)
    while i < len(thelist):
        if thelist[i][0] != '_':
            print(thelist[i])
    i += 1
