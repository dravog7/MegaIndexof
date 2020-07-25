from threading import Thread
from .models import videos
import requests
import re
def updateseries(showname):
    urls=videos.objects.filter(show=showname,flat=True)
    parsed=set()
    for i in urls:
        a=re.search('(.)+((?i)/s[0-9]|season[0-9])',i)
        if(a):
            a=a.group()
            a=a[:a.rindex('/')]
            parsed.update([a])
    #add crawler and process and handler
