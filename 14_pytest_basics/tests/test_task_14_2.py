import pytest
import task_14_2, collections.abc
import sys, ipaddress

sys.path.append('..')

from common_functions import check_attr_or_method


def test_attributes():
    net1 = task_14_2.Network('10.1.1.192/30')
    check_attr_or_method(net1, attr="network")
    check_attr_or_method(net1, attr="addresses")
    assert net1.network is not None, "атрибут пустой"
    assert type(net1.network) == str, "аттрибут должен возвращать строку"
    assert net1.network == '10.1.1.192/30', "аттрибут возвращает неправильное значение"
    assert net1.addresses is not None, "атрибут пустой"
    assert type(net1.addresses) == tuple, "аттрибут должен возвращать кортеж"
    assert net1.addresses == ('10.1.1.193', '10.1.1.194'), "аттрибут возвращает неправильное значение"


def test_methods():
    net1 = task_14_2.Network('10.1.1.192/30')
    check_attr_or_method(net1, method="__iter__")
    check_attr_or_method(net1, method="__len__")
    check_attr_or_method(net1, method="__getitem__")
    assert isinstance(net1.__iter__(), collections.abc.Iterable), "метод должен возвращать итератор"
    for ip in net1.__iter__():
        try:
            ip1 = ipaddress.ip_address(ip)
        except ValueError:
            raise ValueError('Итератор возвращает не IP адрес')
    assert net1.__len__() == 2, "метод возвращает неправильное количество адресов"
    assert net1.__getitem__(1) == '10.1.1.194', "метод возвращает неправильное значение"
    assert net1.__getitem__(-1) == '10.1.1.194', "метод возвращает неправильное значение"
    with pytest.raises(IndexError) as excinfo:
        ip1 = net1.__getitem__(2)
