import requests
import kaggle
import os
import pandas as pd
import json
import csv
import zipfile

data = pd.read_csv('spotify-2023.csv', encoding='latin-1')
print(data.columns)

def sort_1():
    a = ''
    column_name = input("Введите название столбца: ")
    sort_sign = input("Введите знак сортировки: ")
    numerical_sort = int(input("Введите ещё одно сортировочное значение: "))
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
        
        sort_1()
    
    if more_sort == 'y':
        sort_2()
    elif more_sort == 'n':
        print(a)
        os.remove('new_data.csv')
        
sort_1()



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