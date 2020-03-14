from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import videos,settings
from .decor import maint_check
import json
# Create your views here.
@csrf_exempt
def showlist(req):
    if(req.POST):
        shows=req.POST["q"]
        res=videos.objects.filter(show__icontains=shows).order_by('show').values('show').distinct()
        showss=[data['show'] for data in res]
        print(res,shows)
        #return render(req,"showlist.html",{'objects':res})
        a=JsonResponse(showss,safe=False)
        #a['Access-Control-Allow-Origin']='http://localhost:8080'
        return a

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
    seasons=[data['season'] for data in res]
    #return render(req,'seasonlist.html',{'show':shows,'objects':res})
    a=JsonResponse(seasons,safe=False)
    #a['Access-Control-Allow-Origin']='http://localhost:8080'
    return a

def episodelist(req,shows,season):
    res=videos.objects.filter(show=shows,season=season).order_by('episode').values('episode').distinct()
    episodes=[data['episode'] for data in res]
    #return render(req,'episodelist.html',{'show':shows,'season':season,'objects':res})
    a=JsonResponse(episodes,safe=False)
    #a['Access-Control-Allow-Origin']='http://localhost:8080'
    return a

def qualitylist(req,shows,season,episode):
    res=videos.objects.filter(show=shows,season=season,episode=episode).order_by('quality').values('quality').distinct()
    qualities=[data["quality"] for data in res]
    #return render(req,'qualitylist.html',{'show':shows,'season':season,'episode':episode,'objects':res})
    a=JsonResponse(qualities,safe=False)
    #a['Access-Control-Allow-Origin']='http://localhost:8080'
    return a

def videoplayer(req,shows,season,episode,quality):
    res=videos.objects.filter(show=shows,season=season,episode=episode,quality=quality).values('url')
    urls=[data['url'] for data in res]
    #return render(req,'videop.html',{'show':shows,'season':season,'episode':episode,'quality':quality,'objects':res})
    a=JsonResponse(urls,safe=False)
    #a['Access-Control-Allow-Origin']='http://localhost:8080'
    return a

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
    videos.objects.bulk_create(vid,ignore_conflicts=True)
    sett.maintenance=False
    sett.save()