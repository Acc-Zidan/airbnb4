from typing import Reversible
from django.db import models
from django.contrib.auth.forms import User
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Item/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
    place = models.ForeignKey('Place', related_name='item_place', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='item_category', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.name)
       super(Item, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return Reversible("model_detail", kwargs={"slug": self.slug})
    

    
class ItemImage(models.Model):
    item = models.ForeignKey('Item', related_name='item_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ItemImages/')

    def __str__(self):
        return str(self.item)


class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='place/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ItemReview(models.Model):
    auther = models.ForeignKey(User, related_name='review_auther', on_delete=models.CASCADE)
    item  = models.ForeignKey(Item , related_name='review_item', on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    feedback = models.CharField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.item)




class Itembook(models.Model):
    user = models.ForeignKey(User, related_name='book_owner', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='book_item', on_delete=models.CASCADE)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    qnty = models.IntegerField(default=1)



    def __str__(self):
        return str(self.item)




