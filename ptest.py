from company import Rota, Polk
from person import Human
from datetime import datetime


person1 = Human('Alice', datetime(1990, 5, 24))
person2 = Human('Bob', datetime(1985, 8, 14))

rota1 = Rota()
rota1.add_person(person1)
