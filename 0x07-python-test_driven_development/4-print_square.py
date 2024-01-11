import function:
	>>> print_square = __import__('4-print_square').print_square

size int
	>>> print_square(4)
	####
	####
	####
	####

size 0
	>>> print_square(0)


size -1
	>>> print_square(-1)
	Traceback (most recent call last):
	ValueError: size must be >= 0

size 1.5
	>>> print_square(1.5)
	Traceback (most recent call last):
	TypeError: size must be an integer

size hi
	>>> print_square("hi")
	Traceback (most recent call last):
	TypeError: size must be an integer

size None
	>>> print_square(None)
	Traceback (most recent call last):
	TypeError: size must be an integer

size ()
	>>> print_square()
	Traceback (most recent call last):
	TypeError: print_square() missing 1 required positional argument: 'size'