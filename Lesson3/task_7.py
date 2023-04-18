from functools import lru_cache
import decimal

@lru_cache()
def recursive_fib(n: int) -> int:
    """В данной реализации возможено переполнение стека"""
    if n >= 500:
        return 'Слишком большое число'

    if n in (1, 2):
        return 1
    return recursive_fib(n - 1) + recursive_fib(n - 2)

def bine_fib(n: int) -> int:
    decimal.getcontext().prec = 10000

    root_five: decimal.Decimal = decimal.Decimal(5).sqrt()
    phi: decimal.Decimal = (1 + root_five) / 2

    result: decimal.Decimal = (phi ** n - (-phi)**(-n)) / root_five

    return round(result)

if __name__ == '__main__':
    n = int(input('Введите номер числа в ряду Фиббоначи: '))
    print(f'[Бине]: Число Фиббоначи под номером {n} = {bine_fib(n)}')
    print(f'[Рекурсия]: Число Фиббоначи под номером {n} = {recursive_fib(n)}\n')