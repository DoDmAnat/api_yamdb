# Проект «API YAMDB»

### Описание
«API YAMDB» - Совместный проект YaMDb собирает отзывы пользователей на произведения.

### Использумые технологии

[Python 3.7](https://docs.python.org/3.7/whatsnew/3.7.html)

[Django 2.2.16](https://docs.djangoproject.com/en/4.1/releases/2.2.16/)

[DjangoRestFramework 3.12.4](https://www.django-rest-framework.org/community/release-notes/)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:DoDmAnat/api_yamdb.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры запросов к API
###  Регистрация пользователя
```
POST /api/v1/auth/signup/
{
  "email": "string",
  "username": "string"
}
```
###  Получение JWT-токена:
```
POST /api/v1/auth/token/
{
  "username": "string",
  "confirmation_code": "string"
}
```
###  Добавление категории:
```
POST /api/v1/categories/
{
  "name": "string",
  "slug": "string"
}
```
###  Удаление категории:
```
DELETE /api/v1/categories/{slug}/
```
###  Добавление произведения:
```
POST /api/v1/titles/
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```

### Полная документация по эндпоинту /redoc/

Авторы:

[Домрачев Дмитрий](https://github.com/DoDmAnat)

[Латыпов Юлиян](https://github.com/remark-ekz)

[Шакиржанов Надим](https://github.com/Nadim1309)
