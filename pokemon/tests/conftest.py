import pytest

from pokemon.models import Pokemon


@pytest.fixture
def fire_pokemon():
    return Pokemon.objects.create(name="firey", description="does fire")


@pytest.fixture
def wind_pokemon():
    return Pokemon.objects.create(name="Windy", description="does wind, HA HA HA")
