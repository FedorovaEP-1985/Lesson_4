import pytest

from string_utils import StringUtils
string_util = StringUtils()

# Тест 1: Переворачивает строку и возвращает перевернутую строку,
# тестирует функцию reverse_string с различными входными параметрами.


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("Тест", "тсеТ"),  # Реверс строки
        ("", ""),         # Пустая строка
        (" ", " "),       # Строка с пробелом
        (None, None),    # None
        ("123", "321"),  # Реверс строки с цифрами
    ],
)
def test_reverse_string(input_str, expected_output):
    string_util = StringUtils()
    assert string_util.reverse_string(input_str) == expected_output
    # Тест кейс 2: Проверяет, делает функцию "capitalize"
    # первую букву заглавной.

    @pytest.mark.parametrize(
        "string, result",
        [
            # Positive cases
            ("hello", "Hello"),
            ("venera", "Venera"),
            ("h", "H"),
            ("python", "Python"),
            ("привет", "Привет"),
            # Negative cases
            ("Hello", "Hello"), ("LTE", "Lte"), ("123abc", "123abc"),
            ("Skypro", "Skypro"),
        ],
    )
    def test_capitalize(string, result):
        string_util = StringUtils()  # Instantiate the class
        print(f"Input string: {string}")
        print(f"Expected result: {result}")
        res = string_util.capitalize(string)  # Call the method
        print(f"Actual result: {res}")
        assert res == result
    # Тест кейс 3: Проверяет функцию "contains"
    # наличие символа в строке
    # и возвращает True/False.

    @pytest.mark.parametrize(
        "string, symbol, result",
        [
            # positive test cases:
            ("flower", "f", True),
            (" test", "t", True),
            ("space  ", "e", True),
            ("Mary-Anne", "-", True),
            ("123", "1", True),
            ("GPS", "P", True),
            ("", "", True),
            # negative test cases:
            ("City", "c", False), ("parameter", "P", False),
            ("hello", "x", False), ("hello", "!", False), ("hello", "", False),
            ("", "x", False), ("hello", "xyz", False),
        ],
    )
    def test_contains(string, symbol, result):
        string_util = StringUtils()
        print(f"Input string: {string}")
        print(f"Inputed symbol: {symbol}")
        print(f"Expected result: {result}")
        res = string_util.contains(string, symbol)
        print(f"Actual result: {res}")
        assert res == result
    # Тест кейс 4: Проверяет, удаляет ли функция
    # "trim" пробелы в начале строки
    # и возвращает обрезанную строку.

    @pytest.mark.parametrize(
        "string, result",
        [
            # positive test cases:
            ("  dog", "dog"),
            (" ABC", "ABC"),
            ("  123  ", "123  "),
            ("   venera", "venera"),
            ("   Peter1", "Peter1"),
            # negative test cases:
            ("", ""),
            ("ca t", "ca t"),
            ("monkey", "monkey"),
            ("123  ", "123  "),
            (1, 1),
            (0, 0),
        ],)
    def test_trim(string, result):
        string_util = StringUtils()
        print(f"Input string: {string}")
        print(f"Expected result: {result}")
        res = string_util.trim(string)
        print(f"Actual result: {res}")
        assert res == result

    # Тест 5: Проверяет функцию 'delete",
    # удаляет все вхождения указанного символа
    # из строки и возвращает новую строку.
    @pytest.mark.parametrize(
        "string, symbol, result", [
            # positive test cases:
            ("test", "t", "es"), ("Voshod", 'o', "Vshd"), ("123", "1", "23"),
            ("Sky Pro", " ", "SkyPro"), ("spase", "spa", "se"),
            # negative test cases:
            ("moon", "k", "moon"), ("", "", ""),
            ("", "l", ""), ("milk", "", "milk"),
        ],
    )
    def delete_symbol(string, symbol):
        return string.replace(symbol, '')
        # Тест 6: Преобразует список элементов в строку
        # с указанным разделителем \n

    @pytest.mark.parametrize(
        'list, output_list',
        [
            (["", "", "", ""], ",,,"),
            ([" ", " ", " ", " "], " , , , "),
        ],
    )
    def test_list_to_string_negative(
            list, output_list):
        string_util = StringUtils()
        assert string_util.list_to_string(list) == output_list
