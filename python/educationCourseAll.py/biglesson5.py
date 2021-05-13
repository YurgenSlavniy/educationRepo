#______________________________
# УРОК 5 -  МОДУЛИ И БИБЛИОТЕКИ
#______________________________
#
# 1. Модули. Определение. Применение. Подключение модулей
# 2. Стандартные модули math. random
# 3. Создание собственных модулей
# 4. Пакеты
# 5. Модули as, sys
# 6. Запуск скрипта с параметрами
#
# Модули.
# - определение модуля
# - зачем нужны модули
# - Разновидности модулей
# - подключение модуля
#
# определение модуля. Python позволяет поместить классы, функции, данные
# а также скрипты в отдельный файл и использовать их в других программах
# Модулем в пайтон называется любой файл с программой
#
# зачем нужны?
# - повторное использование кода
# один раз написали код и где надо подключаем его
# - управление пространством имён
# можем использовать одинаковые имена в разных модулях
# - деление большого проекта на мелкие части
# разбиваем на части и работаем с каждой частью отдельно
#
# Три основных разновидности модулей
# 1) встроенные (math, random, ...)
# например биюлиотеки для математики math и работа со случайными числами random
# 2) сторонние модули (django, PyQt5,..)
# для работы с ними их сначала надо скачать и усановить
# 3) наши собственные (любой .py файл)
#
# Варианты подключения
# - подключить модуль целиком import math с помощью команды импорт
# - псевдоним для модуля import math as mt
# - импорт всего содержания from math import * (не рекомендуется)
# мы импортируем все сущности которые есть в модуле math
# - импорт конкретных функций, классов ... from math import sin, cos
#
# будем работать в дальнейшем со всеми типами модулей
# на примере встроенных модулей (math, random, ...):
import math
# модуль можно также назвать библиотекой. После импорта нам доступны
# функции, данные которые есть в модуле
print(math.pi)
# например число пи, которое содержится в модуле: 3.141592653589793
# также можем использовать какие любо функции из модуля
# например функцию синус. угол задаётся в радианах
print(math.sin(67))
# импортирование с псевдонимом на примере рандом.
import random as rd
# псевдоним должен быть говорящим, используют редко, проще вызывать модуль целиком
# используем модуль рандом по псевдониму
print(rd.randint(1, 11111))
# самая простая функция модуля рандом - randint - которая возвращает случайное число
# от 1 до 11111. от начального параметра и до конечного.
#
# рассмотрим вариант который не рекомендуется использовать:
# импорт всего содержимого модуля
from math import *
# мы используем все объекты, функции, классы, данные, скрипты, которые есть в этом модуле
# теперь можем вызвать число пи без указания модуля, потому что импортировали его целиком
# и имя модуля теперь не требуется
print(pi)
print(sin(45))
# когда мы импортируем все объекты, мы не знаем с какими именами у нас есть эти объекты
# поэтому могут быть накладки по именам
#
# импортировать отдельные функции, классы, данные
from random import randint, randrange
# from random import и через запятую перечисляем всё что нужно, например 2 функции randint, randrange
# объектов, функций, классов может быть сколько угодно. указываем их через запятую
# после этого можем их использовать без указания имени модуля
print(randint(3, 98))
# таким образом мы контролируем имена, которые есть в этом модуле.
# и ограждаем себя от проблемы пересечения имён

