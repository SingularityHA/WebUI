# encoding: utf8
from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=50),), ('ip', models.CharField(max_length=16),)],
            bases = (models.Model,),
            options = {},
            name = 'Server',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=50),), ('data', models.CharField(max_length=255),)],
            bases = (models.Model,),
            options = {},
            name = 'Module_List',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('module', models.ForeignKey(to='infrastructure.Module_List', to_field=u'id'),), ('server', models.ForeignKey(to='infrastructure.Server', to_field=u'id'),)],
            bases = (models.Model,),
            options = {},
            name = 'Module',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=50),), ('module', models.ForeignKey(to='infrastructure.Module', to_field=u'id'),), ('attributes', jsonfield.fields.JSONField(max_length=255, blank=True),)],
            bases = (models.Model,),
            options = {},
            name = 'Device',
        ),
    ]
