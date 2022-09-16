# УРОК 2.
# Управление БД. Язык запросов SQL

# - Типы баз данных
# - Основы реляционных БД
# - MySQL и клиенты
# - Управление БД

# Данные и программы
# Иерархические БД
# Сетевые БД
# Реляционные БД
# NoSQL БД
# БД в современных приложениях

# Данные живут дольше программ
# одни и теже данные могут обслуживать
# несколько программ одновременно
# (десктопная программа, web сайт, мобильное приложение)
# могут обращаться к одной БД.
# Данные отделяются от кода и хронятся в БД отдельно

# Трудности работы с файлами
# - Трудно добиться компактности
# - Сложно обеспечить конкурентный доступ
# - Затруднено удаление и редактирование данных
# - Сканирование всех данных во врем поиска
# - файл может не помещаться на компьютере
# - конфликты при совместном редактировании

# данные лучше записывать для компактности
# в бинарном. а не в текстовом формате

# Системы управления БД (СУБД). Надстройка для БД
# для управления, редактирования, и удобной работы с БД

# История развития СУБД
# - Иерархические
# - Сетевые
# - Реляционные
# - NoSQL

# Иерархия дерево состоящие из узлов
# Транспорт: водный воздушный наземный
# Водный: речной морской. Наземный: Авто ЖД
# Есть вершина - транспорт.
# от него расходятся 3 ветки
# водный воздушный наземный
# от водного расходятся 2 ветки
# речной морской
# минус иерархий: невозможность реализовать
# отношение многие-ко-многим

# сетевая бд. одна запись участвует
# в нескольких отношениях предок-потомок
# сейчас реализуются в виде графовых СУБД

# реляционные БД
# отсутствие явной структуры предок-потомок
# все данные в виде простых таблиц,
# разбитых на строки и столбцы
# самый распространёный вид БД

# Реляционные СУБД:
# коммерческие: Oracle, MS SQL (Microsoft), DB2 (IBM),
# свободные СУБД: MySQL, PostgreSQL, Firebird
# db-engines.com  - можно следить за рейтингом БД

# Если раньше на одном сервере умещалось множество сайтов
# то сейчас один сайт занимает множество серверов
# С базами данных анологичное развитие
# множество сайтов к одной БД.
# А сейчас один сайт к множеству БД.
# Распределённые хранилища

# Специализированные NoSQL БД
# Redis, MongoDB, ElasticSearch, ClickHouse, Cassandra
# могут полностью распологаться в оперативной памяти
# со своим языком запросов
# Например Redis. Очень быстрое хронилище
# построенное по принципу: ключ-значение
# оно полностью расположено в оперативной памяти
# сервер реализован в виде однопоточного
# eventloop цикла
# поток опрашивает по кругу соединения
# в неблокирующем режиме
# за счёт того что не происходит переключение процессора
# на другие процессы достигается гигантская производительность
# достигающая 100 000 рпс

# Сейчас актуально совместное использование СУБД
# под конкретные задачи специализированные БД
# нам андо запоминать результаты ресурсоёмкой
# операции для ускорения и кэш в оперативной памяти - REDIS
# Основная БД для долговременного хронения - MySQL
# искать данные, полнотекстовый поиск - ElasticSearch
# перемолоть большие объёмы накопенных данных
# колоночная БД - ClickHouse

# Основы реляционных БД
# - реляционные БД
# - Таблицы, строки и столбцы
# - первичные и внешние ключи
# - Транзакции ACID
# - CAP-теорема

# в реаляционных БД
# информация организована в виде прямоугольных таблиц
# разделёных на строки и столбцы
# на пересечении которых содержится значение.
# БД состоит из нескольких таблиц.
# каждая таблица имеет уникальное имя
# описывающее её содержимое

# Начнём формировать БД.
# на пересечении столбца и строки
# содержится только одно значение.
# все значения содержащиеся в одном
# и том же столбце - данные одного типа.
# у каждого столбца в таблице есть своё имя
# обычно служит заголовком столбца.
# все столбцы в одной таблице
# должны иметь уникальные имена.
# разрешается присваивать одинаовые имена столбцам,
# расположенным в разных таблицах.
# столбцы таблицы упорядочены слева направо.
# у любой таблицы есть минимум один столбец.
# в таблице может содержаться любое количество строк
# в том числе и ноль строк. в этом случае таблица путсая
# т.к строки не упорядочены
# в таблице нет первой, поледней n-ой строки
# В правильно построенной РБД
# в каждой таблице есть столбец, или комбинация столбцов,
# для кторого значения во всех строках различны
# (столбец ID с порядковыми номерами)
# этот столбец или столбцы - ПЕРВИЧНЫЙ КЛЮЧ (primary key)
# Первичный ключ у каждой строки - уникален
# Таблица в которой все строки отличаются друг от друга
# в математических терминах   - отношения (Relation)

# В иерархических БД очень легко выстраивать отношения предок-потомок
# столбец одной таблицы,
# значения которого совпадают со значением столбца,
# являющегося первичным ключом другой таблицы
# называется внешним ключом

# Categories
# |id | name          |
# |1  | Процессоры    |
# |2  | Видеокарты    |

# products
# |id | name          | category_id  |
# | 1 |intel core i7  | 1            |
# | 2 |intel xeon     | 1            |
# | 3 |AMD  Ryzen     | 1            |
# | 4 |GeForce 1060   | 2            |
# | 5 |Radeon RX 5500 | 2            |
# | 6 |GeForce 1280   | 2            |
# category_id  - ВНЕШНИЙ КЛЮЧ

# В РБД можно извлекать связанные между собой данные
# используя эти отношения

# В приложении многое может пойти не так:
# - отказ аппаратного обеспечения
# - исключительная ситуация внутри приложения
# - разрыв сети может отрезать приложение от БД
# все эти проблемы обычно решаются при омощи транзакций
# ТРАНЗАКЦИИ - способ группировки приложением
# нескольких операций записи
# и чтения в одну логическую единицу
# все опрации записи и чтения выполняются как одна
# все транзакции либо целиком выполняются успешно
# с фиксацией изменений
# либо целиком завершается неудачно
# с прерыванием и откатом к исходному состоянию

# Почти все РБД поддерживают транзакции

# Исходные гарантии безопасности
# которые должны обеспечивать транзакции
# ACID
# a - atomicy - атомарность (Реакция БД на сбой)
# c - consistency - согласованность
# i - isolation  - изолированность
# (параллельно выполняемые транзакции изолированы друг от друга)
# d - durability  - сохраняемость

# допустимость или недопустимость данных
# проверяется приложением
# БД лишь обеспечивает хронение

# С развитием web мы получили приложения
# к которым одновременно обращаются тысячи клиентов
# это приводит к проблеме масштабированности БД

# одна БД может оказаться на разных машинах
# и даже в разных data центрах
# Как только БД оказывается распределённой
# необходимо обеспечивать устойчивость к сетевым сбоям
# Противоречие обеспечения согласованности и распределёности систем
# CAP-теорема
# теорема касается трёх взаимосвязанных терминах
# доступность (availibility)
# все клиенты БД
# всегда имеют возможность читать и записвать БД
# согласованность (consistency)
# все клиенты должны прочитать одно
# и тоже значение в ответ на один и тот же запрос
# Устойчивость к разделению (Partition tolerance)
# БД можно разделить между несколькими машинами
# и она продолжет работу даже в случае отказа сегмента сети

