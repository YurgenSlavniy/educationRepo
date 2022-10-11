# -*- coding: utf-8 -*-
"""2. Работа с Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ECunzNF2-XX69-Q4ovKjwT84icX-7-sw

# Работа с Pandas

`Pandas` - это библиотека, которая позволяет удобно работать с таблицами. Как и в `numpy`, некоторые компоненты библиотеки `pandas` написаны на языке `C`, что ощутимо ускоряет работу с таблицами, содержащими большие объёмы данных.

## Series

`Series` - это одна из структур данных библиотеки `pandas`. Она представляет собой что-то вроде словаря, однако, является упорядоченной.

Создадим какой-нибудь список, а затем получим на его основе объект `Series`:
"""

import pandas as pd

a = [1, 3, 5, 7, 2]

b = pd.Series(a)

print(b)

"""В результате такой операции получается объект `Series`, содержащий элементы из списка `a`. Здесь справа располагаются элементы из `a`, а слева - их индексы. Поскольку индексы для этих элементов мы явно не указали, используются стандартные.

Индексы можно также указать явно, для этого нужно подать в качестве аргумента `index` список из индексов. Данный список должен быть той же длины, что и список `a`.

В качестве индексов можно использовать что угодно: числа, строки и пр. Например, проиндексируем наш список `a` объектами типа `datetime.date`:
"""

from datetime import date

index = [date(2019, 4, i) for i in a]

c = pd.Series(a, index=index)

print(c)

"""Индексы можно задать сразу, а можно и изменить позже:"""

b.index = ["a", "b", "c", "d", "e"]

print(b)

"""Рассмотрим индексы объекта `Series` поподробнее. Их можно получить с помощью атрибута `c.index`:"""

c.index

"""Мы видим, что в качестве индексов здесь используются объекты типа `object`. Этот тип объектов используется также в `numpy`. Он используется для объектов, для которых заранее не известно, сколько памяти они требуют (в отличие от, например, `numpy.int64`, для которого заранее известно, сколько памяти под него нужно).

Тип `object` в `numpy` и `pandas` приписывается, например, строкам, а также объектам из других библиотек. В массивы данных, состоящие из объектов типа `object` (например, в наш массив `c.index`), помещаются не сами объекты, а лишь указатели на них, а сами объекты хранятся в специально выделенном месте. Мы всё ещё можем использовать для этих объектов методы, присущие им (например, для каждого индекса из массива `c.index` мы можем посмотреть его год, месяц или день):
"""

print(c.index[0].month)

"""Однако, это возможно делать лишь с отдельными элементами из индекса.

В `pandas`, как и в `numpy`, возможно выполнять различные операции с массивами целиком, но лишь когда эти массивы содержат объекты типов, поддерживаемых `numpy` и `pandas` (вроде `numpy.int32` или `numpy.float64`). 

Для работы с датой и временем в `numpy` также есть специальный тип: `numpy.datetime64`. Приведём элементы нашего индекса к этому типу и посмотрим, что это нам позволит делать. Это можно сделать с помощью функции `pd.to_datetime`, которая получает на вход массив и возвращает новый массив, элементы которого приведены к типу `numpy.datetime64`:
"""

c.index = pd.to_datetime(c.index)

"""Теперь мы можем, например, посмотреть атрибут `day` у всех элементов индекса одновременно:"""

print(c.index.day)

"""Индексы в `Series` не обязаны быть уникальными:"""

d = pd.Series(a, index=[0, 1, 0, 1, 0])

print(d)

"""Тип данных в `Series` можно также задать явно. Можно это сделать либо сразу же:"""

import numpy as np

e = pd.Series(a, dtype=np.float32)

print(e)

"""либо позже с помощью метода `.astype`:"""

e = pd.Series(a)

e = e.astype(np.float32)

print(e)

