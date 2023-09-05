# [Тестовое задание](task.pdf) Python Django Rest Framework

## Описание:

Был разработан API для представления структуры компании, присутствует:

1. Набор API методов для работы с данными по сотрудникам и департаментам.
2. Swagger документация(http://localhost/swagger/).
3. Админка по модели данных.
4. Реализована авторизация.
5. Присутствует пагинация.

[Более подробно про тз в файле](task.pdf)

## API endpoints департаменты

1. **GET api/v1/departments/** - Возвращает список всех департаментов.
2. **POST api/v1/departments/** - Позволяет создать новый, несуществующий департамент.
3. **GET api/v1/departments/{id}/** - Возвращает департамент по заданному id.
4. **PUT or PATH api/v1/departments/{id}/** -Позволяет изменить данные департамента.
5. **DELETE api/v1/departments/{id}/** - Позволяет удалить департамент.
6. **GET api/v1/departments/{id}/employees/** - Возвращает список сотрудников указанного департамента, НУЖНА
   АВТОРИЗАЦИЯ!

## API endpoints сотрудники

ДЛЯ ДОСТУПА НЕОБХОДИМА АВТОРИЗАЦИЯ.

1. **GET api/v1/employees/** - Возвращает список всех сотрудников.
2. **POST api/v1/employees/** - Позволяет создать нового сотрудника.
3. **GET api/v1/employees/{id}** - Возвращает конкретного сотрудника по заданному id.
4. **PUT or PATH api/v1/employees/{id}** -Позволяет изменить данные сотрудника.
5. **DELETE api/v1/employees/{id}** - Позволяет удалить сотрудника.

## Авторизация:

Так как по тз необходимо было сделать аутентификацию, для того чтобы получить доступ к
некоторым endpoints, которые отмечены соответствующим образом, необходимо добавить заголовок:

        Authorization: Token токен_авторизации

Для того чтобы получить этот токен, необходимо создать superuser:

         python manage.py createsuperuser

А затем:

         python manage.py drf_create_token имя_пользователя

## Запуск через Docker:

      docker build -t test_drf .
      docker run -d -p 8080:8000 django_drf

## Локальный запуск:

1. Устанавливаем все зависимости:

        pip install requirements.txt -r
        python manage.py makemigrations
        python manage.py migrate


2. Запускаем приложение:

        python manage.py runserver


