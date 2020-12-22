import os
import csv

name = input("csvファイルの名前を入力してください")
stores_path = name + ".csv"

with open(stores_path, encoding="cp932") as f:
    reader = csv.reader(f)
    # ヘッダーを読み飛ばす
    # next(reader)
    for row in reader:
        folder_name = row[0] + '_' + row[1]
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)