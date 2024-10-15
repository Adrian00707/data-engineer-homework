a = 5
if a > 2:
    print("a bigger than 2")
else:
    print("a is not bigger than 2")

list1 = [1, 2, 3, 4, 5, 6, 7]
a = 3
b = 5

if a > b:
    print("A is bigger than b")
else:
    print("B is bigger than a")

a = 5

if a > 0:
    print(a*5)
else:
    print(a/2)

a = 18
if a % 2 == 0:
    print(a / 2)
else:
    print(a * 3)

a = 17
if a % 2 == 0:
    print('a % 2 = 0')
    if a == 18:
        print(a * 10)
    else:
        print(" a =! 18")
else:
    print(a * 5)

a = 5
b = 9
if isinstance(a, int) and isinstance(b, int):
    print(a + b)

list2 = [1, 2, 3, 4, 5, 6, 7, 8]
if list2:
    print(list2)
else:
    print(list1)

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if 9 in list3:
    print(list3)
else:
    print(list1)


a = 5
b = 7
if a < b:
    print("b bigger than a")

a = 3

if a < 0:
    print(a * 10)
else:
    print(a / 2)

a = 5
if a % 2 == 0:
    print(a / 2)
else:
    print(a * 3)

b = 8
if b % 2 == 0:
    print('b can be divided')
    if b < 10 and b == 8:
        print("b is not bigger than 10 it's 8")
else:
    print("b is can't be divided")

a = 7
b = 9
if isinstance(a, int) and isinstance(b, int) or isinstance(b, float):
    print(a+b)
else:
    print("One of them is not int")

list4 = [1, 2, 3, 4, 5, 6, 7, 9]
if 9 in list4:
    print("9 is in list4")
else:
    print("There is no 9")
