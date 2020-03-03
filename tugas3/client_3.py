import logging
import requests
import os
import threading


def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


threads = []
link = [
    'https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg',
    'https://asset.kompas.com/crops/YVr3kdj_B-52xLgtwsTy9qynK0Q=/73x42:850x560/750x500/data/photo/2019/10/29/5db78a6be8801.png',
    'https://asset.kompas.com/crops/kuHzPU-tTcTl1Ut2JwBuGK3cAoU=/0x0:996x664/750x500/data/photo/2020/02/27/5e57bc165e812.jpg'
]
for i in range(3):
    t = threading.Thread(target=download_gambar,args=(link[i],))
    threads.append(t)
    
for thr in threads:
    thr.start()