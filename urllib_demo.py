#coding=utf-8
#Version=python3.6.0
#Tools:Pycharm 2017.3.2
__date__ = '2019/2/21 15:31'
__author__ = 'toaakira'
import urllib.request
import urllib.parse

def print_list(list):
    for i in list :
        print(i)
def demo():
    s = urllib.request.urlopen('http://blog.kamidox.com')
    # print(s.read())
    # for i in range(10):
    #     print('line %d: %s' % (i+1, s.readline()))
    list = s.readlines()
    print_list(list)

def demo1():
    s = urllib.request.urlopen('http://blog.kamidox.com')
    msg = s.info()
    # print_list(msg._headers)
    print_list(dir(msg))

def retrieve():
    fname, msg = urllib.request.urlretrieve('http://blog.kamidox.com', 'index.html',reporthook=progress)
    print(fname)
    print_list(msg.items())

def progress(blk, blk_size, totla_size):
    print('%d/%d - %.02f%%' % (blk * blk_size, totla_size, (float)(blk * blk_size) * 100 / totla_size))

def urlencode():
    params = {'score': 100, 'name': '爬虫基础', 'comment': 'very good'}
    qs = urllib.parse.urlencode(params)
    parse_qs = urllib.parse.parse_qs(qs)
    print(parse_qs)

def urlparse():
    url = 'https://www.baidu.com/s?wd=%E8%BE%BE%E8%BE%BE%E5%85%94&rsv_spt=1&rsv_iqid=0xe9ce3ff40002a932&issp=1&f=3&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=3&rsv_sug1=3&rsv_sug7=100&rsv_sug2=1&prefixsug=d%2520d&rsp=0&inputT=1342&rsv_sug4=1342';
    result = urllib.parse.urlparse(url)
    query = result.query
    dict = urllib.parse.parse_qs(query)
    print(dict)


if __name__ == '__main__':
    urlparse()