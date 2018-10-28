from django.db import models

# Create your models here.
class settings(models.Model):
    maintenance=models.BooleanField(default=False)

class website(models.Model):
    url=models.URLField()
    noof=models.BigIntegerField(default=0)

    def __str__(self):
        return self.url

class show(models.Model):
    name=models.TextField()
    
    def __str__(self):
        return self.name

class videos(models.Model):
    website=models.ForeignKey(website,on_delete=models.CASCADE)
    show=models.ForeignKey(show,on_delete=models.CASCADE)
    season=models.IntegerField(default=1)
    episode=models.IntegerField(default=1)
    quality=models.TextField(default='0p')
    url=models.URLField()

    def __str__(self):
        return "%s s%de%d %s"%(self.show,self.season,self.episode,self.quality)