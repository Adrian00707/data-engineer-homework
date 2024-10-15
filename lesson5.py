def greet():
    greet = 'Hello'
    return greet


print(greet())


def greet_name(name):
    print(f"Hello {name.title()}")


greet_name('kevin')


def dictnab(name, age, blood):
    dict1 = {}
    dict1['name'] = name
    dict1['age'] = age
    dict1['blood'] = blood
    print(dict1)


dictnab('lola', 21, '+1')


def dictnab(name, age, blood='+1'):
    dict1 = {}
    dict1['name'] = name
    dict1['age'] = age
    dict1['blood'] = blood
    print(dict1)


dictnab('lola', 21)

namelist = ['kevin', 'tom', 'tina', 'luke']
for name in namelist:
    print(greet_name(name))


def sum_of_list(numbers):
    return sum(numbers)


list_numbers = [1, 2, 3, 4, 5, 6, 7]
results = sum_of_list(list_numbers)
print(results)


def sums_numbers(numbers):
    return sum(numbers)


def cuntitty(numbers):
    slog = f"There is {numbers} of numbers!"
    return slog


list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(cuntitty(sums_numbers(list_numbers)))


def greet():
    print("Hello people")


print(greet())


def greet_by_name(name):
    print(f"Hello {name.title()}")


print(greet_by_name('raph'))


def greet_by_full_name(name, surname, second_name):
    print(f"Hello Mister/Miss {surname.title()} your name is {
          name.title()} and your second name is {second_name.title()}")


print(greet_by_full_name('raph', 'smith', 'michael'))


def greet_by_fill_name(name, second_name, surname='doe'):
    print(f"Hello Mister/Miss {surname.title()} your name is {
          name.title()} and your second name is {second_name.title()}")


print(greet_by_fill_name('michael', 'john'))

list_names = ['joe', 'david', 'anna', 'luke', 'jack', 'betty', 'ross']

for name in list_names:
    print(greet_by_name(name))


def sums_of_num(numbers):
    return sum(numbers)


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

print(sums_of_num(list_of_numbers))


def count(numbers):
    count = len(numbers)
    return count


def slog(n):
    slog = f"There is {n} of numbers"
    return slog


list_of_numbers2 = list(range(1, 13))

print(list_of_numbers2)
print(slog(count(list_of_numbers2)))
