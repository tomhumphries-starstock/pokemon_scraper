import pokebase as pb
import requests


class PokemonScraper:

    def get_pokemon_count(self):
        return requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0").json()[
            'count']

    def get_pokemon(self, pokemon_id):
        return pb.pokemon(pokemon_id)
