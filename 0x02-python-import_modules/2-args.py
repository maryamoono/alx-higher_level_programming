#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    v = len(sys.argv)
    if (v == 1):
        print("{} arguments.".format(v - 1))
    elif (v == 2):
        print("{} argument:".format(v - 1))
        print("1:", sys.argv[1])
    else:
        print("{} arguments:".format(v - 1))
        for x in range(1, v):
            print("{}:".format(x), sys.argv[x])
