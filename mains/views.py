from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import videos,show,website,settings
from .decor import maint_check
import json
# Create your views here.
@maint_check
def showlist(req):
    if(req.GET):
        shows=req.GET["q"]
        res=show.objects.filter(name__icontains=shows)
        return render(req,"showlist.html",{'objects':res})

@maint_check
def seasonlist(req):
    shows=req.GET['show']
    res=videos.objects.filter(show__name=shows).order_by('season').values('season').distinct()
    return render(req,'seasonlist.html',{'show':shows,'objects':res})

@maint_check
def episodelist(req):
    shows=req.GET['show']
    season=int(req.GET['season'])
    res=videos.objects.filter(show__name=shows,season=season).order_by('episode').values('episode').distinct()
    return render(req,'episodelist.html',{'show':shows,'season':season,'objects':res})

@maint_check
def qualitylist(req):
    shows=req.GET['show']
    season=req.GET['season']
    episode=req.GET['episode']
    res=videos.objects.filter(show__name=shows,season=season,episode=episode).order_by('quality').values('quality').distinct()
    return render(req,'qualitylist.html',{'show':shows,'season':season,'episode':episode,'objects':res})

@maint_check
def videoplayer(req):
    shows=req.GET['show']
    season=req.GET['season']
    episode=req.GET['episode']
    quality=req.GET['quality']
    res=videos.objects.filter(show__name=shows,season=season,episode=episode,quality=quality).values('url')
    return render(req,'video.html',{'show':shows,'season':season,'episode':episode,'quality':quality,'objects':res})

@maint_check
def searchView(req):
    return render(req,"search.html")

@maint_check
@login_required(login_url='/admin')
def process(req):
    if(req.FILES):
        handler(req.FILES['json'])
        return HttpResponse(1)
    else:
        return render(req,"addmore.html")

def handler(a):
    sett=settings.objects.get_or_create()[0]
    sett.maintenance=True
    sett.save()
    js=json.loads(a.read())
    web=website.objects.get_or_create(url=js.pop(0),noof=0)
    showset=set()
    shows={}
    vid=[]
    for i in js:
        showset.update([i['show'].lower()])
    for j in showset:
        shows[j]=show.objects.get_or_create(name=j)
    for i in js:
        vid.append(videos(website=web[0],show=shows[i['show'].lower()][0],season=i['season'],episode=i['episode'],quality=i['quality'],url=i['url']))
    videos.objects.bulk_create(vid)
    sett.maintenance=False
    sett.save()