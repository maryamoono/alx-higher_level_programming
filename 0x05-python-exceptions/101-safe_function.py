#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as v:
        sys.stderr.write("Exception: {}\n".format(v))
        result = None

    return (result)
