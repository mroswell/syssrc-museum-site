from django.db import models

# Create your models here.
class Artifact(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    description = models.CharField(max_length=8000)
    def __unicode__(self):
        return  self.description