"""Создать массив `Series` можно не только из списка, но и из словаря. В таком случае, ключи этого словаря становятся индексами, а соответствующие значения словаря - значениями массива:"""

dict_ = {
    "1st": "a",
    "2nd": "b",
    "3rd": "c",
}

f = pd.Series(dict_)

print(f)

"""Значения массива `Series` можно получить с помощью атрибута `.values`. Значения массива представлены как `numpy.ndarray`."""

f.values

"""### Выбор данных из массива Series

Для получения значений массива `Series` по индексу используется тот же синтаксис, что и с массивами в `numpy`:

* Чтобы получить значение или значения по одному индексу, достаточно поставить этот индекс в квадратные скобки после массива: `f["1st"]`.
* Если необходимо получить значения по нескольким индексам, в квадратные скобки массива подаётся список индексов: `f[["1st", "3rd"]]`.

У массивов `Series` также имеются методы `.head` и `.tail`, позволяющие посмотреть, соответственно, первые несколько или последние несколько значений массива. В каждом из этих методов можно указать, сколько именно значений нужно вернуть. По умолчанию возвращается 5 значений.
"""

e.tail(3)

"""Для массивов `Series`, также как и для `numpy`-массивов, доступна булева индексация. С помощью неё можно получать значения массива, которые удовлетворяют некоторому условию:"""

e[e > 2]

"""Как и ранее, условия можно комбинировать, используя логические операторы "и" (обозначается символом $\&$), "или" (символ $\mid$) и оператор отрицания "не" (символ $\sim$). При этом каждое условие необходимо поставить в круглые скобки:"""

e[(e > 2) | (e == 1)]

"""Изменять массив `Series` можно теми же способами, что и при работе с обычными словарями. Например, команда `e[2] = 4` заменит значение массива `e` с индексом 2 на 4.

Однако, в массивах `Series` мы можем менять несколько значений одновременно. Например, с помощью тех же самых условий:
"""

e[e > 2] = -1

print(e)

"""либо передав в массив какие-то конкретные индексы:"""

e[[1, 3]] = 10

print(e)

"""### Добавление и удаление данных в Series

С помощью метода `.append` мы можем добавлять к одному массиву `Series` другой:
"""

g = e.append(f)

print(g)

"""С помощью метода `.drop` мы можем удалять из массива элементы с определёнными индексами. Эти индексы мы и подаём в метод в виде списка:"""

h = g.drop([0, 4, "2nd"])

print(h)

"""Обратите внимание, что эти методы, в отличие от аналогичных методов из стандартных библиотек питона, не изменяют исходный массив, но возвращают новый.

### Запись и чтение массивов Series из файла


Для записи массивов `Series` в файлы используется формат файлов под названием `pickle`. Этот формат позволяет полностью сохранять питоновские объекты, а затем загружать их в неизменном виде.

Для записи массива `Series` в файл используется метод `.to_pickle`, а для чтения - функция `np.read_pickle`:
"""

h.to_pickle("h.pkl")

h = pd.read_pickle("h.pkl")

print(h)

"""## DataFrame

`DataFrame` - двумерная структура данных из библиотеки `pandas`, позволяющая удобно работать с таблицами.

Самый простой способ задать `DataFrame` - с помощью словаря, в котором каждый ключ отвечает за столбец, а соответствующее значение - это список из элементов данного столбца. Эти списки должны иметь одинаковую длину.
"""

a = {
    "col1": [1, 2, 4, 5, 6, 7, 8],
    "col2": ["a", "c", "e", "g", "z", "x", "y"]
}

b = pd.DataFrame(a)

b

"""С помощью атрибута `.shape` можно посмотреть форму массива `DataFrame`. Атрибут `.columns` содержит массив из столбцов, а `.index`, как и ранее, содержит массив индексов."""

print("Форма b: {}".format(b.shape))

print("Столбцы b: {}".format(b.columns))

print("Индексы b: {}".format(b.index))

