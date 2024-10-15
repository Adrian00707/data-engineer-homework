dict1 = {'name': 'Ed',
         'age': 25,
         'Nat': 'Ukr'}

dict2 = {'name': 'Bob',
         'age': 27,
         'Nat': 'Uk'}

dict3 = {'name': 'Lola',
         'age': 23,
         'Nat': 'Amer'}

list1 = ['Ed', 'Bob', 'Lola']
list2 = [25, 27, 23]
list3 = ['Ukr', 'Uk', 'Amer']

dict4 = {'names': list1,
         'ages': list2,
         'nats': list3}

dict5 = {'Ed170': dict1,
         'BiGbob': dict2,
         'HLol': dict3}


print(dict5['Ed170']['name'])

keyList = list(dict3.keys())
valuesList = list(dict3.values())
print(keyList)
print(valuesList)
dict2['age'] = 28

print(dict2['age'])

pp1 = "Let's start!"
print(pp1)

pp2 = 3
pp3 = 3.5
pp4 = True

list11 = [1, 2, 3]
list12 = [4, 5, 6, 7]

list11.append('and')
list11.append(list12)

list31 = list11 + list12

list41 = [1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5,]
list51 = [1, 1, 3, 3, 3, 5, 5, 7, 2, 9,]
list61 = set(list41 + list51)
print(list61)

dict1 = {'N': 'Alex',
         'A': 23,
         'B': 'O'}

dict2 = {'N': 'Mona',
         'A': 22,
         'B': '1+'}

dict3 = {'N': 'Bob',
         'A': 21,
         'B': 'A+'}

Nlist = ['Alex', 'Mona', 'Bob']
Alist = [23, 22, 21]
Blist = ['O', '1+', 'A+']

dict4 = {'Names': Nlist,
         'Ages': Alist,
         'Blood': Blist}

dict5 = {'AlexKing': dict1,
         'MonaSax': dict2,
         'BobBurger': dict3}

print(dict5.get('AlexKing')['N'])
dict1['N'] = 'Toby'
dict4['Names'][0] = 'Toby'
print(dict5)
print(dict4)
listkeys = list(dict5.keys())
listvalues = list(dict5['MonaSax'].values())
print(listkeys)
print(listvalues)
