from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import videos,website,settings
from .decor import maint_check
import json
# Create your views here.
def showlist(req):
    if(req.POST):
        shows=req.POST["q"]
        res=videos.objects.filter(show__icontains=shows).order_by('show').values('show').distinct()
        print(res,shows)
        return render(req,"showlist.html",{'objects':res})

def viewredirect(req,shows,season=0,episode=0,quality=''):
    if(season==0):
        return seasonlist(req,shows)
    elif(episode==0):
        return episodelist(req,shows,season)
    elif(quality==''):
        return qualitylist(req,shows,season,episode)
    else:
        return videoplayer(req,shows,season,episode,quality)
    return Http404()

def seasonlist(req,shows):
    res=videos.objects.filter(show=shows).order_by('season').values('season').distinct()
    return render(req,'seasonlist.html',{'show':shows,'objects':res})

def episodelist(req,shows,season):
    res=videos.objects.filter(show=shows,season=season).order_by('episode').values('episode').distinct()
    return render(req,'episodelist.html',{'show':shows,'season':season,'objects':res})

def qualitylist(req,shows,season,episode):
    res=videos.objects.filter(show=shows,season=season,episode=episode).order_by('quality').values('quality').distinct()
    return render(req,'qualitylist.html',{'show':shows,'season':season,'episode':episode,'objects':res})

def videoplayer(req,shows,season,episode,quality):
    res=videos.objects.filter(show=shows,season=season,episode=episode,quality=quality).values('url')
    return render(req,'videop.html',{'show':shows,'season':season,'episode':episode,'quality':quality,'objects':res})

def searchView(req):
    return render(req,"index.html")

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
    vid=[]
    for i in js:
        vid.append(videos(website=web[0],show=i['show'].lower(),season=i['season'],episode=i['episode'],quality=i['quality'],url=i['url']))
    videos.objects.bulk_create(vid)
    sett.maintenance=False
    sett.save()