from bs4 import BeautifulSoup
import urllib3

class Web:
    def __init__(self, url):
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        html = response.data
        self.soup = BeautifulSoup(html, 'html.parser')

    def getHtml(self):
        return self.soup.prettify()


if __name__ == '__main__':
    web = Web('http://www.itmtu.com/mm/35178/4')
    print(web.getHtml())
