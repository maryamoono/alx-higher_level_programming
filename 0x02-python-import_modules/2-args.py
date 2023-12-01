#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = len(sys.argv)
    if (s == 1):
        print("{} arguments.".format(s - 1))
    elif (s == 2):
        print("{} argument:".format(s - 1))
        print("1:", sys.argv[1])
    else:
        print("{} arguments:".format(s - 1))
        for x in range(1, s):
            print("{}:".format(x), sys.argv[x])
