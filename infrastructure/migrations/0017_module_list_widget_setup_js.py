# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0016_auto_20140209_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='module_list',
            name='widget_setup_js',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
