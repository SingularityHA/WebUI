# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0005_auto_20140127_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='module_list',
            name='package',
            field=models.CharField(default='Empty', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='module_list',
            name='config',
            field=models.TextField(null=True, blank=True),
        ),
    ]
