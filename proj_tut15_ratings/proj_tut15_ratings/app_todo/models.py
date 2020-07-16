from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.


class Task(models.Model):
    task = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), default=None, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
