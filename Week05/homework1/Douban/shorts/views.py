from django.shortcuts import render
from .models import Shorts
from django.http import HttpResponse


# Create your views here.


def shorts(request):
    infos = Shorts.objects.filter(stars__gt=3).order_by('-stars')  # 倒序
    if 'q' in request.GET:
        infos = Shorts.objects.filter(shorts__contains=request.GET.get(
            'q')).order_by('-stars')  # 写法2  infos = Shorts.objects.filter(shorts__contains=request.GET['q'])
    return render(request, 'shorts.html', locals())


def index(request):
    infos = Shorts.objects.all().order_by('-stars')
    if 'q' in request.GET:
        infos = Shorts.objects.filter(shorts__contains=request.GET.get(
            'q')).order_by('-stars')
    return render(request, 'shorts.html', locals())
