# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0002_auto_20140127_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='module_list',
            name='config',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
