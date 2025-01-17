# Написание вашего первого приложения на Django, часть 1 #

Давайте учиться на примере.

В этом уроке мы расскажем о создании базового приложения 'Hello, World'.

Мы предполагаем, что вы уже установили Django. Вы можете узнать, установлена ли Django и какая версия, выполнив в командной строке следующую команду (указывается префиксом $):

```cmd
$ python -m django --version
```
Если фреймворк Django установлен, вы увидите номер версии. Если нет, вы получите сообщение об ошибке «Нет модуля с именем django».

Этот учебник написан для Django 4.1, который поддерживает Python 3.8 и более поздние версии. 

## Создание проекта ##
Если вы раньше Django не использовали, то необходимо позаботиться о начальной настройке. А именно, необходимо автоматически сгенерировать определенный код, который устанавливает Django project — набор настроек для конкретного экземпляра Django, включающий в себя конфигурацию базы данных, специфичные для Django опции специфичные настройки для приложения.

Выполните в терминале в командной строке смену каталога на тот, в котором вы сохранили код
```cmd
$ cd  myproject
```
затем запустите следующую команду:
```cmd
$ django-admin startproject mysite
```
Это создание пустого проекта на основе Django. Для этого открываем терминал и обращаемся к такой команде как django-admin, мы обращаемся к django-admin и говорим что нужно сделать: мы хотим создать новый проект поэтому обращаемся ещё к команде startproject и дальше мы должны назвать свой проект. Назвать проект можно как угодно, но без использования специальных символов. 
Это создаст каталог mysite в текущем каталоге. Если этого не произошло, то смотрите Проблемы с запуском django-admin.

Давайте посмотрим на результат выполнения команды startproject:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
Разберем, для чего нужны эти файлы и каталоги:

