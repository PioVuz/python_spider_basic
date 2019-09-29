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

class bing_img_top100():
    def __init__(self):
        # 定义session
        self.session = requests.session()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        self.url = 'https://bing.ioliu.cn/ranking?p=%d'
        self.proxies = {'http': 'http://proxy3.bj.petrochina:8080',
                        'https': 'https://proxy3.bj.petrochina:8080'}
        self.save_path = 'G:/Desktop/down_bings_pic'

    # 字节bytes转化K\M\G
    def format_size(bytes):
        try:
            bytes = float(bytes)
            kb = bytes / 1024
        except:
            print("传入的字节格式不对")
            return "Error"
        if kb >= 1024:
            M = kb / 1024
            if M >= 1024:
                G = M / 1024
                return "%.3fG" % (G)
            else:
                return "%.3fM" % (M)
        else:
            return "%.3fK" % (kb)

    def img_scrapy(self):
        # 定义urlretrieve回调函数，用来显示下载进度
        def Schedule(blocknum, blocksize, totalsize):
            """
                回调函数(显示下载进度)
                @blocknum: 已经下载的数据块
                @blocksize: 数据块的大小
                @totalsize: 远程文件的大小
            """
            current = blocknum * blocksize * 100.0 if blocknum * blocksize * 100.0 < 1 else totalsize
            print("\rdownloading: %5.1f%%" % (current / totalsize), end="")

        for i in range(1, 2):
            get_resp = self.session.get(self.url % i, headers=self.headers, proxies=self.proxies)
            selector = etree.HTML(get_resp.text)
            imgs = selector.xpath('//div[@class="card progressive"]/img/@src')
            time.sleep(random.random())
            if not os.path.isdir(self.save_path):
                os.mkdir(self.save_path)
            for imgurl in imgs:
                # print('IMG_URL:%s' % img)
                if not os.path.isfile(os.path.join(self.save_path, os.path.basename(imgurl))):
                    print('Downloading data from %s' % imgurl)
                    urlretrieve(imgurl, filename=os.path.join(self.save_path, os.path.basename(imgurl)), reporthook=Schedule)
                    print('\nDownload finished!')
                else:
                    print('File already exsits!')

                # 获取文件大小
                filesize = os.path.getsize(os.path.join(self.save_path, os.path.basename(imgurl)))
                # 文件大小默认以Bytes计， 转换为Mb
                print('File size = %.2f Mb' % (filesize / 1024 / 1024))

bing = bing_img_top100()
bing.img_scrapy()