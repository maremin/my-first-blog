'''
GG
'''

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import FB
import ftplib
from django.http import HttpResponse


def index(request):
    return render(request, 'first/index.html', {})

def crm(request):
    return render(request, 'first/crm.html', {})

def crm_insert(request):
    a = FB(email = request.POST['email_fb'], text = request.POST['text_fb'])
    a.save()
    return HttpResponseRedirect(reverse('index'))