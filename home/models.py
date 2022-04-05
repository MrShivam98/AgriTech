from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    time = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.email


class driver(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(primary_key=True, max_length=50)
    phone = models.CharField(max_length=13)
    vehicle = models.CharField(max_length=10)
    timeStamp = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.email + ' - ' + self.vehicle


class service(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.TextField(max_length=100)
    weight = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user')
    driveby = models.ForeignKey(driver, on_delete=models.DO_NOTHING, related_name='driveby')
    timeStamp = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.phone
