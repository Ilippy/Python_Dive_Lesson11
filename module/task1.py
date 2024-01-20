# Создайте класс МояСтрока
# где будут доступны все возможности str и дополнительно хранится имя автора строки и время создания (time.time)

from time import time


class MyString(str):
    """
    Строка с именем и временем
    """
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time()
        return instance


if __name__ == '__main__':
    my_str = MyString("строка", "Иван")
    print(my_str.title())
