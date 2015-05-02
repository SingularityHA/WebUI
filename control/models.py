from django.db import models

# Create your models here.

class Statetable(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    device = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    attributes = models.TextField(blank=True)
    lock = models.IntegerField()
    lastchange = models.DateTimeField(db_column='lastChange')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'statetable'
