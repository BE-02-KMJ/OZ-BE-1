from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=20)
#     description = models.TextField()
#     age = models.PositiveIntegerField(null=True)
#     gender = models.CharField(max_length=10)

#     def __str__(self):
#         # return self.name
#         return f"{self.name} / ({self.age}살)"  # f-string 사용 가능

class User(AbstractUser):
    is_business = models.BooleanField(default=False)
    grade = models.CharField(max_length=10, default='C')