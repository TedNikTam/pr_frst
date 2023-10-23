import pandas as pd
import os


#=================================СОРТИРОВКА ПО ВВОДИМЫМ ДАННЫМ===============================
#===========================================W_O_R_K===========================================
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