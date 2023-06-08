#!/usr/bin/python3
for ascii in range(ord('a'), ord('z') + 1):
    if chr(ascii) not in ['e', 'q']:
        print("{}".format(chr(ascii)), end="")
