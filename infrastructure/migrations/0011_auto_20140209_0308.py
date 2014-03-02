# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0010_location_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True, blank=True)),
                ('picture', models.CharField(default='img/rooms/blank.png', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AddField(
            model_name='device',
            name='Room',
            field=models.ForeignKey(to='infrastructure.Room', default=1, to_field=u'id'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='device',
            name='location',
        ),
    ]
