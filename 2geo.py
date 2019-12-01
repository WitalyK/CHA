# -*- config: utf8 -*-
import requests
from re import finditer

with open('html.txt') as html:
    regex = ('<a href="(/shops/\S+/)" title="Магазины DNS (.+)">')
    all_shops = finditer(regex, html.read())
for match in all_shops:
    print(match.groups())

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
r = requests.post('https://www.dns-shop.ru/shops/Aginskoe/', headers=header)
print(r.text)

'''
http-equiv="X-UA-Compatible" content="IE=edge" charset="UTF-8"
name="csrf-param" content="_csrf"
name="csrf-token" content="maAs0qLCqB95e8urPfdIZrX9_yKcbtq0uFNG971lt4zVmWux8arLdRIPrf5wwy5R_aS4aq8-uPH6Yy6E2gjVxw=="
r = requests.get('https://www.dns-shop.ru/shops/syktyvkar')
print(r.text)
print(r.json())
https://www.dns-shop.ru/shops/syktyvkar/
'''