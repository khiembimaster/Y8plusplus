from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    genre = models.ForeignKey(Genre, related_name='games', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    iframe = models.URLField(max_length=200, null=True, blank=True)
    thumnail = models.ImageField(upload_to='game_images', blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='games', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['genre']