def func_prime(num):
    global x
    for x in range(2, num + 1):
        num_of_complete_divisions = 0
        for y in range(2, x):
            if x % y == 0:
                num_of_complete_divisions = num_of_complete_divisions + 1
        if num_of_complete_divisions == 0:
            print(str(x) + " is a prime number")

func_prime(11)

print(str(x) + " is a variable")