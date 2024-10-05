from django.db import models

class Item(models.Model):
    Name = models.CharField(max_length=255, unique=True)
    Description = models.TextField()
    Quantity = models.IntegerField()

    def __str__(self):
        return self.Name
