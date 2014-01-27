# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0004_auto_20140127_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module_list',
            name='data',
            field=models.TextField(max_length=255, blank=True),
        ),
    ]
