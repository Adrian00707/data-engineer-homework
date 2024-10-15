list1 = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]
list2 = [2, 2, 3, 4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8]
list3 = set(list1 + list2)
list3.remove(6)
print(list3)

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

print(dict5.get('AlexKing')['A'])
print(dict3.get('B'))
print(dict4.get('Names')[1])
KeyList = list(dict3.keys())
ValuesList = list(dict3.values())
print(KeyList)
print(ValuesList)
dict2['N'] = 'Nata'
print(dict2)
dict5['AlexKing']['N'] = 'Toby'
print(dict5)

dict11 = {'n': 'David',
          'a': 32,
          'p': 'actor'}

dict12 = {'n': 'Sarah',
          'a': 38,
          'p': 'journalist'}

dict13 = {}
dict13['n'] = dict3['N']
dict13['a'] = dict3['A']
dict13['p'] = 'student'

Namlist = ['David', 'Sarah', dict13['n']]
Aglist = [32, dict12['a'], dict13['a']]
Prolist = ['actor', 'journalist', 'student']

dict14 = {'Nam': Namlist,
          'Ag': Aglist,
          'Pro': Prolist}

dict15 = {'DVD': dict11,
          'Sar83': dict12,
          'JustBob': dict13}

print(dict14.get('Pro')[0])
dict14['Pro'][0] = 'freelancer'
print(dict14.get('Pro'))
dict15['DVD']['p'] = 'freelancer'
print(dict15.get('DVD'))
list11 = list(dict15.keys())
list12 = list(dict15.values())
print(list11)
print(list12[1]['p'])

lis11 = [1, 1, 2, 2, 3, 3, 3, 4, 5]
lis12 = [4, 4, 4, 5, 6, 6, 7]
lis3 = set(lis11 + lis12)
print(lis3)
