# Создайте любую программу.py при помощи виртуального окружения и PIP. 
# отправте репозиторий где будет этот файл и файл requirements.txt

import statistics as stat

data = (input('Введите список чисел для расчета моды '))
data1 = list(data.split(','))

# Вывод моды
print(stat.mode(data1)) 
