list=[]

for i in range(1,101):
    if(i%2==0):
        list.append(i)

# короткая запись

list2=[i for i in range(1,100) if i%2==0]


# захотели пару каждому из чисел (кортеж)
list3=[(i,i) for i in range(1,20) if i%2==0]

# добавляем функцию

def f(x):
    return x**3

# отбираем числа, а потом возводим в куб
list4=[(i,f(i)) for i in range(1,20) if i%2==0]

print(list4)
