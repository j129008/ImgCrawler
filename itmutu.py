from lib.crawlib.webCraw import Craw

base_url = 'http://www.itmtu.com'
img_type = 'mm'
img_id = 67496

url = '{}/{}/{}/'.format(base_url, img_type, img_id)

craw = Craw(url, next_keyword='下一页', img_pattern='http://img.itmtu.com/.*.jpg')
craw.setUrlPattern(url + '.*')
folder = img_id
path = 'web_view/img_viewer/static/{}/'.format(folder)
imgs = craw.getAllImg(path)