#______________________________
# УРОК 2 - СТАНДАРНТЫЕ МОДУЛИ math, random
#______________________________
# - библиотека math
# - библиотека random
# - примеры применения
#
# библиотека math содержит математические функции, работает с числами
# основные функции:
# factorial - факториал числа
# exp - экспонента
# log, log2, log10 - различные логорифмы
# sqrt - квадратный корень
# sin, cos, asin, asoc - функции для работы с углами
# и многие другие
# с остальными функциями можно познакомиться в официальных документах пайтон
# либо в интернете
# можно решать некоторые математические задачи с помощью math
# - длина окружности с определёным радиусом
# для того чтобы пользоваться модулем, его необходимо импортировать
import math
r = 100
print(2*math.pi*r)
# - площадь окуржности с определёным радиусом
print(math.pi*(r**2))
print((math.pow(r,2))*math.pi)
# также можно воспользоваться библиотекой math, функцией pow
# для вызова math.pow(r,2) -  r будем возводить во вторую степень
# - по координатам 2 ух точек определить растояние между ними
# х1, y1 - координаты первой точки
# x2, y2 - координаты второй точки
x1 = 16
y1 = 3
x2 = 45
y2 = 56
l = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(l)
# для нахождения корня модуль math.sqrt(), функция sqrt()
# вычисляем по теореме пифагора расстояние
# - найти факториал числа 9
print(math.factorial(9))
# берём из библиотеки math стандартную функцию factorial
# передаём параметром число для которого нужно найти факториал
#
# Использование random
# генерация случайных чисел, букв, элементов последовательности
# основные функции:
# randint (a, b) целое случайное число от a до b
# choice - случайный элемент последовательности
# shuffle - перемешивает последовательность случайным образом
# random - случайное число от 0 до 1
# sample - список длиной k из последовательности
# и многие другие
# примеры задач
# - загадать случайное число от 0 до 100
import random
print(random.randint(1, 100))

from random import randint, choice, sample
print(randint(1,10000))

# - выбрать победителя лотереи из списка players
players = ['Max', 'Leo', 'Kate', 'Igor', 'Peter']
print(random.choice(players))
print(choice(players))
# выбираем случайный элемент из списка
#  - выбрать трёх победителей лотереи из списка
print(sample(players, 3))
# первый параметр последовательность из которой выбираем, второй параметр сколько выбираем
# - перемешать карты в списке cards
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A' ]
print(cards)
random.shuffle(cards)
print(cards)
# shuffle не возвращает значение, просто перемешивает

#______________________________
# УРОК 3 - СОЗДАНИЕ СОБСТВЕННОГО МОДУЛЯ
#______________________________
# - создание своего модуля
# - импорт данных из своего модуля
# - импорт скриптов
# - if__name__=='__main__'
#
# Модули в пайтон - это просто файлы с расширением .py
# создаём в специальной папке файл .py
# файл находится в папке, мы к нему можем обращаться
# импорт данных из своих модулей осуществляется также как и из стандартных
# при импорте необходимо учитывать путь до нашего модуля
# import firstmodele - если модуль в нашей корневой папке с проектом
# import folder.secondmodule - если модуль в подпапке
#
# создал папку my_moduls. Там буду хронить свои модули.
# создал файл firstmodule. в нём переменная и функция
# если в той же папке что и index - import moda
# таким образом нам будут доступны и переменная и функция: print(moda.foo) , moda.bar
# импортируем firstmodule
import my_moduls.firstmodule
# либо прссто импортировать переменную или функцию
from my_moduls.firstmodule import foo, bar
print(foo)
bar()
# импорты работают как и в стандартных модулях
#
# Модули со  скриптами
# в которых уже написан какой то код, который должен выполниться
# при любом варианте импорта такого модуля, скрипты в нём будут выполняться
# если не указано никаких условий (if__name__=='__main__')
# это обязательно надо учитывать при импорте данных модулей
import my_moduls.modc
# если попробывать импортировать например только переменную,
from my_moduls.modc import foo
# при любом варианте импорта не важно всего модуля или только данных из него
# будет выполняться скрипт или код, который написан в модуле
#
# конструкция if__name__=='__main__'
# ограничивает выполнение скриптов
# если мы пользуемся if__name__=='__main__'
# при импорте код скрипта не будет выполняться
# но он будет выполняться при запуске самого модуля
# ограничение прописывается в самом модуле
# foo = 'foo C'
#
# if __name__ == '__main__':
#     print('Я выполняюсь всегда')
#     print('Когда меня импортируют')
#     print('Ну или почти всегда')
#
# Если запускаем модуль самостоятельно - все принты работают
# если будем импортировать данные или сам модуль в другое место,
# код не будет выполняться
#
# Как это работает?
# print(name)
# if __name__ == '__main__':
#     print('Я выполняюсь всегда')
#     print('Когда меня импортируют')
#     print('Ну или почти всегда')
#
# Если мы сделаем print(name)
# это внутренняя переменная нашего модуля которая означает его название
# если запустить модуль из самого себя увидим, что print(name) выведит __main__
# __name__ == '__main__'
# поэтому условие выполняется и мы заходим в стандартные условные операторы
# и выполняем код принтов
#
# Но если мы вызовим модуль откуда нибудь с другого места
# переменная name? когда сделали принт стала равняться modec
# т.к когда вызываем модуль через импорт, то имя равняется имени модуля
# если код модуля запускаем в самом модуле переменная name = main
# за счёт этого выполняется условие __name__ == '__main__'
# скрипты работают в одном случае и не работают в другом

