y = 1

while True:
    divisible = True

    for x in range(1, 201):
        if y % x != 0:        #not divisible by x
            divisible = False
            break

    if divisible:
        break

    y += 1

print("The smallest number that is evenly divisible from 1 to 200 is:", y)
