# Урок 9.

# ТРАНЗАКЦИИ
# - транзакции
# - внутренняя реализация транзакций
# - переменные, впеменные таблицы и динамические запросы
# - представления

# механизм поддержания целостности данных в СУБД

# ПОНЯТИЯ И СИНТАКСИС ТРАНЗАКЦИЙ
# - транзакции
# - ключевые слова COMMIT и ROLLBACK
# - точки сохранения
# - режим автозавершения транзакций
# - принцип ACID
# - уровни изоляции

# Транзакция - аттомарная группа запросов SQL
# она рассматривается как единое целое.
# Если БД может выполнить всю группу запросов
# она делает это.
# состояние базы до транзакции:
#   SELECT -> UPDATE -> DELETE -> INSERT
# состояние базы после транзакции
# если любой из запросов не может быть выполнен
# в результате сбоя, по какой либо другой причине
# не будет выполнени ни один запрос такой группы
#   SELECT -> UPDATE -> DELETE -> программная ошибка
#   SELECT -> UPDATE -> аппаратный сбой
# ВСЁ ИЛИ НИЧЕГО!

# операции с денежными средствами
# является класическим примером,
# показывающим почему необходимы транзакции
# ПЕРЕМЕЩЕНИЕ ДЕНЕЖНЫХ СРЕДСТВ

# |id|user_id|total|    |id|user_id|total|
# | 1|  4    | 5000|    |1 |  4    | 3000|
# | 2|  3    | 0   | -> |2 |  9    |  0  |
# | 3|  2    |  200|    |3 |  2    |  200|
# | 4| NULL  |25000|    |4 |  4    |27000|

# если при оплате покупки денежные средства
# переходят со счёта покупателя на счёт продавца
# то счёт покупателя должен уменьшиться на эту сумму,
# а счёт продавца должен увеличится на эту сумму
# пость у нас есть таблица ACOUNT со счетами пользователей
# в этой же таблице етсть счёт продавца (id = 4)
# он отличается тем, что внешний ключ user_id = NULL
# для осуществления покупки
# нам необходимо переместить 2000 со счёта покупателя
# на счёт продавца.
# ПЕРЕВОД СРЕДСТВ:
# - убедиться, что остаток на счёте клиента больше 2000 рублей
# - вычесть 2000 рублей со счёта клиента
# - добавить 2000 к счёту продавца
# вся операция должна быть организована ка ктранзакция
# чтобы в случае неудачи в любом из этих этапов
# все выполненные ранее шаги были отменены.

# создадим таблицу accounts
#   mysql> CREATE TABLE accounts (
#       -> id SERIAL PRIMARY KEY,
#       -> user_id INT,
#       -> total DECIMAL (11,2) COMMENT 'счёт',
#       -> created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
#       -> updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
#       -> ); COMMENT = 'счета пользователей и интернет магазина'
# заполняем таблицу
#   mysql> INSERT INTO accounts (user_id, total) VALUES
#       ->  (4, 5000.00),
#       ->  (3, 0.00),
#       ->  (2, 200.00),
#       ->  (NULL, 25000.00);
# посмотрим текущее состояние таблицы
#   mysql> SELECT * FROM accounts;
# +----+---------+----------+---------------------+---------------------+
# | id | user_id | total    | created_at          | updated_at          |
# +----+---------+----------+---------------------+---------------------+
# |  1 |       4 |  5000.00 | 2021-10-22 11:03:58 | 2021-10-22 11:03:58 |
# |  2 |       3 |     0.00 | 2021-10-22 11:03:58 | 2021-10-22 11:03:58 |
# |  3 |       2 |   200.00 | 2021-10-22 11:03:58 | 2021-10-22 11:03:58 |
# |  4 |    NULL | 25000.00 | 2021-10-22 11:03:58 | 2021-10-22 11:03:58 |
# +----+---------+----------+---------------------+---------------------+
# 4 rows in set (0.10 sec)
# начинаем транзакцию. для этого команда SRART TRANSACTION;
#   mysql> START TRANSACTION;
# далее выполняем команды входящие в транзакцию
#   mysql> SELECT total FROM accounts WHERE user_id = 4;
# +---------+
# | total   |
# +---------+
# | 5000.00 |
# +---------+
# убеждаемся, что на счету пользователя достаточно средств
# снимаем средства со счёта прользователя
#   mysql> UPDATE accounts SET total = total - 2000 WHERE user_id =4;
# Query OK, 1 row affected (0.06 sec)
# Rows matched: 1  Changed: 1  Warnings: 0
# перемещаем их на счёт интернет магазина
#   mysql> UPDATE accounts SET total = total + 2000 WHERE user_id IS NULL;
# Query OK, 1 row affected (0.07 sec)
# Rows matched: 1  Changed: 1  Warnings: 0
# посмотрим состояние таблицы accounts
#   mysql> SELECT * FROM accounts;
# +----+---------+----------+---------------------+---------------------+
# | id | user_id | total    | created_at          | updated_at          |
# +----+---------+----------+---------------------+---------------------+
# |  1 |       4 |  3000.00 | 2021-10-22 11:03:58 | 2021-10-22 11:10:20 |
# |  2 |       3 |     0.00 | 2021-10-22 11:03:58 | 2021-10-22 11:03:58 |
# |  3 |       2 |   200.00 | 2021-10-22 11:03:58 | 2021-10-22 11:03:58 |
# |  4 |    NULL | 27000.00 | 2021-10-22 11:03:58 | 2021-10-22 11:51:37 |
# +----+---------+----------+---------------------+---------------------+
# 4 rows in set (0.00 sec)
# на данный момент изменения в рамках транзакции не сохранены
# если переключиться в другую консоль и посмотреть
# на таблицу глазами другого пользователя
# то изменений мы не увидим
# для фиксации должны выполнить команду COMMIT
#   mysql> COMMIT;
# Query OK, 0 rows affected (0.07 sec)

