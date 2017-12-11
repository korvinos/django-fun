from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^read_data$', views.read_data, name='read_data'),
    url(r'^$', views.page, name='page'),
]