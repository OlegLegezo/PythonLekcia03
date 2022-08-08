

data1 = "1 2 3 5 8 15 23 38".split()

res = map(int, data1)
# список только четных
res = filter(lambda x: not x % 2, res)
# тут кортеж
res = list(map(lambda x: (x, x**2), res))
print(res)
