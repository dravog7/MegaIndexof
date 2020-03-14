from queue import Queue
import asyncio
try:
    from crawler import Crawler
    from scrap import scrap
except:
    from .crawler import Crawler
    from .scrap import scrap
    from .updater import Updater

async def pri(q,stop):
    loop = asyncio.get_event_loop()
    try:
        while stop['signal']:
            val=await loop.run_in_executor(None,q.get)
            if(val):
                print(val)
        print("exit")
    except:
        pass

async def inp(stop):
    try:
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None,input,"input")
        stop['signal']=False
    except:
        pass

q = Queue()
links = Queue()
out = Queue()
start_url=["","http://s6.bitdl.ir/"]

stop={"signal":True}
th = Crawler(q,links,stop)
sc = scrap(links,out)
q.put(start_url)
print("start")
try:
    th.start()
    sc.start()
    loop = asyncio.get_event_loop()

    loop.create_task(inp(stop))
    loop.create_task(pri(out,stop))
    
    loop.run_forever()
    print("exit2")
    th.join()
    sc.join()
except:
    print("error end")