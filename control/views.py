from django.shortcuts import render
from django.http import HttpResponse

from infrastructure.models import Room, Device, Module, Module_List


# Create your views here.
def index(request):
	rooms = Room.objects.all()
	context = {"rooms" : rooms }
	return render(request, 'control/index.html', context)

def room(request, room_id):
	room = Room.objects.filter(id=room_id).get()
	modules = []
	actuator_modules = {}
	actuators = Device.objects.filter(room_id=room_id,type="actuator")
	for actuator in actuators.values():
		module = Module.objects.get(module_id=actuator["module_id"]).name_only()
		actuator_modules[actuator["name"]] = module
		modules.extend([module])
	modlist = list(set(modules))
	moduleData = {}
	for module in modlist:
		data = Module_List.objects.get(name=module)
		dict = {"name": data.name, "widget_mqtt_js": data.widget_mqtt_js, "widget_setup_js": data.widget_setup_js, "widget_body": data.widget_body}
		moduleData[module] = dict
	actuators_to_template = []
	for actuator in actuators.values():
		#print moduleData["limitlessLED"]
		#print actuator_modules
		if actuator["nice_name"] is None:
			actuator["nice_name"] = actuator["name"]
		#print actuator
		widget_html = moduleData[actuator_modules[actuator["name"]]]["widget_body"]
		widget_html = widget_html.replace("{{DeviceName}}", actuator["nice_name"])
		widget_html = widget_html.replace("{{DeviceShortName}}", actuator["name"])		
		dict = {"name": actuator["name"], "widget_html": widget_html}
		actuators_to_template.extend([dict])
		#print actuators_to_template
	context = {"room_name" : room.name, "actuators" : actuators_to_template, "modules" : moduleData}
	return render(request, 'control/room.html', context)
#	return HttpResponse("You picked room ID %s." % room_id)x
	
