from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from news.models import News


@login_required
def home(request):
    news = News.objects.all().order_by('-id')
    context = {'news': news}
    return render(request, 'child/index.html', context)
