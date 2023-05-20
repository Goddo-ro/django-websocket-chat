# Soft -  django websocket chat

# Установка и запуск

Клонируйте репозиторий
```bash
git clone https://github.com/Yakser/django-websocket-chat
```
Перед установкой зависимостей необходимо скачать [C++ Build Tools](https://stackoverflow.com/questions/40504552/how-to-install-visual-c-build-tools) Они нужны для сборки некоторых библиотек.

# Установка зависимостей

В папке проекта (`/django-websocket-chat/`) выполните команду:
```
pip install -r requirements.txt
```

#  Redis

## Linux/Mac OS

Скачайте [Redis](https://redis.io) и запустите его

## Windows
- Установите [WSL2](https://docs.microsoft.com/ru-ru/windows/wsl/install)
- В WSL установите  `redis-server`:

```bash
sudo apt-add-repository ppa:redislabs/redis
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install redis-server
```

Запустите `redis-sever`:
```bash
sudo service redis-server start
```

# Запуск 
Сделайте и заполните файл `.env` в соответствии с `.env.example`

Перейдите в директорию django-проекта:
```shell
cd chat
```

Запустите приложение командой

```shell
python manage.py runserver
```

# Технические детали
- Python 3.10.4 
- Django 3.2.13
- БД: SQLite
- Библиотека для работы с вебсокетами: channels 3.0.4 
- CSS препроцессор: SCSS

# Изображения

![photo_2023-05-20_21-08-38](https://github.com/Goddo-ro/django-websocket-chat/assets/98981618/ec6a1c12-312f-4bf9-95da-6df6356eed9a)
![photo_2023-05-20_21-10-30](https://github.com/Goddo-ro/django-websocket-chat/assets/98981618/4d834e46-3fd1-405d-a2f6-70d27832835b)
![photo_2023-05-20_21-11-36](https://github.com/Goddo-ro/django-websocket-chat/assets/98981618/a8b2bd79-f553-4278-8e84-fab3d7e23160)
![photo_2023-05-20_21-16-00](https://github.com/Goddo-ro/django-websocket-chat/assets/98981618/4e85e89e-8834-4f71-8843-c146a920ad2a)
![photo_2023-05-20_21-16-09](https://github.com/Goddo-ro/django-websocket-chat/assets/98981618/d667ddbf-bc9b-4a56-9541-7b2dace6a874)
