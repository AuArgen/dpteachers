from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from children.models import Child
from docchild.models import DocChild
from klass.models import Klass
from news.models import News
from raspisanie.models import Raspisanie


@login_required
def home(request):
    news = News.objects.all().order_by('-id')
    context = {'news': news}
    return render(request, 'child/index.html', context)


@login_required
def raspisanie(request):
    DAYS_OF_WEEK = [
        'Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница',
        'Суббота',
        'Воскресенье',
    ]
    child = Child.objects.get(child=request.user)
    raspisanie = Raspisanie.objects.filter(klass=child.klass).order_by('saat__saat_start')
    ras = [];
    for i in DAYS_OF_WEEK:
        ra = []
        for j in raspisanie.filter(day=i):
            ra.append(j)
        ras.append(ra)
    context = {'raspisanie': ras}
    return render(request, 'child/raspisanie.html', context)


@login_required
def document(request):
    child = Child.objects.get(child=request.user)
    childDoc = DocChild.objects.filter(child=child).order_by('-id')
    context = {'childDoc': childDoc}
    return render(request, 'child/doc.html', context)
