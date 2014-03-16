from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.serializers.json import DjangoJSONEncoder
from jsonfield import JSONField
import json

class Module_List(models.Model):
	name = models.CharField(max_length=50)
	package = models.CharField(max_length=255)
	actuatorfile = models.CharField(max_length=255, blank=True, null=True,verbose_name="Actuator file")
	data = models.TextField(max_length=255, blank=True)
	widget_setup_js = models.TextField(blank=True, null=True)
	widget_mqtt_js = models.TextField(blank=True, null=True)
	widget_body = models.TextField(blank=True, null=True)

	def __unicode__(self):
        	return u'%s' % (self.name)

class Server(models.Model):
	name = models.CharField(max_length=50)
	ip = models.CharField(max_length=16)
	
	def __unicode__(self):
        	return u'%s' % (self.name)

class Module(models.Model):
	module = models.ForeignKey(Module_List)
	server = models.ForeignKey(Server)	
	config = models.TextField(blank=True, null=True)
	
	def name_only(self):
		return self.module.name

	def __unicode__(self):
        	return u'%s (%s)' % (self.module.name, self.server.name)

class Room(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True, null=True)
	picture = models.CharField(max_length=50,default="img/rooms/blank.png")

	def __unicode__(self):
        	return u'%s' % (self.name)

class Device(models.Model):
	TYPE_CHOICES = (('sensor', 'Sensor'),
                    ('actuator', 'Actuator'))
	name = models.CharField(max_length=50)
	nice_name = models.CharField(max_length=255,blank=True,null=True)
	module = models.ForeignKey(Module)	
	type = models.CharField(max_length=9, choices=TYPE_CHOICES, default="sensor")
	attributes = JSONField(max_length=255,blank=True)
	room = models.ForeignKey(Room)

	def __unicode__(self):
        	return u'%s' % (self.name)

def pre_device_save(sender, **kwargs):
	if kwargs['instance'].attributes is None:
		kwargs['instance'].attributes = json.loads(kwargs['instance'].module.module.data)
	print kwargs['instance'].attributes
pre_save.connect(pre_device_save, sender=Device)
