# imports for django
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import os.path
from project.settings import MEDIA_ROOT
import subprocess
from .models import *
from functions import *

def indexView(request):
    if request.session.has_key('sessid'):
        sessid = request.session['sessid']
        if Audio.objects.filter(audioid= sessid).exists():
            Audio.objects.get(audioid= sessid).delete()
            del request.session['sessid']
            sessid = 0
        else: 
            sessid = 0
    else:
        sessid = 0

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        if uploaded_file.name.endswith('.wav') or uploaded_file.name.endswith('.mp3'):
            savefile = FileSystemStorage()
            name = savefile.save(uploaded_file.name, uploaded_file)
            if name.endswith('.mp3'):
                subprocess.call(['ffmpeg', '-i', os.path.join(MEDIA_ROOT, name),
                                     os.path.join(MEDIA_ROOT, name[:-4]+'.wav')])
                savefile.delete(os.path.join(MEDIA_ROOT, name))
            
            path = os.path.join(MEDIA_ROOT, name[:-4]+'.wav') 
            aud = Audio()
            aud.audio = path
            aud.save()
            sessid = aud.audioid
            request.session['sessid'] = sessid
            print(sessid)
            return redirect(loadingView)
        else:
            messages.warning(request, 'File was not uploaded. Please use .wav or .mp3 file extension!')    
    return  render(request,  'frontend/index.html', {'sessid':sessid})

def loadingView(request):

    if request.method == 'POST':
        print("post")
        
        if request.session.has_key('sessid'):
            sessid = request.session['sessid']

            aud = Audio.objects.get(audioid=sessid)
            filename = aud.audio.path
            timestamp, labels, duration, path, nospeakers = diraize_audio(filename, model_vggvox2, vad)
            pipath = duration_plot(filename, labels, duration)
            aud.diraize = path
            aud.nospeaker = nospeakers
            aud.duration = pipath
            aud.save()
            print("saved")

            spath = speakerfiles(filename, timestamp)
            for path in spath:
                sp = Speaker()
                sp.sp_audio = path
                sp.audioid = aud
                sp.save()
                print("saved ",path)
                

            spu = Speaker.objects.filter(audioid=sessid).values_list('spid',flat=True)
            for id in spu:
                sp = Speaker.objects.get(spid = id)
                filename = sp.sp_audio.path
                ebpath, epath = emotion_analysis(filename, vad, quantized_vggvox_v2)
                sp.sp_emo = epath
                sp.sp_emobar = ebpath
                sp.save()
                print("saved id",id)

            aud = Audio.objects.get(audioid=sessid)
            filename = aud.audio.path    
            ftran = transcribe(filename)
            muword = common_words(ftran)
            aud.tnscript = ftran
            aud.freqwrd = muword
            aud.save()
            print("saved trans")
         
        return redirect(dashboardView)
    return render(request, 'frontend/loading.html') 

def dashboardView(request): 
    if request.session.has_key('sessid'):
        sessid = request.session['sessid']

        content = { }
        aud = Audio.objects.filter(audioid=sessid)
        content['object'] = aud
        spu = Speaker.objects.filter(audioid=sessid)
        content['speakers'] = spu
        
        return  render(request, 'frontend/dashboard.html', content)
    else: 
        return  render(request, 'frontend/dashboard.html', { })
