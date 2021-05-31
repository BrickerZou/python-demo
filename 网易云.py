import requests
from bs4 import BeautifulSoup
from lxml import etree
import base64

#获取音乐信息
def get_music():
    url = 'http://music.163.com/discover/toplist?id=3778678'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    res = requests.get(url,headers=headers)
    res_text = res.text
    music_soup = BeautifulSoup(res_text,'html.parser')
    music_list = music_soup.find('ul',class_="f-hide").find_all('a')
    for a in music_list[0:20]:
        name = a.text
        b = a['href']
        song_id = b[9:]
        url2 = 'http://music.163.com/song/media/outer/url?id='+song_id+'.mp3'
        song = requests.get(url2,headers = headers)
        print(url2)
        r = song
        with open(name+'.mp3','wb') as f:
            f.write(r.content)
get_music()
# 14975887091615289850567
def gethtml(url):
    try:
        kw = {
            'cookies':'UM_distinctid=17121941056289-00038658d91354-f313f6d-190140-17121941057216; CNZZDATA1260502790=625044373-1585405157-https%253A%252F%252Fblog.csdn.net%252F%7C1585405157',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        res = requests.get(url,headers=kw,timeout=30)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
    except:
        print("访问出错!")
    else:
        return res.text

def parsehtml(html):
    response = etree.HTML(html)
    name = response.xpath('//tr/td[@class="song-name"]/text()')
    link = response.xpath('//tr/td[@class = "song-bitrate"]/a[last()]/@href')
    name = name[1::]
    for i in range(len(name)):
        print(f'{i+1}:{name[i]}')

    if len(name)==0:
        print('该平台没有相关歌曲,可以换一个平台!')
    else:
        ind = int(input("请输入需要下载的序号:"))
        print(f'{name[ind-1]}下载中......')
        downloadmp3(link[ind-1],name[ind-1])

def downloadmp3(link, name):
    with open(f'D:/mp3/{name}.mp3', 'wb') as f:
        data = requests.get(link)
        # print(f'{name}下载中......')
        f.write(data.content)
        print(f'{name}-下载完成!')
        f.close()
    # print(link[ind-1])