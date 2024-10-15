list1 = [1, 2, 3, 4, 5, 6, 7]
for i in list1:
    print(i)


list2 = ['tiptop', 'pop', 'liponse', 'lipop', 'hops', 'rentops', 'top']
for item in list2:
    if len(item) > 5:
        print(item)


list3 = [1, 2, 3, list1, list2]
for item in list3:
    print(item)
    if isinstance(item, list):
        for i in item:
            print(i)


dict1 = {'N': 'Alex',
         'A': 23,
         'B': 'O'}
for k in dict1:
    print(k, dict1[k])


i = 1
while i < 100:
    print(i)
    i += 1


dict2 = {'N': 'Mona',
         'A': 22,
         'B': '1+'}

dict3 = dict1.copy()
for k in dict2:
    dict3[k] = dict2[k]

print(dict3)
print(dict2)


list11 = [1, 2, 3, 4, 5, 6, 7]
for i in list1:
    print(i)

list12 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list12:
    if i > 5:
        print(i)

list13 = [1, 2, 3, list11]
for i in list13:
    print(i)
    if isinstance(i, list):
        for p in i:
            print(p)

dict4 = {'n': 'Sarah',
         'a': 38,
         'p': 'journalist'}

for k in dict4.keys():
    print(k, dict4[k])

i = 1
while i < 10:
    print(i)
    i += 1

dict4 = {'n': 'Sarah',
         'a': 38,
         'p': 'journalist'}

dict5 = dict4.copy()
for v in dict2:
    dict5[v] = dict2[v]

print(dict5)
