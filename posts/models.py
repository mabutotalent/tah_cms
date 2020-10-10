from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

from categories.models import Category


class Post(TimeStampedModel):
    Status = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
    )

    author   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True)
    title    = models.CharField(max_length=100)
    slug     = AutoSlugField(unique=True, always_update=False, populate_from='title')
    content  = models.TextField()
    image    = models.ImageField(upload_to='cms/%Y/%m/%d', default='image_1')
    status   = models.CharField(max_length=20, choices=Status)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post    = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name    = models.CharField(max_length=80)
    email   = models.EmailField()
    body    = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active  = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

