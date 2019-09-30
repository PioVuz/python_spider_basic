#coding=utf-8
#Version=python3.6.0
#Tools:Pycharm 2017.3.2
__date__ = '2019/9/29 15:30'
__author__ = 'toaakira'
import requests
from lxml import etree
import time
import random
from urllib.request import urlretrieve
import os
import sys
import threading

gImageList = []
gCondition = threading.Condition()
session = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
request_url = 'https://bing.ioliu.cn/ranking?p=%d'
proxies = {'http': 'http://proxy3.bj.petrochina:8080',
                'https': 'https://proxy3.bj.petrochina:8080'}
save_path = 'G:/Desktop/down_bings_pic'

class Producer(threading.Thread):


    def run(self):
        global gImageList
        global gCondition
        print('%s started' % threading.current_thread())
        gCondition.acquire()
        for i in range(1, 100):
            get_resp = session.get(request_url % i, headers=headers, proxies=proxies)
            selector = etree.HTML(get_resp.text)
            imgs = selector.xpath('//div[@class="card progressive"]/img/@src')
            for imgurl in imgs:
                gImageList.append(imgurl)
            # time.sleep(random.random())
        print('%s: produced %d urls. Left %d urls.' % (threading.current_thread(), len(imgs) - 1, len(gImageList)))
        gCondition.notify_all()
        gCondition.release()



class Consumer(threading.Thread):

    def run(self):
        global gImageList
        global gCondition

        print('%s started' % threading.current_thread())
        while True:
            gCondition.acquire()
            print('%s: trying to download image. Queue length is %d' % (threading.current_thread(), len(gImageList)))
            while len(gImageList) == 0:
                gCondition.wait()
                print('%s: waken up. Queue length is %d' % (threading.current_thread(), len(gImageList)))
            url = gImageList.pop()
            gCondition.release()
            _down_load(self, url)



# 定义urlretrieve回调函数，用来显示下载进度
def Schedule(blocknum, blocksize, totalsize):
    """
        回调函数(显示下载进度)
        @blocknum: 已经下载的数据块
        @blocksize: 数据块的大小
        @totalsize: 远程文件的大小
    """
    curren_percent = blocknum * blocksize * 100.0 / totalsize
    curren_percent = curren_percent if curren_percent < 100 else 100
    # print("\rdownloading: %5.1f%%" % (curren_percent), end="")

def _download_wallpaper_list(self):
    for i in range(1, 100):
        get_resp = self.session.get(self.url % i, headers=self.headers, proxies=self.proxies)
        selector = etree.HTML(get_resp.text)
        imgs = selector.xpath('//div[@class="card progressive"]/img/@src')
        for imgurl in imgs:
            gImageList.append(imgurl)
        time.sleep(random.random())


def _down_load(self, img):
    if not os.path.isdir(save_path):
        os.mkdir(save_path)
    if not os.path.isfile(os.path.join(save_path, os.path.basename(img))):
        # print('\nDownloading data from %s' % img)
        urlretrieve(img, filename=os.path.join(save_path, os.path.basename(img)), reporthook=Schedule)
        print('\nDownload finished!')
    else:
        print('File already exsits!')

        # 获取文件大小
    filesize = os.path.getsize(os.path.join(save_path, os.path.basename(img)))
    # 文件大小默认以Bytes计， 转换为Mb
    print('File size = %.2f Mb' % (filesize / 1024 / 1024))

if __name__ == '__main__':
    # Producer().start()
    #
    # for i in range(5):
    #     Consumer().start()
    for maindir, subdir, file_name_list in os.walk('G:/Desktop/down_bings_pic'):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            ext = os.path.splitext(apath)[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
            os.path.getsize


