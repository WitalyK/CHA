import pytest
import task_14_1
import sys

sys.path.append('..')

from common_functions import check_function_exists, check_function_params


def test_function_created():
    check_function_exists(task_14_1, 'generate_access_config')


def test_function_params():
    check_function_params(function=task_14_1.generate_access_config,
                          param_count=1, param_names=['intf_vlan_mapping'])


def test_function_retuned_type():
    vlan_mapping = {
        'FastEthernet0/12': 10,
        'FastEthernet0/14': 11,
        'FastEthernet0/16': 17
    }
    correct_value = ['interface FastEthernet0/12',
                     'switchport mode access',
                     'switchport access vlan 10',
                     'switchport nonegotiate',
                     'spanning-tree portfast',
                     'spanning-tree bpduguard enable',
                     'interface FastEthernet0/14',
                     'switchport mode access',
                     'switchport access vlan 11',
                     'switchport nonegotiate',
                     'spanning-tree portfast',
                     'spanning-tree bpduguard enable',
                     'interface FastEthernet0/16',
                     'switchport mode access',
                     'switchport access vlan 17',
                     'switchport nonegotiate',
                     'spanning-tree portfast',
                     'spanning-tree bpduguard enable']
    return_value = task_14_1.generate_access_config(vlan_mapping)
    assert return_value != None, "Функция ничего не возвращает"
    assert type(return_value) == list, "Функция должна возвращать список"
    assert return_value == correct_value, "Функция возвращает неправильное значение"
