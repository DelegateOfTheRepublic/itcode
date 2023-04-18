from math import sqrt
import numpy as np
import random as rnd

def raise_to_power(num: float, power: int) -> int:
    if num == 1:
        return num

    values: list = []
    raised_prev: float = num
    bin_power: str = f"{power:b}"
    result: int = 1
    i: int = 2

    values.append(raised_prev)

    while i < power - 1:
        raised_prev *= raised_prev
        values.append(raised_prev)
        i *= 2

    for i in range(len(values)):
        if bin_power[len(bin_power) - i - 1] != '0':
            result *= values[i]

    return result if result != 0 else raised_prev * raised_prev


def is_prime_stochastic(number: int, maxTests: int) -> bool:
    """Данный алгоритм является тестом простоты Ферма - вероятностный тест"""
    for i in range(1, maxTests):
        n = rnd.randint(1, number)
        if (raise_to_power(n, number - 1) % number != 1):
            return False

    return True

def is_prime(number: int) -> bool:
    """Данный алгоритм - решето Эратосфена"""
    primes: list = []
    is_composite: np.ndarray = np.zeros(number + 1, dtype=bool)
    next_prime: int = 2
    stop_at: int = int(sqrt(number))

    for i in range(4, number + 1, 2):
        is_composite[i] = True

    while next_prime <= stop_at:
        for i in range(next_prime ** 2, number + 1, next_prime):
            if is_composite[i]:
                is_composite[i] = True

        next_prime += 2

        while next_prime <= number and is_composite[next_prime]:
            next_prime += 2

    for i in range(2, number + 1):
        if not is_composite[i]:
            primes.append(i)

    return True if len(primes) == 2 else False

if __name__ == '__main__':
    number: int = 19
    maxTests: int = 25

    print(f'Проверка на простоту по тесту Ферма для числа {number}: {is_prime_stochastic(number, maxTests)}\n')
    print(f'Проверка на простоту по решету Эратосфена для числа {number}: {is_prime(number)}')