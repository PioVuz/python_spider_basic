import json
import requests
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

class MusicParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.musics = []
        self.in_musics = False

    def handle_data(self, data):
        data = data.strip()
        if data and self.in_musics:
            music = {}
            music['title'] = data
            self.musics.append(music)
            # print "handle_data -->", data

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None


        if tag == 'a' and _attr(attrs, 'href') and _attr(attrs, 'onclick'):
            # par = '%s' % _attr(attrs, 'onclick')
            music = {}
            music['cover-url'] = _attr(attrs, 'href')

            self.in_musics = True
            self.musics.append(music)

            # print('%(cover-url)s' % music)
        else:
            self.in_musics = False



# definded top_post_rock func.
def top_post_rock(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    s = requests.get(url, headers=headers)
    parser = MusicParser()
    parser.feed(s.content)
    return parser.musics


if __name__ == '__main__':
    url = 'https://music.douban.com/tag/post-rock'
    musics = top_post_rock(url)
    print('%s' % json.dumps(musics, sort_keys=True, indent=4, separators=(',', ': ')))
