from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.serializers.json import DjangoJSONEncoder
from jsonfield import JSONField
import json

class Module_List(models.Model):
	name = models.CharField(max_length=50)
	package = models.CharField(max_length=255)
	data = models.TextField(max_length=255, blank=True)
	config = models.TextField(blank=True, null=True)
	actuatorfile = models.CharField(max_length=255, blank=True, null=True,verbose_name="Actuator file")

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
	
	def __unicode__(self):
        	return u'%s (%s)' % (self.module.name, self.server.name)

class Device(models.Model):
	name = models.CharField(max_length=50)
	module = models.ForeignKey(Module)	
	attributes = JSONField(max_length=255,blank=True)

	def __unicode__(self):
        	return u'%s' % (self.name)

def pre_device_save(sender, **kwargs):
	if kwargs['instance'].attributes is None:
		kwargs['instance'].attributes = json.loads(kwargs['instance'].module.module.data)
	print kwargs['instance'].attributes
pre_save.connect(pre_device_save, sender=Device)
