from lib.crawlib.webCraw import Craw

craw = Craw('http://www.itmtu.com/mm/35178/4', next_keyword='下一页', img_pattern='http://img.itmtu.com/.*.jpg')
folder = 'test'
path = 'web_view/img_viewer/static/{}/'.format(folder)
imgs = craw.getAllImg(path)

