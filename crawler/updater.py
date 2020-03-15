from threading import Thread
from mains.models import videos
import time
class Updater(Thread):
    def __init__(self,out):
        Thread.__init__(self)
        self.out = out
        self.arr=[]
    
    def run(self):
        time1 = time.time() #update every 2 mins
        while True:
            try:
                val = self.out.get(timeout=10)
                print("updater",val)
                self.process(val)
            except:
                pass
            time2 = time.time()
            if((len(self.arr)>0)and(abs(time2-time1)>=60)):
                print("bulk create")
                videos.objects.bulk_create(self.arr,ignore_conflicts=True)
                self.arr = []
                time1 = time.time()
    
    def process(self,fields):
        a = videos(**fields)
        self.arr.append(a)