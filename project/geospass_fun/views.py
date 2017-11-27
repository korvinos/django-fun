from django.http import HttpResponse
# Create your views here.

# #---
# #
#import os, sys
#os.environ['DJANGO_SETTINGS_MODULE'] = 'geospaas_project.settings'
#sys.path.insert(0, '/vagrant/shared/course_vm/geospaas_project/')
#
#import django
#django.setup()
#
from django.conf import settings
from geospaas.catalog.models import Dataset
# from geospaas.catalog.models import DatasetURI
# #---



def index(request):
    return HttpResponse("Hello, The details of the data  will be printed here: ")

#
def  read_data(request):
#     #search by instrument
#      ds = Dataset.objects.filter(source__instrument__short_name='MODIS')
#       output = ';  '.join([str(d.time_coverage_start) for d in ds])
       output = "This suppose to be a list of data read with geospas models"
       return HttpResponse(output)