

data = [x for x in range(10)]
print(data)
# res = list(filter(lambda x: x % 2 == 0, data))
res = list(filter(lambda x: not x % 2, data))
print(res)
