from django.shortcuts import render_to_response
from glob import glob

def index(request):
    folders = glob('../../img/*')
    return render_to_response('index.html', {
        'folders': [folder.split('/')[-1] for folder in folders]
    })
