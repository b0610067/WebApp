from django.db import models
from django.db.models import CharField,DateField,ForeignKey,IntegerField
from django.contrib.auth.models import User

# Create your models here.
EVENT_TYPE = (('active','active'),('old','old'))

class Record(models.Model):
    date        = DateField()
    title       = CharField(max_length=300)
    description = CharField(max_length=300)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    event_type= CharField(max_length=2,choices=EVENT_TYPE)
    def __str__(self):
        return self.description
