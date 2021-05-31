from lxml import etree
import requests
import re
import os

netease_download_url = "http://music.163.com/song/media/outer/url?id={0}.mp3"
netease_music_url = "https://music.163.com/m/song?id={0}"

headers = {
    "referer": "https://music.163.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52"
}

def requestMusicName(url) :
    try :
        r = requests.get(url, headers = headers, timeout = 30)
        r.raise_for_status()
        html = etree.HTML(r.content, etree.HTMLParser())
        return html.xpath("/html/head/title/text()")[0]
    except :
        print("网络请求出现异常")
        os._exit(0)

def requestDownloadMusic(url, fileName) :
    try :
        print("开始下载 【" + fileName + "】")
        r = requests.get(url, headers = headers)
        r.raise_for_status()
        saveFile(fileName, r.content)
        print("下载完成")
    except :
        print("网络请求出现异常")
        os._exit(0)

def saveFile(fileName, content) :
    with open(os.path.join(path, fileName), "wb") as file :
        file.write(content)

if __name__ == "__main__" :
    netease_url = input("请将要下载的网易云音乐歌曲链接粘贴到此处:")
    path = 'C:/Users/lenovo/Music'
    netease_music_id = re.search(r"(?<=id=)\d*", netease_url).group()

    netease_music_name = requestMusicName(netease_music_url.format(netease_music_id))
    requestDownloadMusic(netease_download_url.format(netease_music_id), netease_music_name + ".mp3")
