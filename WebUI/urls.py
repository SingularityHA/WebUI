from django.conf.urls import patterns, include, url
from rest_framework import routers
from infrastructure import views

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/groups', views.GroupViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebUI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

