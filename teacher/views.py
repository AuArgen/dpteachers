from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from children.models import Child
from news.models import News
from raspisanie.models import Raspisanie
from teacher.models import Teacher, DocTeacher


@login_required
def home(request):
    news = News.objects.all().order_by('-id')
    context = {'news': news}
    return render(request, 'teacher.html', context)



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
    teacher = Teacher.objects.get(user=request.user)
    raspisanie = Raspisanie.objects.filter(teacher=teacher).order_by('saat__saat_start')
    ras = [];
    for i in DAYS_OF_WEEK:
        ra = []
        for j in raspisanie.filter(day=i):
            ra.append(j)
        ras.append(ra)
    context = {'raspisanie': ras}
    return render(request, 'raspisanie.html', context)


@login_required
def document(request):
    teacher = Teacher.objects.get(user=request.user)
    teacherDoc = DocTeacher.objects.filter(teacher=teacher).order_by('-id')
    context = {'teacherDoc': teacherDoc}
    return render(request, 'doc.html', context)


def logins(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if Child.objects.filter(child=user).exists():
                return redirect('children')
            return redirect('home')
        messages.error(request, 'Логин же пароль туура эмес')
    return render(request, 'login.html')


def logouts(request):
    logout(request)
    return redirect('login')
