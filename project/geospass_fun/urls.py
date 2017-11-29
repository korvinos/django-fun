from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.page, name='page'),
    #url(r'^$', views.header, name='header'),
]