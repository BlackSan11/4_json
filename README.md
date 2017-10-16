# Что делает?

В данном репозитории расположен скрипт, который на вход принимает путь до файла с произвольными данными в формате JSON и выводит его содержимое в консоль в удобном для чтения виде: добавляет переносы строк, отступы слева и пробелы. 

# Требования к окружению.

Скрипт запускается с помощью Python версии 3.x. 

# Как установить?

Просто произведите git clone репозитория на Ваш компьютер. 


# Как использовать?

Перейдите в папку с клонированым репозиторием, и с помощью командной строки запустите файл pprint_json.py с параметром path, где path это путь к Вашему файлу с JSON, пример:

пусть файл json.txt находится в одном каталоге с файлом pprint_json.py
содержимое файла json.txt: {"firstName": "Иван","lastName": "Иванов","address": {"streetAddress": "Московское ш., 101, кв.101","city":"Ленинград","postalCode": 101101},"phoneNumbers": ["812 123-1234","916 123-4567"]}

запускаем pprint_json.py и в качестве аргумента передаем путь к файлу json.txt

> python pprint_json.py json.txt

программа выведет нам следующий текст:

{
   "firstName": "Иван",
   "lastName": "Иванов",
   "address": {
       "streetAddress": "Московское ш., 101, кв.101",
       "city": "Ленинград",
       "postalCode": 101101
   },
   "phoneNumbers": [
       "812 123-1234",
       "916 123-4567"
   ]
}


# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
