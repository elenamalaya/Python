def my_func(x, y):
    for i in range(abs(y + 1)):
        x *= x
    return 1 / x
print(my_func(16,-2))