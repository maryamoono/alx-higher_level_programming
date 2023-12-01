#!/usr/bin/python3
if __name__ == "__main__":
    import tem
    sum = 0
    if (len(tem.argv) == 1):
        print(0)
    else:
        for i in range(1, len(tem.argv)):
            sum += int(tem.argv[i])
        print(sum)
