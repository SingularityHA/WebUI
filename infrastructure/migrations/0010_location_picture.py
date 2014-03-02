# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0009_auto_20140208_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='picture',
            field=models.CharField(default='img/rooms/blank.png', max_length=50),
            preserve_default=True,
        ),
    ]
