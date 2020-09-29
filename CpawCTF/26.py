a = 32134
b = 1584891
c = 193127
d = 3438478
for i in range(d):
    x = b * i + a
    if x % d == c:
        print(x)