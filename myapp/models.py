from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40)
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    def __str__(self):
        return f"user details {self.username} and {self.first_name} and {self.last_name} and {self.email} and {self.password}"