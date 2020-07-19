from django.urls import path
from .views import index, about, contacts, add

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),
    path('add', add, name='add'),
]
