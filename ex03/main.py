import os
path1 = os.path.join('PythonLekcia03', 'ex03', 'input1.txt')
f = open(path1, 'r')
# прочитал что есть в строчке и добавил пробел:
data1 = f.read()+' '
f.close()



# data1="1 2 3 5 8 15 23 38".split()
print(data1)
numbers = []

while data1 != '':
    spacePos = data1.index(' ')
    numbers.append(int(data1[:spacePos]))
    data1 = data1[spacePos+1]

print(numbers)
# print(numbers)
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)
