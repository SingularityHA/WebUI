# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0014_auto_20140209_0435'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceState',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('device', models.ForeignKey(to='infrastructure.Device', to_field=u'id')),
                ('state', models.CharField(max_length=255)),
                ('attributes', models.TextField(null=True, blank=True)),
                ('stateLock', models.BooleanField(default=False)),
                ('lastChange', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
