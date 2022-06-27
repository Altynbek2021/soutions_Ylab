'''Задача №3. Секция статьи "Задача №3."
Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:

Будьте осторожны 1000! имеет 2568 цифр.

Доп. инфо: http://mathworld.wolfram.com/Factorial.html'''


def zeros(x):
    i = 5
    zeros = 0
    while x >= i:
        zeros += x // i
        i *= 5
    return zeros


print(zeros(1000))


def test_zeros():
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7


if __name__ == "__main__":
    test_zeros()
    print("All tests passed!")
