from django.db import models

class ImageModel(models.Model):
    name = models.CharField(max_length=255,blank=True)
    image = models.ImageField(upload_to='images/')
    probability = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return f"{self.name} - {self.probability}"