from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    Poster = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.post.title