# если в момент когда выполнялась транзакция
# какая то другая транзакция
# уже изменила счёт пользователя
# то команда COMMIT завершится ошибкой
# и изменения в рамках текущей транзакции будут анулированы

# можем самостоятельно отменять транзакции
# спишем ещё 2000 рублей со счёта пользователя
#   mysql> START TRANSACTION;
#   mysql> SELECT total FROM accounts WHERE user_id = 4;
#   mysql> UPDATE accounts SET total = total - 2000 WHERE user_id = 4;
#   mysql> UPDATE accounts SET total = total + 2000 WHERE user_id IS NULL;
# выясняем что не можем завершить транзакцию,
# пользователь её отменил
# отменяем транзакцию ROLLBACK
#   mysql> ROLLBACK;
#   mysql> SELECT * FROM accounts;
# видим, что изменений не прризошло

# НЕОБРАТИМЫЕ КОМАНДЫ (откат ROLLBACK не выполнится)
# - CREATE INDEX
# - DROP INDEX
# - CREATE TABLE
# - DROP TABLE
# - TRUNCATE TABLE
# - ALTER TABLE
# - RENAME TABLE
# - CREATE DATABASE
# - DROP DATABASE
# - ALTER DATABASE
# следует избегать помещать их в транзакции с другими опертаторами

# НЕЯВНОЕ ЗАВЕРШЕНИЕ ТРАНЗАКЦИЙ
# - ALTER TABLE
# - BEGIN
# - CREATE INDEX
# - CREATE TABLE
# - CREATE DATABASE
# - DROP DATABASE
# - DROP INDEX
# - DROP TABLE
# - LOAD MASTER DATA
# - LOCK TABLES
# - RENAME
# - SET CAUTOCOMMIT=1
# - START TRANSACTION
# - TRUNCATE TABLE
# эти команды неявно завершают транзакцию
# так как была бы вызвана команда COMMIT
# транзакции не могут быть ложными
# это связано с тем,
# что любой оператор начинающий транзакцию
# приводит к завершению предидущей транзакции

# точка сохранения SAVEPOINT - место в последовательности
# выполнения транзакции которая может выступать
# в качестве промежуточной точки восстановления откат
# в текущей транзакции может быть выполнен к точке сохранения
# SAVEPOINT savename - указываем имя точки сохранения

# состояние до транзакции
#   SELECT -> SAVEPOINT -> DELETE -> INSERT
# состояние базы после транзакции
# в случае ошибки возвращаемся к SAVEPOINT
#   SELECT -> SAVEPOINT -> DELETE -> ошибка -> SAVEPOINT

# КОМАНДЫ ДЛЯ ТОЧЕК СОХРАНЕНИЯ
# - SAVEPOINT - создаёт точку сохранения
# - ROLLBACK TO SAVEPOINT - откат к одной из точек сохранения

# пример работы точек сохранения
#   mysql> START TRANSACTION;
#   mysql> SELECT total FROM accounts WHERE user_id = 4;
#   mysql> SAVEPOINT accounts_4;
# продолжим выполнение транзакций
#   mysql> UPDATE accounts SET total = total - 2000 WHERE user_id = 4;
# мы хотим отменить транзакцию
#   mysql> ROLLBACK TO SAVEPOINT accounts_4;
# последний UPDATE оператор был отменён

# допускается создание нескольких точек сохранения.
# если транзакция имеет точку сохранения с таким же именем
# старая точка удаляется и устанавливается новая.
# все точки сохранения удаляются,
# если выполняется оператор COMMIT
# или ROLLBACK без указания имени точки сохранения.

