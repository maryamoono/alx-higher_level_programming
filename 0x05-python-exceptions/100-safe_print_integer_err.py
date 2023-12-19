#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except Exception as v:
        sys.stderr.write("Exception: {}\n".format(v))
        return (False)
    else:
        return (True)
