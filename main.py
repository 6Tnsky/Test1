def count_vowels(string):
    """
    Функция для подсчета количества гласных в строке на русском языке.

    :param string: Входная строка
    :return: Количество гласных в строке
    """
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"  # Список русских гласных букв (строчные и прописные)
    return sum(1 for char in string if char in vowels)