# пока не используем оператор START TRANSACTION
# в mysql каждый запрос рассматривается как транзакция
# обычно говорят mysql работает в режиме
# автозавершения транзакций
# можем отключить такой режим с помощью команды
#   mysql> SET AUTOCOMMIT=0
# в этом случае любая последовательность команд
# будет рассматриваться как транзакция.
# нам не обязательно начинать её с помощью команды START
#   mysql> SELECT total FROM accounts WHERE user_id = 4;
#   mysql> UPDATE accounts SET total = total - 2000 WHERE user_id = 4;
#   mysql> UPDATE accounts SET total = total + 2000 WHERE user_id IS NULL;
#   mysql> SELECT * FROM accounts;
# чтобы сохранить изменения надо выполнить команду COMMIT;
# или отменить предыдущие комнды при помощи ROLLBACK
# для того чтобы снова включить режим автозавершения транзакций
#    mysql> SET AUTOCOMMIT=1

# транзакций не достаточно если они не удовлетворяют принципу ACID
#  - Atomicy  атомарность
# (должна функционировать как единая недилимая единица)
# вся транзакция либо выполняется либо отменяется
# когда транзакция атомарна не существует
# такого понятия как частично выполненная транзакция
#  - Consistency - согласованность
#  (БД всегда должна переходить
#  из одного непротиворечивого состояния
# в другое непротиворечивое состояние)
# в нашем примере согласованность гарантирует
# что сбой между 2умя UPDATE командами
# не приведёт к исчезновению 2000 р со счёта пользователя
# транзакция не будет зафиксирована
# и ни одно из изменений
# в этой транзакции не будет отражено в БД
#  - Isolation - изолированность
# (результаты транзакций обычно не видны другим транзакциям
# пока текущая транзакция не закончена)
# это гарантирует, что в нашем примере
# во время транзакции будет выполнен запрос
# на извлечение средств пользователем
# такой запрос попрежнему увидит 2000 р.
# на счету у пользователя
#  - Durability - сохраняемость
# (гарантирует что изменения внесёные во время транзакции
# будучи зафиксированными становятся постоянными)
# изменение должно быть записано так
# чтобы данные не могли быть потеряны
# в случае сбоя системы

# транзакции ACID гарантируют
# что интернет магазин не потеряет ваши деньги
# с помощью логики приложения это сделать невозможно
# транзакции требуют давольно много ресурсов
# и замедляют раблту БД
# часто идут на компромисы
# и дополнительную натсройку транзакций

# УРОВНИ ИЗОЛЯЦИИ ТРАНЗАКЦИЙ
# стандарт sql определяет 4 уровня изоляции
# с конкретными правилами,
# устанавливающими какие изменения видны
# внутри и вне транзакций, а какие нет.

# - READ UNCOMMITTED наиболее слабая.
# большая степень совместного доступа
# и меньше накладных расходов.
# на этом уровне транзакции могут видеть
# результаты не зафиксированных транзакций.
# мы выидим промежуточные результаты
# чужих транзакций то есть осуществляете грязночтение
# - READ COMMITTED транзакции увидят только те изменения
# которые были уже зафиксированы другими
# транзакциями к моменту её начала.
# а произведённые ей изменения
# останутся невидимыми для других транзакций,
# пока текущая транзакция не будет зафиксирована.
# другими транзакциями к моменту её начала.
# на этом уровне возможен феномен невоспроизводимого чтения
# (можем выполнить одну и туже команду
# и получить разный результат)
# - REPEATABLE READ решает проблемы
# которые возникают на предыдущем уровне.
# Гаранирует, что любые строки,
# которые считываются в контексте транзакции
# будут выглядить точно также как
# при последовательных операциях
# чтения в пределах одной и тойже транзакции.
# теоретически на этом уровне возможен феномен фантомного чтения.
# возникает в случае выбора некоторого диапазона строк,
# а затем другая транзакция вставляет новую страку
# в этот диапазон. после чего выбирая тот же даипазон снова
# и в результате видим новую фантомную строку.
# УРОВЕНЬ В MYSQL УСТАНОВЛЕН ПО УМОЛЧАНИЮ.
# - SERIALIZABLE наиболее сильная.
# решена проблема фантомного чтения
# заставляет транзакции выполняться в таком поорядке
# чтобы исключить возможность конфликта.
# уровень блокирует каждую строку
# которую транзакция читает
# может возникать множество задержек и конфликтов
# при блокировках.

# ИЗМЕНИТЬ УРОВЕНЬ ИЗОЛЯЦИИ
# можно изменить при помощи команды SET TRANSACTION

# КАК УСТРОЕНЫ ТРАНЗАКЦИИ В MYSQL
# - взаимоблокировка
# - журнал транзакций
# - управление режимом сохранения транзакций в журнал
# - MVCC (механизм многоверсионного управления конкурентным доступом)
# - связь MVCC с уровнями изоляции

