from django.urls import path
from pokemon.views import PokemonListView

urlpatterns = [path("", PokemonListView.as_view(), name="pokemon_list")]
