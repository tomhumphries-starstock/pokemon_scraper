from django.views.generic import ListView
from .models import Pokemon, Species, Ability
from pokemon.pokemon_scraper import PokemonScraper


class PokemonListView(ListView):
    model = Pokemon
    context_object_name = "pokemon_list"
    template_name = "pokemon_list.html"

    def dispatch(self, request, *args, **kwargs):
        update_pokemon_database()
        return super().dispatch(request, *args, **kwargs)


def update_pokemon_database():
    scraper = PokemonScraper()
    pokemon_available = scraper.get_pokemon_count()
    pokemon_in_db = Pokemon.objects.count()
    if  pokemon_in_db < pokemon_available:
        difference = pokemon_available - pokemon_in_db
        start = pokemon_available-difference if pokemon_available - difference else 1
        end  = start + 5 if difference > 5 else pokemon_available + 1
        for pokemon_id in range(start, end):
            pokemon_data = scraper.get_pokemon(pokemon_id)
            species, _ = Species.objects.get_or_create(name=pokemon_data.species.name)
            pokemon = Pokemon.objects.create(
                    name=pokemon_data.name,
                    height=pokemon_data.height,
                weight=pokemon_data.weight,
                base_experience=pokemon_data.base_experience,
                species=species
                )
            for ability in pokemon_data.abilities:
                ability, _ = Ability.objects.get_or_create(name=ability.ability.name)
                pokemon.abilities.add(ability)
            pokemon.save()