# Теорема утверждает, что в любой системе
# можно гарантировано обеспечить
# выполнение только 2ух из этих трёх требований
# аналог поговорки:
# программа может быть хорошей, быстрой и дешёвой
# выбирайте любые 2 свойства.

# Чем больше требуется согласованность от системы
# тем меньше будет её устойчивость к разделению
# в распределёной системе сетевые сбою вероятны
# мы не можем избежать задержек и потери пакетов
# избежать узла устойчивости к разделению
# в современых реалиях практически невозможно

# традиционные реляционные СУБД
# спроектированы для работы на одном компьютере
# обеспечивают согласованность и доступность
# и с трудом может обеспечить устойчивость к разделению

# MySQL И КЛИЕНТЫ

# - СУБД MySQL
# - Клиент-серверное взаимодействие
# - Утилита mysql
# - Конфигурационный файл .my.cnf
# - Утилита mysqldump SQL-дамп

# MySQL на сегодняшний день самая популярная БД
# с открытым кодом
# Например википедия создана с применением MySQL
# Существует множество форков БД

# Архитектура MySQL
# условно разбивается на 2 части:
# ядро - сама БД
# и движки которые реализуют тот или иной механизм БД
# InnoDB, MyISAM, Memory, Archive
# Такая архитектура позволяет разробатывать БД
# усилиями нескольких команд
# кто то сосредотачивается на ядре, кто то на отдельном движке

# MySQL построена по клиент-серверной технологии
# Сервер хронит и обслуживает БД
# Клиенты шлют ему запросы на языке SQL
# и получают в ответ результирующие таблицы с данными
# Клиентами могут выступать разные программы:
# mysql, Dbeaver, Ruby, Python, Java

# Например программа Dbeaver
# позволяет подключаться к различным БД
# и доступна в основных ОС

# Будем учиться работать в консольных утилитах.
# в командной строке
#   >>> mysql -u root -p
#   mysql> SELECT 'Hello Databases';
# КОМАНДЫ ЗАВЕРШАЮТСЯ ";" - СИНТАКСИС
# только после того как консольный клиент mysql встретит ';'
# команда отправляется на сервер
# обратим внимание на результирующую таблицу
# +-----------------+
# | Hello Databases |
# +-----------------+
# | Hello Databases |
# +-----------------+
# 1 row in set
# в первой строке таблицы с результатами
# содержится заголовок столбцов
# в следующих строках идёт ответ сервера на запрос
# для ввода команд можем использовать
# любой регистр (верхний и нижний)
# КЛАВИШИ ВВЕРХ И ВНИЗ ДЛЯ ПРОСМОТРА ВВЕДЁНЫХ КОМАНД

# Если сервер установлен на удалённом хосте,
# соединяемся указав ай пи адрес или домен
# удалёного сервера в параметре ейч (h)
# в параметре P мы можем указать порт
#   >>> mysql -u root -h 192.168.0.10 -P 3306 -p
# утилиты mysql поддерживает различные команды
# Команда   Сокращкение  Описание
# USE       \u           выбор БД
# SOURCE    \.           Выполнение sql-команд из файла
# SYSTEM    \!           Выполнение команды ОС
# STATUS    \s           Вывод информации о состоянии сервера
# EXIT      \q           Выход
#           \G           Вывод результата в вертикальном формате

# \G иногда результирующие таблицы очень велики
# и они рассыпаются в консольном выводе
#   mysql> SELECT * FROM mysql.user LIMIT 1\G
# это команда mysql а не часть sql запроса

# Посмотрим как работают разные команды
#   mysql> STATUS
# запрос статуса сервера
#   mysql> \s
# аналогичная команда в сокращёном варианте
# выполнить системную команду
#   mysql> SYSTEM ls
# Для linux и Mac
# для windows
#   mysql> SYSTEM dir
# в сокращённом варианте
#   mysql> \! dir

# Команды можно набирать в файлах в любом редакторе.
# После того как sql файл сформирован
# мы можем выполнить его при помощи команды SOURCE

# воспользуемся редактором DBeaver для создания sql файла
# 1) ВП -> Новое соединение
# 2) ВП -> Открыть скрипт SQL
# 3) в открывшимся пространстве
#   >>> SELECT 'Hello database!'
# 4) ВП -> файл -> сохранить как

# Файл с рабочего стола не получилось запустить.
# Затем файл перетащил в папку
# C:\Program Files\MySQL\MySQL Server 8.0\bin
# где аходится MySQL.exe
#   mysql> SOURCE hello.sql
#   -->
# +-----------------+
# | Hello Databases |
# +-----------------+
# | Hello Databases |
# +-----------------+
# 1 row in set
# файл открылся !
# и команды записанные в файле отработают

# короткий вариант команды
#   mysql> \. hello.sql

# Специальный конфигурационный файл:
# обычно распологается в домашней директории пользователя
# если параметры не задаются явно,
# они извлекаются из конфигурационного файла

# создадим файл с помощью клиента DBeaver
# >>> [mysql]
#     user=root
#     password=0108
# конфиг файлы sql начинаются обычно с секций
# секция начинается с квадратных скобок
# в которых указывается утилита
# мы настраиваем утилиту [mysql]
# user=root - укажем имя пользователя
# password=0108 и его пароль
# сохранить как .my.cnf
# Теперь можем запускать mysql без запуска пароля

# перенос бд с одного сервера на другой
# или создание резервной копии бд.
# для этого создаётся sql dump
# текстовый файл с командами

# утилита mysql dump
# откроем в Dbreaver сновва файл .my.cnf и внесём изменения
#   [client]
#   user=root
#   password=0108
#
# [client] означает что для всех дестрибютивов mysql

# создадтим дамп системной базы mysql
#   mysql> mysqldump mysql > mysql.sql
# > mysql.sql - перенаправляем > в файл mysql.sql
#   >>> tail -10 mysql.sql
#   -> прочитать последние 10 строчек файла

#  mysql> mysql mysql < hello.sql
# это когда мы хотим развернуть dump
# мы будем пользоваться утилитой mysql
# далее указываем базу данных
# вторая mysql в  mysql> mysql mysql < hello.sql
# и направляем туда содержимое файла < hello.sql

# УПРАВЛЕНИЕ БАЗАМИ ДАННЫХ
# - создание и удаление баз данных
# - текущая база данных
# - создание и удаление таблиц
# - оператор SHOW
# - информационная схема
# - документация

