from django.urls import path
from .views import welcome



urlpatterns = [
    path('',welcome, name='home')
    # path('dynamic/<slug:query>/' , dynamic_urls, name='dynamic')
]