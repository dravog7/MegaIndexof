from threading import Thread
import re
from urllib.parse import unquote,urlparse
class scrap(Thread):
    def __init__(self,links,out,filetypes=[".mov",".wmv",".mp4",".mkv",".flv",".avi",".m4v"]):
        Thread.__init__(self)
        self.links = links
        self.out = out
        self.filetypes = filetypes
    
    def run(self):
        #wait for links.get() and output to out.put()
        while True:
            url = self.links.get()
            print(url)
            entry={'website':urlparse(url).netloc,
                    'show':'',
                    'season':'',
                    'episode':'',
                    'quality':'',
                    'url':'',
                    'folder':''}
            fileformat=url[url.rindex('.'):]
            if(fileformat.lower() in self.filetypes):
                path=unquote(urlparse(url).path).lower()
                entry["season"]=self.getseason(path)
                entry['episode']=self.getepisode(path)
                entry['quality']=self.getquality(path)
                entry['show']=self.getshow(path)
                entry['url']=url
                entry['folder']=path[:path.rfind("/")+1]

                if(self.isdubbed(path)):
                    continue
                if(entry['show']=='unknwn'):
                    continue
                self.out.put(entry)
    
    def getseason(self,a):
        s=re.search('s[0-9]+',a)
        if not(s):
            s=re.search('season(\.| |_)[0-9]+',a)
            if not(s):
                return 1
            return int(s.group()[7:])
        return int(s.group()[1:])

    def getepisode(self,a):
        s=re.search('e[0-9]+',a)
        if not(s):
            s=re.search('ep[0-9]+',a)
            if not(s):
                return 1
            return int(s.group()[2:])
        return int(s.group()[1:])

    def getquality(self,a):
        qualities=['480','720','1080','2160']
        rep='('+"|".join(qualities)+')'
        s=re.search(rep,a)
        if not(s):
            return 'unknwn'
        return s.group()+'p'

    def getshow(self,a):
        qualities=['480','720','1080','2160']
        rep="|".join(qualities)
        s=re.findall('/([a-z| |\.|-|_]+)(?:/|\.|_|-)(?:(?:s[0-9]+)|'+rep+'|E/)',a)
        if not(s):
            return 'unknwn'
        m=s[0]
        return re.sub("(\.| |_|-)"," ",m).strip()

    def isdubbed(self,a):
        a=re.findall('(dubbed)',a)
        return True if a else False