from re import M
from django.db import models
from django.contrib.auth.models import User
from asyncio.windows_events import NULL
import datetime
class Student(models.Model):
    user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    mob=models.CharField(max_length=12)
    address=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    edt=models.DateField(auto_now=False)
    remarks=models.CharField(max_length=100,default=None)
    name=models.CharField(max_length=20,default=None)
    def __str__(self) -> str:
        return self.course
class Joined(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    joined_dt=models.DateField(auto_now=False)
    total=models.IntegerField()
    first_ins=models.IntegerField()
    first_dt=models.DateField(auto_now=False)
    last_ins=models.IntegerField()
    last_dt=models.DateField(auto_now=False)
    duration=models.CharField(max_length=20)
    dues=models.IntegerField(default=0)
    def __str__(self) -> str:
        return str(self.last_dt.strftime("%Y-%m-%d"))
class Batch(models.Model):
    students=models.ManyToManyField(Joined)
    start_dt=models.DateField(auto_now=False)
    trainer=models.CharField(max_length=20)
    bname=models.CharField(max_length=20)
    def __str__(self) -> str:
        return str(self.start_dt.strftime("%Y-%m-%d"))
class Trainer(models.Model):
    tname=models.CharField(max_length=20)
    languages=models.CharField(max_length=20)
    sal=models.IntegerField()
    joined_dt=models.DateField( auto_now=False)
    timings=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.tname
    
    

   