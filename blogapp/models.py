from django.db import models
from django.conf import settings
import datetime
# Create your models here.

class Post(models.Model):
      owner        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
      title        = models.CharField(max_length=255,unique=True)
      content      = models.CharField(max_length=2000)
      post_date    = models.DateField(auto_now_add=True)
      def __str__(self):
            return self.title;
class Comment(models.Model):
      owner        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      post_id      = models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
      content      = models.CharField(max_length=1000)
      def __str__(self):
            return self.content

