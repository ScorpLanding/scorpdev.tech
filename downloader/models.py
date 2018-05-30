from django.db import models

class Lab(models.Model):
    title = models.CharField(max_length=100)
    node = models.CharField(max_length=100)
    lol = models.CharField(max_length=100)

    def __str__(self):
        return self.title