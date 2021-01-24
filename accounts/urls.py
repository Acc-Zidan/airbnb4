from django.urls import path
from .views import ItemList , ItemDetail

app_name = 'accounts'

urlpatterns = [
    path('', ItemList.as_view()),
    path('', ItemDetail.as_view())
]
