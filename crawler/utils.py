import asyncio
import sys

def CancelandExcept(func):
    async def decor(self,*args,**kwargs):
        try:
            future=func(self,*args,**kwargs)
            ids = str(future)
            self.futures[ids]=future
            print("awaiting future")
            value = await future
            print(value)
            del self.futures[ids]
            return value
        except asyncio.CancelledError as e:
            print("cancelled")
        except:
            print("err:",sys.exc_info()[0])
    return decor
