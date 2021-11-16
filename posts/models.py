from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class PostsModel(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField()
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CommentModel(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    postComment = models.ForeignKey(PostsModel, related_name='postsComment', on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.postComment.name
