# Создать модуль music_deserialize.py
# В этом модуле открыть файлы group.json и group.pickle
# прочитать из них информацию
# Получить объект словарь из предыдущего задания

# мы используем 2 файла, чтобы смодулировать ситуацию,
# когда например один разработчик записывает данные в файл
# и передаёт другому разработчикутакже данные
# можно например вместо вывода в терминал передовать по сети.
# Импортируем модули json и pickle
import json
import pickle
# далее открываем файл
with open('group.json', 'r', encoding='utf-8') as jsonfile:
    result = json.load(jsonfile)
# открываем файл 'group.json'
# на чтение 'r'
# указываем кодироку encoding='utf-8'
# ту же самую кодировку в которой мы записывали файл
# после того как файл открыт ,
# создаём переменную в которую мы будем читать результат
# result =  используем метод json и метод load
# и передаём в него параметр jsonfile название файла

# после того как мы получили результат проверим,
# что у нас он совпадает с тем, что был изначально
print(result) # <class 'dict'>
print(type(result))

# теперь используем
# модуль pickle похоже на метод json
# но мы работаем с байтами
with open('group.pickle', 'rb') as picklefile:
    result = pickle.load(picklefile)
print(result) # <class 'dict'>
print(type(result))
# открываем файл 'group.pickle'
# на чтение байт 'rb'
# Объявляем переменную result
# и используем метод .load