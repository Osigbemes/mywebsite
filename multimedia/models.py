from django.db import models

# Create your models here.
class Multimedia(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    media_type = models.CharField(max_length=20)
    # image = models.FilePathField(path="/img")
    image = models.ImageField(upload_to='image')
