from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    usertype = models.CharField(
        max_length=128,
        choices=[
            ("rider", "Rider"),
            ("driver", "Driver")
            
        ],
    )

    @property
    def fullname(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.username

    def __str__(self):
        return self.fullname