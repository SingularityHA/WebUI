# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0011_auto_20140209_0308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='Room',
            new_name='room',
        ),
        migrations.AddField(
            model_name='device',
            name='type',
            field=models.CharField(default='sensor', max_length=9, choices=[('sensor', 'Sensor'), ('actuator', 'Actuator')]),
            preserve_default=True,
        ),
    ]
