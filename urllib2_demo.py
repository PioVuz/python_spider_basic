#coding=utf-8
#Version=python3.6.0
#Tools:Pycharm 2017.3.2
__date__ = '2019/2/22 9:11'
__author__ = 'toaakira'
import urllib.request
def request():
    #定制http头
    headers = {'User-Agent': 'Mozilla/5.0', 'x-my-header':'my value'}
    req = urllib.request.Request('http://blog.kamidox.com', headers=headers)
    s = urllib.request.urlopen(req)
    print(s.read(10000))
    print(req.headers)
if __name__ == '__main__':
    request()