# запустим клиент mysql
# CTRL + l - очистка экрана
# Создать базу данных с помощью SQL оператора
#   mysql> CREATE DATABASE crypto;
# создадим базу данных с именем crypto
# бд создана посмотрим список существующих БД
#   mysql> SHOW DATABASES;
# БД появилась в списке
# узнаем где расположен каталог данных
#   mysql> SHOW VARIABLES LIKE 'datadir';
# --> /var/lib/mysql/
# CTRL + D - выходим из MySQL
#   mysql> exit
#   mysql> \q
# каждая папка - это база данных
#  >>> cd /crypto/
#  >>> ls -la
#  --> видим файл db.opt
#  >>> cat db.opt
#  --> default-character-set=utf8
#      default-collation=utf8_general_ci
# Это файл с настройками кодировки
#  >>> cd ..
# возвращаемся на уровень выше
#  >>> cp -r crypto foo
# -r для рекурсивного копирования
# всего содержимого директории
# crypto foo - мы скопировали каталог crypto в каталог foo

# Для копирования таблиц лучше применять sql dump
# или к специализированным утилитам

# УДАЛЕНИЕ БАЗ ДАННЫХ
#   mysql> DROP DATABASE crypto;

# чтобы избежать моментов повторяющихся имён
#   mysql> CREATE DATABASE IF NOT EXISTS crypto;
# если бд с таким именем
# уже существует ничего не произойдёт
#   mysql> DROP DATABASE IF EXIST crypto;
# Если база данных есть она удалится,
# если бд нет - ничего не произойдёт

# запросим список текущих таблиц не выбирая БД
#  mysql>  SHOW TABLES;
#  --> No database selected
# сообщние об ошибке - бд не выбрана
#  mysql> USE crypto
# ; можно не указывать т.к
# USE не является SQL оператором
# а является командой клиента mysql
#   mysql>  SHOW TABLES;
# отработало без ошибки

# если не выбирать БД.
# то в каждом операторе надо явно указывать
# какая БД будет использоваться
#   mysql>  SHOW TABLES FROM mysql;
#   mysql>  SHOW TABLES FROM crypto;

#   mysql> SELECT mysql.user.user, mysql.user.Host FROM mysql.User;
# в операторе select мы явно указываем имя БД mysql.
# имя таблицы user. и имя столбцов user Host
# и в ключевой команде FROM
# указываем имя БД и таблицы
# FROM mysql.user;

#   >>> mysql -u root -p crypto;
# мы выбрали БД по умолчанию crypto при входе

# СОЗДАНИЕ ТАБЛИЦЫ ВНУТРИ БД

#  >>> CREATE TABLE имя_таблицы (
#       имя_столбца параметры,
#       имя_столбца параметры,
#       ...
#       )

#   >>> CREATE TABLE users (k INT);
# создалась таблица с именем users
# в которой есть одна колонка k
# и значения в этой колонке INT

# При повторной попытки создать такую же таблицу
# у нас сообщение об ошибке.
# чтобы этого избежать
#   >>> CREATE TABLE IF NOT EXIST users(k INT);
# если такой таблицы нет то она создастся
# иначе ничего не произойдёт
#   >>> SHOW TABLES;
# смотрим создана ли таблица
# --> mysql> SHOW TABLES;
# +------------------+
# | Tables_in_crypto |
# +------------------+
# | tradepair        |
# +------------------+
# 1 row in set (1,20 sec)

# ПРОСМОТР СТРУКТУР ТАБЛИЦЫ
#   >>> DESCRIBE users;
#   -->
#   +-------+---------+------+-----+---------+-------+
# | Field | Type    | Null | Key | Default | Extra |
# +-------+---------+------+-----+---------+-------+
# | first | int(11) | YES  |     | NULL    |       |
# +-------+---------+------+-----+---------+-------+
# 1 row in set (2,30 sec)

# каждая строка
# в результирующей таблице
# соответствует отдельному столбцу
# У нас в таблице содержится единственный столбец
# Field :first

# Выберем бд Mysql
# чтобы порботать с боле еобъёмной таблицей
#   >>> USE mysql;
#   >>> DESCRIBE user;
# Оператор Describe
# может принимать доп. параметр - имя столбца
#   >>> DESCRIBE user 'User';
#   -->
#   +-------+----------+------+-----+---------+-------+
# | Field | Type     | Null | Key | Default | Extra |
# +-------+----------+------+-----+---------+-------+
# | User  | char(32) | NO   | PRI |         |       |
# +-------+----------+------+-----+---------+-------+
# 1 row in set (0,00 sec)

# Используем лайтшаблоны
# вместе с оператором DESCRIBE
# заменять с помощью символа процента %
# любое количество символов, а символом _ один символ
# Запросим с таблице юзер все столбцы,
# которе начинаются с символа m
#   >>> DESCRIBE user 'm%';
#   -->
#   +----------------------+------------------+------+-----+---------+-------+
# | Field                | Type             | Null | Key | Default | Extra |
# +----------------------+------------------+------+-----+---------+-------+
# | max_questions        | int(11) unsigned | NO   |     | 0       |       |
# | max_updates          | int(11) unsigned | NO   |     | 0       |       |
# | max_connections      | int(11) unsigned | NO   |     | 0       |       |
# | max_user_connections | int(11) unsigned | NO   |     | 0       |       |
# +----------------------+------------------+------+-----+---------+-------+
# 4 rows in set (0,00 sec)

# операторы SHOW DESCRIBE не реализуют другие БД

# БД information_schema находится в ОЗУ ,
# специальная, её невозможно выбрать
# с помощью команды USE
# INSERT UPDATE DELITE нельзя выполнять для таблиц этой БД
# имеем дело не с таблицами а с представлениями

#   >>>SHOW DATABASES;
#   -->
# +--------------------+
# | Database           |
# +--------------------+
# | information_schema |
# | crypto             |
# | mysql              |
# | performance_schema |
# | sys                |
# +--------------------+
# 5 rows in set (1,52 sec)
# Запросим весь список баз данных из information_schema

#   >>> SELECT * FROM information_schema.SCHEMATA;
#   -->
# +--------------+--------------------+----------------------------+------------------------+----------+
# | CATALOG_NAME | SCHEMA_NAME        | DEFAULT_CHARACTER_SET_NAME | DEFAULT_COLLATION_NAME | SQL_PATH |
# +--------------+--------------------+----------------------------+------------------------+----------+
# | def          | information_schema | utf8                       | utf8_general_ci        | NULL     |
# | def          | crypto             | latin1                     | latin1_swedish_ci      | NULL     |
# | def          | mysql              | latin1                     | latin1_swedish_ci      | NULL     |
# | def          | performance_schema | utf8                       | utf8_general_ci        | NULL     |
# | def          | sys                | utf8                       | utf8_general_ci        | NULL     |
# +--------------+--------------------+----------------------------+------------------------+----------+
# 5 rows in set (0,00 sec)

#   >>> SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'crypto';
# -->
# +---------------+--------------+------------+------------+--------+---------+------------+------------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-------------------+----------+----------------+---------------+
# | TABLE_CATALOG | TABLE_SCHEMA | TABLE_NAME | TABLE_TYPE | ENGINE | VERSION | ROW_FORMAT | TABLE_ROWS | AVG_ROW_LENGTH | DATA_LENGTH | MAX_DATA_LENGTH | INDEX_LENGTH | DATA_FREE | AUTO_INCREMENT | CREATE_TIME         | UPDATE_TIME | CHECK_TIME | TABLE_COLLATION   | CHECKSUM | CREATE_OPTIONS | TABLE_COMMENT |
# +---------------+--------------+------------+------------+--------+---------+------------+------------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-------------------+----------+----------------+---------------+
# | def           | crypto       | tradepair  | BASE TABLE | InnoDB |      10 | Dynamic    |          0 |              0 |       16384 |               0 |            0 |         0 |           NULL | 2021-09-05 19:42:15 | NULL        | NULL       | latin1_swedish_ci |     NULL |                |               |
# +---------------+--------------+------------+------------+--------+---------+------------+------------+----------------+-------------+-----------------+--------------+-----------+----------------+---------------------+-------------+------------+-------------------+----------+----------------+---------------+
# 1 row in set (0,14 sec)

