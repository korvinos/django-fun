# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render

def page(request):
    context = {'filename': ['I cant', 'believe', 'that', 'this works!']}
    return render(request, 'geospass_fun/index.html', context)