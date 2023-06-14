from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class Post(models.Model):
    title = models.CharField(max_length=155)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="posts")

    class Meta:
        verbose_name = 'Sent post'

    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('posts')


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.PROTECT)
    date_sent = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
