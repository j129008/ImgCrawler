from bs4 import BeautifulSoup
import urllib3
import re
from pprint import pprint

class Web:
    def __init__(self, url):
        http = urllib3.PoolManager()
        if url is not None:
            response = http.request('GET', url)
            html = response.data
            self.soup = BeautifulSoup(html, 'html.parser')

    def getHtml(self):
        return self.soup.prettify()

    def getImg(self, src='src'):
        imgs = self.soup.find_all('img')
        imgs = [img[src] for img in imgs]

        return imgs

    def getRegexImg(self, pattern):
        imgs = self.getImg()
        return [
            img for img in imgs if re.search(pattern, img) is not None
        ]

    def getLink(self):
        links = self.soup.find_all('a')

        return [link['href'] for link in links]

    def getRegexLink(self, pattern):
        links = self.getLink()
        return [
            link for link in links if re.search(pattern, link) is not None
        ]

    def searchLink(self, pattern):
        links = self.soup.find_all('a')
        return [
            link['href'] for link in links if re.search(pattern, str(link)) is not None
        ]


