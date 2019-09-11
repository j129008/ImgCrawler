from django.shortcuts import render_to_response
from glob import glob
from .lib.crawlib.webCraw import Craw
import sys
import threading
from django.http import HttpResponseRedirect


def fetchImg(img_id):
    base_url = 'http://www.itmtu.com'
    img_type = 'mm'

    url = '{}/{}/{}/'.format(base_url, img_type, img_id)

    craw = Craw(url, next_keyword='下一页', img_pattern='http://img.itmtu.com/.*.(jpg|png)')
    craw.setUrlPattern(url + '.*')
    folder = img_id
    path = 'media/{}/'.format(folder)
    imgs = craw.getAllImg(path)

def index(request):
    if 'img_id' in request.GET:
        img_id = request.GET['img_id']
        print('img id: {}'.format(img_id))
        thread = threading.Thread(target=fetchImg, args=(img_id, ))
        thread.start()
        return HttpResponseRedirect(redirect_to='/')

    folders = glob('media/*')
    return render_to_response('index.html', {
        'folders': [folder.split('/')[-1] for folder in folders]
    })
