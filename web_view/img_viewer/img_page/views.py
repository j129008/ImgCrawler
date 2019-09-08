from django.shortcuts import render_to_response
from glob import glob

def imgView(request, folder):
    imgs = glob('static/{}/*.jpg'.format(folder))
    return render_to_response('page.html', {
        'imgs': sorted(imgs)
    })
