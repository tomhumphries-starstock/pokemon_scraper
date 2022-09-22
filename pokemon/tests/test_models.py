import pytest

from pokemon.models import Pokemon


@pytest.mark.django_db
def test_pokemon_to_str():
    pokemon_name, pokemon_description = "test", "stupid test pokemon"
    pokemon = Pokemon.objects.create(
        name=pokemon_name, description=pokemon_description
    )
    assert str(pokemon) == pokemon_name