#______________________________
# УРОК 4 - ПАКЕТЫ
#______________________________
# - Определение пакета
# - создание пакета
# - назначение пакета
# - импорт из пакета
#
# Пакет - каталог, включающий в себя другие пакеты и модули
# пакет содержит внутри себя файл __init__.py
# пакеты можно создавать как из пайчарма, так и в ручную.
# ПКМ в ЛП по директории --> create new python package --> вводим название пакета
# создали новый покет он появился в ЛП mypack
# пайчарм создал папку, и врней пустой файл __init__.py
# пакет обязательно должен содержать этот файл
#
# основное назначение пакетов - формирование пространства имён.
# работа с модулями с указанием уровня вложенности
# пакет1.пакет2.модуль
# уровни вложенности отделяются точкой
#
# варианты импортов
# import.модуль - внутри пакета из одного модуля в другой
# import пакет.модуль - стандартно, если мы находимся в другом пакете
# import, from, as ... работают любые варианты импорта. импорт всего пакета, одного модуля,
# либо функции, классов, объектов из этого модуля
# вложенность пакетов может быть любой (пакет в пакете)
#
# пример. программа для медицинского учереждения и возможную её структуру
# Сама программа в файле main.py в директории example и из нё она будет запускаться
# Создаём пакет , который будет отвечать за всё медицинское учреждение
# назовём его hospital
# после зоздания пакета у нас есть папка, а в ней пустой __init__ файл
# внутри пакетов можно создавать новые пакеты для разграничения пространства имён и структуры
# например создадим в пакете hospital пакет doctors
# после этого в пакете doctors у нас есть опять пустой питон файл __init__
# здесь мы сделаем 2 модуля: первый модуль - хирурги
# создаём в пакете doctors питон файл surgeons
# это уже модуль с расширением .py а не папка.
# второ модуль - меедсёстры nususures
# создали в пакете doctors питон файл.
# у нас следующая структура:
# пакет hospital -> внутри пакет doctors ->
# внутри пакета doctors 2 модуля: surgeons.py и nususures.py
# и один файл __init__.py
# в пакете hospital создадим ещё один пакет, он будет называться clients
# и в этом пакете создадим файл index.py
# после того как структура пакетов готова, в каждый модуль добавим по функции:
def get_index():
    print('Все пациенты')
# в index.py
def get_nurses():
    print('медсестры из пакета doctors')
# в nususures.py
def get_surgions():
    print('Хирурги из пакета doctors')
# surgeons.py
# на примере этих функций потренируемся делать импорты в такой сложной структуре
# если например нам надо импортировать модуль surgeons.py в функцию def get_nurses
# то в файле surgeons.py
# вызываем surgeons.py
# таким образом из текущего пакета doctors импортируем фу-ю get_nurses
# вызывем в surgeons.py, чтобы посмотреть результат
def get_surgions():
    get_nurses()
    print('Хирурги из пакета doctors')
# в пакете hospital создал файл h.py
# в этом файле попробуем импортировать туда функции . например get_surgions()
# вложенность будет другой: from .doctors.surgions import get_surgions
# после этого из модуля h импортировать данные в main.py
# в main.py вызываем: from hospital.h import get_main
# таким образом с помощью точки, мы можем разграничивать пространства имён
# и делать различные импорты
# импорт из main.py / нам нужно модуль из doctors
# from hospital.doctors.nususores

