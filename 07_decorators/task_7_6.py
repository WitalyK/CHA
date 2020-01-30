# -*- coding: utf-8 -*-
"""
Задание 7.6

Создать декоратор total_order, который добавляет к классу методы:

* __ge__ - операция >=
* __ne__ - операция !=
* __le__ - операция <=
* __gt__ - операция >


Декоратор total_order полагается на то, что в классе уже определены методы:
* __eq__ - операция ==
* __lt__ - операция <

Если методы __eq__ и __lt__ не определены, сгенерировать исключение ValueError при декорации.

Проверить работу декоратора можно на примере класса IPAddress. Определение класса нельзя менять, можно только декорировать.
Декоратор не должен использовать переменные класса IPAddress. Для работы методов
должны использоваться только существующие методы __eq__ и __lt__.
Декоратор должен работать и с любым другим классом у которого
есть методы __eq__ и __lt__.


Пример проверки методов с классом IPAddress после декорирования:
In [4]: ip1 = IPAddress('10.10.1.1')

In [5]: ip2 = IPAddress('10.2.1.1')

In [6]: ip1 < ip2
Out[6]: False

In [7]: ip1 > ip2
Out[7]: True

In [8]: ip1 >= ip2
Out[8]: True

In [9]: ip1 <= ip2
Out[9]: False

In [10]: ip1 == ip2
Out[10]: False

In [11]: ip1 != ip2
Out[11]: True

"""
from pprint import pprint
import ipaddress


def total_order(cls):
    list1 = list(cls.__dict__)
    if '__eq__' in list1 and '__lt__' in list1:
        pprint(list(cls.__dict__))
        def __ne__(self, other):
            return not self.__eq__(other)

        def __gt__(self, other):
            return not self.__lt__(other) and not self.__eq__(other)

        def __ge__(self, other):
            return not self.__lt__(other) or self.__eq__(other)

        def __le__(self, other):
            return self.__lt__(other) or self.__eq__(other)

        setattr(cls, '__ne__', __ne__)
        setattr(cls, '__gt__', __gt__)
        setattr(cls, '__ge__', __ge__)
        setattr(cls, '__le__', __le__)
    else:
        print('Ы')
        raise ValueError('Не определены методы __eq__ и __lt__')
    return cls


@total_order
class IPAddress:
    def __init__(self, ip):
        self._ip = int(ipaddress.ip_address(ip))

    def __repr__(self):
        return f"IPAddress('{self._ip}')"

    def __eq__(self, other):
        return self._ip == other._ip

    def __lt__(self, other):
        return self._ip < other._ip


# don't run on import
if __name__ == "__main__":
    ip1 = IPAddress('10.10.1.1')
    ip2 = IPAddress('10.2.1.1')
    print(ip1 < ip2)
    print(ip1 > ip2)
    print(ip1 >= ip2)
    print(ip1 <= ip2)
    print(ip1 == ip2)
    print(ip1 != ip2)