- Внешний корневой каталог mysite/ — это контейнер для вашего проекта. Его имя не имеет значения для Джанго; Вы можете переименовать его на что угодно.
- manage.py: утилита, позволяющая взаимодействовать с проектом различными способами. Вы можете прочитать все подробности о manage.py в django-admin и manage.py.
- Внутренний каталог mysite/ это Python модуль вашего проекта. Его название вы будете использовать для импорта чего-либо из этого модуля (например, mysite.urls).
- mysite/__init__.py: пустой файл, который сообщает Python, что этот каталог должен рассматриваться как пакет Python’а. Если вы новичок в Python, прочитайте больше о пакетах в официальной документации Python.
- mysite/settings.py: Конфигурация и настройки проекта Django. В Настройки Django рассказано все о том, как работают настройки.
- mysite/urls.py: указание URL проекта на Django, можно сказать, что это «оглавление» вашего проекта. Прочитайте больше информации о URL в Диспетчер URL.
- mysite/asgi.py: точка входа для ASGI-совместимых веб-серверов для обслуживания вашего проекта. Смотрите Как развертывать с помощью ASGI для получения более подробной информации.
- mysite/wsgi.py: Точка входа для WSGI совместимых веб-серверов для работы с проектом. Смотрите Как развертывать с помощью WSGI для уточнения деталей работы.
### manage.py ###
Файл с которым придётся часто работать. Конкретно с кодом этого файла работать не будем, но часто через терминал будем обращаться именно к этому файлу. При помощи этого файла можно запустить локальный сервер, можем создать какие нибудь файлы, провести какие нибудь миграции. Через этот файл создаются новые файлы, запускается локальный сервер. 
### Внутренний каталог mysite/ ###
Папка, которая называется как название самого джанго проекта (внешний корневой каталог). Внутри этой папки находятся те основные файлы, которые служат для полного описания нашего проекта. 
### mysite/__init__.py ###
В будущем в этот файл будем дописывать какие либо характеристики, которые должну будут быть обработаны при запуске самого проекта. 
### mysite/asgi.py, mysite/wsgi.py ###
Оба файла обеспечивают корректное подключение к серверу. asgi более новый стандарт, wsgi более старый. С этими файлами можно работать лишь косвенно. Код в этих файлах практически никогда не меняятся. При выгрузке сайта на удалённый сервер, именно эти файлы и эти технологии у нас происходит выгрузка сайта. С этими файлами мы не работаем, не работаем в плане кода, но эти файлы нужны и без этих файлов не будет корректно настроена работа с сервером. 
### mysite/settings.py ###
Очень важный файл в котором описываются все глобальные настройки для джанго проекта. Какие в этом файле есть переменные? 
```Go
BASE_DIR = Path(__file__).resolve().parent.parent
```
описывает полный путь к нашему проекту. Будь проект на сервере или на локальном компьютере. В эту переменную записывается полный путь к нашему проекту. 
```Go
SECRET_KEY = "django-insecure-8t8n!5zeo3h#=s_96(k-s#!q^e-3d8m(3q88c7a0-t5s@j*654"
```
переменная SECRET_KEY хронит секретный ключ нашего приложения. Доступ к этому ключу поможет взломать сайт. и затем что то делать с сайтом. Перед выгрузкой сайта на сервер лучше этот ключ поменять на что либо другое, сгенерировать новый. 
```Go
DEBUG = True
```
Все ошибки которые могут возникать . они будут показаны прямиком на страничках вебсайта. т.к установленно значение TRUE. При выгрузке сайта на сервер лучше будет значение поменять на FALSE. Конечному пользователю ошибки видить не обязательно и не нужно. 
```Go
ALLOWED_HOSTS = []
```
Можем указать те хосты, домены, имена на которых нам будет разрешено опубликовать данный вебсайт, написанный на джанго. Сейчас проект нигде не публикуем, поэтому пока пустой список.  Если захотим опубликовать на сайте, то указываем адрес сайта. ALLOWED_HOSTS = ["https://yandex.ru"]. 
```Go
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```
список хронит набор всех тех установленных приложений, которые сейчас есть в нашем проекте. это различные встроенные проекты, приложения. Например панель администратора обеспечивает приложение "django.contrib.admin". Эти приложения обеспечивают тот или иной функционал. Также сюда будем добавлять новые приложения, которые понадобятся и доустановятся в ходе разработки проекта. 
```Go 
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
```
В этом списке находится различное промежуточное ПО. Можем их считать плагинами, библиотеками, которые обеспечивают различный функционал внутри нашего проекта. 
безопасность django.middleware.security.SecurityMiddleware" , работа с сессиями "django.contrib.sessions.middleware.SessionMiddleware" ...
```Go
ROOT_URLCONF = "mysite.urls"
```
В переменной указывается какой основной файл урл будет использоваться для всего проекта. "mysite.urls" здесь сказано основной файл urls находится в папке mysite. 
```Go
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```
Указывается какие шаблоны можно использовать внутри нашего проекта. 
```Go
WSGI_APPLICATION = "mysite.wsgi.application"
```
указание что мы используем файл wsgi. При помощи этой технологии мы сможем выгрузить сайт на сервер. Главное что есть эта переменная указывающая на данный файл.
```Go
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```
указывается с какой базой данных мы работаем. Указано по умалчанию работа с db.sqlite3. Она предустановлена по умолчанию. можно менять на ту с которой будет работа. 
```Go
LANGUAGE_CODE = "en-us"
```
позволяет менять язык приложения
```Go
TIME_ZONE = "UTC"
```
временная зона приложения

- В ходе работы над проектом в этот файл будут вноситься новые переменные, которые будут обеспечивать дополнительный функционал,  будут меняться существующие базовые настройки. Важный файл описывающий все глобальные настройки внутри нашего джанго проекта. 
 
