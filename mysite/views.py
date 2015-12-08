# -*- coding: utf-8 -*-
__author__ = 'junerain'

from django.http import HttpResponse

def first_page(request):
    return HttpResponse("<p><b>世界好</b></p>")