#______________________________
# УРОК 5. MOДУЛИ os, sys
#______________________________
# - модуль os
# - модуль sys
# - sys.path
# - Практическое применение
#
# Модуль os
# содержит функции для работы с операционной системой
# не зависит от конкретной операционной системы
# что позволяет делать программы переносимыми
#
# основные функции и переменные os:
# name - имя операционной системы
# chdir - смена текущей директори
# getxwd() - текущая рабочая директория
# mkdir() - создание директории (папки)
# os.path - модуль для работы с путями
# и многие другие можно посмотреть в интернете или официальной документации
#
# для того чтобы использовать модуль, его надо изначально импортировать
import os
# имя операционной системы
print(os.name)
# текущая рабочая директория
print(os.getcwd())
# создаём новый путь
new_path = os.path.join(os.getcwd(), 'new_f')
# данный путь будет универсальный для каждой ос
# первый параметр - наш текущий путь: os.getcwd()
# второй параметр 'new_f' - папка которую мы будем создавать
# создаём папку по новому пути
#     os.mkdir(new_path)
# после того как создали новый путь, можем создать папку с помощью
# функции mkdir по этому новому пути
# В ЛП видим что после запуска кода создалась папка new_f.
# пустая папка в корневом каталоге с программой, которая запусилась и создала папку
# print(os.name) возвращает нам nt - у нас windows 10
# print(os.getcwd()) возвращает папку с нашим проектом
# C:\Users\777\Desktop\практика\python\educationCourseAll.py
# далее мы сделали новый путь и создали директорию
# папка появилась в новом проекте
#
# модуль sys
# обеспечивает взаимодействие с интерпритатором python
#
# функции и переменные sys:
# executable - путь к интерпритатору python
# exit() - выход из python
# platform - информация об ОС
# path - список путей поиска модулей
# argv - список аргументов командной строки
# и многие другие
import sys
# Импортируем модуль.
# путь до интерпритатора
print(sys.executable)
# информация о платформе
print(sys.platform)
# выход из пайтон
# sys.exit()
#
# sys.path - один из основных модулей
# ОЧЕНЬ ВАЖНАЯ переменная
# она хронит пути, по которым пайтон ищет подключаемые модули
# она имеет изменяемый тип данных list
# таким образом мы можем изменять эту переменную
#
# мы ожем импортировать  import math
# но не можем импортировать наш модуль с диска с
# import module
# КАК ПИТОН НАХОДИТ МОДУЛИ:
# import sys
# print(sys.path)
# print(type(sys.path))
#
# Как пайтон узнаёт, что у него есть модуль math и есть например наш модуль?
# для этого используется переменная sys.path
# если мы импортируем модуль sys и возьмём переменную sys.path
# то мы получим список папок или путей по которым пайтон ищет модули
print(sys.path)
# ['C:\\Users\\777\\Desktop\\практика\\python\\educationCourseAll.py', 'C:\\Users\\777\\Desktop\\практика\\python\\educationCourseAll.py',...
# эта переменная является тип list
# т.е списком
for p in sys.path:
    print (p)
