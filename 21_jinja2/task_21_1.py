# -*- coding: utf-8 -*-
'''
Задание 21.1
Создать функцию generate_config.
Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон
Функция должна возвращать строку с конфигурацией, которая была сгенерирована.
Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.
'''
from jinja2 import Environment, FileSystemLoader
from yaml import safe_load
import os


def generate_config(template, data_dict):
    with open(data_dict) as src:
        vars_dict = safe_load(src)
    template_dir, template_file = os.path.split(template)
    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True)
    templ = env.get_template(template_file)
    return templ.render(vars_dict)

#don't run on import
if __name__ == '__main__':
    print(generate_config("templates/for.txt", "data_files/for.yml"))