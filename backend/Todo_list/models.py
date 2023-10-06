from django.db import models
from Todo_users.models import Users
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(Users,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.title
    
    