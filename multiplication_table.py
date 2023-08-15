# Print out the multiplication table

i = 1  # The vertical value

print( "-" * 50 )
while i < 16:
    n = 1        # The horizontal value
    while n <= 15:
        print( "%4d" % (i * n), end=" ")
        n += 1
    print()
    i += 1

print( "-" * 50)