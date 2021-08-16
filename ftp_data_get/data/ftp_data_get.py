import os
import shutil
import ftplib
FTP_HOST = '*****'
FTP_ACCOUNT = '***@*****'
FTP_PASSWORD = '****'
FTP_DIR = './data'
LOCAL_DIR = './data'

ftp = ftplib.FTP_TLS(FTP_HOST)  # ホストに接続
ftp.set_pasv("true")  # PASVモードにする
ftp.login(FTP_ACCOUNT, FTP_PASSWORD)  # ログインする
ftp.prot_p()  # セキュアコネクションに変更
ftp.cwd(FTP_DIR)  # 指定したディレクトリ変更

DIR_LIST = ['pdf', 'jpeg']

for directory in DIR_LIST:
    current_dir = LOCAL_DIR + '/'+directory
    os.makedirs(LOCAL_DIR + '/'+directory, exist_ok=True)
    ftp.cwd(directory)

    files = ftp.nlst()
    local_dir_list = os.listdir(current_dir)

    for file in files:
        if(file == '.' or file == '..'):
            continue
        # 指定フォルダがローカルに存在しているか確認
        if(file in local_dir_list):
            print('既にフォルダが存在しているためスキップします。')
            continue
        # サーバーにてディレクトリの移動
        ftp.cwd(file)
        # 存在するファイル一覧を取得
        file_list = ftp.nlst()
        # ローカル側の保存先フォルダの作成
        dir_path = current_dir + '/' + file
        os.makedirs(dir_path)
        for fname in file_list:
            if(fname == '.' or fname == '..' or fname == '.DS_Store'):
                continue
            with open(fname, "wb") as f:
                ftp.retrbinary('RETR ' + fname, f.write)
            # ダウンロードしたフォルダの移動
            shutil.move(fname, dir_path)
        print(file+'ダウンロードok')

        ftp.cwd('../')

    ftp.cwd('../')
    print(directory+'のファイルダウンロードが完了しました')

print('ダウンロードが完了しました、終了します。')
ftp.quit()
