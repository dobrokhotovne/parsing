# PARSING COURSE PROJECT
Описание проекта:
Программа по сбору данных с сайта kinometro.ru за период, заданный пользователем.
Может быть использована в работе сотрудниками рекламных агенств при планирования рекламных кампаний в разрезе конкурентного анализа по уже прошедшим релизам. 
Собранная информация позволяет проводить анализ помесячных релизов в рамках запрошенного периода по различным параметрам (Кинокомпании, Кассовые сборы, Страны выпуска, Жанры и др.)

# Принцип работы:
1. Пользователь задает количество необходимых периодов.
2. Для каждого периода пользователь задает месяц и год, за который необходимо получить информацию.

Программа проходится по всем периодам и собирает информацию о каждом выходившем в этом периоде фильме.
Также программа скачивает обложки фильмов.
После сбора информации она загружается в базу данных MongoDB

# Необходимые модули:
scrapy - сам парсер
(pip install scrapy)

pymongo - необходим для работы с базой данных MongoDB
(pip install pymongo)

pillow - обязателен для скачивания изображений
(pip install pillow)
