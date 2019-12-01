from django.db import models
from django.db.models import CharField,DateField,ForeignKey,IntegerField
from django.contrib.auth.models import User

# Create your models here.
BALANCE_TYPE = ((u'收入',u'收入'),(u'支出',u'支出'))

class Category(models.Model):
    category = CharField(max_length=20)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.category

class Record(models.Model):
    date        = DateField()
    description = CharField(max_length=300)
    category    = ForeignKey(Category,on_delete=models.CASCADE,null=True)
    cash        = IntegerField()
    balance_type= CharField(max_length=2,choices=BALANCE_TYPE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
