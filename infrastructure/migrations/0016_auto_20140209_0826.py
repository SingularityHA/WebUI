# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('infrastructure', '0015_devicestate')]

    operations = [
        migrations.DeleteModel(
            'DeviceState',
        ),
        migrations.AlterField(
            field = models.CharField(default='sensor', max_length=9, choices=(('sensor', 'Sensor',), ('actuator', 'Actuator',),)),
            name = 'type',
            model_name = 'device',
        ),
    ]
