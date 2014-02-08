# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0007_module_list_actuatorfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='config',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='module_list',
            name='config',
        ),
        migrations.AlterField(
            model_name='module_list',
            name='actuatorfile',
            field=models.CharField(max_length=255, null=True, verbose_name='Actuator file', blank=True),
        ),
    ]
