from django.shortcuts import render_to_response
from glob import glob
from .lib.crawlib.webCraw import Craw
import sys
import threading
from django.http import HttpResponseRedirect
import re


def fetchImg(img_id):
    base_url = 'http://www.itmtu.com'
    img_type = 'mm'

    url = '{}/{}/{}/'.format(base_url, img_type, img_id)

    craw = Craw(url, next_keyword='下一页', img_pattern=r'((http://img\.itmtu\.com/mm/.*\.(jpg|png))|http://www\.itmtu\.com/wp-content/uploads/\d+/\d+/[0-9\-x]+\.(jpg|png))')
    craw.setUrlPattern(url + '.*')
    folder = img_id
    path = 'media/{}/'.format(folder)
    imgs = craw.getAllImg(path)

def index(request):
    if 'url' in request.GET:
        url = request.GET['url']
        m = re.search(r'http://www.itmtu.com/mm/([\d]+).*', url)
        if m is not None:
            img_id = m.group(1)
            thread = threading.Thread(target=fetchImg, args=(img_id, ))
            thread.start()
        return HttpResponseRedirect(redirect_to='/')

    folders = glob('media/*')
    return render_to_response('index.html', {
        'folders': [folder.split('/')[-1] for folder in folders]
    })
