import requests
import re
import uuid
from bs4 import BeautifulSoup
import time
import os


#  取得するURL
url = "https://search.nifty.com/imagesearch/search?select=1&chartype=&q=%s&xargs=2&img.fmt=all&img.imtype=color&img.filteradult=no&img.type=all&img.dimensions=large&start=%s&num=20"
# url = "http://search.nifty.com/search/error/image_nokey.html"
#  検索するキーワード
keyword = "アンパンマン"
#  キーワード名でディレクトリを作成
os.mkdir(keyword)
pages = [1, 20, 40, 60, 80, 100]

print("ディレクトリ「" + keyword + "」を作成しました。")
print(keyword + "に関連する画像を100枚保存します。")

for p in pages:
    r = requests.get(url % (keyword, p))
    soup = BeautifulSoup(r.text, 'lxml')
    imgs = soup.find_all('img', src=re.compile('^https://msp.c.yimg.jp/yjimage'))
    for img in imgs:
        r = requests.get(img['src'])
        with open(str('./' + keyword + '/') + str(uuid.uuid4()) + str('.jpeg'), 'wb') as file:
            file.write(r.content)
    print(str(p) + "枚目の画像を保存しました。")
    time.sleep(1)     # 礼儀作法

print("画像保存が完了しました。")
