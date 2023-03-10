from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=160)
    link = models.URLField()
    teacher = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.title
