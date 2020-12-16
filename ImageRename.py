# 画像の名前を指定した文字列+連番に変更するプログラム
import glob, os
# files = glob.glob("*.jpg")
extension = input("写真の形式を入力してください。")
files = glob.glob("*." + extension)
name = input("ファイルの名前を入力してください。")
for i, old_name in enumerate(files): # --- (*1)
    # ファイル名を決定する --- (*2)
    new_name = name +("{0:03d}." +extension).format(i + 1)
    # 改名する
    os.rename(old_name, new_name)
    # 状況を報告
    print(old_name + "→" + new_name)