from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.



class Blog(models.Model):
    user = models.CharField(max_length=40)
    card = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)