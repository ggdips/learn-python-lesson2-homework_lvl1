#!env/bin/python3
import csv
"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
mydict = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
    {'name': 'Пётр', 'age': 40, 'job': 'CTO'},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

def main():
    mydictkeys = mydict[0].keys()
    expfile = open('export.csv', 'w', encoding='utf-8')
    dict_writer = csv.DictWriter(expfile, mydictkeys)
    dict_writer.writeheader()
    dict_writer.writerows(mydict)
    expfile.close()


if __name__ == "__main__":
    main()
