from django.db import models

class MyText(models.Model):
    tree = models.CharField(max_length=255)
    limit = models.IntegerField(default=20)
    
    
