'=============строки========================'
# строки - неизменяемый тип данных, который предназначен для хранения текста (последовательность стиволов), заключенного в одинарные или двойные ковычки

# Синтаксис;
string1 = 'строка с одинарным ковычками'
string2 = "строка с двойным кавычками"
# error = 'не правильная строка"
string3 = "Don't # внутри двойных ковычек все одинарные - просто символы"
string4 = '"Makers bootkamp"' # внутри одинарных кавычек все двойные - просто символы

string5 = '''
Многострочный текст
в одинарных ковычках
тут можно оставить "любые" кавычки
""""
'''
string6 = """ногострочный текст
в одинарных ковычках
тут можно оставить "любые" кавычки
'''''''
"""





"=====================Экранизация строк=========================="
# экранизация спец - символов
'\n' # перенеос на новую строку
'\t' # табуляция
'\\' # отображения \ (ротому что он является интструкцией, которая влияет на наш код)
'\'' # отображение ковычки '
"\"" # отображение двойных ковычек "
'\r' # возврашение каретки в начала строки
'\v' # перенос на новую строку со смешением вправо на длингу с предыдушей строки
'hello\world' 
#hello
#world

'hello\world'
#hello  world
'чтобы экранировать нужен символ \\'
# чтобы эранировать нужен символ \
'My website is Latracal \rSolution'
# Solutionte is Latracal

'hello\world'
# hello
#      world







"===============Форматирование строк==================="
title = 'плов'
price = 1500
format1 =  f'название: {title}, цена: {price} '
# Название: плов, Цена: 1500

format2 = 'Название: %s, цена: %s'
print(format2 % ("Гуляш", "250"))
print(format2 % ("Самсы", "70"))
# Название: Гуляш, Цена: 250
# Название: Самсы, Цена: 70

format3 = 'Название: {}, цена: {}'
print(format3.format('Шакарап', '35'))
# Название: Шакарап, Цена: 35






"===============Методы строк======================="
# Методы тиов данных - функции, к которым мы обрашаемся через точку
dir(str) # Позволяет посмотреть все методы класса (типа данных)
print(dir(str))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

'HELLO' .lower() # 'hello'
'hello' .upper() # 'HELLO'
'hello' .swapcase() # 'hELLO'

'hello' .title() # 'Hello'
'hello world' .title() # 'Hello World'

'hello world' .capitalize() # 'Hello world'
'hello' .center() # '   hello   '
'hello' .center(11, '-') # '---hello---'

'hello' .count('l') #2
'hello' .count('ll') #1
'hello hello' .count('hello') #2
'hello' .count('w') #0

'hello world' .startswith('hell') # True
'hello world' .startswith('h') # False
'Hello world' .endswith('ld') # true

'hello world' .find(' ') # 5
'hello world' .find('o') #4
'hello world' .find('wo') #6
'hello world' .find('hello') #0

'hello world' .split() #['hello', 'world']
'hello world' .split('o') #['hell', ' w' 'rld']
'$'.join(['hello', 'world']) # 'hello$world'
' '.join(['hello', 'world']) # 'hello world'
''.join(['hello', 'world']) # 'helloworld'

# конкатенация - склеивание строк
'hello' + 'world' # 'helooworld'







"==================Индексы======================="
# тндексы - порядковый ноиер символы в строке
'h e l l o w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
string = 'hello world'
string[0] # 'h'
string[10] # 'd'
string[5] # '  '


# срез - подстрока строки
string[0:5] # 'hello'
string[0:6] # 'hello '
string[2:4] # 'll'
string[0:5][2:4] # 'll'

string[:5] # 'Hello'
string[6:] # 'world'
string[:] # 'hello world'
string[0:11:2] #'hlowrd'
string[::3] # 'hlwl'
string[::-1] # 'dlrow olleh'
string[::-2] # 'drwolh'





"======================Доп инфа================="
a = 5
b = 5
print(id(a))
print(id(b))

print(hash(a))
