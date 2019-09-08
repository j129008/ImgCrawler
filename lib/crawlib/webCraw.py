from ..weblib.webImg import Web
from urllib.parse import urljoin
import re

class Craw:
    def __init__(self, url=None, next_keyword=None, img_pattern=None):
        self.page_now = Web(url)
        self.url_base = re.search(r'^(http(s)?://)?[^/]+', url).group()
        self.setNextPage(next_keyword)
        self.setImgPattern(img_pattern)

    def setNextPage(self, next_keyword):
        self.next_keyword = next_keyword

    def setImgPattern(self, pattern):
        self.img_pattern = pattern

    def loadNextPage(self):
        next_page = self.page_now.searchLink(self.next_keyword)
        if len(next_page) == 0:
            return False
        next_page = next_page[0]
        next_page = urljoin(self.url_base, next_page)
        self.page_now = Web(next_page)
        return True

    def getImg(self):
        img = self.page_now.getRegexImg(self.img_pattern)
        if len(img) == 0:
            return None

        return img[0]

    def getAllImg(self):
        imgs = []
        while self.loadNextPage() == True:
            img = self.getImg()
            print(img)
            imgs.append(img)