
class Rota:

    def __init__(self):
        self.members = []

    def add_person(self, person):
        self.members.append(person)

    def remove_person(self, person):
        if person in self.members:
            self.members.remove(person)
        else:
            print("There is no such person")

    def show_all_members(self):
        for person in self.members:
            print(person.get_name())


class Polk:

    def __init__(self):
        self.rotas = []

    def add_rota(self, rota):
        if rota:
            self.rotas.append(rota)

    def remove_rota(self, rota):
        if rota:
            self.rotas.remove(rota)

    def show_rotas(self):
        for rota in self.rotas:
            print(rota.show_all_members())
