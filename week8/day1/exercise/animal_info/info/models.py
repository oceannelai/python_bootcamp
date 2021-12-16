

# Create your models here.
from django.db import models

# Create your models here.
class Family(models.Model):
    class Meta:
        db_table = 'family'

    # models.AutoField() same as serial in postgres
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Animals(models.Model):
    class Meta:
        db_table = 'animals'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.IntegerField()
    family_id = models.IntegerField()
    def __str__(self):
        return self.name


