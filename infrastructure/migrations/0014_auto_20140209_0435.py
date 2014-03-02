# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0013_module_list_widget'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module_list',
            old_name='widget',
            new_name='widget_body',
        ),
        migrations.AddField(
            model_name='module_list',
            name='widget_js',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
