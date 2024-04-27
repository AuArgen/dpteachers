from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', logins, name='login'),
    path('logout/', logouts, name='logout'),
]
