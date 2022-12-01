#!/usr/bin/python3
import sys
if __name__ == "__main__":
    largs = sys.argv
    if (len(sys.argv) - 1) == 0:
        print("0 arguments.")
    elif (len(sys.argv) - 1) == 1:
        print("1 argument:")
    else:
        print(f"{(len(sys.argv) - 1):d} arguments:")
    for i in range(1, len(largs)):
        print(f"{i:d}: {largs[i]}")
