# coding: utf-8

import datetime

from django.utils.timezone import utc
# from django.http import HttpResponse
from django.shortcuts import render


TODAY = datetime.datetime.utcnow().replace(tzinfo=utc)


def home(request):
    """ Carrega página inicial """
    return render(request, 'home.html')