# Начнём транзакции в 2 ух разных сессиях:
#   1mysql> START TRANSACTION;
#   1mysql> UPDATE accounts SET total = total - 2000 WHERE user_id = 4;
#   1mysql> UPDATE accounts SET total = total + 2000 WHERE user_id IS NULL;
#
#   2mysql> START TRANSACTION;
#   2mysql> UPDATE accounts SET total = total - 1000 WHERE user_id = 4;
# вторая транзакция не выполняет запрос
# т.к она завершает выполнение первой транзакции
# этот запрос выполнится только в том случае,
# если в первой транзакции мы введём COMMIT или ROLLBACK
#   1mysql> START TRANSACTION;
#   1mysql> UPDATE accounts SET total = total - 2000 WHERE user_id = 4;
#   1mysql> UPDATE accounts SET total = total + 2000 WHERE user_id IS NULL
#   1mysql> COMMIT;
# 2 транзакция продолжила свою работу
# возможны ситуации взаимоблокировки
# когда 2 или более транзакций запрашивают
# блокировку одних и тех же ресурсов
# в результате чего образуется циклическая зависимость
# в этом случае одна транзакция будет
# ожидать до бескогечности завершения другой
# и конфликт не завершится до тех пор
# пока не произойдёт какое нибудь событие,
# которое снимет взаимную блокировку

# для разрешения такой проблемы системы баз данных
# реализованы разные формы обнаружения взаимоблокировок
# и таймаутов

# В БД транзакции редко записываются сразу в таблицу
# вместо этого все транзакции сразу помещаются
# в журнал тарнзакций
# когда происходит изменение
# оно изменяет не таблицу на жёстком диске,
# а находящуюся в памяти копию данных
# затем подсистема хранения записывет сведения об изменении
# в журнал транзакций.
# журнал также расположен на диске
# событие добавляется в конец журанла
# вместо того чтобы записывать данные в разных местах таблицы
# в процессе фоновый процесс перегонит данные
# из журнала транзакций в таблицы.
# Большинство БД, использующих журнал транзакций
# сохроняют изменения на диске дважды
# если происходит сбой, после того как занесена
# соответствующая запись в журна транзакций
# но до того как обновлены сами данные
# система хронения может восстановить изменения
# после перезапуска сервера

# ЗАПРОСИТЬ ПАРАМЕТРУ ЖУРНАЛА ТРАНЗАКЦИЙ
#   mysql> SHOW VARIABLES LIKE 'innodb_log_%'
# +-----------------------------+----------+
# | Variable_name               | Value    |
# +-----------------------------+----------+
# | innodb_log_buffer_size      | 16777216 |
# | innodb_log_checksums        | ON       |
# | innodb_log_compressed_pages | ON       |
# | innodb_log_file_size        | 50331648 |
# | innodb_log_files_in_group   | 2        |
# | innodb_log_group_home_dir   | ./       |
# | innodb_log_write_ahead_size | 8192     |
# +-----------------------------+----------+
# 7 rows in set (0.44 sec)
# из полученного отчёта видно,
# что журнал транзакций имеет 2 файла
# | innodb_log_files_in_group   | 2
# размером по 50 мб
# | innodb_log_file_size        | 50331648 |
# по умолчанию файлы
# журнала транзакций распологаются в каталоге данные
# получить путь к каталогу данные нашей системы
# можно при помощи следующего запроса
#   mysql> SHOW VARIABLES LIKE 'datadir';
# +---------------+-----------------+
# | Variable_name | Value           |
# +---------------+-----------------+
# | datadir       | /var/lib/mysql/ |
# +---------------+-----------------+
# 1 row in set (0.00 sec)

# выйдем из диалогового режима mysql
# в консоль операционной системы
#   mysql> EXIT
# и перейдём в каталог данных
#   student@Ubuntu-MySQL-VirtualBox:~$> cd  /var/lib/mysql/
# не заходит выдаёт ошибку
# вхожу под суперпользователем root
#   student@Ubuntu-MySQL-VirtualBox:~$> sudo su - root
#   root@Ubuntu-MySQL-VirtualBox:~# > cd  /var/lib/mysql/
# запрашиваем содержимое (дли виндоус команда dir)
#   root@Ubuntu-MySQL-VirtualBox:/var/lib/mysql# > ls -la
# итого 122960
# drwx------  7 mysql mysql     4096 окт 24 11:32 .
# drwxr-xr-x 70 root  root      4096 окт  7 11:16 ..
# -rw-r-----  1 mysql mysql       56 апр 22  2019 auto.cnf
# -rw-------  1 mysql mysql     1680 окт  7 11:23 ca-key.pem
# -rw-r--r--  1 mysql mysql     1112 окт  7 11:23 ca.pem
# -rw-r--r--  1 mysql mysql     1112 окт  7 11:23 client-cert.pem
# -rw-------  1 mysql mysql     1676 окт  7 11:23 client-key.pem
# -rw-r--r--  1 mysql mysql        0 окт  7 11:22 debian-5.7.flag
# drwxr-x---  2 mysql mysql     4096 окт 11 15:31 example_db
# -rw-r-----  1 mysql mysql      679 окт  7 11:23 ib_buffer_pool
# -rw-r-----  1 mysql mysql 12582912 окт 24 11:32 ibdata1
# -rw-r-----  1 mysql mysql 50331648 окт 24 11:32 ib_logfile0
# -rw-r-----  1 mysql mysql 50331648 апр 22  2019 ib_logfile1
# -rw-r-----  1 mysql mysql 12582912 окт 24 11:32 ibtmp1
# drwxr-x---  2 mysql mysql     4096 окт  7 11:23 mysql
# -rw-r--r--  1 root  root         6 окт  7 11:23 mysql_upgrade_info
# drwxr-x---  2 mysql mysql     4096 окт  7 11:23 performance_schema
# -rw-------  1 mysql mysql     1676 окт  7 11:23 private_key.pem
# -rw-r--r--  1 mysql mysql      452 окт  7 11:23 public_key.pem
# -rw-r--r--  1 mysql mysql     1112 окт  7 11:23 server-cert.pem
# -rw-------  1 mysql mysql     1676 окт  7 11:23 server-key.pem
# drwxr-x---  2 mysql mysql     4096 окт 22 11:02 shop
# drwxr-x---  2 mysql mysql    12288 окт  7 11:23 sys

