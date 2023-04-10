from django.db import models
from app.models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profilepics/')
    shortdesc = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
