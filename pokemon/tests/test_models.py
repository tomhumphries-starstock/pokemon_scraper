import pytest


@pytest.mark.django_db
def test_pokemon_to_str(fire_pokemon):
    assert (
        str(fire_pokemon)
        == f"Pokemon named {fire_pokemon.name}, {fire_pokemon.height} tall, weighing"
        f" {fire_pokemon.weight}, "
        f"of species {fire_pokemon.species}"
    )
