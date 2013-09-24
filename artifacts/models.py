from django.db import models

# Create your models here.
class Artifact(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=200, null=True, blank=True, default='http://www.syssrc.com')
    title = models.CharField(max_length=200,  null=True, blank=True)
    price = models.CharField(max_length=200,  null=True, blank=True)
    description = models.CharField(max_length=8000,  null=True, blank=True)
    release_date = models.CharField(max_length=200, null=True, blank=True)
    memory = models.CharField(max_length=200, null=True, blank=True)
    cpu = models.CharField(max_length=200, null=True, blank=True)
    display = models.CharField(max_length=200, null=True, blank=True)
    storage = models.CharField(max_length=200, null=True, blank=True)
    ports = models.CharField(max_length=200, null=True, blank=True)
   




    def __unicode__(self):
        return  self.description