# среди файлов можем обнаружить 2
# -rw-r-----  1 mysql mysql 50331648 окт 24 11:32 ib_logfile0
# -rw-r-----  1 mysql mysql 50331648 апр 22  2019 ib_logfile1
# это и есть файлы журнала транзакций
# все транзакции сначала помещаются сюда
# по умолчанию мы используем движок innodb
# innodb хронит таблицы всех БД
# в едином табличном пространстве
# в файле
# -rw-r-----  1 mysql mysql 12582912 окт 24 11:32 ibdata1
# физически единое табличное пространство
# может распологаться в нескольких файлах
# более того мы можем выделить отдельные табличные прсотранства
# под каждуюиз таблиц
# транзакции помещаются в файлы
# -rw-r-----  1 mysql mysql 50331648 окт 24 11:32 ib_logfile0
# -rw-r-----  1 mysql mysql 50331648 апр 22  2019 ib_logfile1
# и потом перегоняются в файл единого табличного пространства
# -rw-r-----  1 mysql mysql 12582912 окт 24 11:32 ibdata1

# Если сервер mysql останавливается штатно
# то транзакции из журнала сохроняются в таблице
# при аварийной остановке сервера, неплановой,
# перед старартом mysql проверяет журнал транзакций
# и перегоняет все транзакции в единое табличное пространство
# таким образом потерять сохранённые транзакции невозможно

# увеличивая размер журнала транзакций
# можно ускорить вставку записей при штатной работе mysql
# чем больше журнал транзакций, тем медленнее стартует сервер

# УПРАВЛЕНИЕ РЕЖИМОМ СОХРАНЕНИЯ ЖУРНАЛА ТРАНЗАКЦИЙ
# innodb_flush_log_at_trx_commit
# - 0 - сохранение журнала раз в секунду
# - 1 - сохранение после каждой транзакции
# - 2 - сохранение журнала раз в секунду
# и после каждой транзакции

# innodb_flush_log_at_trx_commit
# серверная переменная отвечающая
# за режим сохранения транзакций
# в этой переменной устанавливается 0, 1 или 2
# запросим состояние переменной
#   mysql> SHOW VARIABLES LIKE 'innodb_flush_log_at_trx_commit';
# +--------------------------------+-------+
# | Variable_name                  | Value |
# +--------------------------------+-------+
# | innodb_flush_log_at_trx_commit | 1     |
# +--------------------------------+-------+
# 1 row in set (0.00 sec)
# установим сохранение журнала раз в секунду
#   mysql> SET GLOBAL 'innodb_flush_log_at_trx_commit' = 0;

# MVCC механизм транзакций использует
# не просто режим блокировки строк в дополнение
# к обычной блокировке,
# реализован механизм повышения степени конкурентности
# под названием многоверсионное управление конкурентным доступом
# механизм распространён среди реляционных БД

# мы упоминали фантомные и невоспроизводимые чтения
# если жёстко блокировать записи как на уровне SERIALIZABLE
# нам не избежать блокировок даже на операцию чтения
# механизм MVCC позволяет во многих случаях
# вообще отказаться от блокировок
# и способен значительно снизить накладные расходы
# идея механизма - создание мгновенных снимков состояния
# каждая транзакция читает данные
# из согласованного сниимка состояния
# т.е видит данные которые были зафиксированы в БД
# на момент начала транзакции
# даже если данные были затем изменены другой транзакцией
# каждая транзакция видит только старные данные
# по состоянию на конкретный момент времени
# выполняющая операции записи транзакций
# может блокировать выполнение другой транзакции
# записывающей тот же объект
# однако операция чтения не требует никаких блокировок
# чтение никогда не блокирует запись,
# а запись чтение
# БД способна выполнять длительные запросы на чтение
# продолжая в тоже время операции записи
# без какой либо конкуренции и блокировок между ними

# многоверсионное управление конкурентным доступом
# работают только на уровнях изоляции
# READ COMMITED , REPEATABLE READ

