import asyncio
from threading import Thread
from mains.models import videos
class Updater(Thread):
    def __init__(self,out):
        Thread.__init__(self)
        self.out = out
        self.arr=[]
    
    def run(self):
        while True:
            self.process(self.out.get())
            if(len(self.arr)>10):
                videos.objects.bulk_create(self.arr,ignore_conflicts=True)
                self.arr = []
    
    def process(self,fields):
        a = videos(**fields)
        self.arr.append(a)