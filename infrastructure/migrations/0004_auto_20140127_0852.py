# encoding: utf8
from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0003_module_list_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module_list',
            name='data',
            field=jsonfield.fields.JSONField(max_length=255, blank=True),
        ),
    ]
