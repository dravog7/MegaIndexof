import requests
from bs4 import BeautifulSoup
import asyncio
from urllib.parse import urlparse,urljoin
from threading import Thread
try:
    from .utils import CancelandExcept
except:
    from utils import CancelandExcept

class Crawler(Thread):
    def __init__(self,q,links,stop,count=3):
        Thread.__init__(self)
        self.q = q
        self.links = links
        self.stop = stop
        self.futures={}
        self.count=count

    async def tillstop(self):
        while self.stop['signal']:
            await asyncio.sleep(1)
        for future in self.futures.values():
            future.cancel()
        print("exited")
        return 0

    def run(self):
        #process q.get() and output files to link.put()
        try:
            loop = asyncio.new_event_loop()
            for _ in range(self.count):
                loop.create_task(self.main())
            loop.run_until_complete(self.tillstop())
        except:
            print("error")
        return 0

    async def main(self):
        try:
            #print("start main")
            while self.stop['signal']:
                url = await self.qget()
                print(url)
                #check type of url
                req = await self.head(url[1])
                print(req)
                if(not req):
                    continue
                if(self.checkType(contentType=req.headers)):
                    req = await self.get(url[1])
                    if(not req):
                        continue
                    tags = BeautifulSoup(req.content,features="html.parser").find_all("a")
                    for ele in tags:
                        urlc = ele.attrs['href']
                        typ = self.urlfilter(urlc,url)
                        if(not typ):
                            continue
                        elif(typ[0]=="html"):
                            self.q.put([url[1],typ[1]]) #add to q
                        elif(typ[0]=="media"):
                            self.links.put(typ[1]) #add to links
            print("exit")
        except asyncio.CancelledError:
            print("cancelled")
        except Exception as e:
            print("error stop!"+str(e))
        return 0


    def urlfilter(self,urlc,url):
        #return html/media/None for each url
        urlc = urljoin(url[1],urlc)
        components = urlparse(urlc)
        old = urlparse(url[1])

        if(old.netloc!=components.netloc): # if not same website
            return None
        if(url[1].count("/")>urlc.count("/")): #if going up tree
            return None

        typ = self.checkType(url=urlc)
        if(typ):
            if(url[1].count("/")==urlc.count("/")): #no traversing sibling
                return None
            return ("html",urlc)
        else:
            return ("media",urlc)

    @CancelandExcept
    def qget(self):
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None,self.q.get)
        return future

    @CancelandExcept
    def head(self,url):
        print("in head")
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None,requests.head,url)
        print("gotfuture")
        return future

    @CancelandExcept
    def get(self,url):
        print("in get")
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None,requests.get,url)
        return future
    
    def checkType(self,url="",contentType=""):
        #if the url is not html\htm\blank
        if(url!=""):
            path = urlparse(url).path
            slashIndex = path.rfind("/")
            if(slashIndex!=-1):
                dotIndex = path[slashIndex:].rfind(".")
                if(dotIndex!=-1):
                    if(path[dotIndex:] in [".html",".htm"]):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return True

        elif(contentType!=""):
            contentType = contentType['Content-Type']
            if(("/html" in contentType)|("/htm" in contentType)):
                return True
            else:
                return False
        return False