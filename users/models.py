from django.db import models
from django.contrib.auth.models import User as Django_user
from app.models import Post


class Profile(models.Model):
    user = models.OneToOneField(Django_user, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profilepics/')
    shortdesc = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class User(Django_user):
    likes = models.IntegerField(default=0)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
