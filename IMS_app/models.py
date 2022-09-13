from pyexpat import model
from django.db import models
from telnetlib import STATUS


# Create your models here.


class Supervisor(models.Model):
    
    name = models.CharField(max_length=200,null=True)
    phone =models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)

    def __str__(self):
        return str(self.name)
    
class Intern(models.Model):

    name = models.CharField(max_length=200,null=True)
    phone =models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.name)

class Assign_task(models.Model):
    title = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=200, null=True)
    allot_to = models.ManyToManyField(Intern)
    alloted_by = models.ManyToManyField(Supervisor)
    date_created = models.DateField(auto_now=True,null=True)
    due_date = models.DateField(blank=True, null=True)
    
    
    def __str__(self):
        return str(self.title)

class Attendence(models.Model):
    STATUS =(
        ('Present','Present'),
        ('Absent','Absent'),
        )
    
    intern_id= models.ForeignKey(Intern, null=True,on_delete=models.CASCADE)
    status = models.CharField(max_length=10,null=True,choices=STATUS)
    attendence_date = models.DateField(blank=True,null=True)


class Task_for_intern(models.Model):
    intern = models.ManyToManyField(Intern)
    title = models.ForeignKey(Assign_task,on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.title)
    