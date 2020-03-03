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


arr_gambar = ['https://www.persebaya.id/thumbs/large/uploads/post/2020/03/02/0203-Pre_Order_Authentic_Jersey_Persebaya.jpg','https://www.persebaya.id/thumbs/medium/uploads/post/2020/03/01/DBL09792_Original.jpg','https://www.persebaya.id/thumbs/medium/uploads/post/2020/03/01/2902-Persebaya_Tertahan_di_Laga_Pembuka_Shopee_Liga_1_2020.jpeg']

if __name__=='__main__':
    threads = []
    for i in arr_gambar:
        t = threading.Thread(target=download_gambar,args=(i,))
        threads.append(t)
        
    for thr in threads:
        thr.start()
