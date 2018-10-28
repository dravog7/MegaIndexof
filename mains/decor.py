from mains.models import settings
from django.shortcuts import render
def maint_check(func):
    def wrapper(a):
        sett=settings.objects.get_or_create()[0]
        if not(sett.maintenance):
            print(sett.maintenance)
            b=func(a)
        else:
            b=render(a,'maint.html')
        return b
    return wrapper