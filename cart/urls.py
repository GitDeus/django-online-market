from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.CartDetail, name='CartDetail'),
    url(r'^remove/(?P<id>\d+)/$', views.CartRemove, name='CartRemove'),
    url(r'^add/(?P<id>\d+)/$', views.CartAdd, name='CartAdd'),
]
