from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Task: {self.title},  {self.date}'