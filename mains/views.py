from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import videos,show,website
from threading import Thread
import json
# Create your views here.
def showlist(req):
    if(req.GET):
        shows=req.GET["q"]
        res=show.objects.filter(name__icontains=shows)
        return render(req,"showlist.html",{'objects':res})

def seasonlist(req):
    shows=req.GET['show']
    res=videos.objects.filter(show__name=shows).order_by('season').values('season').distinct()
    return render(req,'seasonlist.html',{'show':shows,'objects':res})

def episodelist(req):
    shows=req.GET['show']
    season=int(req.GET['season'])
    res=videos.objects.filter(show__name=shows,season=season).order_by('episode').values('episode').distinct()
    return render(req,'episodelist.html',{'show':shows,'season':season,'objects':res})

def qualitylist(req):
    shows=req.GET['show']
    season=req.GET['season']
    episode=req.GET['episode']
    res=videos.objects.filter(show__name=shows,season=season,episode=episode).order_by('quality').values('quality').distinct()
    return render(req,'qualitylist.html',{'show':shows,'season':season,'episode':episode,'objects':res})
def videoplayer(req):
    shows=req.GET['show']
    season=req.GET['season']
    episode=req.GET['episode']
    quality=req.GET['quality']
    res=videos.objects.filter(show__name=shows,season=season,episode=episode).values('url')
    return render(req,'video.html',{'show':shows,'season':season,'episode':episode,'quality':quality,'objects':res})
def searchView(req):
    return render(req,"search.html")

def process(req):
    if(req.FILES):
        a=Thread(target=handler,args=(req.FILES['json'],))
        a.start()
        return HttpResponse(1)
    else:
        return render(req,"addmore.html")

@login_required()
def handler(a):
    js=json.loads(a.read())
    web=website.objects.get_or_create(url=js.pop(0),noof=0)
    for i in js:
        sho=show.objects.get_or_create(name=i['show'].lower())
        vid=videos.objects.get_or_create(website=web[0],show=sho[0],season=i['season'],episode=i['episode'],quality=i['quality'],url=i['url'])
        web[0].noof=web[0].noof+1
    web[0].save()