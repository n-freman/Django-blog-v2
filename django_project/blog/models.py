from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 


class Post(models.Model):
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username}\'s Post with id: {self.pk}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})