import requests
import kaggle
import os
import pandas as pd
import json
import csv
import zipfile

#=====делаем запрос на список  (20 файлов)======
# rqst = input("Введите запрос на английском: ")
# str = os.system(f"kaggle datasets list -s {rqst}")
# qwe = os.system(f"kaggle datasets files {rqst} {str}")

#=========СКАЧИВАНИЕ CSV-ФАЙЛА, ПОЛУЧЕНИЕ ИНФОРМАЦИИ, УДАЛЕНИЕ==========
obj_adress = ("gauravduttakiit/media-campaign-cost-prediction") # адрес для скачивания 
obj_dwnld = os.system(f'kaggle datasets download -d {obj_adress}') # скачивание файла
file = (str(obj_adress.split('/')[1]) +'.zip') # формирование названия zip-файла
f_zip = zipfile.ZipFile(file, 'r') # zip-файл открывается на чтение
f_zip.extractall('./') # извлекается содержимое zip-файла
for file_info in f_zip.infolist(): # запускается цикл по чтению содержимого zip-файла
    p = file_info.filename
    data = pd.read_csv(file_info.filename, encoding='latin-1')
    os.remove(p) # после получения информации файл удаляется
    print(
        "\nНазвание файла: ", file_info.filename,
        "\nИнформация о колонках в файле: ", data.columns,
        "\nКол-во строк и столбцов: ", data.shape,
        )
f_zip.close() # zip-файл закрывается
os.remove(file) # zip-файл удаляется
print(f"-"*20 + "\nФайлы удалены!")
#=============================================================================



# print(str)
# with open("data.csv", 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         [str]
#     )

# df = pd.DataFrame({
#     'ref': [str], 'title': [str], 'size': [str], 'lastUpend': [str], 'downloadCount': [str], 'voteCount': [str], 'usabilityRating': [str]
# })
# df.to_excel('data4.xlsx')


# data = pd.read_csv('spotify-2023.csv', encoding='latin-1') # encoding='latin-1'- дал возможность читать файл скодировкой UTF-8
# print(data[:10])
# # print(data.columns) # названия столбцов
# # print(data.shape) #кол-во строк и столбцов
# # print(data['artist(s)_name'][:5])
# # print(data.loc[1]) # выводит данные по номеру строки
# # print(data.loc[[1, 2]]) # выводит данные по номеру более одной строки
# # print(data.index.get_loc("Olivia Rodrigo"))
# # print(data[data['acousticness_%']>=55]) # выводит данные столбцов отсортированные по значению
# print(data[(data['acousticness_%']>=55) & (data['liveness_%']>=25)]) # выводит данные столбцов отсортированные по  2м значениям

# with open("spotify-2023.csv", encoding='latin-1') as r_file:
#     # Создаем объект DictReader, указываем символ-разделитель ","
#     file_reader = csv.DictReader(r_file, delimiter = ",")
#     # Счетчик для подсчета количества строк и вывода заголовков столбцов
#     count = 0
#     # Считывание данных из CSV файла
#     for row in file_reader:
#         if count == 0:
#             # Вывод строки, содержащей заголовки для столбцов
#             print(f'Файл содержит столбцы: {", ".join(row)}')
#         else:
#             # Вывод строк
#             print(f'{row["artist(s)_name"]} - {row["track_name"]} -> год релиза - {row["released_year"]} году.\n', end='')
#         count += 1
#     print(f'Всего в файле {count} строк.')


# link = 'https://www.kaggle.com'
# response = requests.get(f"{link}/datasets/anshtanwar/monthly-food-price-estimates")
# # print(responce.status_code)
# print(response.headers)

# response = requests.get("https://www.kaggle.com/datasets/anshtanwar/monthly-food-price-estimates")

# print(response.status_code)
# print(response.headers)
# print(response.text)