# воспользуемся вертикальным выводом
#   >>> SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'crypto'\G;
# -->
# *************************** 1. row ***************************
#   TABLE_CATALOG: def
#    TABLE_SCHEMA: crypto
#      TABLE_NAME: tradepair
#      TABLE_TYPE: BASE TABLE
#          ENGINE: InnoDB
#         VERSION: 10
#      ROW_FORMAT: Dynamic
#      TABLE_ROWS: 0
#  AVG_ROW_LENGTH: 0
#     DATA_LENGTH: 16384
# MAX_DATA_LENGTH: 0
#    INDEX_LENGTH: 0
#       DATA_FREE: 0
#  AUTO_INCREMENT: NULL
#     CREATE_TIME: 2021-09-05 19:42:15
#     UPDATE_TIME: NULL
#      CHECK_TIME: NULL
# TABLE_COLLATION: latin1_swedish_ci
#        CHECKSUM: NULL
#  CREATE_OPTIONS:
#   TABLE_COMMENT:
# 1 row in set (0,00 sec)
#
# ERROR:
# No query specified

#  mysql> HELP DESCRIBE;
# откроет помощь прямо в коноле

# ВВЕДЕНИЕ В SQL
# ЧИСЛОВЫЕ И СТРОКОВЫЕ ТИПЫ ДАННЫХ
# КАЛЕНДАРНЫЕ ТИПЫ ДАННЫХ И МНОЖЕСТВА
# ИНДЕКСЫ
# CRUD-ОПЕРАЦИИ

# ВВЕДЕНИЕ В SQL
# - стандарт sql
# - Описание данных DDL
# - управление данными DML
# - комментарии
# - ключевые слова
# - кавычки и их использование

# SQL - STRUCTURED QUERY LANGUAGE
# язык для интерактивного общения с СУБД
# Достоинства:
# - декларативная природа
# - высокоуровневая структура
# - высокая эффективность обработки множеств
# - независимость от конкретных СУБД
# - межплатформенная переносимость
# - наличие стандартов

# Недостатки:
# - слабоструктурированый язык
# - язык старый
# - Плохо взаимодействует с ООП-языками
# - SQL - не универсальный язык
# - Множество диалектов

# Элементы языка:
# - комментарии
# - скалярные выражения
# - ключевые слова
# - операторы
# - таблицы
# - столбцы
# - индексы
# - предопределенные функции
# - представления
# - переменные
# - хранимые процедуры
# - хранимые функции
# - триггенры
# - коды ошибок

# КОММЕНТАРИИ .
# Односрочные начинаются с 2 ух символов дефиса --
# -- это однострочный комментарий
# /* многострочный комментарий */

# DDL (Data Definition Language) - язык описания данных
# инструкция создания, удаления, редактирования бд и таблиц
# операторы позволяющие воссоздать структуру БД
# DML (Data Manipulation Language) - язык управления данных
# запросы на зоздание, удаление и извлечения данных из бд
# из таблиц. Операторы обслуживающие данные которые хронятся внутри бд

# структура запроса
#   mysql> SELECT id, name FROM users WHERE name='Игорь'
# ключевые слова : SELECT FROM WHERE
# SELECT id, name  (id, name - столбцы)
# FROM users (users - тблица)
# WHERE name='Игорь' ( name='Игорь' - скалярное выражение)

# скалярные выражения - числа и строки. фактически это константы
#   mysql> SELECT 'Hello db!'
# 'Hello db!' - скалярное выражение
#   mysql> SELECT 'Hello db!'s'
# когда ковычки внутри ковычек интерпритатор запутается
# надо экранировать символ ковычек при помощи слэша
#   mysql> SELECT 'Hello db\'s'
# также можем воспользовться двойными ковычками
#   mysql> SELECT "Hello db's"

# имена БД , таблиц, столбцов строк
# могут содержать разные символы кроме |\./
# если имя совпадает с ключевым словом
# его заключают в обратные ковычки `
#   mysql> CREATE TABLE tbl (create INT)
# имя команды CREATE совпадает с именем столбца create
# мы получим ошибку.
#   mysql> CREATE TABLE tbl (`create` INT)

# ТИПЫ ДАННЫХ:
# - типы данных
# - целые числа
# - вещественные числа
# - строки

# в таблице в каждом столбце данные одного типа
# Типы данных MySQL
# - числовые (целые, вещественные с плавающей точкой)
# - строковые (фиксированные, переменного типа)
# - NULL (неопределённое значение, отсутствие информации)
# - календарные (сохраниение даты и времени)
# - коллекции (множество значение , json документ)

# Атрибуты
# - NULL или NOT NULL
# (задаёт ограничение на столбец,
# позволяя присваивать элементам
# неопределённые значения)
# - DEFAULT
# (задать полю значени епо умолчанию)
# - UNSIGNED
# (только для числовых значений
# запрещает хронить отрицательные значения)

# INT (-2 147 683 648  до 2 147 683 647)
# INT (-2^31  до 2^31)
# INT UNSIGNED (0 - 4 294 967 295 )  (0 - 2^32)

# Числовые типы
# числовые:
# - целочисленные
#   TINYINT (1 байт = 8 бит) (0 - 2^8) (0-256) (-128 до 127)
#   SMALLINT
#   MEDIUMINT
#   INT
#   BIGINT
# - вещественные (с плавающий точкой)
#   FLOAT
#   DOUBLE
# - точные
#   DECIMAL

#   mysql> CREATE TABLE tbl (id INT(8));
# создаём таблицу tbl со столбцом id
# тип данных INT и поле размером 8 символов (8)

# поместим в таблицу число 5
#   mysql> INSERT INTO tbl VALUES (5);
# выведим содержимое таблицы
#   mysql> SELECT * FROM tbl;
#   -->
# +------+
# | id   |
# +------+
# |    1 |
# +------+

#   mysql> DROP TABLE IF EXISTS tbl;
# удаляем таблицу tbl

#   mysql> CREATE TABLE tbl (id INT(3) ZEROFILL);
# Создадим таблицу, где столбец id
# будет содержать числовое значение INT
# столбец будет занимать 3 символа INT(3)
# ZEROFILL вместо пробелов отображать нули
#   mysql> INSERT INTO tbl VALUES (1);
# поместим в таблицу значение 1
#   mysql> SELECT * FROM tbl;
#   -->
# +------+
# | id   |
# +------+
# |  001 |
# +------+

