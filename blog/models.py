from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    auther = models.ForeignKey(User, related_name='post_auther', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    tags = TaggableManager()
    image = models.ImageField(upload_to='Post/')
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=15000)
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.title)
       super(Post, self).save(*args, **kwargs) # Call the real save() method


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


    
