from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    date = models.DateTimeField(default=datetime.now, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='media',blank=True,null=True,verbose_name='Image')
    def __str__(self):
        return self.title