# СЕАНСОВЫЕ ИНСТРУМЕНТЫ mysql
# большенство сущностей которые рассмотрим
# живут только в рамках текущей сессии
# после закрытия соединений с сервером
# они удоляются.
# ПЕРЕМЕННЫЕ, ВРЕМЕННЫЕ ТАБЛИЦЫ и ДИНАМИЧЕСКИЕ ЗАПРОСЫ
# - пользовательские переменные
# - системные переменные
# - временные таблицы
# - динамические запросы

# часто результаты запросы
# необходимо использовать в дальнейших запросах
# для этого полученные данные необходимо сохранить
# во временных структурах.
# эту задачу решают переменные sql
#   mysql> SELECT @total := COUNT(*) FROM products;
# в следующих запросах мы получаем
# возможность обращаться к переменной
# переменная будет доступна только в текущей сессии
#   mysql> SELECT @total;
# если откроем новую консоль
# и попробуем обратиться к переменной @total;
# получим NULL
# мы не можем обратиться к переменной
# которую установил другой пользователь

# переменные можно использовать не только в SELECT списке
# но и например в WHERE условии.
# извлечём например товарную
# позицию с самой высокой ценой
#   mysql> SELECT @price := MAX(price) FROM products;
# сохроняем максимальную цену в переменную @price
# после этого можем использовать
# переменную в следующем запросе
#   mysql> SELECT * FROM products WHERE price = @price;
# воспользуемся модификатором \G
# для выводв в вертикальном режиме
#   mysql> SELECT * FROM products WHERE price = @price \G

# Если в качестве значений переменной
# передаётся имя столбца
# который содержит множество значений,
# то переменная получит полседнее значение
#   mysql> SELECT @id := id FROM products;
# итак мы присваиваем переменной значение первичного ключа
# из таблицы products
#   mysql> SELECT @id;
# переменной присвоилось последнее значение @id = 7
# она получает последнее значение из результирующей таблицы

# Имена переменных не чувствительны к регистру
#   mysql> SELECT @id, @ID;

# Переменные могут также объявляться с помощью оператора SET
#   mysql> SET @last = NOW() - INTERVAL 7 DAY;
#   mysql> SELECT @last;
# +---------------------+
# | @last               |
# +---------------------+
# | 2021-10-18 09:34:29 |
# +---------------------+
# 1 row in set (0.04 sec)

#   mysql> SELECT CURDATE(), @last;
# | CURDATE()  | @last               |
# +------------+---------------------+
# | 2021-10-25 | 2021-10-18 09:34:29 |
# +------------+---------------------+
# 1 row in set (0.03 sec)

# переменные можно использовать для нумерации записей таблицы
#   mysql> SELECT * FROM tbl1;
# +-------+
# | value |
# +-------+
# | fst1  |
# | fst2  |
# | fst3  |
# +-------+
# 3 rows in set (0.06 sec)
# имеется таблица с единственным столбцом
# без первичного ключа
# нам требуется при выводе таблицы пронумировать строки
# мы можем завести переменную @start
#   mysql> SET @start := 0;
# и инициализировать её нулевым значением
# затем мы можем увеличивать переменную на 1
# по мере вывода записей
#   mysql> SELECT @start := @start + 1 AS id, VALUE FROM tbl1;
# +------+-------+
# | id   | VALUE |
# +------+-------+
# |    1 | fst1  |
# |    2 | fst2  |
# |    3 | fst3  |
# +------+-------+
# 3 rows in set (0.05 sec)

# помимо пользовательских сервер mysql поддерживает
# СИСТЕМНЫЕ ПЕРЕМЕННЫЕ
# с помощью которых можно осуществлять его тонкую настройку
# и масштабирование
# полный список системных переменных:
#   mysql> SHOW VARIABLES;
#   mysql> SHOW VARIABLES\G

# оператор выводит большое количество системных переменных
# для того чтобы найти нужную перменную
# можно воспользоваться ключевым словом LIKE
# которое ведёт себя точно также как select запрос
# при помощи LIKE можно фильтровать выборку
#   mysql> SHOW VARIABLES LIKE 'read_buffer_size';
# +------------------+--------+
# | Variable_name    | Value  |
# +------------------+--------+
# | read_buffer_size | 131072 |
# +------------------+--------+
# 1 row in set (0.00 sec)

# Типы системных переменных
# - GLOBAL - глобальные (влияют на весь сервер)
# - SESSION - сеансовые (влияют на текущее соединение)

# при старте сервера происходит инициализация
# глобальных переменных значениями по умолчанию
# оператор SET позволяет изменять
# значения глобальных переменных
# уже после старта
#   mysql> SET GLOBAL read_buffer_size = 2097152;
#   mysql> SET @@global.read_buffer_size = 2097152;

# Помимо глобальных сервер поддерживает
# набор сеансовых переменных для каждого
# соединения клиента с сервером
# при установке соединений с сервером
# сеансовые переменные получают значения
# заданные для глобальных переменных
# клиент при помощи оператора SET
# может выставлять новые значения
#   mysql> SET SESSION read_buffer_size = 2097152;
#   mysql> SET @@session.read_buffer_size = 2097152;
# действие такой переменной будет отражаться
# только на текущем соединении
# не затранивая соседних клиентов

