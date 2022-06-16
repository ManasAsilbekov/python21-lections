'''==========================комприхеншиоун================================'''
#сокращение слов
#генерация последовательностей в одну строку используя цикл
# действие for # in итерируемый обьект [if фильтр]
# есть 2 варика как шо делать
# результат for # in итерируемый обьект [if фильтр]
# результат  for # in итерируемый обьект [if фильтр] if фильтр
# 1 вармант

"=======================list"
"Создать список состоящий из чисел от 1 до 10 умножений на 2"
list_ = []
for a in range (11):
    list_.append(a)
print(list_)

# 2 вариант

list_ = list_(i*2 for i in range (1, 11))
# list_ = [1,4,6,8,10,12,14,16,18,20]

list_ = (i*2 for i in range (1, 11))
# list_ = [1,4,6,8,10,12,14,16,18,20]

"создать список состоящий из четных чисел от 1 до 10"

list_ = []
for i in range(1,11):
    #if not 0 (Четное)
    if not i % 2:
        list_.append(i)

list_ = [i for i in range(1,100)if not i%2]

list_ = [i for i in range(2,11,2)]

# list_ = [2,4,6,8,10]

list_ = [print(i) for i in range(10)]
print(list_)
#[none,none......none]

list_ = ["hello" for i in range(10)]
# ["hello","hello","hello","hello","hello","hello","hello","hello","hello","hello"]

print([input() for i in range(10)])
# на каждом итерации запрашивает инпут


"Создать список состоящий из чисел от 1 до 10, но вместо чисел написать (четное или не четное)"

list_ = [ 'нечетное' if i % 2 else 'четное' for i in range(1, 11) ]
print(list_)
# [нечетное,четное,,,,,,,,,,,,,,,,,,,,,]

list_ = [ (i, 'нечетное' if i % 2 else 'четное') for i in range(1, 11) ]
print(list_)
# [1нечетное,2четное ,,,,,,,,,,,,,,,,,,,,]

# Создать список из чисел,находящихся в list1, заменив их на четное или не четное
list1 = [1,'hello', 3, 'a', 4, 6, 8, 'hw']
[ 'нечетное' if i % 2 else 'четное' 
for i in list1 
if type(i) == int or type(i) == float ]
print(list_)


"==================Dict comprehension==============="
# Создать словарт,где ключи - числа от 1 до 10,а значения эти числа ввиде строки
list_ = dict( (i, str(i)) for i in range (1, 11) )
# {1:, '1', 2: '2' ......................}


"даны 2 списка, создайте словарь где ключи, элементы 1 списка, а значения - второго"

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

dict_ = dict( (list1[index], list2[index]) for index in range(len(list1) ) )
print(dict_)
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

dict_ = {(list1[index]: list2[index]) for index in range(len(list1) ) }
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}


'создайте копию словаря'
dict1 = {"a":1, "b":2, 4:"c"}
dict2 = { key: value for key, value in dict1.items() }

"поменяйте ключ и значение местами"
dict1 = {"a":1, "b":2, 4:"c"}
dict2 = { value: key for key, value in dict1.items() }
# {1:"a", 2:"b", "c":4}

"дан словарь, где значение - список с числами, создайте новый словарь, где значения - сумма тех чисел"
dict1 = {
    "a":[1,2,3,4,5],
    "b":[10,30,2,5],
    "c":[74,28,47],
    "d":[4,6,2,92,9]
    }

dict2 = { key: sum(value) for key, value in dict1.items() }
print(dict)
# {'a': 15, 'b' : 47, 'c' : 149, 'd' : 113}

"======================Вложенные comprehension==============="
"создайте словарь, шде ключами будут числа от 1 до 10, ф значениями спсики от 1 до числа (который ключ)"

dict_ = {i: list(range(1, i+1)) for i in range (1, 5) }
# {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4].......................}

dict_ = {i: [j for j in range(1, i+1)] for i in range (1, 5) }
# {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4].......................}

'Создайте список, состоящий из 10 списков, в которых строка "hello world" повторяется 5 раз'

list_ = [
    ["hello world" for i in range(5)]
    for i in range(10)
]
#"hello world"
"hello world""hello world""hello world""hello world""hello world"
"hello world"
"hello world""hello world""hello world""hello world""hello world"
"hello world"
"hello world""hello world""hello world""hello world""hello world"
"hello world"
"hello world""hello world""hello world""hello world""hello world"