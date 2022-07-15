Книжный каталог [v.1.0]
=========================

Проект позволяет размещать книжную продукцию и оформлять заказ. 
- v1.0 - Каталог, ссылки, пагинация, оставить запрос на оформление заказа
- v2 - Корзина покупок, личная страница пользователя (в разработке)

## Установка

Клонируйте проект
```sh
cd dev
mkdir book-catalog
git clone git@github.com:imsemin/book-catalog.git
```

Установите виртуальное окружение и зависимости

```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Выполните миграции и создайте суперпользователя

```sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py creatersuperuser
```

Запустите сервер разработчика
```sh
python3 manage.py runserver
```
### Authors

backend - Evgeniy Semin
frontend - Nikolay Saprikin
