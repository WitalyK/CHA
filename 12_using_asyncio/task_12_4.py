# -*- coding: utf-8 -*-

"""
Задание 12.4

Создать класс CiscoSSH, который наследует класс BaseSSH из файла base_ssh_class.py.

Переписать метод connect в классе CiscoSSH:

1. после подключения по SSH должен выполняться переход в режим enable. Для этого также необходимо добавить
параметр secret к методу __init__.
2. после перехода в режим enable, отключить paging (команда terminal length 0)

Добавить методы:

* send_show_command - принимает как аргумент команду show и возвращает
   вывод полученный с обрудования
* send_config_commands - должен уметь отправлять одну команду конфигурационного
  режима или список команд. Метод дожен возвращать вывод аналогичный методу
  send_config_set у netmiko.

Проверить работу класса.
Ограничение: нельзя менять класс BaseSSH.

Для заданий в этом разделе нет тестов!
"""
from base_ssh_class import BaseSSH
import async_timeout, yaml, asyncio, asyncssh


class CiscoSSH(BaseSSH):
    def __init__(self, host, username, password, secret, timeout=30):
        super().__init__(host, username, password, timeout=timeout)
        self.secret = secret

    async def connect(self):
        await super().connect()
        with async_timeout.timeout(self.timeout):
            self._writer.write('enable' + '\n')
            await self._reader.readuntil('#')
            self._writer.write('terminal length 0' + '\n')
            await self._reader.readuntil('#')
        return self

    async def send_show_command(self, sh_command):
        with async_timeout.timeout(self.timeout):
            self._writer.write(sh_command + '\n')
            output = await self._reader.readuntil('#')
        return output

    async def send_config_commands(self, conf_commands):
        if isinstance(conf_commands, str): conf_commands = [conf_commands]
        with async_timeout.timeout(self.timeout):
            self._writer.write('conf t' + '\n')
            output = await self._reader.readuntil('#')
            for command in conf_commands:
                self._writer.write(command + '\n')
                output += await self._reader.readuntil('#')
            self._writer.write('end' + '\n')
            output += await self._reader.readuntil('#')
        return output


async def send_show_command_to_device(device_to_show, command_sh):
    async with CiscoSSH(**device_to_show) as ssh:
        output = await ssh.send_show_command(command_sh)
    return output


async def send_config_command_to_device(device_to_conf, command_conf):
    async with CiscoSSH(**device_to_conf) as ssh:
        output = await ssh.send_config_commands(command_conf)
    return output


async def main(devs, shcomand, confcommands):
    tasks = [asyncio.create_task(send_show_command_to_device(dev, shcomand)) for dev in devs]
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)
    print('*' * 50)
    tasks = [asyncio.create_task(send_config_command_to_device(dev, confcommands)) for dev in devs]
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)


# don't run on import
if __name__ == "__main__":
    with open('devices_netmiko.yaml') as f:
        devices = yaml.safe_load(f)
    for device in devices:
        del device['device_type']
    show_command = 'sh ip int br'
    config_command = ['router ospf 55',
                      'auto-cost reference-bandwidth 1000000',
                      'network 0.0.0.0 255.255.255.255 area 0']
    asyncio.run(main(devices, show_command, config_command))
