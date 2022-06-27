'''Задача №5. Секция статьи "Задача №5."
Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
предел (limit), после чего попробуйте сгенерировать по порядку все числа.
Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.'''

import itertools
import math


def count_find_num(primesL, limit):
    min = 1  # minimum multiplyer
    for number in primesL:
        min = min * number
    degree_list = []
    for number in primesL:
        degree_list.append(
            [number ** x for x in range(1, math.floor(
                math.log(limit / (min / number), number)) + 1)])
    degree_tuples = list(itertools.product(*degree_list))
    result = []
    for tup in degree_tuples:
        multiply = 1
        for number in tup:
            multiply = multiply * number
        if multiply <= limit:
            result.append(multiply)
    if len(result):
        return [len(result), max(result)]
    return []


def test_ip():
    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []


if __name__ == "__main__":
    test_ip()
    print("All tests passed!")
