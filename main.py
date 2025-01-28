# main.py

def get_remainder(dividend, divisor):
    """
    Функция для вычисления остатка от деления.
    Если делитель равен 0, вызывается исключение ValueError.
    """
    if divisor == 0:
        raise ValueError("Деление на ноль невозможно")

    return dividend % divisor