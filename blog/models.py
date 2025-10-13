import uuid

from django.db import models
from accounts.models import UserProfile, User
# Create your models here.

class BlogCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Blog Categories"
    def __str__(self):
        return self.name


def short_uuid():
    return str(uuid.uuid4())[:13]


class Blog(models.Model):
    link = models.CharField(default=short_uuid, unique=True, editable=False, db_index=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog')
    title = models.CharField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(null=True, blank=True, upload_to='blog/images/')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class BlogLikes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('blog', 'user')

    def __str__(self):
        return self.user.username


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment

    
        