import pytest


@pytest.mark.django_db
def test_pokemon_to_str(fire_pokemon):
    assert str(fire_pokemon) == fire_pokemon.name
