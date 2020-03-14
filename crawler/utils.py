import asyncio
import sys

def CancelandExcept(func):
    async def decor(self,*args,**kwargs):
        try:
            future=func(self,*args,**kwargs)
            ids = str(future)
            self.futures[ids]=future
            value = await future
            del self.futures[ids]
            return value
        except asyncio.CancelledError as e:
            pass
        except:
            print("err:",sys.exc_info()[0])
    return decor
