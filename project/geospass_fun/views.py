from django.http import HttpResponse
# Create your views here.

# #---
# #
import os, sys
#os.environ['DJANGO_SETTINGS_MODULE'] = 'geospaas_project.settings'
#sys.path.insert(0, '/vagrant/shared/course_vm/geospaas_project/')
#
import django
django.setup()
#
from django.conf import settings
from geospaas.catalog.models import Dataset
from geospaas.catalog.models import DatasetURI
# #---

def index(request):
    return HttpResponse("Hello, The details of the data  will be printed here: ")

#


def read_data(request):
    #search by instrument
    #ds = Dataset.objects.filter(source__instrument__short_name='MODIS')
    ds = Dataset.objects.all()
    output = ';  '.join([str(d.time_coverage_start) for d in ds])
    output= ' This time coverage start for >>>>>>>>: \n' + output \
            +'     >>>  from  data center=' + ';  '.join([str(d.data_center) for d in ds])
    #output = "This suppose to be a list of data read with geospas models"
    return HttpResponse(output)

# def read_data(request):
#     #----------
#     # search by instrument
#     #ds = Dataset.objects.filter(source__instrument__short_name='MODIS')
#     ds = Dataset.objects.all()
#     #output = ';  '.join([str(d.time_coverage_start) for d in ds])
#     #ds_array=[]
#     #for d in ds:
#          #print d.time_coverage_start
#     #    print str(d.time_coverage_start)
#     #    ds_array.append(str(d.time_coverage_start))
#     #return output
#     #print 'Time coverage start:'
#     print 'Data objects platform: all'
#     print '  -------------------------------------------------------------------  '
#     print '        Object      '  +    '                              file '
#     print '  -------------------------------------------------------------------  '
#     for d in ds:
#         print   str(d) +  '     ' + d.dataseturi_set.first().uri
#
#     #
#     print '    '
#     print '  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ '
#     print '    '
#     print '  List of more details ...............  '
#     print '    '
#     print '  -------------------------------------------------------------------  '
#     print '  Short name      '  + 'Time coverage start         Time coverage end  '
#     print '  -------------------------------------------------------------------  '
#     for d in ds:
#          #print d.time_coverage_start
#          print '  '+ d.source.instrument.short_name +'       '  +  \
#                 str(d.time_coverage_start) + '     ' + str(d.time_coverage_end)
















































































































































































































































































































































































































































































