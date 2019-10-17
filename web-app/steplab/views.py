import os
import json

from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from .models import Post
from .models import StepSession
from .models import StepFile
from django.core.files.storage import default_storage
from smart_insole_utils.utils import get_data
from smart_insole_utils.classifiers import ClassiffierFacade, ClassifierType

from collections import Iterable

'''
url = "http://www.neo4j.com"
params = {'ref':"mark-blog"}
req.prepare_url(url, params)
'''
def _generateStepFiles(n, user):
    stepFiles = []
    n = 0
    for i in range(0, n):
        stepFiles.append(StepFile(title='____', author=user, footsize=42, productId='KKJFDUD58', steps=150, content=''))
    
    return stepFiles

@login_required(login_url='login')
def home(request):
    user = request.user

    n = 10
    stepFiles = _generateStepFiles(n, user)
    

    context = {
        'stepSessions'      : StepSession.objects.all(),
        'fields'            : ['field1'] * n,
        'stepRows'          : [['a'] * n] * n,
        'files'             : ['filename1'] * 10,
        'stepFiles'         : stepFiles,
        'title'             : 'StepLab'
    }
    return render(request, 'steplab/home.html', context) # request, template and context(arguments)

@login_required(login_url='login')
def recordings(request):
    user = request.user
    usrFolder = user.username
    context = {}
    if request.method == 'POST':
        #stepfiles = request.POST.getlist('new-stepfiles', None) # request.POST.get and request.POST.getlist
        stepfiles = request.FILES.getlist('new-stepfiles')
        print(stepfiles)
        for stepfile in stepfiles:
            full_filename = os.path.join(settings.MEDIA_ROOT, usrFolder, stepfile.name)
            # TODO: SAVE THE FILE INTO DB FOR LINDA USERS
            path = default_storage.save(full_filename, stepfile)

            fileName = os.path.basename(path)
            stepFileObj = StepFile(title=fileName, author=user, footsize=42, productId='KKJFDUD58', steps=150, content='')
            stepFileObj.save()

    elif request.method == 'GET':
        fileName = request.GET.get('filename', '')
        if fileName.strip():
            # TODO SECURITY RISK
            path = os.path.join(settings.MEDIA_ROOT, usrFolder, fileName)

            if os.path.exists(path):
                fields, samples = get_data(path)
                fileContent = {'fields': fields, 'samples': samples}
                context = {
                    'fileName'          :  fileName,
                    'fileContent'       :  fileContent,
                    'title'             : 'Recordings/' + fileName
                }

                return render(request, 'steplab/recordingDetail.html', context) # request, template and context(arguments)

    stepFiles = StepFile.objects.filter(author=user)

    context = {
                'stepFiles'         : stepFiles,
                'title'             : 'Recordings'
    }

    return render(request, 'steplab/recordings.html', context) # request, template and context(arguments)

@login_required(login_url='login')
def diagnosis(request):
    context = {'title': 'diagnosis'}
    return render(request, 'steplab/diagnosis.html', context)

@login_required(login_url='login')
@csrf_protect
def newDiagnose(request):
    stepFiles = StepFile.objects.filter(author=request.user)
    context = {
        'stepFiles'         : stepFiles,
        'title'             : 'diagnosis',
    }

    if request.method == 'POST':
        postFilesJSON = request.POST.get("analyse", "")
        postFiles = json.loads(postFilesJSON)
        for postFile in postFiles:
            print(postFiles)
        classificationMethods = [ClassifierType.MOCKED]
        if postFiles is not None and isinstance(postFiles, Iterable) and len(postFiles) > 0:
            ClassiffierFacade.analyseImbalances(request.user, postFiles, classificationMethods, 100)

    return render(request, 'steplab/newDiagnose.html', context)

def about(request):
    return render(request, 'steplab/about.html', {'title': 'About'})


'''
from django.contrib.auth.models import User
users = User.objects.all()
StepFile.objects.filter(footsize=42)
'''