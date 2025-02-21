﻿import pytest
from string_utils import StringUtils

string_util = StringUtils

# тест 1: Переворачивает строку и возвращает перевернутую строку, тестирует функцию reverse_string с различными входными параметрами.

# @pytest.mark.parametrize(
#     "input_str, expected_output",
#     [
#         ("Тест", "тест"),
#         ("", ""),
#         (" ", " "),
#         (None, None),
#         ("123", "321"),
#         ("04 апреля 2023", "3204 арылапр 2304"),
#     ],)
# def test_reverse_string(input_str, expected_output):
#     string_util = StringUtils
#     # assert StringUtils.reverse_string(input_str) == expected_output
#     assert [StringUtils.reverse_string(input_str)], (StringUtils.reverse_string(input_str)) == expected_output
#     # Обработка случая, когда input_str является None
#
#     if input_str is None:
#         result = test_reverse_string(None)
#         assert (
#             result == expected_output
#         ), f"Ожидалось {expected_output}, но получилось {result}"
#     else:
#         result = test_reverse_string(input_str)
#         assert (
#             result == expected_output
#         ), f"Ожидалась строка '{expected_output}', но получилась '{result}'"
@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("Тест", "тсеТ"),  # Реверс строки
        ("", ""),
        (" ", " "),
        (None, None),
        ("123", "321"),  # Реверс строки
    ],
)
def test_reverse_string(input_str, expected_output):
    string_util = StringUtils()
    assert string_util.reverse_string(input_str) == expected_output

    # тест кейс 2: Проверяет, делает функцию "capitalize" первую букву заглавной
    @pytest.mark.parametrize(
        "string, result",
    [
        # pozitive:
        ("hello", "Hello"),
        ("venera", "Venera"),
        ("h", "H"),
        ("python", "Python"),
        ("привет", "Привет"),
        # negative:
        ("Hello", "Hello"),
        ("LTE", "Lte"),
        ("123abc", "123abc"),
        ("Skypro", "skypro"),
    ], )
    def test_capitalize(string, result):
        string_util = StringUtils
        print(f"input string: {string}")
        print(f"Expected result: {result}")
        res = string_util.capitalize(string)
        print(f"Actual result: {res}")
        assert res == result

    # Тест кейс 3: Проверяет, наличие символа в строке и возвращает True/False.
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
            ("City", "c", False),
            ("parameter", "P", False),
            ("hello", "x", False),
            ("hello", "!", False),
            ("hello", "", False),
            ("", "x", False),
            ("hello", "xyz", False),
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

    # Тест кейс 3: Проверяет, удаляет ли функция "trim" пробелы в начале строки и возвращает обрезанную строку.
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
# Тест кейс 4: Проверяет, удаляет ли функция "delete_symbol" указанный символ
# @pytest.mark.parametrize(
#     "string, symbol, result",
#     [
#         # positive test cases:
#         ("test", "t", "es"),
#         ("Voshod", 'o', "Vshd"),
#         ("123", "1", "23"),
#         ("Sky Pro", "", "SkyPro"),
#         ("spase", "spa", "se"),
#         # negative test cases:
#         ("moon", "k", "moon"),
#         ("", "", ""),
#         ("", "l", ""),
#         ("milk", "", "milk"),
#     ],)
# def test_delete_symbol(string, symbol, result):
#     string_util = StringUtils()
#     res = string_util.delete_symbol(string, symbol)
#     assert res == result

    @pytest.mark.parametrize (
        "string, symbol, result",
    [
        # positive test cases:
        ("test", "t", "es"),
        ("Voshod", 'o', "Vshd"),
        ("123", "1", "23"),
        ("Sky Pro", " ", "SkyPro"),
        ("spase", "spa", "se"),
        # negative test cases:
        ("moon", "k", "moon"),
        ("", "", ""),
        ("", "l", ""),
        ("milk", "", "milk"),
    ],
    )
    def delete_symbol(string, symbol):
        return string.replace(symbol, '')
    #Тест 6: Преобразует список элементов в строку с указанным разделителем \n
    @pytest.mark.parametrize('list, output_list', [
        (["", "", "", ""], ",,,"),
        ([" ", " ", " ", " "], " , , , "),
    ],)
    def test_list_to_string_negative(list, output_list):
        string_util = StringUtils()
        assert string_util.list_to_string(list) == output_list


