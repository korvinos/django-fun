# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render

# def page(request):
    # return render(request, 'home/index.html')
    
def index(request):
    return render(request, 'home/index.html')
    
def header(request):
    return render(request, 'home/header.html')
    
def footer(request):
    return render(request, 'home/footer.html')
    
def body(request):
    return render(request, 'home/body.html')