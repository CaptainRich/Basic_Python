# This routine generates a Fibonacci Series (up to 100)

a, b = 0, 1           # initialize "a" and "b"

while b < 100:
    print( b )
    a, b = b, a+b

