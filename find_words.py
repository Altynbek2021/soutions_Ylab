'''Задача №4. Секция статьи "Задача №4."
Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.

(Используйте - для обозначения зачеркнутой буквы)

Input: bbananana'''

import itertools


def bananas(s) -> set:
    result = set()
    for mixture in itertools.combinations(range(len(s)), len(s) - len('banana')):
        arr = list(s)
        for i in mixture:
            arr[i] = '-'
        intermediate_result = ''.join(arr)
        if intermediate_result.replace('-', '') == 'banana':
            result.add(intermediate_result)
    return result


def test_banana():
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {
        "ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}


if __name__ == "__main__":
    test_banana()
    print("All tests passed!")