# МОЖЕМ УКАЗЫВАТЬ КОЛИЧЕСТВО СИМВОЛОВ ПОСЛЕ INT
#   mysql> INSERT INTO tbl VALUES (1000);
#   mysql> SELECT * FROM tbl;
#   -->
# +------+
# | id   |
# +------+
# |  001 |
# |  200 |
# +------+

# FLOAT - 4 байта
# DOUBLE - 8 байт
# DECIMAL(7,4) 111.2000 - под всё число отводится 7 байт
# под дробную часть 4 байта
# число хранится в  виде строки
# максимально возможное 999.9999

#   mysql> CREATE TABLE tbldec (price DECIMAL(7,4));
#   mysql> INSERT INTO tbldec VALUES (111.2);
#   mysql> SELECT * FROM tbldec;
# попытаемся ввести число которое не подходит под условия
#   mysql> INSERT INTO tbldec VALUES (11111)
# сообщение об ошибке

# СТРОКОВЫЕ ТИПЫ
# строковые:
# - фиксированные (имеется фиксированный размер)
#   CHAR
# - переменные (нет фикс. размера)
#   VARCHAR
# - BLOB (для хронения бинарных больших объёмов)
#   TINYTEXT
#   TEXT
#   MEDIUMTEXT
#   LONGTEXT

# в круглых скобках после типа
# можно задать максимальный размер строки

# создадим таблицу со строковыми данными
# Воспользуемся графическим редактором DBeaver
# ВП -> Редактор SQL -> открылся блокнот
#   >>> DROP TABLE IF EXISTS tbl;
#       CREATE TABLE tbl (
#       name CHAR(10) DEFAULT 'anonimus',
#       description VARCHAR(255)
#   );

# name CHAR(10) DEFAULT 'anonimus'
# создали столбец - name
# тип данных фиксированный CHAR
# (10) - фиксированный размер 10 байт
# DEFAULT 'anonimus' - если имя не задано,
# то по умалчанию имя будет 'anonimus'
# создали столбец description
# VARCHAR(255) - переменного размера
# (255) байт будет дано на это столбец

# вставим новую строку
#   >>> INSERT INTO tbl VALUES (DEFAULT, 'Новый пользователь');
#   >>> INSERT INTO tbl VALUES ('Юрген', 'Новый пользователь');
#   >>> SELECT * FROM tbl;
# Если имя будет больше чем 10 символов - ошибка выпадет
# ALT + X запустить скрипт в DBeaver

# Столкнулся со следующими трудностями и ошибками
# В DBeaver надо ВП -> текущее соединение
# выставляю MySQL Host
# ВП -> текущий каталог\схема
# выбираю crypto базу данных
# в командах
# >>> INSERT INTO tbl VALUES (DEFAULT, 'Новый пользователь');
# русские символы не читаются и БД ругается в дебивере.
# надо менять кодировку или использовать латиницу

# Итого рабочий скрипт:
# DROP TABLE IF EXISTS tbl;
# CREATE TABLE tbl (
# 	name CHAR(10) DEFAULT 'anonimus',
# 	description VARCHAR(255)
# );
# INSERT INTO tbl VALUES (DEFAULT, 'New User');
# INSERT INTO tbl VALUES ('Yurgen', 'User');
# SELECT * FROM tbl;

# Запись переменной длины
# под неё отводится 65536 байт (2^16)

# Для хранения объёмного текста
# используется тип TEXT
# TINYTEXT 2^8 байт
# TEXT 2^16
# MEDIUMTEXT 2^24
# LONGTEXT 2^32

# СОЗДАДИМ УЧЕБНУЮ БД
# Мы создаём интернет магазин в БД crypto
# создадим файл shop.sql
# куда будем записывать наши наработки
# ВП -> открыть скрипт SQL -> новый скрипт
# ПКМ -> переиминовать в shop.sql
# первым делом создадим таблицу catalog
#   mysql> DROP TABLE IF EXISTS catalogs;
# удаляем таблицу если она существует
#   mysql> CREATE TABLE catalogs (
#       id INT UNSIGNED,
#       name VARCHAR(255) COMMENT 'название раздела'
#   ) COMMENT = 'Разделы интернет магазина';
# id INT UNSIGNED, - создадим первичный ключ
# UNSIGNED т.к отрицательные значения нам не нужны
# name имя для каталога . тип данных VARCHAR(255)
# таблицы и столбцы можно снабжать комментариями

# По аналогии составляем БД для пользователей
# DROP TABLE IF EXISTS users;
# CREATE TABLE users (
#     id INT UNSIGNED,
#     name VARCHAR(255) COMMENT 'name buyer'
# ) COMMENT = 'buyers';

# Создадим таблицу для товара
# DROP TABLE IF EXISTS products;
# CREATE TABLE products (
#    id INT UNSIGNED,
#    name VARCHAR(255) COMMENT 'название',
#    discription TEXT COMMENT 'описание',
#    price DECIMAL (11,2) COMMENT 'цена',
#    catalog_id INT UNSIGNED
# ) COMMENT = 'Товарные позиции';

# Нам потребуются заказы пользователей
# первичный ключ ай ди и юзер ай ди
# DROP TABLE IF EXISTS orders;
# CREATE TABLE orders (
#    id INT UNSIGNED,
#    user_id INT UNSIGNED
# ) COMMENT = 'orders';

# Введём промежуточную таблицу
# DROP TABLE IF EXISTS orders_products;
# CREATE TABLE orders_products (
#    id INT UNSIGNED,
#    order_id INT UNSIGNED,
#    product_id INT UNSIGNED,
#    total INT UNSIGNED DEFAULT 1 COMMENT 'all orders'
# ) COMMENT = 'value orders';

# таблица для скидок
# DROP TABLE IF EXISTS discounts;
# CREATE TABLE discounts (
#    id INT UNSIGNED,
#    user_id INT UNSIGNED,
#    product_id INT UNSIGNED,
#    discount FLOAT UNSIGNED COMMENT 'discount 0.0 - 1.0'
# ) COMMENT = 'discounts';

# Введём таблицу склада и свяжем её с товаром
# DROP TABLE IF EXISTS storehouses;
# CREATE TABLE storehouses (
#    id INT UNSIGNED,
#    name VARCHAR(255) COMMENT 'name'
# ) COMMENT = 'storehouses';

# DROP TABLE IF EXISTS storehouses_products;
# CREATE TABLE storehouses_products (
#    id INT UNSIGNED,
#    storehouse_id INT UNSIGNED,
#    product_id INT UNSIGNED,
#    value INT UNSIGNED COMMENT 'value products'
# ) COMMENT = 'value products on storehouses';

# Это всё каркас нашей учебной БД
# скрипт выглядит целиком так:

