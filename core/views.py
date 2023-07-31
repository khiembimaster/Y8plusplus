from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Game
# Create your views here.
class GameList(LoginRequiredMixin, ListView):
    model = Game
    context_object_name = 'games'

class GameDetail(LoginRequiredMixin, DetailView):
    model = Game
    context_object_name = 'game'
    template_name = 'core/game.html'

class GamePublish(LoginRequiredMixin, CreateView):
    model = Game
    # fields = '__all__'
    fields = ['name', 'genre','description','iframe','thumnail']
    success_url = reverse_lazy('games')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super(GamePublish, self).form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game
    fields = '__all__'
    success_url = reverse_lazy('games')

class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    context_object_name = 'game'
    success_url = reverse_lazy('games')