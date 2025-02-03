from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255)
    media_url = models.URLField()
    address = models.CharField(max_length=500)
    min_age = models.PositiveIntegerField()
    max_age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
