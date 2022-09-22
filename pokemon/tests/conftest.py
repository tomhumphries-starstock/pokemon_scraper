import pytest

from pokemon.models import Pokemon, Ability, Species


@pytest.fixture
def fire_ability():
    return Ability.objects.create(name='Fire strike')


@pytest.fixture
def wind_ability():
    return Ability.objects.create(name="Wind pop")


@pytest.fixture
def elemental_ability():
    return Ability.objects.create(name="Elemental burst")


@pytest.fixture
def elemental_species():
    return Species.objects.create(name="Elemental species")


@pytest.fixture
def fire_pokemon(fire_ability, elemental_ability, elemental_species):
    pokemon =  Pokemon.objects.create(name="firey", description="does fire", height=100, weight=50,
                                  base_experience=113, species=elemental_species)
    pokemon.abilities.add(fire_ability, elemental_ability)
    pokemon.save()
    return pokemon


@pytest.fixture
def wind_pokemon(wind_ability, elemental_ability, elemental_species):
    pokemon =   Pokemon.objects.create(name="Windy", description="does wind, HA HA HA", height=400,
                                  weight=1, base_experience=66, species=elemental_species)
    pokemon.abilities.add(wind_ability, elemental_ability)
    pokemon.save()
    return  pokemon
