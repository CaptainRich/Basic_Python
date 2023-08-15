# This routine generates a Fibonacci Series (up to 100)

a, b = 0, 1           # initialize "a" and "b"

while b < 100:
    print( b, end=" " )  # The 'end=' causes the output to print on one line
    a, b = b, a+b

