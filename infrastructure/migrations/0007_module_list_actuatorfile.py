# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0006_auto_20140127_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='module_list',
            name='actuatorfile',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
