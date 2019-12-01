# -*- config: utf8 -*-
import requests

adresok = 'сыктывкар карла маркса 197'

r = requests.get('http://dev.virtualearth.net/REST/v1/Locations?CountryRegion=RU&addressLine={}&key=AjpbWY8LT5rqIET70iVolfI0biR-u9P5jg5hSuAllOPS77_mHdD7EXMImvKlYlPT'.format(adresok))
d = r.json()
print('Геоданные: ', d['resourceSets'][0]['resources'][0]['point']['coordinates'])
print('Адресок:')
for key, value in d['resourceSets'][0]['resources'][0]['address'].items():
    print('{:>20}  {:<}'.format(key, value))



#r = requests.get('https://www.dns-shop.ru/shops/syktyvkar')
#print(r.text)
#print(r.json())
#https://www.dns-shop.ru/shops/syktyvkar/