# DROP TABLE IF EXISTS catalogs;
# CREATE TABLE catalogs (
#     id INT UNSIGNED NOT NULL,
#     name VARCHAR(255) COMMENT 'name BD categories'
# ) COMMENT = 'categories internet shop';
#
# DROP TABLE IF EXISTS users;
# CREATE TABLE users (
#    id INT UNSIGNED NOT NULL,
#    name VARCHAR(255) COMMENT 'name buyer'
# ) COMMENT = 'buyers';
#
# DROP TABLE IF EXISTS products;
# CREATE TABLE products (
#    id INT UNSIGNED NOT NULL,
#    name VARCHAR(255) COMMENT 'name',
#    discription TEXT COMMENT 'discription',
#    price DECIMAL (11,2) COMMENT 'price' ,
#    catalog_id INT UNSIGNED
# ) COMMENT = 'Positions';LL
#
# DROP TABLE IF EXISTS orders;
# CREATE TABLE orders (
#    id INT UNSIGNED NOT NULL,
#    user_id INT UNSIGNED
# ) COMMENT = 'orders';
#
# DROP TABLE IF EXISTS orders_products;
# CREATE TABLE orders_products (
#    id INT UNSIGNED NOT NULL,
#    order_id INT UNSIGNED,
#    product_id INT UNSIGNED,
#    total INT UNSIGNED DEFAULT 1 COMMENT 'all orders'
# ) COMMENT = 'value orders';
#
# DROP TABLE IF EXISTS discounts;
# CREATE TABLE discounts (
#    id INT UNSIGNED NOT NULL,
#    user_id INT UNSIGNED,
#    product_id INT UNSIGNED,
#    discount FLOAT UNSIGNED COMMENT 'discount 0.0 - 1.0'
# ) COMMENT = 'discounts';
#
# DROP TABLE IF EXISTS storehouses;
# CREATE TABLE storehouses (
#    id INT UNSIGNED NOT NULL,
#    name VARCHAR(255) COMMENT 'name'
# ) COMMENT = 'storehouses';
#
# DROP TABLE IF EXISTS storehouses_products;
# CREATE TABLE storehouses_products (
#    id INT UNSIGNED NOT NULL,
#    storehouse_id INT UNSIGNED,
#    product_id INT UNSIGNED,
#    value INT UNSIGNED COMMENT 'value products'
# ) COMMENT = 'value products on storehouses';

# КАЛЕНДАРНЫЕ ТИПЫ ДАННЫХ И МНОЖЕСТВА
# - значение NULL
# - календарные типы
# - ENUM
# - SET
# - JSON тип
# - изменение структуры таблицы при помощи ALTER TABLE

#  mysql> SELECT NULL;
#  --> NULL
# все операции с NULL возвращают NULL
#  mysql> SELECT NULL + 2
#  --> NULL

#  mysql> CREATE TABLE tbl (id INT UNSIGNED);
#  mysql> INSERT INTO tbl VALUES();
# вставляем новую строку,
# но не  будем задавать ни одного значения

# ПРЕОБРАЗУЕМ С ПОМОЩЬЮ ALTER TABLE
#   mysql> ALTER TABLE tbl CHANGE id id INT UNSIGNED NOT NULL;
# ALTER TABLE - ключевое слово (команда)
# tbl - назвние таблицы
# CHANGE - ключевое слово (изменить)
# id - столбец который изменяем
# id INT UNSIGNED NOT NULL - указываем новые значения столбца

#   mysql> TRUNCATE tbl;
# Очистить таблицу
#   mysql> DESCRIBE tbl\G
# Посмотреть структуру таблицы

# КАЛЕНДАРНЫЕ ТИПЫ
# - TIME (хранение времени в течении суток)
# - YEAR (хронит год)
# - DATE (хронит дату с точностью до дня)
# - DATETIME (хронит дату и время)
# - TIMESTAMP (хронит дату и время занимает меньше места
# хронит даты от 1970 до 2038 года. первый столбец
# этой таблицы обнавляется автоматически
# при операции создания и обнавления)

# Формат календарных типов
# YEAR 0000
# DATE '0000-00-00'
# TIME '00:00:00'
# TIMESTAMP '0000-00-00 00:00:00'
# DATETIME '0000-00-00 00:00:00'

#   mysql> SELECT '2021-09-09 00:00:00'
#   mysql> SELECT '2021-09-09 00:00:00' - INTERVAL 1 DAY
# можем вычитать, складывать
#   mysql> SELECT '2021-09-09 00:00:00' + INTERVAL 1 WEEK
#   mysql> SELECT '2021-09-09 00:00:00' + INTERVAL '1-1' YEAR_MONTH
# интервалы могут быть комбинированными

# ENUM и SET
# их допустимые значения задаются списком строк
# Внутри БД элементы множеств хронятся в виде чисел
# ENUM - поле может получить всего одно значение из списка
# SET - может применять комбинацию заданных значений

# JSON формат столбца
# добавим столбец при помощи ALTER TABLE
#   mysql> ALTER TABLE tbl ADD collect JSON;
# посмотрим структуру таблицы
#   mysql> DESCRIBE tbl;
# вставим новую запись из JSON объекта
#   mysql> INSERT INTO tbl VALUES (1, '{"first": "Hello", "second": "World"}');
# в столбце id добавится 1.
# в столбец collect '{"first": "Hello", "second": "World"}'
# обращаться к полям JSON извлекая значение ключей
#   mysql> SELECT collect->>"$.first" FROM tbl;

# Поправим БД нашего магазина,
# используя вышеизложенное
# первичные ключи снабдим атрибутом NOT NULL
# добавим в таблицу пользователей
# столбец день рожденья
# DROP TABLE IF EXISTS users;
# CREATE TABLE users (
#    id INT UNSIGNED NOT NULL,
#    name VARCHAR(255) COMMENT 'name buyer',
#    birthday_at DATE COMMENT 'user birhtday'
# -> created_at DATETIME COMMENT 'date of registration'
# ) COMMENT = 'buyers';

# Добавим дату и время создания записи
# (время регистрации)
# DROP TABLE IF EXISTS users;
# CREATE TABLE users (
#    id INT UNSIGNED NOT NULL,
#    name VARCHAR(255) COMMENT 'name buyer',
#    birthday_at DATE COMMENT 'user birhtday'
# -> created_at DATETIME COMMENT 'date of registration'
# ) COMMENT = 'buyers';

# добавим дату и время последгнего
# обновления записи пользователя
# чтобы автоматически дата обнавлялась
# DEFAULT CURRENT_TIMESTAMP
# если этим полям не присваивать значение,
# автоматически присвоится текущее значение
# даты и времени

# DROP TABLE IF EXISTS users;
# CREATE TABLE users (
#    id INT UNSIGNED NOT NULL,
#    name VARCHAR(255) COMMENT 'name buyer',
#    birthday_at DATE COMMENT 'user birhtday',
#    created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'date of registration',
#    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT ON UPDATE CURRENT_TIMESTAMP 'date of update'
# ) COMMENT = 'buyers';

# чтобы поле updated_at обнавлялось автоматически
# при операции вставки и обнавлении записи
# ON UPDATE CURRENT_TIMESTAMP

#  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT ON UPDATE CURRENT_TIMESTAMP 'date of updqte'

# Добавим в таблицу данные
#  >>> INSERT INTO users (id, name, birthday_at) VALUES (1, 'hello', '1979-01-27');
#  >>> SELECT * FROM users;

# внесём аналогичные изменения в таблицу
# products, orders, orders_product
# В таблицу discounts добавим 4 календарных поля
# started_ad - начало действия скидки
# finish_ad - конец действия скидки
# добавляем в 2 оставшиеся таблицы
# created_at и updated_at

