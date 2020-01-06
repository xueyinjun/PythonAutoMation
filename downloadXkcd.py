#encoding =utf-8

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', mode=0o777, exist_ok=True)
while not url.endswith('#'):
    #Download the page.
    print('Downloading page %s...' % (url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')

        print('DownLoading image %s' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')