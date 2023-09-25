from django.db import models

# Create your models here.
class TodoUser(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.username}'

class Session(models.Model):
    key = models.CharField(max_length=64, unique=True)
    user = models.OneToOneField(TodoUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.key}'

class Task(models.Model):
    user = models.OneToOneField(TodoUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=128)
    content = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.name}'