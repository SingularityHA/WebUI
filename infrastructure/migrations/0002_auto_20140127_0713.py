# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module_list',
            name='data',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
