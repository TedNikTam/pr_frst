import pandas as pd

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

#============================================================================================