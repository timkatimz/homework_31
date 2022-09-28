import pytest


@pytest.mark.django_db
def test_retrieve_ad(client, ads, get_token):
    response = client.get(f"/ads/{ads.pk}/", HTTP_AUTHORIZATION="Bearer " + get_token)

    expected_response = {

        "id": ads.pk,
        "name": "test",
        "author": ads.author.username,
        "price": 2000,
        "description": None,
        "is_published": False,
        "image": None,
        "category": ads.category.name
    }
    assert response.status_code == 200
    assert expected_response == response.data
