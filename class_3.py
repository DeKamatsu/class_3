# class_3


# Working with list
"""
b = ['text_1','text_2']
print (b[1])

b = [
        [
            ['text_1','text_2']
        ]
    ]
print (f"Print element 0-0-1: {b[0][0][1]}")

some_list = [1, 2, 3, 4]
print(some_list[2:])

some_list = [1, 2, 3, 4, 5, 6, 7, 8]
print (f"Print every second element: {some_list[1::2]}")

some_list = [1, 2, 3, 4, 5, 6, 7, 8]
print (f"Print last element: {some_list[len(some_list) - 1]}")



some_list = [1, 2, 3, 4, 5, 6, 7, 8]
del some_list [3]
print (f"List without element #3 (counting from 0): {some_list}")


some_list = [1, 2, 3, 4, 5, 10, 7, 8]
some_list.remove(10) #delete named element
print (some_list)

some_list.pop(2) #delete element by number
print (some_list)

x = []
# Do I have to definite list x!?
for v in some_list:
    if v == 4:
        x.append(v)
    else:
        continue
print(x)

some_list = [1, 2, 3, 4, 5, 10, 7, 8]
if 2 in some_list:
    print('YES')
else:
    print('NO')

# some problem
num = 1
a = f'one is {num}'
print (a)


some_list = ['1', '2', '3', '4', '5', '10', '7', '8', ]
print(f"Number of 10 in list: {some_list.index('10')}")
# Return number of element in list

some_list = ['134', 'f2', '3', '34', '315', '10', '7', '8', ]
some_list.sort()
print(f"Print sorted list: {some_list}")

some_list.reverse()
print(f"Print sorted backward list: {some_list}")
some_list.clear()

# Не глубокая копия: место экономится: 2 имени для одного участка памяти - после очистки имеем 2 пустых списка
some_list = ['134', 'f2', '3', '34', '315', '10', '7', '8', ]
list_copy = some_list
some_list.clear()
print(list_copy)
print(some_list)

# Глубокая копия: место экономится: 2 имени для одного участка памяти - после очистки имеем 2 пустых списка
some_list = ['134', 'f2', '3', '34', '315', '10', '7', '8', ]
list_copy ----------
some_list.clear()
print(list_copy)
print(some_list)
"""

# Working with tuple
some_tuple = ('134', 'f2', '3', '34', '315', '10', '7', '8', )
print(some_tuple)

"""
#Генератор - что-то не работает
t = ()
t = (n for n in range(1,5))
print (t)
"""

a = () # Почему не создается кортеж сразу на основе элементов?
b = 'text'
c = 'text_2'
d = 'text_3'
a = tuple ((a, b, d))
lit = tuple(b)
print (a)
print(lit)

# Working with set

some_set = set(a)

