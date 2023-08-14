from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Game(models.Model):
    genre = models.ForeignKey(Genre, related_name='games', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField()
    description = RichTextField(blank=True, null=True)
    iframe = models.URLField(max_length=200, null=True, blank=True)
    thumnail = models.ImageField(upload_to='game_images', blank=False, null=True)
    created_by = models.ForeignKey(User, related_name='games', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['genre']
    
    def get_absolute_url(self):
        return f'/{self.genre.slug}/{self.slug}/'
    
    def get_thumbnail(self):
        if self.thumnail:
            return 'http://127.0.0.1:8000' + self.thumnail.url
        else:
            return ''
