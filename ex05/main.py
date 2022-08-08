users = ['user1', 'user2', 'user3']
ids = [4, 3, 5]
data=list(zip(users, ids))
print(data)

# а тут будет распечатан кортеж по мин (но нумеровать можно функцией enumerate)
salary=[123,222]
data2=list(zip(users, ids, salary))
print(data2)

# (но нумеровать можно функцией enumerate)
data3=list(enumerate(users))
print(data3)