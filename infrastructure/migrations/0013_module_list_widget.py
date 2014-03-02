# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0012_auto_20140209_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='module_list',
            name='widget',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
