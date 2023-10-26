import requests
import kaggle
import os
import pandas as pd
import json
import csv
import zipfile

def sort_1():
    a = ''
    column_name = input("Введите название столбца: ")
    print(data.dtypes[column_name])  # тип данных в таблице может быть разным
    sort_sign = input("Введите знак сортировки: ")
    if data.dtypes[column_name] == 'int64': #
        numerical_sort = int(input("Введите ещё одно сортировочное значение: "))
    else:
        numerical_sort = input("Введите ещё одно сортировочное значение: ")
    more_sort = input("Добавить ещё один параметр сортировки? (y/n или да/нет): ")
    if sort_sign == '>':
        a = (data[(data[f'{column_name}'] > numerical_sort)])
    elif sort_sign == '<':
        a = (data[(data[f'{column_name}'] < numerical_sort)])
    elif sort_sign == '==' or '=':
        a = (data[(data[f'{column_name}'] == numerical_sort)])
    elif sort_sign == '!=':
        a = (data[(data[f'{column_name}'] != numerical_sort)])
    elif sort_sign == '>=':
        a = (data[(data[f'{column_name}'] >= numerical_sort)])
    elif sort_sign == '<=':
        a = (data[(data[f'{column_name}'] <= numerical_sort)])
        
    df = pd.DataFrame(a)
    df.to_csv('new_data.csv', index=False)
    
    def sort_2():
        data = pd.read_csv('new_data.csv', encoding='latin-1')
        a = ''
        column_name = input("Введите название столбца: ")
        print(data.dtypes[column_name])  # тип данных в таблице может быть разным
        sort_sign = input("Введите знак сортировки: ")
        if data.dtypes[column_name] == 'int64':
            numerical_sort = int(input("Введите ещё одно сортировочное значение: "))
        else:
            numerical_sort = input("Введите ещё одно сортировочное значение: ")
        more_sort = input("Добавить ещё один параметр сортировки? (y/n или да/нет): ")
        
        if sort_sign == '>':
            a = (data[(data[f'{column_name}'] > numerical_sort)])
        elif sort_sign == '<':
            a = (data[(data[f'{column_name}'] < numerical_sort)])
        elif sort_sign == '==' or '=':
            a = (data[(data[f'{column_name}'] == numerical_sort)])
        elif sort_sign == '!=':
            a = (data[(data[f'{column_name}'] != numerical_sort)])
        elif sort_sign == '>=':
            a = (data[(data[f'{column_name}'] >= numerical_sort)])
        elif sort_sign == '<=':
            a = (data[(data[f'{column_name}'] <= numerical_sort)])
        
        df = pd.DataFrame(a)
        df.to_csv('new_data.csv', index=False)
        
        if more_sort == 'y':
            sort_2()
        elif more_sort == 'n':
            print(a)
            os.remove('new_data.csv')
    
    if more_sort == 'y':
        sort_2()
    elif more_sort == 'n':
        print(a)
        # os.remove('new_data.csv')
        

#=========СКАЧИВАНИЕ CSV-ФАЙЛА, ПОЛУЧЕНИЕ ИНФОРМАЦИИ, УДАЛЕНИЕ==========
# obj_adress = ("gauravduttakiit/media-campaign-cost-prediction") # адрес для скачивания 
obj_adress = ("sahityasetu/crime-data-in-los-angeles-2020-to-present") # адрес для скачивания 
obj_dwnld = os.system(f'kaggle datasets download -d {obj_adress}') # скачивание файла
file = (str(obj_adress.split('/')[1]) +'.zip') # формирование названия zip-файла
f_zip = zipfile.ZipFile(file, 'r') # zip-файл открывается на чтение
f_zip.extractall('./') # извлекается содержимое zip-файла
for file_info in f_zip.infolist(): # запускается цикл по чтению содержимого zip-файла
    p = file_info.filename
    data = pd.read_csv(file_info.filename, encoding='latin-1')
    print(
        "\nНазвание файла: ", file_info.filename,
        "\nИнформация о колонках в файле: ", data.columns,
        "\nКол-во строк и столбцов: ", data.shape,
        )
    sort_1()
    os.remove(p) # после получения информации файл удаляется
f_zip.close() # zip-файл закрывается
os.remove(file) # zip-файл удаляется
print(f"="*35 + "\nФайлы удалены!")
#=============================================================================





# data = pd.read_csv('spotify-2023.csv', encoding='latin-1') # encoding='latin-1'- дал возможность читать файл скодировкой UTF-8
# print(data.take([12,99])) # показывает выбранные номера строк
# print(data.take(range(12,99))) # показывает выбранный интервал
# print(p)
# print(data[:10])
# print(data.columns) # названия столбцов
# print(data.shape) #кол-во строк и столбцов
# print(data['artist(s)_name'][:5])
# print(data.loc[1]) # выводит данные по номеру строки
# print(data.loc[[1, 2]]) # выводит данные по номеру более одной строки
# print(data.index.get_loc("Olivia Rodrigo"))
# print(data[data['acousticness_%']>=55]) # выводит данные столбцов отсортированные по значению
# print(data[(data['acousticness_%']>=55) & (data['liveness_%']>=25)][:10]) # выводит данные столбцов отсортированные по  2м значениям