# Итоговый скрипт:

# DROP TABLE IF EXISTS catalogs;
# CREATE TABLE catalogs (
#     id INT UNSIGNED NOT NULL,
#     name VARCHAR(255) COMMENT 'name BD categories'
# ) COMMENT = 'categories internet shop';
#
# DROP TABLE IF EXISTS users;
# CREATE TABLE users (
#    id INT UNSIGNED NOT NULL,
#    name VARCHAR(255) COMMENT 'name buyer',
#    birthday_at DATE COMMENT 'user birhtday',
#    created_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'date of registration',
#    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
# ) COMMENT = 'buyers';
#
# DROP TABLE IF EXISTS products;
# CREATE TABLE products (
#    id INT UNSIGNED NOT NULL,
#    name VARCHAR(255) COMMENT 'name',
#    discription TEXT COMMENT 'discription',
#    price DECIMAL (11,2) COMMENT 'price' ,
#    catalog_id INT unsigned,
#    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
# ) COMMENT = 'Positions';
#
# DROP TABLE IF EXISTS orders;
# CREATE TABLE orders (
#    id INT UNSIGNED NOT NULL,
#    user_id INT UNSIGNED,
#    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
# ) COMMENT = 'orders';
#
# DROP TABLE IF EXISTS orders_products;
# CREATE TABLE orders_products (
#    id INT UNSIGNED NOT NULL,
#    order_id INT UNSIGNED,
#    product_id INT UNSIGNED,
#    total INT UNSIGNED DEFAULT 1 COMMENT 'all orders',
#    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
# ) COMMENT = 'value orders';
#
# DROP TABLE IF EXISTS discounts;
# CREATE TABLE discounts (
#    id INT UNSIGNED NOT NULL,
#    user_id INT UNSIGNED,
#    product_id INT UNSIGNED,
#    discount FLOAT UNSIGNED COMMENT 'discount 0.0 - 1.0',
#    started_at DATETIME,
#    finished_at DATETIME,
#    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
# ) COMMENT = 'discounts';
#
# DROP TABLE IF EXISTS storehouses;
# CREATE TABLE storehouses (
#    id INT UNSIGNED NOT NULL,
#    name VARCHAR(255) COMMENT 'name',
#    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
# ) COMMENT = 'storehouses';
#
# DROP TABLE IF EXISTS storehouses_products;
# CREATE TABLE storehouses_products (
#    id INT UNSIGNED NOT NULL PRIMARY KEY,
#    storehouse_id INT UNSIGNED,
#    product_id INT UNSIGNED,
#    value INT UNSIGNED COMMENT 'value products',
#    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
# ) COMMENT = 'value products on storehouses';

# ИНДЕКСЫ
# - индексы
# - устройство индекса
# - типы индексов
# - атрибут AUTO_INCREMENT
# - управление индексами

# ключи - столбцы при помощи которых
# мы добиваемся уникальности записей
# и связываем записи в разных таблицах
# ключи могут снабжаться ИНДЕКСАМИ
# ИНДЕКСИРОВАТЬ можно любой столбец

# идея индексов - создать копию стлбца
# которая постоянно будет поддерживаться
# в отсортированном состоянии

# Индексы
# - обычные
# - уникальные (первичный ключ)
# - полнотекстовый

# В таблице может быть только один первичный ключ
# первичный ключ таблицы помечается
# специальным ключевым словом
# значение должно быть уникальным
# и не повторяться в пределах таблицы
# столбцы помеченные pramiery key
# не могут принимать значение NULL

# DROP TABLE IF EXISTS catalogs;
# CREATE TABLE catalogs (
#     id INT UNSIGNED NOT NULL PRIMARY KEY,
#     name VARCHAR(255) COMMENT 'name BD categories'
# ) COMMENT = 'categories internet shop';

# Посмотрим в консоле на описание таблицы
#   mysql> DESCRIBE catalogs;

# Альтернативный способ объявления первичного ключа
# выбрали БД.
#   mysql> PRIMARY KEY(id)
# в скбках название столбца к которому применяем (id)
# ключвое слово PRIMARY KEY может встречаться в таблице только 1 раз
# т.к в таблице разрешён только один первичный ключ
#  mysql> PRIMARY KEY(id, name(10))
# допустимо объявление индека не по одному столбцу
# по двум и более
# первичный ключ создаётся по столбцу id
# и по первым 10 символам столбца name(10)
# как правило для индекса достаточно первых индексов строки

# AUTO_INCREMENT - автоматическое создание уникального номера
#  mysql> id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT;

#   mysql> SELECT * FROM catalogs;
# убедимся что таблица пустая
# вставим несколько строк
#   mysql> INSERT INTO catalogs (name) VALUES ('Процессоры');
# не указываем поле id - оно должно сформироваться автоматически
# значение поле id - 1
#   mysql> INSERT INTO catalogs (name) VALUES ('Видеокарты');
# поле ай ди сформировалось автоматически . значение поля id 2
# В INSERT запросеспециально не указали id,
# чтобы оно получило значение NULL

# Псевдоним SERIAL
# SERIAL == BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
# это позволяет более компактно записывать
# id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT;
# равнозначно
#  mysql> id SERIAL PRIMARY KEY;

# Ттаблица может содержать
# несколько обычных и уникальных индексов
# для того чтобы их различать индексы
# могут иметь собственные имена
# часто имена индексов совпадают с именами столбцов
# которые они индексируют
# для индекса можно назначить совершенно другое имя
# Объявление индекса происходит
# с помощью ключевого слова
# INDEX или KEY
# для уникальных индексов
# доп. ключевое слово UNIQUE

# В таблице ptoducts снабдим индексом поле
# catalog_id
# DROP TABLE IF EXISTS products;
# CREATE TABLE products (
#    id SERIAL PRIMARY KEY,
#    name VARCHAR(255) COMMENT 'name',
#    discription TEXT COMMENT 'discription',
#    price DECIMAL (11,2) COMMENT 'price' ,
#    catalog_id INT unsigned,
#    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
# -> KEY index_of_catalog_id(catalog_id)
# ) COMMENT = 'Positions';

# посмотрим через консоль
#   mysql> DESCRIBE products;
# +-------------+-----------------+------+-----+-------------------+--------------
# ---------------------------------+
# | Field       | Type            | Null | Key | Default           | Extra
#                                  |
# +-------------+-----------------+------+-----+-------------------+--------------
# ---------------------------------+
# | id          | bigint unsigned | NO   | PRI | NULL              | auto_incremen
# t                                |
# | name        | varchar(255)    | YES  |     | NULL              |
#                                  |
# | discription | text            | YES  |     | NULL              |
#                                  |
# | price       | decimal(11,2)   | YES  |     | NULL              |
#                                  |
# | catalog_id  | int unsigned    | YES  | MUL | NULL              |
#                                  |
# | created_at  | datetime        | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENER
# ATED                             |
# | updated_at  | datetime        | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENER
# ATED on update CURRENT_TIMESTAMP |
# +-------------+-----------------+------+-----+-------------------+--------------
# ---------------------------------+
# 7 rows in set (0.01 sec)

