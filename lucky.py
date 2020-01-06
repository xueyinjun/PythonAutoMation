# encoding = utf-8
import requests, sys, webbrowser
from BeautifulSoup import bs4

print('Googloo...')

res = requests.get('https://www.baidu.com/s?wd=' + ''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.t a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://www.baidu.com' + linkElems[i].get('href'))
