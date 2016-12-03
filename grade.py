for x in range(2,30):
    for y in range(2,x):
        J = 1
        if x % y == 0:
            J = J + 1,
            break
        if J == 2:
            print(y)
    else:
        J = 1