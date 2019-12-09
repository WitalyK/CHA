from re import findall, match, sub
from datetime import datetime


# with open('air1_20191205.log1') as dop:
#     s = dop.read()
# regex1 = (r'\n20:.+\[ movie.+\]\n(\d{2}:\d{2}:\d{2})(?:.+\[ movie.+ \]\n)+(\d{2}:\d{2}:\d{2}).+\[ movie.+ \]')
# if findall(regex1, s):
#     time_span = findall(regex1, s)[0]
#     print(time_span)
#     ss = s.split('\n')
#     r_strings = []
#     flag = False
#     for line in ss:
#         if line.startswith(time_span[1]):
#             break
#         if line.startswith(time_span[0]):
#             flag = True
#         if flag:
#             r_strings.append(match(r'\d{2}:\d{2}:.+\[ (.+) \]', line).group(1))
#     len_rek = datetime.strptime(time_span[1], "%H:%M:%S") - datetime.strptime(time_span[0], "%H:%M:%S")
#     print(time_span[0])
#     print(len_rek)
#     print(r_strings)
r1 = 'video1 00:13:00.00 Время новостей 16-30 1 часть'
r2 = 'video1 00:16:26.00 ДЕТАЛИ ЧАСТЬ 1 '

r = sub(r'1 $', '2 ', r2)
print(r)