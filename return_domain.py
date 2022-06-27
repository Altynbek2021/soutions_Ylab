'''Задача №1. Секция статьи "Задача №1."
Написать метод domain_name, который вернет домен из url адреса:'''


def domain_name(url):
    parsed = url.split('.')
    if parsed[0][:3] == 'htt':
        if parsed[0].split("//")[1] == 'www':
            return parsed[1]
        if 'https' in parsed[0]:
            parsed[0] = parsed[0][8:]
        if 'http' in parsed[0]:
            parsed[0] = parsed[0][7:]
        return parsed[0]
    if parsed[0][:3] == 'www':
        return parsed[1]
    return parsed[0]


def test_domain():
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"


if __name__ == "__main__":
    test_domain()
    print("All tests passed!")