# запускаем и видим все наши пути
# ['C:\\Users\\777\\Desktop\\практика\\python\\educationCourseAll.py', 'C:\\Users\\777\\Desktop\\практика\\python\\educationCourseAll.py', 'C:\\Users\\777\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 'C:\\Users\\777\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 'C:\\Users\\777\\AppData\\Local\\Programs\\Python\\Python38\\lib', 'C:\\Users\\777\\AppData\\Local\\Programs\\Python\\Python38', 'C:\\Users\\777\\Desktop\\практика\\python\\educationCourseAll.py\\venv', 'C:\\Users\\777\\Desktop\\практика\\python\\educationCourseAll.py\\venv\\lib\\site-packages']
# C:\Users\777\Desktop\практика\python\educationCourseAll.py
# C:\Users\777\Desktop\практика\python\educationCourseAll.py
# C:\Users\777\AppData\Local\Programs\Python\Python38\python38.zip
# C:\Users\777\AppData\Local\Programs\Python\Python38\DLLs
# C:\Users\777\AppData\Local\Programs\Python\Python38\lib
# C:\Users\777\AppData\Local\Programs\Python\Python38
# C:\Users\777\Desktop\практика\python\educationCourseAll.py\venv
# C:\Users\777\Desktop\практика\python\educationCourseAll.py\venv\lib\site-packages
# первые 2 папки это наш текущий проект, т.е папка с нашим кодои
# C:\Users\777\Desktop\практика\python\educationCourseAll.py
# C:\Users\777\Desktop\практика\python\educationCourseAll.py
# как раз отсюда мы и можем импортировать наши модули
# далее видим архив и некоторые библиотеки
# C:\Users\777\AppData\Local\Programs\Python\Python38\python38.zip
# C:\Users\777\AppData\Local\Programs\Python\Python38\DLLs
# C:\Users\777\AppData\Local\Programs\Python\Python38\lib
# папка с интерпритатором пайтон
# C:\Users\777\AppData\Local\Programs\Python\Python38
# далее папки со сторонними библиотеками
# C:\Users\777\Desktop\практика\python\educationCourseAll.py\venv
# C:\Users\777\Desktop\практика\python\educationCourseAll.py\venv\lib\site-packages
#
# посмотрим ка кподключить свой модуль
# из какого то другого места которого нету в этих путях
# предположим на диске d  есть некоторый модуль My_d_module
# т.к sys.path - это список
# sys.path.appened('D:')
# в неё можем с помощью appened добавить новый путь
# и сказать пайтону, чтобы по этому пути он тоже искал модули.
# все модули, которые имеются на диске D можно будет импортировать
# import my_d_module
# Пример для тренировки:
#
# в папке с модулем создать 5 подпапок,
# названия которых состоят из платформы
# на которой запущен интерпритатор
# и порядкового номера, начиная с 1: win32_1, win32_2
#
# Импортируем нужные нам модули:
# import sys, os
# name = sys.platform
# платформа на которой запущен наш интерпритатор пайтон
# после этого будем создавать папки. нам нужно их сделать 5 штук
# for i in range(1, 6):
#     new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
# собераем из двух частей: путь до нашего модуля os.getcwd()
# и вторая часть состоит из названия платформы подчёркивания и порядкового номера
# '{}_{}'.format(name, i)
# после того как у нас есть путь можем создавать папки:
# os.mkdir(new_path)

#______________________________
# УРОК 6. ЗАПУСК СКРИПТОВ С ПАРАМЕТРМИ
#______________________________
# - sys.argv
# - передача параметров в скрипт
# - практическое применение
#
# sys.argv
# список аргументов командной строки при запуске скрипта python
# в нём уже есть первый аргумент это
# sys.argv[0] - путь до скрипта
# остальные параметры передаются при вызове скрипта через пробел.
# нам нужно вызвать скрипт и через пробел записать различные значения.
# python my_script.py par1 par2 par3
# мы будем запускать наши скрипты с помощью командной строки
print('УРОК 6')
import sys
print(sys.argv[0])
# для того чтобы открыть командную строку прямо в пайчарме
# можем выбрать: ВП -> View -> Tool windows -> Terminal (alt + f12)
# внизу будет открыта командная строка с которой мы сможем работать как
# с обычной командной строкой
# теперь чтобы запустить из неё скрипт pr1helloworld.py
# который лежит в текущей папке
# нам достаточно написать Python и название скрипта pr1helloworld.py
# в командной строке
# в самом скрипте записано всего пара строчек import sys и print(sys.argv[0])
# если вызвать скрипт без параметров в терминале:
# мы получим название скрипта выведится
# pr1helloworld.py
# давайте вызовим эот скрипт теперь из пайчарма
# при этом получим другой результат :
# C:/Users/777/Desktop/практика/python/educationCourseAll.py/pr1helloworld.py
# это полный путь до нащего скрипта
# результаты отличаются.
# сверху видно как пайчарм запускает скрипт:
# C:\Users\777\Desktop\практика\python\educationCourseAll.py\venv\Scripts\python.exe C:/Users/777/Desktop/практика/python/educationCourseAll.py/pr1helloworld.py
# он вызывает его по полному пути.
# если же мы пользуемся терминалом
# то мы вызываем скрипт по относительному пути
# и получаем просто имя скрипта pr1helloworld.py
# таким образом sys.argv[0] - это первая часть, которая идёт за словом пайтон
# мы можем получить её внутри нашего скрипта.
# рассмотрим расширенный пример
# создали скрипт param.py
import sys