# Создать индекс в уже существующей таблице
# можно с помощью оператора CREATE INDEX

#   mysql> CREATE INDEX index_of_catalog_id ON products (catalog_id);

# удалить индекс из таблицы
#   mysql> DROP INDEX index_of_catalog_id ON products;

# Индексы BTREE и ХЭШиндексы
# мы можем явно указывать тип индекса USING BTREE
#  mysql> CREATE INDEX index_of_catalog_id USING BTREE ON products (catalog_id);
# указываем явно чтобы индекс был построен как бинарное дерево
# в качестве альтернативы можем использовать HASH
#   mysql> CREATE INDEX index_of_catalog_id USING HASH ON products (catalog_id);
# полезен для точного поиска с указанием всех столбцов индекса
# в индоксе хронятся хэштеги
# и указатели на соответствующие строки

# отрефакторим таблицу products;

# ЗАПРОСЫ НА ПОИСК ИНФО
#   mysql> SELECT * FROM tbl WHERE year = 1990
#   mysql> SELECT * FROM tbl WHERE year = 1990 AND last_name = Борисов

# ДОБАВЛЯЕМ ИНДЕКСЫ ТОЛЬКО В ТОМ СЛУЧАЕ
# КОГДА ЭТО НЕОБХОДИМО

# CRUD ОПЕРАЦИИ
# - Введение в CRUD-операции
# - Вставка данных
# - Извлечение данных
# - Обновление данных
# - удадение данных
# - Команда INSERT ... SELECT

# 4 базовые операции
# создания, чтения, обновления и удаления
# Crete - INSERT
# Read - SELECT
# Update - UPDATE
# Delete - DELETE
# CRUD

# Встава. Оператор INSERT
# Одиночная вставка
#   mysql> INSERT INTO catalogs VALUES (NULL, 'Процессоры');
#   mysql> INSERT INTO catalogs VALUES (NULL, 'Мат.платы');
#   mysql> INSERT INTO catalogs VALUES (NULL, 'Видеокарты');

# Многострочная вставка
#   mysql> INSERT INTO catalogs VALUES
#       (NULL, 'процессоры'),
#       (NULL, 'Мат.платы'),
#       (NULL, 'Видеокарты');

# Вставим в нашу таблицу catalogs записи

# DROP TABLE IF EXISTS catalogs;
# CREATE TABLE catalogs (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(255) COMMENT 'name BD categories'
# ) COMMENT = 'categories internet shop';

# INSERT INTO catalogs VALUES (NULL, 'Processors');
# мы вставляем в таблицу первую запись
# полю id мы присваиваем неопредлённое значение NULL
# Полю name присваиваем значение 'Processors'

# Мы можем явно указывать список столбцов,
# которые мы вставяем
#   mysql> INSERT INTO catalogs (id, name) VALUES (NULL, 'Motherboards');
# можем поменять местами столбцы, такая запись тоже допустима
#   mysql> INSERT INTO catalogs (name, id) VALUES ('Motherboards', NULL);
# также вместо ключевого слова NULL
# можем использовать ключевое слово DEFAULT
#   mysql> INSERT INTO catalogs VALUES (DEFAULT, 'Videocards');

# Множество INSERT запросов можно заменить
# многострочниым вариантом запроса
#   mysql> INSERT INTO catalogs VALUES
#       (DEFAULT, 'Processors'),
#       (DEFAULT, 'Motherboards'),
#       (DEFAULT, 'Videocards');

# Для извлечения данных используется оператор SELECT
#   mysql> SELECT id, name FROM catalogs;
# После ключевого оператора SELECT
# указываем список столбцов id, name
# ключевое слово FROM
# указываем откуда извлекаем
# из какой таблицы catalogs
# порядок столбцов после ключевого слова можно изменять
# тем самым будем менять порядок столбцов
# в результиующей таблице
#   mysql> SELECT name, id FROM catalogs;
# можем выводить только часть столбцов
#   mysql> SELECT name FROM catalogs;
# часто столбцы заменяются символом *
# в этом случае выводятся все столбцы,
# в порядке в котором они определены в CREATE TABLE
#   mysql> SELECT * FROM catalogs;

# вставка при помощи INSERT
# добавим уникальный индекс на столбец name
# таблицы catalogs;
# тем самым мы запретим вставку разделов,
# которые уже вставлены в таблицу
# для того чтобы не раздувать индекс,
# проиндексируем только первые 10 символов
# UNIQUE unigue_name(name(10))

# DROP TABLE IF EXISTS catalogs;
# CREATE TABLE catalogs (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(255) COMMENT 'name BD categories',
#     UNIQUE unigue_name(name(10))
# ) COMMENT = 'categories internet shop';
# в случае вставки уже имеющихся значений,
# получим сообщение об ошибке

# Уникальный ключ не допускает нарушения целостности БД
# избежать такого поведения
# можно с помощью ключевого слова IGNORE
#   mysql> INSERT IGNORE INTO catalogs VALUES (NULL, 'Processors');
# попытка вставить существующее значение просто блокируется

# Удаление данных
#   mysql> DELETE FROM catalogs;
# удаляет все или часть записай из таблицы

# очистка таблицы
#   mysql> TRUNCATE catalogs;
# удаляет все записи и обнуляет счётчики AUTOINCREMANT

# Можем удалять часть данных
#   mysql> DELETE FROM catalogs LIMIT 2;
# мы удалм только 2 записи.
# Перые 2 записи таблицы удалятся

# Удалять только те записи
# первичный ключ ай ди которых больше 1
#   mysql> DELETE FROM catalogs WHERE id > 1 LIMIT 1;

# При использовании операции DELETE
# счётчик и автоинкремент не затрагивается

# вставим данные, удалим и снова вставим,
# чтобы посмотреть как работаетсчётчик автоинкремент

#   mysql> INSERT INTO catalogs VALUES
#       (DEFAULT, 'Processors'),
#       (DEFAULT, 'Motherboards'),
#       (DEFAULT, 'Videocards');
#   mysql> DELETE FROM catalogs;
#   mysql> INSERT INTO catalogs VALUES
#       (DEFAULT, 'Processors'),
#       (DEFAULT, 'Motherboards'),
#       (DEFAULT, 'Videocards');

# столбец id  с натсройками:
# id SERIAL PRIMARY KEY,
# во второй вставке имеет id 4,5,6

# сброс счётчиков
#   mysql> TRINCATE catalogs;
# очищает таблицу, обнуляет счётчики

# команда UPDATE позволяет редактировать данные
# UPDATE
#   catalogs
# SET
#   name = 'Processors (Intel)'
# WHERE
#   name = 'Processors';
# Если убрать ограничение WHERE
# произошла бы попытка замены всех записей таблицы
# а если поле проиндексировано уникальным ключом
# произойдёт ошибка

# специалиный оператор INSERT SELECT
# позволяет вставлять записи из одной таблицы в другую
# в том числе осуществляя преобразоваие над данными
# если таблицы имеют идентичные столбцы
# перемещаем все данные изтаблицы catalog в таблицу cat

#   INSERT INTO
#       cat
#   SELECT
#       *
#   FROM
#       catalogs;
