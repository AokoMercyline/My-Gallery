from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

class Image(models.Model):
    caption = models.CharField(max_length=100)
    title = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    location = models.TextField(max_length=30,null=False,blank=False, default='')
    image=CloudinaryField('image')
    pub_date = models.DateTimeField(auto_now=True)
    

    
    def __str__(self):
        return self.caption

    class Meta:
        verbose_name='Images'
        
        