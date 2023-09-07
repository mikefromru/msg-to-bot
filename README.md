# MSG-TO-BOT
Веб-сервис на базе Django и Django REST Framework для приема сообщений и отправки их в Telegram бот. Сервис доступен только для авторизованных пользователей. 
### Технологии
- Django
- Django REST Framework
###Функционал:
- Авторизация
- Регистрация
- Генерация токена для Телеграм бота
- Отправка сообщений своему боту. На сервере фиксировать: дату и тело
сообщения
- Получение списка всех сообщений: дата отправки, сообщение
### Начать
1. Клонировать репозиторий
```
git clone https://github.com/mikefromru/msg-to-bot.git
```
2. Прейти в папку с проектом
```
cd msg-to-bot
```
3. Переименовать файл `.env.EXAMPLE` в `.env` который находится в каталоге `project/project`
4. Переименовать файл `local_setting.EXAMPLE.py` в `local_settings.py` и установить свой  Телеграм токен а также chat_id в нём.

5. Создать и активировать виртуальное окружение
```
python3.11 -m venv venv
source venv/bin/activate
```
6. Перейти в папку где находится `manage.py` . Сделать миграции и запустить проект.
```
python manage.py migrate
python manage.py runserver
```
### Использование
- Зарегистрироваться `http://localhost:8000/api/v1/rest-auth/register/`
- Войти в систему и получить токен `http://localhost:8000/api/v1/rest-auth/login/`
- Для получения всех сообщений GET method `http://localhost:8000/api/v1/app/`
- Для загрузки и отправки сообщения в Телеграм бот POST method `http://localhost:8000/api/v1/app/`
