#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for index, arguments in enumerate(sys.argv[1:], start=1):
        sum += int(sys.argv[index])
    print("{:d}".format(sum))
