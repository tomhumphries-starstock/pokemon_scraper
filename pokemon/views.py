from django.shortcuts import render
from django.views.generic import ListView
from .models import Pokemon


class PokemonListView(ListView):
    model = Pokemon
    context_object_name = "pokemon_list"
    template_name = "pokemon_list.html"
