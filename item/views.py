from django.shortcuts import render
from  django.views.generic import ListView ,  DetailView
from .models import Item

# Create your views here.


class ItemList(ListView):
   model = Item
   paginate_by = 12

##filtter

class ItemDetail(DetailView):
    model = Item

##book
