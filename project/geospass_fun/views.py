<<<<<<< HEAD
from django.http import HttpResponse
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from geospaas.catalog.models import Dataset

def page(request):
    context = {'filename': ['I cant', 'believe', 'that', 'this works!']}
    return render(request, 'geospass_fun/index.html', context)

def  read_data(request):
#     #search by instrument
#      ds = Dataset.objects.filter(source__instrument__short_name='MODIS')
#       output = ';  '.join([str(d.time_coverage_start) for d in ds])
       output = "This suppose to be a list of data read with geospas models"
       return HttpResponse(output)

