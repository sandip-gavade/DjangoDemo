from django.db import models


# Create your models here.


class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)
    elname = models.CharField(max_length=30)
    esal = models.FloatField()

    def __str__(self):
        return self.ename


class Person(models.Model):
    pno = models.IntegerField()
    pname = models.CharField(max_length=30)
    plname = models.CharField(max_length=30)
    psal = models.FloatField()

    def __str__(self):
        return self.pname
