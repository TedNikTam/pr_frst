import pandas as pd
import os

# 11/29/2021 10:00:00 AM
#=================================СОРТИРОВКА ПО ВВОДИМЫМ ДАННЫМ===============================
#===========================================W_O_R_K===========================================
data = pd.read_csv('Crime_Data_from_2020_to_Present.csv', encoding='latin-1')
print(data.columns)

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
        os.remove('new_data.csv')
        
sort_1()
#============================================================================================