# чтобы установить локальной переменной значение глобальной
#   mysql> SET read_buffer_size = DEFAULT;

# ВРЕМЕННЫЕ ТАБЛИЦЫ
#   mysql> CREATE TEMPORARY TABLE table_name (
#       -> id SERIAL PRIMARY KEY,
#       -> name VARCHAR(255),
#       -> ...
#       -> );

# автоматически удаляются по завершению
# соединения с сервером
# а её имя действительно только
# в течении данного соединения
# 2 разных клента могут использовать временные таблицы
# с одинаковыми именами без конфликта друг с другом
# или существующей таблицы с тем же именем
# создание осуществляется с помощью ключевого слова
# CREATE TEMPORARY TABLE table_name
#   mysql> CREATE TEMPORARY TABLE temp (id INT, name VARCHAR(255));
#   mysql> SHOW TABLES;
# в списке временные таблицы отсутствуют
#   mysql> DESCRIBE temp;
# но можем запросить её структуру

# временные таблицы хронятся
# в специальном табличном пространстве ibtmp1
# -rw-r-----  1 mysql mysql 12582912 окт 24 11:32 ibtmp1

# ДИНАМИЧЕСКИЕ ЗАПРОСЫ
# ещё одна временная структура
# запросы которые пользователь подобно переменным
# может сохронять под конкретным именем
# и вызывать позже в течении сессии
#   mysql> PREPARE ver FROM 'SELECT VERSION()';
# выполняется такой запрос при помощи команды EXECUTE
#   mysql> EXECUTE ver;
# +-------------------------+
# | VERSION()               |
# +-------------------------+
# | 5.7.33-0ubuntu0.16.04.1 |
# +-------------------------+
# 1 row in set (0.00 sec)
# динамические запросы имеют время жизни
# только в течении текущего сеанса
# соединение с сервером закрыто - запрос перестал существовать

# Если необходимо чтобы запрос существовал более долгое время
# необходимо прибегнуть к пердставлению.
# динамические запросы можно параметризовать

# содадим динамический запрос, который извлекает
# товарные позиции только одного из разделов интернет магазина
#   mysql> PREPARE prd FROM 'SELECT id, name, price FROM products WHERE catalog_id = ?';
# вместо внешнего ключа catalog_id используется знак вопроса
# давайте зададим идентификатор раздела при помощи переменной
#   mysql> SET @catalog_id = 1;
# при вызове запроса при помощи операции EXECUTE
# следует передать значение параметра
# при помощи конструкции USING
#   mysql> EXECUTE prd USING @catalog_id;

# динамический запрос может иметь больше одного параметра
# перечисляются после ключевого слова USING
# через запятую в том же порядке как и в динамическом запросе.
# на такого рода запросы накладываются некторые ограничения
# не допускается использования вложенных динамических запросов
# а также нескольких запросов
# т.е динамический запрос - лишь один запрос
# параметр всегда передает строку
# т.е динамически задать имя таблице или столбцу не получится

# удалить динамический запрос
#   mysql> DROP PREPARE prd;

# ПРЕДСТАВЛЕНИЯ
# - создание представлений
# - вертикальные и горизонтальные представления
# - вставка записей в представление
# - обновление представлений
# - управление представлениями

# основные структурные единицы в реляционных БД - таблицы
# однако язык запросов sql - один из способов организации данных
# это представления
# представления - запрос на выборку, которому
# присваивается уникальное имя
# которые можно сохронять, удалять из БД
# как обычную таблицу.
# представления позволяют увидить
# результат сохранёного запроса таким образом
# как будто это полноценная таблица БД
# позволяют более гибко управлять правами доступа к таблицам
# также можно запретить прямое обращения пользователей
# и разрешить их только представлениям
# представления позволяют обеспечить обратную совместимость
# для программ ориентированных на старую структуру БД
# достатоно создать представление со структурой
# соответствующий старым таблицам

#   mysql> SELECT * FROM catalogs;
# создадим представление для таблицы catalogs
# в котором записи будут поддерживаться
# в отсортированном состоянии
#   mysql> CREATE VIEW cat AS SELECT * FROM catalogs ORDER BY name;
# для создания представления команда CREATE VIEW
# после которой указываем имя представления
# затем после ключевого слова AS
# пишем запрос представления
# к пердставлению можем обращаться как к обычной таблице
#   mysql> SELECT * FROM cat;

# представлления рассматриваются mysql как полноценная таблица
#   mysql> SHOW TABLES;
# представление будет в списке таблиц

# в полученном представлении мы использовали *
# поэтому представление принимает структуру таблицы catalogs.
# при создании представления можно явно указывать
# список столбцов даже изменять их названия и порядок следования
#   mysql> CREATE VIEW cat_reverse (catalog, catalog_id)
#       -> AS SELECT name, id FROM catalogs;
# обратимся к пердставлению
#   mysql> SELECT * FROM cat_reverse;
# мы изменили name на catalog, а id на catalog_id
# при этом порядок следования столбцов меняется на обратный