"""Общую информацию о массиве можно запросить с помощью метода `.info`. Нам вернётся информация об индексах и столбцах данного массива, о том, какие типы данных хранятся в каждом из столбцов, а также информация о том, сколько памяти выделено под данный массив."""

b.info()

"""С помощью метода `.describe` можно получить некоторые статистические характеристики по столбцам с числовыми значениями: среднее значение, среднее квадратическое отклонение, максимум, минимум, квантили и пр."""

b.describe()

"""### Выбор данных из массива DataFrame

Для получения данных из массива `DataFrame` используется тот же синтаксис, что и для `Series`. Например, с помощью методов `.head` и `.tail` можно получить несколько первых или несколько последних строк таблицы.

Отдельный столбец можно получить, передав его название в квадратные скобки массива:
"""

b["col1"]

"""Каждый отдельный столбец массива `DataFrame` возвращается как массив типа `Series`.

Если мы хотим указать несколько столбцов, в квадратные скобки нужно подать список из столбцов. Тогда нам вернётся подтаблица исходной таблицы опять в формате `DataFrame`.

Получить данные из строк таблицы `DataFrame` можно получить с помощью атрибута `.loc`. Этот атрибут представляет собой что-то вроде двумерного массива. Конкретное значение (или несколько значений) этого массива можно получить, указав нужный индекс строки и название колонки:
"""

b.loc[2, "col1"]

"""Как и ранее, вместо каждого из ключей можно подать список ключей, чтобы вернуть несколько значений. Кроме того, второй аргумент можно не указывать, тогда будут возвращены значения из всех столбцов:"""

b.loc[[0, 2, 4]]

"""При использовании атрибута `.loc` мы должны указывать именно индекс нужной строки и название нужного столбца. Бывают ситуации, когда удобнее было бы получить значение по позиции (т.е., например, элемент из третьей строки и второго столбца). Для этого можно использовать атрибут `.iloc`:"""

b.iloc[2, 1]

"""Как и в `Series`, в массивах `DataFrame` есть возможность использовать булеву индексацию для указания строк. Причём, условия могут касаться любого столбца или набора столбцов. Как и ранее, условия можно комбинировать с помощью логических операторов.

Например, получим значения из второго столбца у всех строк, значение первого столбца для которых больше 3 или равно 1:
"""

b.loc[(b["col1"] > 3) | (b["col1"] == 1), "col2"]

"""В `pandas` есть также несколько методов, упрощающих булеву индексацию:

* `b["col1"].between(1, 3)` - все строки, для которых значение в первом столбце лежит между 11 и 13 (включая оба конца)
* `b["col2"].isin(["a", "z"])` - все строки, для которых значение второго столбца содержится в списке `["a", "z"]`

Их также можно использовать вместе с логическими операторами. Например, получим все строки из таблицы `b`, для которых значение первого столбца лежит между 3 и 6, а значение второго столбца не равно `"a"` или `"z"`:
"""

b[(b["col1"].between(3, 6)) & (~b["col2"].isin(["a", "z"]))]

"""Более короткий и удобный функционал для таких запросов реализован методом `.query`. В него подаётся строка, содержащая булевы условия на значения столбцов. При этом, переменную массива мы уже не пишем, а к столбцам обращаемся без кавычек. В остальном, допускается тот же синтаксис с использованием булевых операторов. 

Пример:
"""

b.query('(col1 < 6) & (col2 > "c")')

"""Как мы уже отмечали, выбирая один столбец из `DataFrame`, мы получаем массив `Series`. Если хочется получить столбец именно в виде `DataFrame`, можно запросить запросить его, подавая в квадратные скобки не название столбца, а список, содержащий только один этот столбец:"""

type(b["col1"])

type(b[["col1"]])

"""В любом случае, конвертировать `Series` в `DataFrame` можно и явно:"""

c = pd.Series([3, 1, 2])

d = pd.DataFrame(c)

d

