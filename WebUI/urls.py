from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from infrastructure.api import Module_ActuatorResource, Module_ListResource, ServerResource, ModuleResource, DeviceResource

v1_api = Api(api_name='v1')
v1_api.register(Module_ActuatorResource())
v1_api.register(Module_ListResource())
v1_api.register(ServerResource())
v1_api.register(ModuleResource())
v1_api.register(DeviceResource())


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebUI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^control/', include('control.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^keepalive', 'control.views.keepalive', name="keepalive"),
)

