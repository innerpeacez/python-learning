def add3(num, add_number):
    return num + add_number


def add2(a=0, b=0, c=0):
    return a + b + c


print(add2())
print(add2(1))
print(add2(1, 2))
print(add2(1, 2, 3))


def add(*args):
    total = 0
    for num in args:
        total += num
    return total


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
