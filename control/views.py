from django.shortcuts import render
from django.http import HttpResponse
import json

from infrastructure.models import Room, Device, Module, Module_List
from models import Statetable


# Create your views here.
def index(request):
	rooms = Room.objects.all()
	context = {"rooms" : rooms }
	return render(request, 'control/index.html', context)

def room(request, room_id):
	# Figure out which room we're talking to
	room = Room.objects.filter(id=room_id).get()
	
	modules = []
	actuator_modules = {}
	
	# Pull actuators for the room
	actuators = Device.objects.filter(room_id=room_id,type="actuator")
	for actuator in actuators.values():
		module = Module.objects.get(module_id=actuator["module_id"]).name_only()
		actuator_modules[actuator["name"]] = module
		modules.extend([module])
	
	# Pull modules and grab code to add to page
	modlist = list(set(modules))
	moduleData = {}
	for module in modlist:
		data = Module_List.objects.get(name=module)
		moduleDict = {"name": data.name, "widget_mqtt_js": data.widget_mqtt_js, "widget_setup_js": data.widget_setup_js, "widget_body": data.widget_body}
		moduleData[module] = moduleDict
		
	# Generate widgets to display on page
	actuators_to_template = []
	widget_setup = []
	for actuator in actuators.values():
		#print moduleData["limitlessLED"]
		#print actuator_modules
		if actuator["nice_name"] is None:
			actuator["nice_name"] = actuator["name"]
		#print actuator
		widget_html = moduleData[actuator_modules[actuator["name"]]]["widget_body"]
		widget_html = widget_html.replace("{{DeviceName}}", actuator["nice_name"])
		widget_html = widget_html.replace("{{DeviceShortName}}", actuator["name"])
		
		widget_setup_js = moduleData[actuator_modules[actuator["name"]]]["widget_setup_js"]
		widget_setup_js = widget_setup_js.replace("{{DeviceShortName}}", actuator["name"])
		widget_setup_js = widget_setup_js.replace("{{DeviceModule}}", moduleData[actuator_modules[actuator["name"]]]["name"])
		
		state = Statetable.objects.using('SingularityBase').get(device=actuator["name"])
		deviceAttributes = json.loads(state.attributes)
		deviceState = state.state
		
		widget_setup_js = widget_setup_js.replace("{{DeviceState}}", deviceState)
		
		if deviceAttributes['brightness']:
			widget_setup_js = widget_setup_js.replace("{{DeviceBrightness}}", deviceAttributes['brightness'])
		
		actuatorDict = { "name": actuator["name"], "widget_html": widget_html, "widget_setup_js": widget_setup_js }
		actuators_to_template.extend([actuatorDict])
		#print actuators_to_template
	
	context = { "room_name" : room.name, "actuators" : actuators_to_template, "modules" : moduleData }
	return render(request, 'control/room.html', context)
#	return HttpResponse("You picked room ID %s." % room_id)x
	
def keepalive(request):
    html = "OK"
    return HttpResponse(html)