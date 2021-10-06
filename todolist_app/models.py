from django.db import models
from django.contrib.auth.models import User

class TaskList(models.Model):           #created a database-model

    #CASCADE -> DELETE EVERYTHING TILL INITIATE
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)

    def __str__(self):                           #just to show name of task in admin
        return (self.task+" - "+str(self.done))
