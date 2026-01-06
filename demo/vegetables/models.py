from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/')

    def __str__(self):
        return self.name