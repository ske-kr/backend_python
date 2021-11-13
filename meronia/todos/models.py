from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_by = models.CharField(max_length=20, default="meronia")

    def __str__(self):
        return self.title

    def get_assignee(self):
        return self.created_by
