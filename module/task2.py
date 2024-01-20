# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов,
# которые также являются свойствами экземпляра.

class Archive:
    """
        Добавляет в списки переменные
    """
    archive_numbers = []
    archive_lines = []

    def __init__(self, number, line):
        self.number, self.line = number, line
        self.archive_numbers.append(number)
        self.archive_lines.append(line)

    def __str__(self):
        return f"{self.number =}, {self.line = }"

    def __repr__(self):
        return f"Archive({self.number, self.line})"


if __name__ == '__main__':
    my_archive1 = Archive(5, "пять")
    my_archive2 = Archive(2, "два")
    my_archive3 = Archive(3, "три")
    print(Archive.archive_lines, Archive.archive_numbers)
    print(my_archive1, repr(my_archive1), sep='\n')
    print(my_archive1.__doc__)
