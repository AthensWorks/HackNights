from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    date = models.DateField()
    github_url = models.CharField(max_length=255, blank=True)
    pizza_count = models.IntegerField(null=True, blank=True)
    facebook_event_url = models.CharField(max_length=255, blank=True)
    # attendance
