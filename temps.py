from mains.models import videos
import re
a=videos.objects.filter(show__name='supernatural')
count=a.count()
st=0
for i in a:
    m=i.url[i.url.rindex('/')+1:].lower()
    m=re.split(' |\.|-|_|e',m)
    season=1
    episode=1
    for j in m:
        try:
            if(j[0]=='s'):
                season=int(j[1:])
            if(j[0]=='e'):
                episode=int(j[1:])
            if(j.isdigit()):
                episode=int(j)
        except:
            continue
    i.season=season
    i.episode=episode
    i.save()
    st+=1
    print(st,'out of',count)