for arg in sys.argv:
    print(arg)
# после этого в цикле по  sys.argv мы просто печатаем элементы списка
# for arg in sys.argv:
#  print(arg)
# этот скрипт мы уже будем вызывать с параметрами
# в терминале вводим
# python param.py
# и добавляем через пробел какие то значения
# python param.py 123 999 dsdsd 340 3.14
# это могут быть строки или числа или даже числа с плавающей точкой
# выведим их на экран в терминале
# то мы как раз и получим список наших параметров в цикле
# проверим какого вида у нас являются аргументы
import sys

for arg in sys.argv:
    print(arg)
    print(type(arg))
# все пераметры передаются как строка. Не зависимо от того число там
# или строчка или плавающая точка
# в виде строки мы можем записать любой параметр
# и после этого привести к другому типу, если это нам нужно
#
# Практический пример
# В зависимости от параметра вызывать различные функции скрипта
# параметр ping - > функция выводит pong
# 2 параметра name и имя человека <Имя> - > функция приветствия пользователя
# параметр list показать содержтимое текущей директории
# для написания скрипта потребуются модули sys os
# """
# параметр ping - > функция выводит pong
# 2 параметра name и имя человека <Имя> - > функция приветствия пользователя
# параметр list показать содержтимое текущей директории
# """
# СКРИПТ - example.py создаю
#
# для написания скрипта потребуются модули sys os. Импортируем их
import sys, os

def ping():
    print('PonG')
# первая функция пинг будет выводить на экран слово Понг
# делаем вызов убедимся что функция работает
ping()
# функция приветствия пользователя
def hello(name):
# у функции будет один параметр name
    print('Приветствую ', name)
# третья функция получает содержимое текущей директории
def get_info():
    print(os.listdir())
# чтобы получить содержимое текущей директории
# мы вызываем из модуля os функцию listdir()
# если путь пустой, как раз будет содержимое теущей директории
# теперь перейдём к работе с параметрами
# первый параметр arv[0] это название нашего скрипта
# для начала нам понадобится второй параметр comand = sys.argv[1]

import sys, os

def ping():
    print('PonG')

def hello(name):
    print('Приветствую ', name)

def get_info():
    print(os.listdir())

comand = sys.argv[1]
# этот параметр будет отвечать за нашу команду
# после того ка кполучим этот параметр будем писать логику
# if - elif - else
if comand == 'ping':
    ping()
elif comand == 'list':
    get_info()
elif comand == 'name':
    name = sys.argv[2]
# здесь пользователь передаст нам сразу 2 параметра
# поэтому нам нужно получить переменную name из sys.argv[2]
# это будет следующий параметр его индекс будет 2
# после того как мы получим имя мы уже можем пользоваться
# функцией hallo
    hello(name)
# остаётся проверить как работает наш скрипт
# откроем терминал  ВП -> View -> Tool windows -> Terminal (alt + f12)
# очистим с помощью команды cls
# и будем вызывать в терминале наш скрипт с различными параметрами
# python example.py ping
# в результате получили PonG
# python example.py list
# получили список
# третий вариант
# когда нам надо передать 2 параметра
# вызываем наш скрипт - первый параметр mane.
# и второй параметр какое то имя
# python example.py name Yyrgen
# таким образом видно что теперь с помощью параметров
# мы управляем логикой работы нашего скрипта
# если скрипт вызвать без параметров мы получим ошибку
# при получении аргумента первого comand = sys.argv[1]
# потому что его нет. в списке всего их 2
# это можно решить с помощью определённых условий
# if - else, но амый лучший вариант с помощью обработки исключений
