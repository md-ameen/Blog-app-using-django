from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# USER TABLE
# user_id user_name pwd
# 1       Alex      123
# 2       Bob       123

# AUTHOR TABLE
# author_id(fk) author_name
# 1             Alex
# 2             Bob

# POST TABLE
# post_id title content date_posted author(fk)
# 1       bp1   bc1     12          alex
# 2       bp2   bc2     12          alex
# 3       bp3   bc3     12          bob
