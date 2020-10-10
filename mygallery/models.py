from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

class Image(models.Model):
    caption = models.CharField(max_length=100)
    image=CloudinaryField('image')
    
    def __str__(self):
        return self.caption

    class Meta:
        verbose_name='Images'
        
        