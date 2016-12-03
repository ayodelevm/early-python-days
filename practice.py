for p in range(2, 30):
    for i in range(2, p):
        if p % i == 0:
            break
        else:
            print(p)
print('Done')