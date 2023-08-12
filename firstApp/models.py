from django.db import models

# Create your models here.

class taskModel(models.Model): 
    taskNo = models.IntegerField(primary_key=True)
    taskTitle = models.CharField(max_length=40);
    taskDescription = models.CharField(max_length=100);
    is_completed = models.BooleanField()
    
    def __str__(self):
        return self.taskTitle
