from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Game
# Create your views here.
class GameList(ListView):
    model = Game
    context_object_name = 'games'

class GameDetail(DetailView):
    model = Game
    context_object_name = 'game'
    template_name = 'core/game.html'

class GamePublish(CreateView):
    model = Game
    fields = '__all__'
    success_url = reverse_lazy('games')

class GameUpdate(UpdateView):
    model = Game
    fields = '__all__'
    success_url = reverse_lazy('games')

class GameDelete(DeleteView):
    model = Game
    context_object_name = 'game'
    success_url = reverse_lazy('games')