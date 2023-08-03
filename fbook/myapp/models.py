# models.py
from django.db import models

class User(models.Model):
    # User model fields...
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Post(models.Model):
    title = models.CharField(max_length=100, default="")
    image_url = models.URLField(default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='liked_posts', through='PostLike')
    created_at = models.DateTimeField(auto_now_add=False, default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # Comment model fields...
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default="")
    created_at = models.DateTimeField(default=None, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

class Like(models.Model):
    # Like model fields...
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PostLike(Like):
    # Additional fields specific to PostLike if needed
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

class Follow(models.Model):
    # Follow model fields...
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.follower} follows {self.following}'

    class Meta:
        unique_together = ('follower', 'following')
