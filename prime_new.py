def check_prime(num):
    j = num
    counter = 0
    for i in range(2, j):
        if j % i == 0:
            counter = 1
    if counter == 0:
        print(str(j) + " is a prime number")
    else:
        print(str(j) + " is not a prime number")
        

check_prime(111)