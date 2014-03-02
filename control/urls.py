from django.conf.urls import patterns, url

from control import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^room/(?P<room_id>\d+)/$', views.room, name='room'),
)
