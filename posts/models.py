from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self): # improves readabilty for models
        return self.text[:50]