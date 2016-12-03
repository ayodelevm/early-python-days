def factorial(num):
    product = 1
    for x in range(1, num):
        product = product * x
    print(product)

factorial(3)
factorial(7)
factorial(10)