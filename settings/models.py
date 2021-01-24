from django.db import models

# Create your models here.

class Settings(models.Model):
    site_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Settings/')
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    description = models.TextField(max_length=500)
    fb_link = models.URLField( max_length=200)
    tw_link = models.URLField( max_length=200)
    in_link = models.URLField( max_length=200)
    

    def __str__(self):
        return self.site_name
