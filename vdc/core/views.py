# coding: utf-8

from django.shortcuts import render


def home(request):
    """ Exibe a home """
    return render(request, 'home.html')