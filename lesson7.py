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
            print("Возраст должен быть положительным.")

    def show_info(self):
        return f"Имя: {self.__name}, Возраст: {self.__age}"


class Rota:
    def __init__(self):
        self.__soldiers = []  # Список для хранения солдат

    def add_soldier(self, soldier):
        self.__soldiers.append(soldier)

    def remove_soldier(self, soldier):
        if soldier in self.__soldiers:
            self.__soldiers.remove(soldier)
        else:
            print(f"{soldier.get_name()} не найден в роте.")

    def show_soldiers(self):
        if self.__soldiers:
            for soldier in self.__soldiers:
                print(soldier.show_info())
        else:
            print("Рота пуста.")


class Regiment:
    def __init__(self):
        self.__rotas = []

    def add_rota(self, rota):
        self.__rotas.append(rota)

    def remove_rota(self, rota):
        if rota in self.__rotas:
            self.__rotas.remove(rota)
        else:
            print("Рота не найдена в полку.")

    def show_regiment(self):
        if self.__rotas:
            for i, rota in enumerate(self.__rotas):
                print(f"Рота {i + 1}:")
                rota.show_soldiers()
        else:
            print("В полку нет рот.")


soldier1 = Human("Иван", 25)
soldier2 = Human("Петр", 30)

rota1 = Rota()
rota1.add_soldier(soldier1)
rota1.add_soldier(soldier2)

regiment1 = Regiment()
regiment1.add_rota(rota1)


regiment1.show_regiment()


class Person:
    def __init__(self, name, age):
        self.__name = name  # Приватное поле
        self.__age = age    # Приватное поле

    # Геттеры и сеттеры для имени
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Геттеры и сеттеры для возраста
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Возраст должен быть положительным.")

# Класс ребенок, наследующий класс Person


class Child(Person):
    def __init__(self, name, age, location="Дом"):
        super().__init__(name, age)
        self.__location = location  # Текущее местоположение ребенка

    # Геттер для местоположения
    def get_location(self):
        return self.__location

    # Сеттер для изменения местоположения
    def set_location(self, new_location):
        self.__location = new_location
        print(f"{self.get_name()} перемещен в {self.__location}")

# Класс автобус


class Bus:
    def __init__(self):
        self.__children = []  # Список детей в автобусе

    # Метод добавления ребенка в автобус
    def add_child(self, child):
        self.__children.append(child)
        print(f"{child.get_name()} добавлен в автобус.")

    # Метод удаления ребенка из автобуса
    def remove_child(self, child):
        if child in self.__children:
            self.__children.remove(child)
            print(f"{child.get_name()} удален из автобуса.")
        else:
            print(f"{child.get_name()} не найден в автобусе.")

    # Метод для изменения местоположения всех детей
    def change_all_children_location(self, new_location):
        for child in self.__children:
            child.set_location(new_location)


# Пример использования
child1 = Child("Иван", 10)
child2 = Child("Анна", 8)

# Создаем автобус
bus = Bus()

# Добавляем детей в автобус
bus.add_child(child1)
bus.add_child(child2)

# Изменяем местоположение всех детей
bus.change_all_children_location("Школа")


class Book:
    def __init__(self, title, author, pages):
        self.__title = title  # Приватное поле: название книги
        self.__author = author  # Приватное поле: автор книги
        self.__pages = pages  # Приватное поле: количество страниц

    # Геттер для названия
    def get_title(self):
        return self.__title

    # Геттер для автора
    def get_author(self):
        return self.__author

    # Геттер для количества страниц
    def get_pages(self):
        return self.__pages

    # Метод для отображения информации о книге
    def show_info(self):
        print(f"Название: {self.get_title()}, Автор: {
              self.get_author()}, Страниц: {self.get_pages()}")

# Класс-наследник для электронных книг


class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)  # Наследуем свойства из Book
        self.__file_size = file_size  # Приватное поле: размер файла

    # Геттер для размера файла
    def get_file_size(self):
        return self.__file_size

    # Переопределенный метод для отображения информации
    def show_info(self):
        super().show_info()  # Вызываем метод из родительского класса
        print(f"Размер файла: {self.get_file_size()} MB")


class Library:
    def __init__(self, name):
        self.__name = name  # Приватное поле: название библиотеки
        self.__books = []  # Список книг в библиотеке

    # Метод для добавления книги
    def add_book(self, book):
        self.__books.append(book)
        print(f"Книга '{book.get_title()
                        }' добавлена в библиотеку {self.__name}.")

    # Метод для вывода всех книг в библиотеке
    def show_books(self):
        print(f"Книги в библиотеке {self.__name}:")
        for book in self.__books:
            book.show_info()  # Вызываем метод show_info у каждого объекта Book