"""Если требуется скопировать массив `Series` или `DataFrame`, это можно сделать с помощью метода `.copy`: `e = d.copy()`.

### Случайный выбор значений из DataFrame

Случайный выбор строк из массива `DataFrame` производится с помощью метода `.sample`. Вот несколько его важных параметров:

* `frac` - какую долю от общего числа строк нужно вернуть (число от 0 до 1)
* `n` - сколько строк нужно вернуть (число от 0 до числа строк в массиве)
* `replace` - индикатор того, производится ли выбор _с возвращением_, т.е. с возможным повторением строк в выборке, или _без возвращения_ (`True` или `False`)

Нельзя использовать параметры `frac` и `n` одновременно, нужно выбрать какой-то один.
"""

b.sample(frac=0.5, replace=True)

"""Если требуется просто перемешать всю выборку, это также можно выполнить с помощью метода `.sample`, передав в него параметр `frac=1`.

### Запись и чтение DataFrame из файлов

Для хранения таблиц широко распространён формат файлов с расширением `.csv`.

Сохранить массив в файл можно с помощью метода `.to_csv`. Вот несколько важных параметров этого метода:

* `sep` - символ, который нужно использовать для разделения значения столбцов между собой. По умолчанию это `","`, но можно также использовать `";"`, `"\t"` и др.
* `index` - булево значение, индикатор того, нужно ли в файл сохранить также столбец индексов.

"""

b.to_csv("test.csv", sep=";", index=False)

"""Прочитать массив из файла можно с помощью функции `pd.read_csv`. Здесь также можно указать разделитель столбцов в параметре `sep`."""

b = pd.read_csv("test.csv", sep=";")

b

"""У данных команд для сохранения и чтения таблиц есть множество других важных и полезных параметров, поэтому рекомендуется также изучить их документацию: [to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html), [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html).

В `pandas` также имеются аналогичные команды для сохранения и записи таблиц как `excel` и `pickle`.

## Работа с данными в Pandas

### Слияние данных

Рассмотрим следующий пример. Допустим, что мы работаем с небольшим отделом книжного магазина, в котором продаётся классическая литература на английском языке. Наша задача - систематизировать ассортимент отдела.

У нас есть таблица `authors`, содержащая данные об авторах: их идентификаторы (`author_id`) и имена (`author_name`):
"""

authors = pd.DataFrame({
    'author_id': [1, 2, 3],
    'author_name': ['Pushkin', 'Tolstoy', 'Dostoevsky'],
})

authors

"""Кроме того, у нас есть таблица `books`, содержащая информацию о книгах этих авторов. В этой таблице также есть колонка `author_id`, а также колонка `book_title`, содержащая название книги:"""

books = pd.DataFrame({
    'author_id': [2, 3, 3, 4],
    'book_title': ['War and Peace', 'The Idiot', 'Crime and Punishment',
                   'Fathers and Sons'],
})

books

"""Что делать, если мы, например, захотим сопоставить названия книг именам их авторов? Для этого используется функция `pd.merge`: в эту функцию помещаются те таблицы, которые мы хотим соединить, а также несколько других важных аргументов:

* `on` - параметр, отвечающий за то, какой столбец мы будем использовать для слияния,
* `how` - каким образом производить слияние.

Опишем подробнее, какие значения может принимать параметр `how`:

* `"inner"` - внутреннее слияние. В этом случае в слиянии участвуют только те строки, которые присутствуют в обоих таблицах,
* `"left"` - в слиянии участвуют все строки из левой таблицы,
* `"right"` - то же самое, но для правой таблицы,
* `"outer"` - внешнее слияние, соединяются все строки как из левой, так и из правой таблицы.
"""

pd.merge(authors, books, on='author_id', how='inner')

