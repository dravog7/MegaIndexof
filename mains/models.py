from django.db import models

# Create your models here.
class settings(models.Model):
    maintenance=models.BooleanField(default=False)

class videos(models.Model):
    website=models.CharField(default="",max_length=300)
    show=models.TextField(default="")
    season=models.IntegerField(default=1)
    episode=models.IntegerField(default=1)
    quality=models.TextField(default='0p')
    url=models.URLField(max_length=1000,unique=True)
    folder = models.URLField(max_length=1000)

    def __str__(self):
        return "%s s%de%d %s"%(self.show,self.season,self.episode,self.quality)