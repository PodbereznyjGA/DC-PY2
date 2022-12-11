
# TODO Написать 3 класса с документацией и аннотацией типов
class Account:
    def __int__(self, status_, friends):
        """
        Подготовка к работе объекта класса "Аккаунт"
        :param status_: статус аккаунта( online/offline)
        :param friends: количество друзей на аккаунте
        примеры:
        >>> my_Account = Account(0, 200)
        """

        if not isinstance(friends, (int, float)):
            raise TypeError("Введите количество друзей цифрами")
        if friends < 0:
            raise ValueError("Количество друзей не может быть отрицательным")
        self.friends = friends
        if (status_ != 0) and (status_ != 1):
            raise ValueError("Аккаунт может быть offline(0) или online(1)")
        self.status_ = status_

    def online(self):
        """"
        Устанавливаем статус аккаунта online.
        :raise ValueError: вызывает ошибку, если аккаунт online при вызове метода
        Примеры:
        >>> my_Account = Account(0, 200)
        >>> my_Account.online()
        """

    def offline(self):
        """"
        Устанавливаем статус аккаунта offline.
        :raise ValueError: вызывает ошибку, если аккаунт ofline при вызове метода
        Примеры:
        >>> my_Account = Account(1, 200)
        >>> my_Account.offline()
        """


    def add_friends(self, friends_input):
        """
        :param friends_input: количество добавленных друзей
        Добавляем количество добавленных друзей
        :raise TypeError: вызывает ошибку при попытке ввести не целое число друзей
        :raise ValueError: вызывает ошибку при добавлении отрицательного значения людей
        :raise ValueError: вызывает ошибку, если аккаунт offline
        :return: новое число друзей
        примеры:
        >>> my_Account = Account(1, 200)
        >>> my_Account.add_friends(10)
        """

    def del_friends(self, friends_input):
        """
        :param friends_input: количество добавленных друзей
        Добавляем количество добавленных друзей
        :raise TypeError: вызывает ошибку при попытке ввести не целое число друзей
        :raise ValueError: вызывает ошибку при добавлении отрицательного значения людей
        :raise ValueError: вызывает ошибку, если аккаунт offline
        :return: новое число друзей
        примеры:
        >>> my_Account = Account(1, 200)
        >>> my_Account.del_friends(5)
        """

class House:
    def __init__(self, status_, roomers, rooms):
        """"
        Создание объекта класса "Дом"
        :param status_: открыт или закрыт дом
        :param roomers: количество постояльцев
        :param rooms: количество комнат в доме
        Примеры:
        >>> my_House = House(0, 3, 4)
        """


        if (status_ != 0) and (status_!= 1):
            raise ValueError("Дом может быть открыт(1) или закрыт (0)")
        self.status_ = status_
        if not isinstance(roomers, (int, float)):
            raise TypeError("Введите количество постояльцев в цифрах")
        if roomers < 0:
            raise ValueError("Количество жильцов не может быть отрицательным")
        self.roomers = roomers
        if rooms < 0:
            raise ValueError("Количество комнат не может быть отрицательны")
        if not isinstance(rooms, (int, float)):
            raise TypeError("Введите количество комнат в цифрах")
        self.rooms = rooms
    def open_House(self):
        """"
        Открывает дом, выводится сообщение (дом открыт).
        :raise ValueError: вызывает ошибку, если дом уже открыт при вызове метода
        Примеры:
        >>> my_House = House(0, 3, 4)
        >>> my_House.open_House()
        """


    def close_House(self):
        """"
        Закрывает дом, выводится сообщение (дом закрыт).
        :raise ValueError: вызывает ошибку, если дом уже закрыт при вызове метода
        Примеры:
        >>> my_House = House(1, 3, 4)
        >>> my_House.close_House()
        """


    def add_roomers(self, roomers_input):
        """
        :param roomers_input: количество заселяемых людей
        Добавляем постояльцев, если дом открыт
        :raise TypeError: вызывает ошибку при попытке ввести не целое число постояльцев
        :raise ValueError: вызывает ошибку при заселении отрицательного значения людей
        :raise ValueError: вызывает ошибку, если дом закрыт
        :return: новое число постояльцев
        примеры:
        >>> my_House = House(1, 3, 4)
        >>> my_House.add_roomers(5)
        """

    def eject_roomers(self, roomers_input):
        """
        Выселяем постояльцев, если дом открыт
        :param roomers_input: количество выселяемых людей
        :raise TypeError: вызывает ошибку при попытке ввести не целое число постояльцев
        :raise ValueError: вызывает ошибку при выселении отрицательного значения людей
        :raise ValueError: вызывает ошибку, если дом закрыт
        :return: новое число постояльцев
        Примеры:
        >>> my_House = House(1, 3, 4)
        >>> my_House.eject_roomers(2)
        """

class Auto_:
    def __int__(self, construct, cubic_capasity, horsepower):
        """
        Создание и подготовка к работе объкта "Автомобиль"
        :param construct: конструкция кузова
        :param :cubic_capasity: объем двигателя
        :param horsepower: количество лошадиных сил
        Примеры:
        >>> My_Auto = Auto_("Седан", 1998, 180)
        """
        if not isinstance(construct, str):
            raise TypeError("Введите тип кузова текстом")
        self.construct = construct
        if not isinstance(cubic_capasity, (int, float)):
            raise TypeError("Введите объем двигателя в кубических сантиметрах")
        if cubic_capasity <= 0:
            raise ValueError("Объем не может быть отрицательным")
        self.cubic_capasity = cubic_capasity
        if not isinstance(horsepower, (int, float)):
            raise TypeError("Введите мощность двигателя в лошадиных силах")
        if horsepower <= 0:
            raise ValueError("Мощность двигателя не может быть отрицательной")
        self.horsepower = horsepower


    def construct_check(self):
        """
        Метод определяет тип кузова
        :return: возвращает тип кузова
        Примеры:
        >>> My_Auto = Auto_("Кабриолет", 1998, 180)
        >>> My_Auto.construct_check()
        """



    def chip_tuning(self, power):
        """
        Метод увеличивает значение лошадиных сил при тюнинге
        :param power: значение, на которое увеличатся лошадиные силы
        :raise TypeError: ошибка возникает, если введено не число
        :return: возвращает новое значение лошадиных сил
        Примеры:
        >>> My_Auto = Auto_("Кабриолет", 1998, 180)
        >>> My_Auto.chip_tuning(20)
        """
        ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()