"""Если мы выбираем `"left"`, `"right"` или `"outer"`, может случиться так, что строку из одной таблицы будет невозможно соединить со второй. Например, мы видим, что в нашей таблице `books` нет произведений Пушкина (его `id` равен 1). В свою очередь, в таблице `books` есть книга, для которой `author_id` равен 4, хотя, в таблице `authors` нет записи с таким `author_id`. Рассмотрим внешнее слияние этих таблиц:"""

merged_df = pd.merge(authors, books, on='author_id', how='outer')

merged_df

"""Как мы видим, в получившейся таблице присутствуют пропущенные значения (`NaN`).

### Работа с пропущенными данными

Пропущенные значения в `Series` или `DataFrame` можно получить с помощью метода `.isnull`. Наоборот, все имеющиеся непустые значения можно получить с помощью метода `.notnull`:
"""

merged_df[merged_df["author_name"].isnull()]

merged_df[merged_df["author_name"].notnull()]

"""Заполнить пропущенные значения каким-то своим значением можно с помощью метода `.fillna()`:"""

merged_df["author_name"] = merged_df["author_name"].fillna("unknown")

merged_df

"""### Добавление столбцов в `DataFrame`.

Допустим, каждая из наших книг имеется в единственном экземпляре. Мы хотели бы создать в таблице `merged_df` столбец `quantity`, который бы содержал количество экземпляров каждой книги.

Создание нового столбца в таблице `DataFrame` происходит аналогично созданию нового значения в словаре `dict`. Достаточно просто объявить значение `merged_df["quantity"]`. Если подать в это значение какое-нибудь число или строку, то все значения в данном столбце приравняются к этому числу или строке. Также можно подать сюда список, тогда значения из этого списка поступят в соответствующие строки этого столбца. В этом случае длина списка обязана совпадать с числом строк таблицы.

Итак, выберем все строки с непустым значением поля `book_title`, и для них запишем в столбец `quantity` число 1. Это можно сделать с помощью атрибута `.loc`:
"""

merged_df.loc[merged_df["book_title"].notnull(), "quantity"] = 1

merged_df

"""Теперь заполним все пропуски в этом столбце числом 0:"""

merged_df["quantity"].fillna(0, inplace=True)

merged_df

"""Наконец, приведём значения в этом столбце к типу `int`. (Это сделать невозможно, если в столбце содержатся пропуски.)"""

merged_df["quantity"] = merged_df["quantity"].astype(int)

merged_df

"""В `DataFrame` можно использовать индексы по умолчанию, а можно и назначить свои. Например, в качестве индексов можно использовать какой-нибудь из столбцов:"""

merged_df.set_index("author_id", inplace=True)

merged_df

"""Если что, индексы всегда можно сбросить. Тогда текущие индексы становятся столбцом:"""

merged_df.reset_index(inplace=True)

merged_df

"""### Удаление данных

Для удаления данных из `DataFrame` используется метод `.drop`. В этот метод подаётся метка элемента, который необходимо удалить (индекс строки или название столбца), а также ось `axis`. При `axis=0` удаляется строка, при значении `axis=1` - столбец:
"""

merged_df["price"] = 500

merged_df

merged_df.drop("price", axis=1, inplace=True)

merged_df

"""Теперь удалим строку с индексом 1:"""

merged_df.drop(1, axis=0, inplace=True)

merged_df

"""### Сортировка данных

Вернём только что удалённую строку. Напомним, что для этого используется метод `.append`. Кстати, добавлять строки к `DataFrame` можно прямо в виде словарей `dict`:
"""

merged_df = merged_df.append(
    {
        "author_id": 2,
        "author_name": "Tolstoy",
        "book_title": "War and Peace",
        "quantity": 1,
    },
    ignore_index=True,
)

merged_df

"""Параметр `ignore_index=True` подаётся сюда, чтобы индексы соединяемых таблиц не учитывались. В результирующей таблице будут использованы стандартные последовательные индексы, начинающиеся с 0.

Отсортируем эту таблицу по столбцу `author_id`. Это делается с помощью метода `.sort_values`:
"""

