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
print(data)


def column_name():
    column_name = input("Введите название столбца: ")
    if column_name == '':
        print(data)
    else:
        for i in data.columns:
            if i == column_name:
                column_name = input("Введите название ещё одного столбца столбца: ")
                if column_name =='':
                    print(data[(data[i]>2022)])
                for o in data.columns:
                    if o == column_name:
                        column_name = input("Введите название ещё одного столбца столбца: ")
                        print(data[(data[i]>2022) & (data[o]>3)])
                        break
    
            
        
    #     # print(data[(data[column_name]>2022) & (data[column_name]>2) & (data[column_name]>45)])
column_name()
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