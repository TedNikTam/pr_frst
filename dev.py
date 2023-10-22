import requests
import kaggle
import os
import pandas as pd
import json
import csv
import zipfile

#=================================СОРТИРОВКА ПО ВВОДИМЫМ ДАННЫМ===============================

#===========================================W_O_R_K===========================================
data = pd.read_csv('spotify-2023.csv', encoding='latin-1')
# print(pd.Series(data.columns)) # вывод названия столбцов и их индексов
print(data.columns)

column_name = input("Введите название столбца: ")
sort_sign = input("Введите знак сортировки: ")
numerical_sort = int(input("Введите ещё одно сортировочное значение: "))
more_sort = input("Добавить ещё один параметр сортировки? (y/n или да/нет): ")

def sort():
    a = ''
    b = ''
    if sort_sign == '>':
        a = (data[f'{column_name}'] > numerical_sort)
    elif sort_sign == '<':
        a = (data[f'{column_name}'] < numerical_sort)
    elif sort_sign == '==' or '=':
        a = (data[f'{column_name}'] == numerical_sort)
    elif sort_sign == '!=':
        a = (data[f'{column_name}'] != numerical_sort)
    elif sort_sign == '>=':
        a = (data[f'{column_name}'] >= numerical_sort)
    elif sort_sign == '<=':
        a = (data[f'{column_name}'] <= numerical_sort)
        
    if more_sort == 'n':
        print(data[a])
    elif more_sort == 'y':
        column_name1 = input("Введите название 2го столбца: ")
        sort_sign1 = input("Введите знак сортировки: ")
        numerical_sort1 = int(input("Введите ещё одно сортировочное значение: "))
        if sort_sign1 == '>':
            b = (data[f'{column_name1}'] > numerical_sort1)
        elif sort_sign1 == '<':
            b = (data[f'{column_name1}'] < numerical_sort1)
        elif sort_sign1 == '==' or '=':
            b = (data[f'{column_name1}'] == numerical_sort1)
        elif sort_sign1 == '!=':
            b = (data[f'{column_name1}'] != numerical_sort1)
        elif sort_sign1 == '>=':
            b = (data[f'{column_name1}'] >= numerical_sort1)
        elif sort_sign1 == '<=':
            b = (data[f'{column_name1}'] <= numerical_sort1)
        print(data[a][b])
sort()

#=================================================

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