### mysite/urls.py ###
```Go
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('helworld/', include('helworld.urls')),
    path("admin/", admin.site.urls),
]
```
Внутри этого файла мы отслеживаем различные урл адреса. В базовом пустом проекте лишь один адрес указан  path("admin/", admin.site.urls). При переходе по такому урл адресу, как "admin/" у нас будет открываться приложение, которое называется admin (admin.site.urls), то.есть у нас будет открываться панель администратора при переходе по этому урл.  Панель администратора по умалчанию установлена в любом джангопроекте.  Здесь в этом файле urls.py мы добавляем адреса страниц, адреса шаблонов страниц. 

## Сервер разработки ##

Давайте проверим, работает ли ваш проект Django. Перейдите во внешний каталог mysite, если вы этого еще не сделали, и выполните следующие команды:

```cmd
$ python manage.py runserver
```
Мы обращаемся к python и с помощью пайтона обращаемся к файлу manage.py, а дальше мы говорим какую команду мы хотим выполнить: runserver это запуск локального сервера.
Вы увидите следующий вывод в командной строке:
```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

сентября 29, 2022 - 15:50:53
Django version 4.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Примечание

Пока игнорируйте предупреждение о непримененных миграциях базы данных; мы разберемся с базой данных в ближайшее время.

Вы запустили сервер разработки Django - легкий веб-сервер, написанный исключительно на Python. Мы включили его в Django, чтобы вы могли быстро разрабатывать вещи, не занимаясь настройкой производственного сервера - такого как Apache - до тех пор, пока вы не будете готовы к производству.

Сейчас самое время отметить: не используйте этот сервер в чем-либо, напоминающем производственную среду. Он предназначен только для использования во время разработки. (Мы занимаемся созданием веб-фреймворков, а не веб-серверов).

Теперь, когда сервер запущен, зайдите на сайт http://127.0.0.1:8000/ с помощью веб-браузера. Вы увидите страницу «Поздравляем!» с взлетающей ракетой. Все получилось!

### ВЫХОД ИЗ ЛОКАЛЬНОГО СЕРВЕРА ###
Для того, чтобы выйти из локального сервера в терминале комбинация клавиш СTRL + C
```cmd
CTRL + C
```
выполняется остановка какого либо процесса в нашем случае остановка локального сервера. 

### Смена порта ###

По умолчанию команда runserver запускает сервер разработки на внутреннем IP адресе с портом 8000.

Для смены порта передайте его аргументом в командной строке. Например, эта команда запускает сервер на порту 8080:

```
$ python manage.py runserver 8080
```
Для изменения IP адреса сервера, передайте его вместе с портом. Например, чтобы использовать все доступные публичные IP-адреса (что полезно, если вы работаете с Vagrant или хотите показать свою работу на других компьютерах в сети), используйте:

```
$ python manage.py runserver 0:8000
```
0 это сокращение для 0.0.0.0. Полная документация по серверу разработки находится в руководстве runserver.

### Автоматическая перезагрузка runserver ###

Сервер разработки автоматически перезагружает код Python для каждого запроса по мере необходимости. Вам не нужно перезагружать сервер, чтобы изменения в коде вступили в силу. Однако некоторые действия, такие как добавление файлов, в эти условия не входят, поэтому вам придется перезапустить сервер в этих случаях.

## Создание приложения helloworld ##
Теперь, когда ваше окружение - «проект» - настроено, вы можете приступить к дальнейшей работе.

Каждое приложение, которое вы пишете в Django, состоит из пакета Python, который следует определенному соглашению. Django поставляется с утилитой, которая автоматически генерирует базовую структуру каталогов приложения, поэтому вы можете сосредоточиться на написании кода, а не на создании каталогов.

### Проекты и приложения ###

В чем разница между проектом и приложением? Приложение - это веб-приложение, которое что-то делает - например, система блогов, база данных публичных записей или небольшое приложение для проведения опросов. Проект - это набор конфигураций и приложений для определенного веб-сайта. Проект может содержать несколько приложений. Приложение может находиться в нескольких проектах.

Ваши приложения могут находиться где угодно в вашем пути Python. В этом руководстве мы создадим наше приложение для опроса в том же каталоге, что и ваш файл manage.py, чтобы его можно было импортировать как отдельный модуль верхнего уровня, а не как подмодуль mysite.

Чтобы создать приложение, убедитесь, что вы находитесь в том же каталоге, что и manage.py, и введите следующую команду:

```cmd
$ python manage.py startapp helloworld
```
Это создаст каталог helloworld, который выглядит так:
```
helloworld/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
В этой структуре каталогов будет размещено приложение.

