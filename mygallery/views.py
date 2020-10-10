from django.shortcuts import render
from .models import Image

# Create your views here.
def welcome(request):
   title= 'Welcome  to my Gallerie'
   images = Image.objects.all()
   return render(request, 'mygallery/home.html', {'title' :title, 'images':images})

