#from msilib.schema import ListView
from ast import Delete
from audioop import reverse
from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Listening
from django.urls import reverse_lazy

class ListeningList(ListView):
    template_name = 'list_phrase.html'
    model = Listening

class ListeningDetail(DetailView):
    template_name = 'detail.html'
    model = Listening

class ListeningCreate(CreateView):
    template_name = 'create.html'
    model = Listening
    fields = ('title', 'memo')
    success_url = reverse_lazy('phrase_app:list_phrase')


class ListeningDelete(DeleteView):
    template_name = 'delete.html'
    model = Listening
    fields = ('title', 'memo')
    success_url = reverse_lazy('phrase_app:list_phrase')

class ListeningUpdate(UpdateView):
    template_name = 'update.html'
    model = Listening
    fields = ('title', 'memo')
    success_url = reverse_lazy('phrase_app:list_phrase')
