import random, time


def gcd1(a, b):
    """Нахождение наибольшего обещего делителя медленный"""
    if a == b:
        return a
    elif a > b:
        return gcd1(a-b, b)
    else:
        return gcd1(a, b-a)


def gcd2(a, b):
    """Нахождение наибольшего обещего делителя быстрый"""
    if b == 0:
        return a
    else:
        return gcd2(b, a % b)


def gcd2_1(a, b):
    """Нахождение наибольшего обещего делителя быстрый укороченный"""
    return a if b == 0 else gcd2_1(b, a % b)


def test(func, n: int):
    for _ in range(n):
        a, b = random.randint(9, 999), random.randint(999, 99999)
        s = time.time()
        x = func(a, b)
        f = time.time()
        print(f'Наибольший общий делитель чисел {a} и {b} = {x}. Время исполнения алгоритма: {(f-s)*1000} миллисекунд.    {func.__doc__}')


if __name__ == '__main__':
    test(gcd1, 5)
    test(gcd2, 5)
    test(gcd2_1, 5)
