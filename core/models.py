from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    unit = models.IntegerField()
    grade = models.CharField(max_length=1)


class StudySession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)


class PomodoroSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed_at = models.DateField(default=date.today)

class StudyEvent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title