merged_df.sort_values(by="author_id", inplace=True)

merged_df

"""Чтобы сбросить индексы, воспользуемся уже известным методом `.reset_index`. В нашем случае, стоит подать в него аргумент `drop=True`, который означает, что текущий столбец из индексов не нужно сохранять в таблице, а можно удалить."""

merged_df.reset_index(drop=True, inplace=True)

merged_df

"""### Соединение таблиц

Для соединения таблиц можно пользоваться функцией `pd.concat`. С этой функцией мы уже знакомились, когда изучали библиотеку `numpy`. Здесь эта функция работает аналогичным образом: соединяет таблицы либо вертикально (если указан параметр `axis=0`), либо горизонтально (если `axis=1`).

Соединение происходит с сохранением индексов, если не указан параметр `ignore_index=True`.
"""

df1 = pd.DataFrame({
    'author_id': [3, 5],
    'author_name': ['Dostoevsky', 'Chekhov'],
    'book_title': ['The Gambler', 'Three Sisters'],
    'quantity': [2, 3],
})

df2 = pd.concat([merged_df, df1], axis=0, ignore_index=True)

df2

df3 = pd.DataFrame(
    {'price': [700, 450, 500, 400, 350]},
    index=[1, 2, 3, 5, 6],
)

df4 = pd.concat([df2, df3], axis=1)

df4

"""### Операции над таблицами

Как и ранее с массивами `numpy` и `Series`, с таблицами `DataFrame` можно производить различные математические операции. Например, значения различных столбцов можно поэлементно перемножать, складывать и пр.
"""

df4["total"] = df4["quantity"] * df4["price"]

df4

"""С помощью следующих методов можно посчитать основные статистики по желаемым столбцам:

* `df4["price"].max()` - максимум
* `df4["price"].min()` - минимум
* `df4["price"].mean()` - среднее
* `df4["price"].median()` - медиана
* `df4["price"].std()` - среднее квадратическое значение
* `df4["price"].var()` - дисперсия

С помощью метода `.nlargest` можно вывести несколько наибольших значений. Указывается то, сколько значений нужно вернуть, а также то, по какому именно значению нужно сортировать:
"""

df4.nlargest(3, "price")

"""Имеется также аналогичный метод `.nsmallest`.

С помощью метода `.unique` можно получить уникальные значения заданного столбца:
"""

df4["author_name"].unique()

"""Если нужно получить не уникальные значения, а лишь их количество, можно воспользоваться методом `.nunique`.

С помощью метода `.value_counts` можно получить информацию о том, сколько раз каждое уникальное значение появляется в данном столбце:
"""

df4["author_name"].value_counts()

"""К значениям таблицы можно применять и функции, которые не имеются в библиотеках `pandas` и `numpy`. Делается это с помощью метода `.apply`:"""

df4["author_name"].apply(lambda x: x.upper())

"""### Группировка данных

Данные в таблице `DataFrame` можно группировать по повторяющимся значениям выбранного столбца. Группировка позволяет вычислять какие-то _агренированные_ значения, т.е. значения, полученные каким-то образом из групп других значений. Например, если мы захотим сгруппировать нашу таблицу по значениям `author_name`, то каждая группа будет содержать все строки с одинаковым значением `author_name`. По таким группам можно затем посчитать какую-нибудь агрегирующую функцию, например, сумму, среднее, минимум и др.

Вот несколько способов это сделать. В первом случае мы просто выбираем конкретный столбец из группировки и применяем к нему какую-то агрегирующую функцию:
"""

groupby = df4.groupby("author_name")

groupby["price"].mean()

"""Второй способ - с помощью метода `.agg`. Данный метод является более гибким. Например, он позволяет вычислять одновременно несколько различных агрегирующих функций от разных столбцов:"""

groupby.agg({"price": "max", "total": "count"})