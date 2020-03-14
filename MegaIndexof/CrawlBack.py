from django.conf import settings
import sys
from crawler.crawler import Crawler
from crawler.scrap import scrap
from crawler.updater import Updater
CRAWL = settings.CRAWL
LINK = settings.LINK
OUT = settings.OUT
STOP = settings.STOP

THREADS = [Crawler(CRAWL,LINK,STOP,10),scrap(LINK,OUT),Updater(OUT)]


def startup():
    if('makemigrations' in sys.argv or 'migrate' in sys.argv):
        return
    for i in THREADS:
        i.start()