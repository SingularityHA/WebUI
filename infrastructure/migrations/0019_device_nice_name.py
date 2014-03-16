# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0018_auto_20140216_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='nice_name',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
