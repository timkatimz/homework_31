import pytest


@pytest.mark.django_db
def test_selection_ad(client, selection, get_token):
    response = client.get("/selection/", format="json", HTTP_AUTHORIZATION="Bearer " + get_token)

    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            "id": selection.pk,
            "name": "test",
        }]
    }

    assert response.status_code == 200
    assert expected_response == response.data
