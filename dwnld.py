import os
import pandas as pd
import zipfile

# kaggle datasets -h

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