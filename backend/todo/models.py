from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50, unique=False, null=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} | {self.email}"