# Практическое задание
# Решить с помощью генераторов списка.

# 1: Даны два списка фруктов.
# Получить список фруктов,
# присутствующих в обоих исходных списках.
#     Примечание: Списки фруктов создайте вручную в начале файла.

fruits1 = ['яблоки','груши','папайя','маракуя','драгонфрукт','кокос','банан',]
fruits2 = ['мандарин','груши','вишня','маракуя','драгонфрукт','фейхуа','банан',]
# классический способ с помощью for
result = []
# создаём переменную для результата
for fruit in fruits1:
# перебираем первый список. для элемента из списка 1
    if fruit in fruits2:
# если элемент есть в списке 2, добавляем его в результат
        result.append(fruit)
print(result)

# решение с помощью генератора
result = [fruit for fruit in fruits1 if fruit in fruits2]
# записываем фрукт - fruit,
# который у нас идёт в цикле for fruit in fruits1
# а далее пишем условие:
# если этот элемент есть во втором списке
# if fruit in fruits2
print(result)


# 2: Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# Элемент кратен 3,
# Элемент положительный,
# Элемент не кратен 4.
# Примечание: Список с целыми числами создайте вручную в начале файла.
# Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.

numbers = [1, 2, 3, -4, 5, 6, -7, -8, 9, 10, -11, 12, -13, 14, 15, -16, 17, -18, 19, 20, 21, -22]
# создаём генератор списка, записывать мы будем число number
result = [number for number in numbers if number > 0 and number %3 ==0 and number %4 != 0]
# в цикле for перебираем наш список for number in numbers
# далее записываем условие:
# первое условие элемент положительный number > 0
# второе условие элемент кратен 3^ number %3 ==0
# третье условие элемент не кратен 4: number %4 != 0
print(result)

# 3. Напишите функцию которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней чисел
# (если число положительное) и самих чисел (если число отрицательное)
# и возвращает результат (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться.
# Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]
# Примечание: Список с целыми числами создайте вручную в начале файла.
# Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.

import math
# для начала рассмотрим ситуацию, когда входной список может измениться
old_list = [1, 2, 3, -4, 5, 6, -7, -8, 9, 10, -11, 12, -13, 14, 15, -16, 17, -18, 19, 20, 21, -22]
# создаём функцию. в неё попадает входной список input_list
def new_sqrt_list(input_list):
    for i in range(len(input_list)):
# перебираем список по индексам
        number = input_list[i]
# получаем число. Если число больше 0
        if number > 0:
# по индексу записываем корень из этого числа
            input_list[i] = math.sqrt(number)

        # else:
        #     del input_list[i]
    return input_list
# и возвращаем результат
result = new_sqrt_list(old_list)
# вызываем функцию, передаём old_list
print(result)
# печатаем результат
print(old_list)
# печатаем old_list
# запускаем и видим результат равняется old_list
# и old_list изменился

# Помним, чтобы список не менялся, нам нужно работать с его копией
old_list = [1, 2, 3, -4, 5, 6, -7, -8, 9, 10, -11, 12, -13, 14, 15, -16, 17, -18, 19, 20, 21, -22]

def new_sqrt_list(input_list):
# Создаём копию списка
    input_list = input_list.copy()
    for i in range(len(input_list)):
        number = input_list[i]
        if number > 0:
            input_list[i] = math.sqrt(number)

        # else:
        #     del input_list[i]
# если захотим удалить элемент,
# мы этого сделать не сможем.
# т.к циклом идём по немуже
    return input_list
result = new_sqrt_list(old_list)
print(result)
print(old_list)
# пример надуман и плох, т.к имеем дело с индексами
# рассмотрим более удобный способ. воспользуемся генератором
old_list = [1, 2, 3, -4, 5, 6, -7, -8, 9, 10, -11, 12, -13, 14, 15, -16, 17, -18, 19, 20, 21, -22]
def new_sqrt_list(input_list):
# создаём переменную которая будет равняться генератору списка
    result = [math.sqrt(number) for number in input_list if number > 0]
# будем записывать в список math.sqrt(number)
# числа будем брать из списка: for number in input_list
# нам необходимо проверять число больше 0: if number > 0
    return result
result = new_sqrt_list(old_list)
print(result)
print(old_list)
# в этом примере видно, что в этом списке нет отрицательных чисел...
# как изменить генератор, чтобы эти числа остались?
# с помощью комбинации генератора и тернального оператора
def new_sqrt_list(input_list):
    result = [math.sqrt(number) if number > 0 else number for number in input_list ]
    return result
result = new_sqrt_list(old_list)
print(result)
print(old_list)
# мы будем брать корень из числа:  math.sqrt(number)
# если у нас число больше 0: if number > 0
# а иначе записываем в список само число: else number
# комбинации тернарного оператора и генератора
# дают нам новые возможности


# 4. Написать функцию которая принимает на вход число от 1 до 100.
# Если число равно 13, функция поднимает исключительную ситуации ValueError
# иначе возвращает введенное число, возведенное в квадрат.
# Далее написать скрипт.
# Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат,
# который вернула функция. Обработать возможность возникновения исключительной ситуации,
# которая поднимается внутри функции

def unlucky_number(number):
    if number == 13:
        raise ValueError('Вы ввели запретное число!')
# исключение с помощью команды raise ValueError (ошибочное значение)
# в скобках можно написать пояснение ('Вы ввели запретное число!')
    else:
# если число не ровно 13 , то мы возвращаем сисло в квадрате
        return number ** 2

number = int(input('введите число от 1 до 100: '))
# мы вызываем функцию и записываем результат в переменную result
try:
    result = unlucky_number(number)
# Но в этой строке у нас возможна исключительная ситуация,
# поэтому всё мы помещаем в блок try - except и возможно else
except ValueError:
    print('!введено запретное число!')
# если у нас возникает ошибка ValueError:
# мы будем её обрабатывать.
# например просто пишем :
# print('!введено запретное число!')
else:
# ecли всё хорошо выполняем этот код
# - печатаем результат
    print(result)
# функция сгенерировала исключительную ситуацию,
# а мы эту ситуацию обработали
# Если убрать try - except
# то ошибка будет сгенерирована
# и программа у нас остановитя.