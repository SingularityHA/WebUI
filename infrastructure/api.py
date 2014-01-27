from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from infrastructure.models import Device, Module, Server, Module_List

class Module_ListResource(ModelResource):
	class Meta:
		queryset = Module_List.objects.all()
		filtering = {
			"name": ALL,
		}
		excludes = ('name', 'data')
		include_resource_uri = False

class ServerResource(ModelResource):

	class Meta:
		queryset = Server.objects.all()
		filtering = {
			"name": ALL_WITH_RELATIONS,
		}
		include_resource_uri = False

class ModuleResource(ModelResource):
	name = fields.CharField(attribute="module")
 	serverName = fields.CharField(attribute="server")
	server = fields.ForeignKey(ServerResource, 'server',full=False)
		
	class Meta:
		queryset = Module.objects.all()
		filtering = {
			"server": ALL_WITH_RELATIONS,
			"id": ALL_WITH_RELATIONS,
		}
		excludes = ('server')
		include_resource_uri = False

class DeviceResource(ModelResource):
	module = fields.ForeignKey(ModuleResource, 'module', full=False)
	moduleName = fields.CharField(attribute="module")

	class Meta:
        	queryset = Device.objects.all()
		filtering = {
			"module": ALL_WITH_RELATIONS,
		}
		include_resource_uri = False

