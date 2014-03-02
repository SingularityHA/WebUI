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
	actuators = Device.objects.filter(room_id=room_id,type="actuator")
	for actuator in actuators.values():
		module = Module.objects.get(module_id=actuator["module_id"]).name_only()
		modules.extend([module])
	modlist = list(set(modules))
	moduleData = {}
	for module in modlist:
		data = Module_List.objects.get(name=module)
		dict = {"name": data.name, "widget_mqtt_js": data.widget_mqtt_js, "widget_setup_js": data.widget_setup_js, "widget_body": data.widget_body}
		moduleData[module] = dict
		print dict["widget_mqtt_js"]
	context = {"room_name" : room.name, "actuators" : actuators, "modules" : moduleData}
	return render(request, 'control/room.html', context)
#	return HttpResponse("You picked room ID %s." % room_id)x
	
