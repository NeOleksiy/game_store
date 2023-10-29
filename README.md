# Django интернет магазин
Учебный Pet-проект, интернет магазин для продажи игр.
Функционал: каталог игор с возможностью отбора по жанрам, страница с описанием и доп информацией,
регистрация через почту, тестовая версия оплаты stripe(Недоступна)
## Стек:
- **Django 4**
- **HTML/CSS + bootstrap**
- **PostgresSQL** - база данных
- **Redis** - Кэш и хранилище для Celery тасков
- **Celery** - Таск менеджер для email писем
- **Selenium** - Тестирование регистрации и авторизации
- **Stripe** - Платёжка(Больше не работет из-за недоступности в России)

## Как запустить:
 1. `git clone https://github.com/NeOleksiy/game_store.git`
 2. Через psql в терминале или через pgadmin создаём базу данных 
 3. Не забываем про .env куда вводим свои переменные окружении 
 4. В терминале `python3 -m venv env`
 5. В терминале `venv/bin/activate`
 6. В терминале `pip install -r requirements.txt`
 7. В терминале `./python3 manage.py ./game_store/fixtures migrate `
 8. В терминали `redis-server` 
 9. В терминале `./python3 manage.py runserver`
 - Для запуска тестов `./python3 manage.py test`
 

  
