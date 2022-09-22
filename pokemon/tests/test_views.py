import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_pokemon_list(client):
    url = reverse("pokemon_list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_pokemon_list_uses_correct_template(client):
    url = reverse("pokemon_list")
    response = client.get(url)
    assert "pokemon_list.html" in response.template_name


@pytest.mark.django_db
def test_pokemon_list_lists_pokemon(client, fire_pokemon, wind_pokemon):
    url = reverse("pokemon_list")
    response = client.get(url)
    response_content = response.content.decode("utf-8")
    for pokemon in fire_pokemon, wind_pokemon:
        assert pokemon.name in response_content
        assert pokemon.description in response_content
        assert pokemon.species in response_content
        for ability in pokemon.abilities.all():
            assert ability.name in response_content

