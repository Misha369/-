# - С помощью данной программы можно шифровать любые тексты
# - Для начала обновим пакеты, это очень важно
$ apt update && apt upgrade
$ pkg update
$ pkg upgrade

# - Ставим git, благодаря нему мы сможем скачивать остальные утилиты 
$ apt install git
# - Теперь ставим язык программирования python.
$ apt install python && apt install python2
# - Теперь устанавливаем репозиторий
$ git clone https://github.com/Misha369/password
# - Запускаем программу
$ cd password
$ python kod.py
