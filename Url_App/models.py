from hashlib import md5
from django.db import models

# Create your models here.
class Url(models.Model):
    Your_url = models.CharField(unique=True, max_length=500)
    short_url = models.CharField(unique=True, max_length=20)
    
    def __str__(self):
        return self.Your_url
    
    @classmethod
    def create(self, Your_url):
        temp_url = md5(Your_url.encode()).hexdigest()[:6]
        try :
            obj = self.objects.create(Your_url = Your_url, short_url = temp_url)
        except:
            obj = self.objects.get(Your_url = Your_url)
        return obj    
         
    
