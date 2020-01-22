from itertools import combinations


a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
c = [1, 2, 3, 4]
d = [1, 2, 3, 4]
e = [1, 2, 3, 4]
f = [1, 2, 3, 4]
g = [1, 2, 3, 4]
l = [a, b, c, d, e, f, g]
for i in range(2, len(a)+1):
    for item in combinations(l, i):
        print(item)

