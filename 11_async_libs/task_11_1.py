# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать сопрограмму (coroutine) send_config_commands. Сопрограмма
должна подключаться по SSH с помощью asyncssh к одному устройству,
переходить в режим enable, в конфигурационный режим, выполнять указанные команды,
а затем выходить из конфигурационного режима.

Параметры функции:

* host - IP-адрес устройства
* username - имя пользователя
* password - пароль
* enable_password - пароль на режим enable
* config_commands - список команд или одна команда (строка), которые надо выполнить

Функция возвращает строку с результатами выполнения команды:

In [1]: import asyncio

In [2]: from task_11_1 import send_config_commands

In [3]: commands = ['interface loopback55', 'ip address 10.5.5.5 255.255.255.255']

In [4]: print(asyncio.run(send_config_commands('192.168.100.1', 'cisco', 'cisco', 'cisco', commands)))
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#interface loopback55
R1(config-if)#ip address 10.5.5.5 255.255.255.255
R1(config-if)#end
R1#

In [5]: asyncio.run(send_config_commands(**r1, config_commands=commands))
Out[5]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loopback55\r\nR1(config-if)#ip address 10.5.5.5 255.255.255.255\r\nR1(config-if)#end\r\nR1#'


Запустить сопрограмму и проверить, что она работает корректно.
При необходимости можно создавать дополнительные функции.

Для заданий в этом разделе нет тестов!
"""
import asyncio
import asyncssh


async def send_config_commands(device, conf_commands):
    if isinstance(conf_commands, str):
        conf_commands = [conf_commands]
    print(f"Подключаюсь к {device['host']}")
    ssh_coroutine = asyncssh.connect(**device)
    ssh = await asyncio.wait_for(ssh_coroutine, timeout=10)
    writer, reader, stderr = await ssh.open_session(term_type="Dumb", term_size=(24, 80))
    await reader.readuntil('#')
    writer.write('terminal length 0\n')
    await reader.readuntil('#')
    writer.write('conf t\n')
    output = await reader.readuntil('#')
    for command in conf_commands:
        print(f'Отправляю команду {command} на {device["host"]}')
        writer.write(command + '\n')
        output += await reader.readuntil('#')
    writer.write('end\n')
    output += await reader.readuntil('#')
    ssh.close()
    print(f'Получили данные от {device["host"]}')
    return output


async def send_command_to_device(*args, **kwargs):
    result = await send_config_commands(*args, **kwargs)
    return result


if __name__ == "__main__":
    r1 = {'host': '10.111.111.11',
          'username': 'admin',
          'password': 'cisco'}
    commands = ['interface loopback55', 'ip address 10.5.5.5 255.255.255.255']
    print(asyncio.run(send_command_to_device(r1, commands)))


