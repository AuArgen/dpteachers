from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('raspisanie/', raspisanie, name='raspisanie'),
    path('doc/', document, name='document'),
    path('login/', logins, name='login'),
    path('logout/', logouts, name='logout'),
]
