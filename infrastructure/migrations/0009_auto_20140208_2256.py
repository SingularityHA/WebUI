# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('infrastructure', '0008_auto_20140201_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='device',
            name='location',
            field=models.ForeignKey(to='infrastructure.Location', default='undefined', to_field=u'id'),
            preserve_default=False,
        ),
    ]
