class StringUtils:
    def reverse_string(self, input_str, expected_output):
        """
        тест 1: Переворачивает строку и возвращает перевернутую строку.
        Пример: `reverse_string("привет") -> "тевирп"`
        """
        return input_str[::-1]

    def capitalize(self, string: str) -> str:
        """
        тест 2: Делает первую букву строки заглавной и возвращает строку.
        Пример: `capitalize ("venera")-> "Venera"`
        """
        return [string.capitalize()](string.capitalize)
    def trim(self, string: str) -> str:
        """
        тест 3: Удаляет пробелы в начале строки и возвращает обрезанную строку.
        Пример: `trim("   venera") -> "venera"`
        """
        return [string.lstrip()](string.lstrip())

    def contains(string: str, symbol: str) -> bool:
        """
        тест 4: Проверяет наличие символа в строке и возвращает True/False.
        Пример 1: `contains('SkyPro'), 'S') -> True`
        Пример 2: `contains('SkyPro'), 'U') -> False`
        """
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        тест 5: Удаляет все вхождения указанного символа из строки и возвращает новую строку.
            `string` - строка для обработки
            `symbol` - искомый символ для удаления
        """
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string

    def list_to_string(self, lst: list, joiner=", ") -> str:
            """
        Тест 6: Преобразует список элементов в строку с указанным разделителем \n
        Параметры: \n
        lst - список элементов \n
        joiner - разделитель элементов в строке. По умолчанию запятая (", ") \n
        Пример 1: list_to_string([1,2,3,4]) -> "1, 2, 3, 4"
        Пример 2: list_to_string(["Sky", "Pro"]) -> "Sky, Pro"
        Пример 3: list_to_string(["Sky", "Pro"], "-") -> "Sky-Pro"
            """
            string = ""
            length = len(lst)

            if length == 0:
                return string

            for i in range(0, length - 1):
                string += str(lst[i]) + joiner

            return string + str(lst[-1])