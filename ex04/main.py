li = [x for x in range(1, 10)]
print (li)
li = list(map(lambda x: x+10, li))
print (li)


# при необходимости можно и другой разделитель в сплит, вот так: .split(',')
data=list(map(int,input().split()))
print(data)
# результат map - некий итератор, по которому можно циклом for пройти один раз (если не указать list перед map)