#coding=utf-8
#Version=python3.6.0
#Tools:Pycharm 2017.3.2
__date__ = '2019/9/24 15:45'
__author__ = 'toaakira'
# -*- coding: utf-8 -*-
import requests,json,time
import jieba
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

# 存储爬取结果
def write(path,text):
    with open(path,'a', encoding='utf-8') as f:
        f.writelines(text)
        f.write('\n')

# 爬取评论
def getcomments(num,path):
    url = 'https://www.jianshu.com/notes/23437010/comments?comment_id=&author_only=false&since_id=0&max_id=1586510606000&order_by=likes_count&page='+str(num)
    response = requests.get(url).text
    response = json.loads(response)
    num = response['total_pages']
    for i in response['comments']:
        comment = BeautifulSoup(i['compiled_content'],'lxml').text
        write(path,comment)
    return num

# jieba 分词
def read(path):
    text=''
    with open(path, encoding='utf-8') as s:
        for line in s.readlines():
            line.strip()
            text += ' '.join(jieba.cut(line))
    return text

# WordCloud 生成词云
def wordcloud(imagepath):
    backgroud_Image = plt.imread(imagepath)
    wc = WordCloud(background_color='white',  # 设置背景颜色
                   mask=backgroud_Image,  # 设置背景图片
                   max_words=2000,  # 设置最大现实的字数
                   stopwords=STOPWORDS,  # 设置停用词
                   font_path='C:/Users/Windows/fonts/msyh.ttf',  # 设置字体格式，如不设置显示不了中文
                   max_font_size=120,  # 设置字体最大值
                   random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
                   )
    wc.generate(text)
    image_colors = ImageColorGenerator(backgroud_Image)
    wc.recolor(color_func=image_colors)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    path = '评论.txt' # 评论path
    imagepath = 'heart.jpg' #词云背景图path
    print('正在爬取评论')
    i,num=1,2
    while i <= num:
        num=getcomments(i,path) # 爬取评论
        time.sleep(2)
        i += 1
    print('正在分词处理')
    text = read(path)  # jieba 分词处理
    print('正在生成词云')
    wordcloud(imagepath) # WordCloud 生成词云
    print('词云生成成功')