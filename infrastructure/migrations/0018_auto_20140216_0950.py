# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0017_module_list_widget_setup_js'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module_list',
            old_name='widget_js',
            new_name='widget_mqtt_js',
        ),
    ]
