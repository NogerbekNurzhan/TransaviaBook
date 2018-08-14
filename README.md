# Краткое описание

В тестовом проекте `TransaviaBook` есть приложение `book`. В ней описана модель данных `Book` c двумя полями: `id` и `text`.

API состоит из двух запросов:

1) GET запрос. Возвращает список всех книг.

   URL: `http://127.0.0.1:8000/api/book/`

2) POST запрос. На вход принимает массивы pieces и cutouts. Тип элементов в данных массивах является string. На выходе получаем текста книг в которых содержатся все элементы массива pieces, но вырезаны все слова, которые содержат в себе хоть один из элементов массива cutouts.

   URL: `http://127.0.0.1:8000/api/book/filter/`

# Запуск проекта
1) Создать виртуальное окружение. В зависимости от операционной системы команды могут немного отличаться. К примеру в UNIX-подобных операционных систем virtualenv можно создать следующим способом:

    `python -m venv transavia_book_venv`
    
2) Запустить виртуальное окружение:
   
   `source transavia_book_venv/bin/activate`

3) Установить все пакеты в виртуальное окружение:

   `pip install requirements.txt`

4) Запустить проект:

   `python manage.py runserver`

# Результаты

Для тестирования API использовался инструмент [POSTMAN](https://www.getpostman.com/).

Результат GET запроса:

![](https://github.com/NogerbekNurzhan/TransaviaBook/blob/master/screenshots/1.png)

Результат POST запроса:

![](https://github.com/NogerbekNurzhan/TransaviaBook/blob/master/screenshots/2.png)

Также тестировать API можно в терминале. К примеру для POST запроса можно применить следующую команду:

```
curl -d '{"pieces": ["ша", "ар"], "cutouts": ["бу", "ки"]}' -H "Content-Type: application/json" -X POST 127.0.0.1:8000/api/book/filter/
```