# при формировании списка столбцов
# задаются только имена столбцов
# тип данных, их размер и другие характеристики
# берутся из опрделения столбца исходной таблицы
# в качестве столбцов представлений могут выступать
# вычисляемые столбцы

# создадим представление name_cat, которая
# будет выводить столбцы id и name таблицы catalogs
# и дополнительно столбец total
# в который будем помещать количество символов
# в имени каталога
#   mysql> CREATE OR REPLACE VIEW name_cat (id, name, total)
#       -> AS SELECT id, name, LENGTH(name) FROM catalogs;
# CREATE OR REPLACE - чтобы заменить уже существующее представление
#   mysql> SELECT * FROM name_cat ORDER BY total DESC;

# АЛГОРИТМ ФОРМИРОВАНИЯ КОНЕЧНОГО ЗАПРОСА
# - MERGE запрос объединяется с представлением таким образом
# что представление заменяет собой
# соответствующие части в запросе
# - TEMPTABLE в результирующей таблице представлений
# помещается во временную таблицу,
# кторая потом используется в конечном запросе
# - UNDEFINED субд mysql пытается самостоятельно выбрать алгоритм
# если ни одно из значений алгоритма не указано
# по умолчанию используется UNDEFINED
#   mysql> CREATE ALGORITHM = TEMPTABLE VIEW cat2 AS SELECT * FROM catalogs;
# в созданном прдставлении мы требуем от mysql
# в каждом обращении к представлению
# создавать временную таблицу
#   mysql> DESCRIBE products;
# представления способны скрывать ряд столбцов
# за счёт того, что в SELECT запросе могут извлекаться
# не все столбцы таблицы
# такие представления называются вертикальными
# создадим такое представление для таблицы products
#   mysql> CREATE OR REPLACE VIEW prod AS
#       -> SELECT id, name, price, catalog_id
#       -> FROM products
#       -> ORDER BY catalog_id, name;
# мы выбираем только часть столбцов
# обратимся к таблице через данное представление
#   mysql> SELECT * FROM prod;
# в запросах к представлениям
# сами могут содержать условия WHERE
# и собственные сортировки.
# правильное составление конечного запроса
# к исходным таблиам это уже забота mysql
#   mysql> SELECT * FROM prod ORDER BY name DESC;
# воспользовались ключевым словом ORDER BY
# при образении к представлению
#   mysql> SELECT id, name, price, catalog_id FROM products;

# горизонтальные представления
# доступ пользователя к строкам таблицы
# в таких представлениях видим только те строки,
# с которыми они работают

# создадим представление, извлекающее из таблицы products
# только процессоры
#   mysql> CREATE OR REPLACE VIEW processors AS
#       -> SELECT id, name, price, catalog_id
#       -> FROM products
#       -> WHERE catalog_id = 1;
# извлекём результаты
#   mysql> SELECT * FROM processors;

# в реальной практике могут встречаться смешанные представления
# которые ограничивают таблицу и по горизонатли и по вертикале
# термины горизонтальные и вертикальные представления - условные понятия
# предназначены для того, чтобы лучше понять как из исходной таблицы
# формируется представление
#   mysql> SELECT * FROM tbl1;
# чтобы в представление можно было вставлять новые записи
# при помощи команды INSERT
# и обновлять существующие записи при помощи UPDATE
# необходимо при создании представлений
# использовать конструкцию IS CHECK OPTION
# во время вставки происходит проверка
# чтобы вставляемые данные удовлетворяли
# WHERE условию SELECT запроса лежащего
# в основе представления

# воспользуемся таблицей tbl1
# для создания обновляемго представления
#   mysql> CREATE VIEW v1 AS
#       -> SELECT * FROM tbl1 WHERE value < 'fst5'
#       -> WITH CHECK OPTION;
# попробуем вставить запись
#   mysql> INSERT INTO v1 VALUES ('fst4');
#   mysql> INSERT INTO v1 VALUES ('fst5');
# при попытке вставить значение 'fst5'
# срабатывает ограничение WHERE условия

# отредактировать представление можно при помощи команды ALTER
#   mysql> ALTER VIEW v1 AS
#       -> SELECT * FROM tbl1 WHERE value > 'fst4'
#       -> WITH CHECK OPTION;

# кроме того можно воспользоваться командой CREATE OR REPLACE VIEW
#   mysql> CREATE OR REPLACE VIEWv1 AS
#       -> SELECT * FROM tbl1 WHERE value > 'fst4'
#       -> WITH CHECK OPTION;
# эти 2 кманды эквивалентны

# для удаления представления команда DROP VIEW
#   mysql> DROP VIEW cat, cat_reverse, name_cat, prod, processors, v1;
# при попытке удаления несуществующего представления
# возникает ошибка
# DROP VIEW IF EXISTS для игнорирования попыток
# удаления несуществующих представлений

