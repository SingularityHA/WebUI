from django.contrib import admin
from infrastructure.models import Server,Module,Module_List,Device

class ModuleAdmin(admin.ModelAdmin):
	list_filter = ['server']
	list_display = ('module', 'server')
	
	def author_name(self, instance):
        	return instance.server.name

class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1

class ServerAdmin(admin.ModelAdmin):
	inlines = [ModuleInline]

class DeviceAdmin(admin.ModelAdmin):
	list_display = ('name', 'module')

admin.site.register(Server, ServerAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Module_List)
admin.site.register(Device, DeviceAdmin)
