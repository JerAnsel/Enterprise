import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import json
from bs4 import BeautifulSoup
from urllib.request import urlopen



queue = list()
Index = dict()
Start_Url = input ('Enter start url:')

def Crawler(Start_Url):
    cnt = 0
    end = False
    queue.append(Start_Url)
    while (len(queue) is not 0 and not end) :
        url = queue.pop(0)
        if url not in Index :
            Index[url] = Index.get(url, 0)
        try :
            html = urlopen(url).read()
        except :
            print('url did not open')
            url = queue.pop(0)
            continue

        soup = BeautifulSoup(html, "html.parser")
        tags = soup('a')
        for tag in tags :
            print(tag)
            href = tag.get('href', None)
            print('href=',href)
            if href is None :
                continue
            if (not href.startswith('http'))  :
                if (href.startswith('#'))  :
                    continue
                if (href.startswith('/'))  :
                    href = url + 'href'
            if href not in queue :
                    if href not in Index :
                        queue.append(href)
                        cnt = cnt + 1
            if (cnt == 60) :
                print('6000')
                end = True
                print(Index)
                break

Crawler(Start_Url)