## Написание первого отображения ##
Давайте напишем первое представление (view). Откройте файл helloworld/views.py и вставьте в него следующий код Python:
```Python
helloworld/views.py
___________________
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")
```   
Это самое простое представление, возможное в Django. Чтобы вызвать представление, нам нужно сопоставить его с URL - и для этого нам нужен URLconf.

Чтобы создать URLconf в каталоге helloworld/, создайте файл с именем urls.py. Ваш каталог с приложением должен выглядеть примерно так:
```
helloworld/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```
В файл helloworld/urls.py добавьте следующий код:
```Python
helloworld/urls.py
__________________
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
Следующим шагом является указание корневого URLconf на модуль helloworld.urls. В mysite/urls.py добавьте импорт django.urls.include и вставьте include() в список 'urlpatterns', у вас должно получиться так:
```Python
mysite/urls.py
__________________
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('helloworld/', include('helloworld.urls')),
    path('admin/', admin.site.urls),
]
```
Функция include() позволяет ссылаться на другие URLconfs. Всякий раз, когда Django встречает include(), он отсекает любую часть URL-адреса, совпадающую с этой точкой, и отправляет оставшуюся строку во включенный URLconf для дальнейшей обработки.

Идея, стоящая за include(), состоит в том, чтобы упростить добавление и воспроизведение URL-адресов. Так как опросы находятся в их собственном URLconf(helloworld/urls.py), их можно поместить в «/helloworld/», или в «/fun_helloworld/», или в «/content/helloworld/», или по любому другому корневому пути, и приложение все равно будет работать.

Когда использовать include()

Вы всегда должны использовать include() при включении других шаблонов URL. admin.site.urls - единственное исключение из этого.

Теперь вы подключили представление index к URLconf. Убедитесь, что он работает с помощью следующей команды:

```
$ python manage.py runserver
```
Перейдя в браузере по адресу http://localhost:8000/polls/, вы должны увидеть текст «Hello, World.», который вы определили в представлении index.

Функция path() передает четыре аргумента, два обязательных: route и view, и два необязательных: kwargs и name. На данный момент стоит рассмотреть, для чего эти аргументы.

- path(), аргумент route¶
- route - строка, содержащая шаблон URL. При обработке запроса Django начинается с первого шаблона в urlpatterns и пробирается вниз по списку, сравнивая запрошенный URL с каждым шаблоном, пока не найдет тот, который соответствует.

Шаблоны не выполняют поиск параметров GET и POST или имени домена. Например, в запросе к https://www.example.com/myapp/, URLconf будет искать myapp/. В запросе к https://www.example.com/myapp/?Page=3, URLconf также будет искать только myapp/.

#### path(), аргумент view ####
Когда Django находит соответствующий шаблон, он вызывает указанную функцию представления с объектом HttpRequest в качестве первого аргумента и любые «захваченные» значения из маршрута в качестве аргументов ключевого слова. Мы приведем пример этого чуть позже.

#### path(), аргумент kwargs ####
Произвольные ключевые аргументы могут быть переданы в словаре в целевое представление. Мы не собираемся использовать эту функцию Django в этом уроке.

#### path(), аргумент name ####
Присвоение имени URL-адресу позволяет вам однозначно ссылаться на него из других мест Django, особенно из шаблонов. Эта мощная функция позволяет вам вносить глобальные изменения в шаблоны URL вашего проекта, касаясь только одного файла.

Когда вы освоитесь с основами запросов и ответов, прочитайте вторую часть этого руководства, чтобы начать работу с базой данных.
