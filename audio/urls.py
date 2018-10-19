from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.audio_list, name='audio_list'),
    url(r'^audio/(?P<pk>\d+)/$', views.audio_detail, name = 'audio_detail'),
]
