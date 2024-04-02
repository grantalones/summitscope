from django.db import models

class Mountain(models.Model):
    name = models.CharField(max_length=100)
    elevation = models.PositiveIntegerField()
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.name