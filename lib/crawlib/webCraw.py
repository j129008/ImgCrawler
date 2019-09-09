from ..weblib.webImg import Web
from urllib.parse import urljoin
from urllib.request import urlopen
import re
from pathlib import Path

class Craw:
    def __init__(self, url=None, next_keyword=None, img_pattern=None, url_pattern='.+'):
        self.url = url
        self.page_now = Web(url)
        self.url_base = re.search(r'^(http(s)?://)?[^/]+', url).group()
        self.setNextPage(next_keyword)
        self.setImgPattern(img_pattern)
        self.url_pattern = url_pattern
        self.file_id = 0

    def setNextPage(self, next_keyword):
        self.next_keyword = next_keyword

    def setImgPattern(self, pattern):
        self.img_pattern = pattern

    def setUrlPattern(self, pattern):
        self.url_pattern = pattern

    def loadNextPage(self):
        next_page = self.page_now.searchLink(self.next_keyword)
        if len(next_page) == 0:
            return False
        next_page = next_page[0]
        next_page = urljoin(self.url_base, next_page)
        self.url = next_page
        if re.search(self.url_pattern, next_page) is None:
            return False
        self.page_now = Web(next_page)
        return True


    def fetch(self, url, max_retry=10):
        retry = 0
        while retry < max_retry:
            try:
                response = urlopen(img_url)
                return response.read()
            except:
                retry += 1
        return None

    def saveAndLoadNext(self, path):
        img_url = self.getImg()
        data = self.fetch(img_url)
        if data is None:
            return False

        self.file_id += 1
        file_name = '{:04d}.jpg'.format(self.file_id)
        data = response.read()

        p = Path(path)
        if not p.exists():
            p.mkdir(exist_ok=True)
        with open(path + file_name, 'wb') as f:
            f.write(data)

        return self.loadNextPage()

    def getImg(self):
        img = self.page_now.getRegexImg(self.img_pattern)
        if len(img) == 0:
            return None
        img = img[0]
        print(img)
        return img

    def getAllImg(self, path):
        while self.saveAndLoadNext(path):
            pass

