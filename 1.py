# -*- config: utf8 -*-
from urllib.parse import urlparse, urlunparse

original = 'http://prognozrk.ru/prognoz/48/sykt.shtml'
print('ORIG  :', original)
parsed = urlparse(original)
print('PARSED:', type(parsed), parsed)
t = parsed[:]
print('TUPLE :', type(t), t)
print('NEW   :', urlunparse(t))

