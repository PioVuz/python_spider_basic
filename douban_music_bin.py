# -*- coding: gbk -*-
import sys
import json
import requests
import csv
from bs4 import BeautifulSoup

# class MusicParser():
#     def __init__(self):
#         self.musics = []
#         self.in_musics = False
reload(sys)
sys.setdefaultencoding('utf-8')
global musics
musics = []
# definded top_post_rock func.
def top_post_rock(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    s = requests.get(url, headers=headers)
    bs = BeautifulSoup(s.content, 'lxml')
    div_all = bs.find_all('div', class_='pl2')
    a_all = bs.find_all('a', class_='nbg')
    # define global list
    global musics
    for index, div in enumerate(div_all):
        music = {}
        album = div.find('a').get_text(strip=True)
        if album:
            music['album'] = album
            music['info'] = div.find('p', class_='pl').get_text()
            music['score'] = div.find('span', class_='rating_nums').get_text()
            judge_num = (div.find('span', class_='pl').get_text(strip=True))
            music['judge'] = judge_num.split('(')[1].strip().split(')')[0].strip()
            music['img-url'] = a_all[index].img['src']
            downloading_imgurl(music)
        musics.append(music)
    return musics

def downloading_imgurl(music):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    img_url = music['img-url']
    print('downloading post cover from %s' % img_url)
    s = requests.get(img_url, headers=headers)
    fname = music['album'] + '.jpg'
    path_fname = './img/' + fname
    with open(path_fname, 'wb') as f:
        f.write(s.content)
    music['cover-file'] = fname

def save_for_csv(musics):
    # 1、create file object
    with open('./csv/PostRock.csv', 'wb') as f:
        # 2、written object
        csv_writer = csv.writer(f)
        # 3、written data
        csv_writer.writerow(['album', 'info', 'score', 'judge', 'img-url', 'cover-file'])
        for music in musics:
            row_data = []
            row_data.append(music['album'])
            row_data.append(music['info'])
            row_data.append(music['score'])
            row_data.append(music['judge'])
            row_data.append(music['img-url'])
            row_data.append(music['cover-file'])
            csv_writer.writerow(row_data)
        # 4、close file
        f.close()


if __name__ == '__main__':
    url = 'https://music.douban.com/tag/post-rock'
    musics = top_post_rock(url)
    save_for_csv(musics)
    print('%s' % json.dumps(musics, sort_keys=True, indent=4, separators=(',', ': ')))

