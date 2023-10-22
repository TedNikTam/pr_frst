import requests
import kaggle
import os
import pandas as pd
import json
import csv
import zipfile


#=========СОРТИРОВКА ПО ВВОДИМЫМ ДАННЫМ=============
# data = pd.read_csv('spotify-2023.csv', encoding='latin-1')
# print(data.columns)

# column_name = input("Введите название столбца: ")
# sort = input("Введите значение сортировки: ")

# print(column_name)
# print(sort)
# print(data[(data[column_name]!=2022)])

#=====================W_O_R_K=====================
# data = pd.read_csv('spotify-2023.csv', encoding='latin-1')
# print(data.columns)
# column_name_1 = input("Введите название столбца: ")
# column_name_2 = input("Введите название столбца: ")
# column_name_3 = input("Введите название столбца: ")
# print(data[(data[column_name_1]>2022) & (data[column_name_2]>2) & (data[column_name_3]>45)])

data = pd.read_csv('spotify-2023.csv', encoding='latin-1')
# a = list(data.columns)
# print(type(a))
# print(pd.Series(data.columns)) # вывод названия столбцов и их индексов
print(data.columns)

# df = pd.DataFrame(data)
# www = input('Введите название столбца: ')
# eee = input('Введите сортировочное значение: ')
# qqq = int(input('Введите ещё одно сортировочное значение: '))
# if eee == '>':
#     print (df.loc[df[f'{www}'] > qqq])
#     print(data[data[f'{www}'] > qqq])
# elif eee == '<':
#     print (df.loc[df[f'{www}'] < qqq])
#     print(data[data[f'{www}'] < qqq])
# elif eee == '==' or '=':
#     print (df.loc[df[f'{www}'] == qqq])
#     print(data[data[f'{www}'] == qqq])
# elif eee == '!=':
#     print (df.loc[df[f'{www}'] != qqq])
#     print(data[data[f'{www}'] != qqq])
# elif eee == '>=':
#     print (df.loc[df[f'{www}'] >= qqq])
#     print(data[data[f'{www}'] >= qqq])
# elif eee == '<=':
#     print (df.loc[df[f'{www}'] <= qqq])
#     print(data[data[f'{www}'] <= qqq])

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
            # if more_sort == 'y':
            #     print(data[b])
        print(data[a][b])
sort()


# else:
#     print('нет так нет')



# def column_name():
#     column_name = input("Введите название столбца: ")
#     # sort_sign = input('Введите знак сортировки: ')
#     # numerical_sort = int(input('Введите ещё одно сортировочное значение: '))
#     if column_name == '':
#         print(data)
#     else:
#         for i in data.columns:
#             if i == column_name:
#                 sort_sign = input("Введите знак сортировки: ")
#                 numerical_sort = int(input("Введите ещё одно сортировочное значение: "))
#                 more_sort = input("Добавить ещё один параметр сортировки? (y/n или да/нет): ")
#                 if more_sort == 'n':
#                     if sort_sign == '>':
#                         print(data[data[f'{column_name}'] > numerical_sort])
#                     elif sort_sign == '<':
#                         print(data[data[f'{column_name}'] < numerical_sort])
#                     elif sort_sign == '==' or '=':
#                         print(data[data[f'{column_name}'] == numerical_sort])
#                     elif sort_sign == '!=':
#                         print(data[data[f'{column_name}'] != numerical_sort])
#                     elif sort_sign == '>=':
#                         print(data[data[f'{column_name}'] >= numerical_sort])
#                     elif sort_sign == '<=':
#                         print(data[data[f'{column_name}'] <= numerical_sort])
#                 else:
#                     print('нет так нет')

#                     # column_name = input("Введите название ещё одного столбца столбца: ")
#                     # if column_name == '':
#                     #     print(data)
#                     # if sort_sign == '>':
#                     #     print(data[data[f'{column_name}'] > numerical_sort])
#                     # elif sort_sign == '<':
#                     #     print(data[data[f'{column_name}'] < numerical_sort])
#                     # elif sort_sign == '==' or '=':
#                     #     print(data[data[f'{column_name}'] == numerical_sort])
#                     # elif sort_sign == '!=':
#                     #     print(data[data[f'{column_name}'] != numerical_sort])
#                     # elif sort_sign == '>=':
#                     #     print(data[data[f'{column_name}'] >= numerical_sort])
#                     # elif sort_sign == '<=':
#                     #     print(data[data[f'{column_name}'] <= numerical_sort])
#                 # for o in data.columns:
#                 #     if o == column_name:
#                 #         if sort_sign == '==' or '=':
#                 #             print(data[data[f'{column_name}'] == numerical_sort & data[f'{o}'] == numerical_sort])
#                 #         break
# column_name()

#=================================================

# def column_name():
#     column_name = input("Введите название столбца: ")
#     if column_name == '':
#         print(data)
#     else:
#         for i in data.columns:
#             if i == column_name:
#                 column_name = input("Введите название ещё одного столбца столбца: ")
#                 if column_name == '':
#                     print(data[(data[i]==2018)])
#                 for o in data.columns:
#                     if o == column_name:
#                         column_name = input("Введите название ещё одного столбца столбца: ")
#                         print(data[(data[i]>2022) & (data[o]>3)])
#                         break
# column_name()
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