# FTP_Data_Get

## 概要

FTP クライアントを利用して、特定のサーバーからデータを取得するプログラム。<br>
Python のコードで動いており、組み込みモジュールの`ftplib`を利用している。<br>
本来であれば、パスワードなどは env ファイルを使うべきなのだが、今回は実装時間の都合上省略とさせていただく。

## 公式ドキュメント

https://docs.python.org/ja/3/library/ftplib.html

## 実装における参考記事

https://www.yoheim.net/blog.php?q=20170401

https://roy29fuku.com/web/python-ftplib/

https://intellectual-curiosity.tokyo/2019/12/01/python%E3%81%A7ftp%E3%82%A2%E3%83%83%E3%83%97%E3%83%AD%E3%83%BC%E3%83%89%E3%82%92%E8%A1%8C%E3%81%86%E6%96%B9%E6%B3%95/

## デバッグ時の参考情報

```
# print(directory)
# print(LOCAL_DIR + '/'+directory)
# print(ftp.pwd())
# print(files)
# print(local_dir_list)
# print(dir_path)

```

## 動作手順

- FTP に接続
- 指定ディレクトリに移動
- 欲しいフォルダを順に探索
- `.`や`..`というファイルがあるのでスキップ処理
- 同じ名前のフォルダがローカルに存在していたらスキップ処理
- フォルダに入って順にファイルをダウンロード

## モジュール解説

| 名前   | 説明                |
| ------ | ------------------- |
| python | 3.9.1               |
| os     | OS 依存の機能を利用 |
| shutil | ファイル操作        |
| ftplib | FTP 接続用          |

## cron ないしタスクスケジューラーを利用した自動実行

Python、Git をインストール
毎朝 8 時に動作するように設定。

## 現状の設定等解説文章

​​
​1. 毎日 AM8:00 に Python のプログラムが動作します。​
​2. データが存在するサーバにアクセスします。​
​3. PC​ の該当フォルダに存在しない jpeg と PDF のデータをダウンロードします。（注文番号で判定）​​
​​
​ 利用ツール ​
​- windows PC​
​- Python​
​- タスクスケジューラ（windows のデフォルトアプリ）
​​​
​ ダウンロードしたデータは data 配下に存在します。​
​​