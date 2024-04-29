from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='children'),
    path('raspisanie/', raspisanie, name='children-raspisanie'),
]
