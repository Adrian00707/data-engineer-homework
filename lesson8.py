class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be possitive")

    def show_info(self):
        return f"Name: {self.__name}, Age: {self.__age}."


class Rota:
    def __init__(self):
        self.__soldiers = []

    def add_soldier(self, soldier):
        self.__soldiers.append(soldier)

    def remove_soldier(self, soldier):
        if soldier in self.__soldiers:
            self.__soldiers.remove(soldier)
        else:
            print(f"{soldier.get_name()} not in rota")

    def show_soldiers(self):
        if self.__soldiers:
            for soldier in self.__soldiers:
                print(soldier.show_info())
            else:
                print("Rota is abcent")


class Regiment:
    def __init__(self):
        if self.__rotas:
            for i, rota in enumerate(self.__rotas):
                print(f"Rota {i+1}:")
                rota.show_soldiers()
        else:
            print("There is nobody in rota")


class Human:
    def __init__(self, name='Ivan'):
        self.__name = name
        self.__location = 'Kiev'

    def get_name(self):
        return self._name

    def get_location(self):
        return self.__location

    def set_name(self, location):
        self.__location = location


class Children(Human):
    _age = 5

    def __init__(self, name='Ivan'):
        super().__init__(name)

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self.__name + " " + self._age


class Bus:
    __children: list()

    def __init__(self, children: list):
        self.__humans = children

    def add_children(self, children: list):
        self.__children = self.__children + children

    def remove_children(self, children: list):
        for one_children in children:
            if one_children in self.__children:
                self.__children.remove(one_children)


one_human = Human()
print(one_human.get_location())


list1 = [1, 2, 3, 4, 'hello', 5, 6, 7]


def list_division(local_list: list):
    l_result = list()
    for one_element in local_list:
        try:
            l_result.append(one_element/2)
        except Exception as e:
            print(e)
        finally:
            print(one_element)
    return l_result


print(list_division(list1))
