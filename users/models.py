from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profilepics/')
    shortdesc = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"