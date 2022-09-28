import pytest


@pytest.mark.django_db
def test_create_ad(client, ads, get_token):
    response = client.get(f"/ads/", format="json", HTTP_AUTHORIZATION="Bearer " + get_token)

    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            "id": ads.pk,
            "name": "test",
            "author": ads.author.username,
            "price": 2000,
            "description": None,
            "is_published": False,
            "image": None,
            "category": ads.category_id
        }]
    }
    assert response.status_code == 200
    assert expected_response == response.data
