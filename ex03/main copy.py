
# формируем новый список и возвращаем
def select(f, col):
    return [f(x) for x in col]

# возвращаем список
def where(f, col):
    return[x for x in col if f(x)]


data1 = "1 2 3 5 8 15 23 38".split()

res = select(int,data1)
# список только четных
res = where(lambda x: not x % 2, res)
# тут кортеж
res = select(lambda x: (x,x**2), res)
print (res)
