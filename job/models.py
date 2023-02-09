from django.db import models

# Create your models here.
class Job(models.Model):    # Table    
    title = models.CharField(max_length=100)    # Column