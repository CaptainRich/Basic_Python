sticks = 21  # Initialize the count

print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("Whoever will take the last stick will lose")

while True:
    print("Sticks left: " , sticks)
    sticks_taken = int(input("Take sticks(1-4):"))       # taken by the player

    if sticks == 1:
        print("You took the last stick, you lose")
        break

    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue

    print("Computer took: " , (5 - sticks_taken) , "\n") #taken by the computer
    sticks -= 5