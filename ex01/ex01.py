def sum(x, y):
    return x+y

# sum=lambda x,y:x+y короткая запись того, что сверху


def sum(x, y): return x+y


def mul(x, y):
    return x*y


def calc(op, a, b):
    print(op(a, b))


# в качестве аргумента тут функция
calc(mul, 4, 5)
# calc(lambda x,y:x+y, 4,5) короткая запись
calc(lambda x, y: x+y, 4, 5)
