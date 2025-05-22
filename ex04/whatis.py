from sys import argv

if len(argv) == 1:
    exit()

assert len(argv) == 2, "more than one argument is provided"
try:
    
    num = int(argv[1])
except ValueError:
    raise AssertionError("argument is not an integer")

if num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")