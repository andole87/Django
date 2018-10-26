from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.audio_list, name='audio_list'),
    url(r'^audio/(?P<i>\d+)/$', views.audio_detail, name='details'),
    url(r'^search/(?P<title>.*)/$', views.audio_search, name='audio_search'),
]
